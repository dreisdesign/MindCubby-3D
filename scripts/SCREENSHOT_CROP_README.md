# Screenshot → 4:3 Crop Tool

Automated screenshot capture with interactive 4:3 aspect ratio cropping and pan/zoom controls. Perfect for quick screen captures to your SCREENSHOTS_INBOX folder.

## Setup

### Prerequisites
- macOS with Homebrew installed
- Python 3.11+ with tkinter and Pillow

### Installation

All dependencies are pre-installed. If needed, manually install:

```bash
# Install Python with tkinter support
brew install python-tk@3.11

# Install Pillow (image processing)
/opt/homebrew/bin/python3.11 -m pip install Pillow
```

### Files

- **`screenshot-interactive.sh`** - Main script (fullscreen capture → Python GUI)
- **`screenshot-crop-4-3.py`** - Interactive crop tool with pan/zoom
- **`script_mac--screenshot-crop-4-3.scpt`** - AppleScript wrapper for Stream Deck

## Usage

### Via Stream Deck

1. Open Stream Deck app
2. Add action that runs: `~/shortcuts-scripts/script_mac--screenshot-crop-4-3.scpt`
3. Click the button to activate

### Via Terminal

```bash
bash ~/Documents/3D_PRINTING/MINDCUBBY-3D/scripts/screenshot-interactive.sh
```

## Workflow

1. **Trigger** → Takes fullscreen screenshot
2. **Python GUI opens** with:
   - Full screen image displayed
   - Green 4:3 aspect ratio crop box (fixed center)
3. **Adjust crop area:**
   - **Scroll wheel** = Zoom in/out
   - **Click & drag** = Pan image to position desired content
4. **Position** your desired crop area inside the green box
5. **Press ENTER** → Saves cropped image to `SCREENSHOTS_INBOX` with timestamp
6. **Press ESC** → Cancel without saving

## Output

Screenshots are saved to:
```
~/Documents/3D_PRINTING/SCREENSHOTS_INBOX/screenshot_YYYYMMDD_HHMMSS.png
```

Each image is automatically:
- Cropped to perfect 4:3 aspect ratio
- Timestamped with date/time
- Ready for upload to Printables or other platforms

## Controls

| Control | Action |
|---------|--------|
| **Scroll wheel** | Zoom in/out (1.0x - 3.0x) |
| **Click & drag** | Pan/move the image |
| **ENTER** | Save crop to file |
| **ESC** | Cancel without saving |

## Technical Details

- **Screenshot method:** PIL.ImageGrab (native macOS)
- **GUI framework:** tkinter (Python 3.11)
- **Aspect ratio:** 4:3 (locked, non-adjustable)
- **Crop box:** Fixed in center, image moves behind it
- **Output format:** PNG with transparent background support

## Troubleshooting

**Python GUI doesn't appear:**
- Check tkinter: `/opt/homebrew/bin/python3.11 -c "import tkinter; print('OK')"`
- Verify Pillow: `/opt/homebrew/bin/python3.11 -c "from PIL import Image; print('OK')"`

**ENTER key doesn't save:**
- Focus the Python window (click on it first)
- Try pressing both ENTER and RETURN

**Screenshot is all black:**
- Close and retry
- Check `/tmp/screenshot_temp.png` exists

**Stream Deck not triggering:**
- Verify Shortcut "script_mac--screenshot-crop-4-3" exists in Shortcuts app
- Grant accessibility permissions: Settings → Privacy & Security → Accessibility

## Development

Main logic in `screenshot-crop-4-3.py`:
- `CropWindow` class: GUI and image handling
- `take_screenshot()`: PIL screen capture
- `on_scroll()`: Zoom logic (0.9x / 1.1x multiplier)
- `on_pan()`: Image panning
- `save_crop()`: Extract crop box area and save

Modify these functions to customize behavior (zoom limits, colors, output format, etc.)
