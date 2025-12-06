#!/bin/bash

export PATH="/opt/homebrew/bin:$PATH"
export PYTHONUNBUFFERED=1

SCREENSHOT_PATH="/tmp/screenshot_temp.png"
PYTHON_SCRIPT="$HOME/Documents/3D_PRINTING/MINDCUBBY-3D/scripts/screenshot-crop-4-3.py"
SAVE_FOLDER="$HOME/Documents/3D_PRINTING/SCREENSHOTS_INBOX"

# Create folder
mkdir -p "$SAVE_FOLDER"

# Take fullscreen screenshot
screencapture "$SCREENSHOT_PATH"

# Run Python GUI crop tool with Homebrew Python that has tkinter
/opt/homebrew/bin/python3.11 "$PYTHON_SCRIPT" "$SAVE_FOLDER" 2>&1
