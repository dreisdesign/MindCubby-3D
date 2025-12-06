#!/usr/bin/env python3
"""
Interactive screenshot tool: Take screenshot → crop to 4:3 (pan/zoom) → save
Usage: python3 screenshot-crop-4-3.py [output_folder]
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk
import os

class CropWindow:
    def __init__(self, image_path, output_folder):
        self.image_path = image_path
        self.output_folder = output_folder
        self.original_img = Image.open(image_path)
        self.original_width, self.original_height = self.original_img.size
        
        # Calculate initial 4:3 crop box (centered)
        self.aspect_ratio = 4 / 3
        if self.original_width / self.original_height > self.aspect_ratio:
            # Width is too wide, constrain by height
            crop_width = int(self.original_height * self.aspect_ratio)
            crop_height = self.original_height
        else:
            # Height is too tall, constrain by width
            crop_width = self.original_width
            crop_height = int(self.original_width / self.aspect_ratio)
        
        self.crop_x = (self.original_width - crop_width) // 2
        self.crop_y = (self.original_height - crop_height) // 2
        self.crop_width = crop_width
        self.crop_height = crop_height
        self.zoom_level = 1.0
        self.pan_x = 0
        self.pan_y = 0
        
        # Create window
        self.root = tk.Tk()
        self.root.title("Crop to 4:3 - Use Mouse Wheel to Zoom, Drag to Pan, ENTER to Save")
        self.root.geometry("1000x750")
        self.root.attributes('-topmost', True)  # Keep window on top
        
        # Canvas for image
        self.canvas = tk.Canvas(self.root, bg="gray20", cursor="hand2")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<MouseWheel>", self.on_scroll)
        self.canvas.bind("<Button-4>", self.on_scroll)  # Linux scroll up
        self.canvas.bind("<Button-5>", self.on_scroll)  # Linux scroll down
        self.canvas.bind("<B1-Motion>", self.on_pan)
        self.canvas.bind("<Button-1>", self.start_pan)
        self.canvas.bind("<Return>", self.save_crop)
        self.canvas.bind("<Escape>", lambda e: self.root.quit())
        
        # Also bind to root for better key capture
        self.root.bind("<Return>", self.save_crop)
        self.root.bind("<Escape>", lambda e: self.root.quit())
        
        # Info label
        self.info_label = tk.Label(self.root, text="", bg="gray20", fg="white", font=("Courier", 10))
        self.info_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        
        self.pan_start_x = 0
        self.pan_start_y = 0
        self.photo = None
        
        # Force window to foreground
        self.root.lift()
        self.root.focus_force()
        
        # Schedule first update
        self.root.after(100, self.update_display)
        
    def on_scroll(self, event):
        """Zoom with mouse wheel"""
        if event.num == 5 or event.delta < 0:
            self.zoom_level *= 0.9
        else:
            self.zoom_level *= 1.1
        self.zoom_level = max(0.5, min(3.0, self.zoom_level))
        self.update_display()
    
    def start_pan(self, event):
        """Start panning"""
        self.pan_start_x = event.x
        self.pan_start_y = event.y
    
    def on_pan(self, event):
        """Pan the image"""
        dx = event.x - self.pan_start_x
        dy = event.y - self.pan_start_y
        self.pan_x += dx
        self.pan_y += dy
        self.pan_start_x = event.x
        self.pan_start_y = event.y
        self.update_display()
    
    def update_display(self):
        """Redraw canvas with current zoom/pan and crop box overlay"""
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if canvas_width <= 1:
            canvas_width = 1000
        if canvas_height <= 1:
            canvas_height = 750
        
        # Scale image to fit window initially
        scale_x = canvas_width / self.original_width
        scale_y = canvas_height / self.original_height
        scale = min(scale_x, scale_y)
        
        # Apply zoom
        scaled_width = int(self.original_width * scale * self.zoom_level)
        scaled_height = int(self.original_height * scale * self.zoom_level)
        
        # Resize image
        if scaled_width > 0 and scaled_height > 0:
            scaled_img = self.original_img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)
            
            # Image position with pan (centered initially, then offset by pan)
            img_x = (canvas_width - scaled_width) // 2 + self.pan_x
            img_y = (canvas_height - scaled_height) // 2 + self.pan_y
            
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(scaled_img)
            self.canvas.delete("all")
            
            # Draw image
            self.canvas.create_image(img_x, img_y, image=self.photo, anchor="nw")
            
            # Draw FIXED 4:3 crop box in center (doesn't move)
            crop_box_width = int(canvas_width * 0.8)
            crop_box_height = int(crop_box_width / (4/3))
            crop_box_x1 = (canvas_width - crop_box_width) // 2
            crop_box_y1 = (canvas_height - crop_box_height) // 2
            crop_box_x2 = crop_box_x1 + crop_box_width
            crop_box_y2 = crop_box_y1 + crop_box_height
            
            # Draw crop box border
            self.canvas.create_rectangle(crop_box_x1, crop_box_y1, crop_box_x2, crop_box_y2,
                                         outline="lime", width=3)
            
            # Store for save operation
            self.crop_box_screen = (crop_box_x1, crop_box_y1, crop_box_x2, crop_box_y2)
            self.img_position = (img_x, img_y)
            self.scaled_size = (scaled_width, scaled_height)
            
            # Update info
            info_text = f"Zoom: {self.zoom_level:.1f}x | Drag to pan | ENTER=Save | ESC=Cancel"
            self.info_label.config(text=info_text)
    
    def save_crop(self, event=None):
        """Save the cropped image based on fixed crop box position"""
        if not hasattr(self, 'crop_box_screen'):
            print("❌ Crop box not initialized")
            self.root.quit()
            return
        
        # Get screen crop box coordinates
        crop_x1, crop_y1, crop_x2, crop_y2 = self.crop_box_screen
        img_x, img_y = self.img_position
        scaled_width, scaled_height = self.scaled_size
        
        # Convert screen coordinates back to original image coordinates
        # Account for image position and scaling
        img_left = img_x
        img_top = img_y
        
        # Crop box in image coordinates
        crop_img_x1 = int((crop_x1 - img_left) / (scaled_width / self.original_width)) if scaled_width > 0 else 0
        crop_img_y1 = int((crop_y1 - img_top) / (scaled_height / self.original_height)) if scaled_height > 0 else 0
        crop_img_x2 = int((crop_x2 - img_left) / (scaled_width / self.original_width)) if scaled_width > 0 else self.original_width
        crop_img_y2 = int((crop_y2 - img_top) / (scaled_height / self.original_height)) if scaled_height > 0 else self.original_height
        
        # Clamp to image bounds
        crop_img_x1 = max(0, min(crop_img_x1, self.original_width))
        crop_img_y1 = max(0, min(crop_img_y1, self.original_height))
        crop_img_x2 = max(0, min(crop_img_x2, self.original_width))
        crop_img_y2 = max(0, min(crop_img_y2, self.original_height))
        
        # Ensure x1 < x2 and y1 < y2
        if crop_img_x1 > crop_img_x2:
            crop_img_x1, crop_img_x2 = crop_img_x2, crop_img_x1
        if crop_img_y1 > crop_img_y2:
            crop_img_y1, crop_img_y2 = crop_img_y2, crop_img_y1
        
        # Crop the image
        crop_box = (crop_img_x1, crop_img_y1, crop_img_x2, crop_img_y2)
        cropped = self.original_img.crop(crop_box)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path(self.output_folder) / f"screenshot_{timestamp}.png"
        cropped.save(output_path)
        print(f"✅ Saved: {output_path}")
        self.root.quit()
    
    def run(self):
        self.root.mainloop()

def take_screenshot():
    """Capture fullscreen screenshot"""
    import time
    temp_path = "/tmp/screenshot_temp.png"
    
    # Use PIL to capture the screen directly
    try:
        from PIL import ImageGrab
        print("📸 Capturing screen with PIL...")
        img = ImageGrab.grab()
        img.save(temp_path)
        print(f"✅ Screenshot saved: {temp_path}")
        return temp_path
    except Exception as e:
        print(f"⚠️ PIL capture failed: {e}, falling back to screencapture")
        # Fallback to screencapture
        import subprocess
        subprocess.run(["screencapture", temp_path], check=True)
        return temp_path

def main():
    # Default folder
    output_folder = sys.argv[1] if len(sys.argv) > 1 else "/Users/danielreis/Documents/3D_PRINTING/SCREENSHOTS_INBOX"
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Take screenshot
    print("📸 Taking screenshot...")
    screenshot = take_screenshot()
    print(f"✅ Screenshot: {screenshot}")
    
    # Verify file exists
    if not os.path.exists(screenshot):
        print(f"❌ Screenshot file not found: {screenshot}")
        sys.exit(1)
    
    # Verify it's a valid image
    try:
        img = Image.open(screenshot)
        print(f"✅ Image loaded: {img.size}")
    except Exception as e:
        print(f"❌ Failed to load image: {e}")
        sys.exit(1)
    
    # Open crop window
    print("🎯 Opening crop tool (4:3 aspect ratio locked)")
    print("   Scroll wheel: Zoom | Drag: Pan | ENTER: Save | ESC: Cancel")
    crop_window = CropWindow(screenshot, output_folder)
    crop_window.run()
    
    # Cleanup
    try:
        os.remove(screenshot)
    except:
        pass

if __name__ == "__main__":
    main()
