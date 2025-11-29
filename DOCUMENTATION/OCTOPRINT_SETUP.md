# OctoPrint Setup Guide - Ender-3 V2

**Status:** ✅ Fully configured and operational (Nov 29, 2025)

## Quick Start

```bash
# 1. Start OctoPrint (keep terminal open)
~/Documents/3D_PRINTING/MINDCUBBY-3D/scripts/start-octoprint.sh

# 2. Open in browser
http://localhost:5001

# 3. Upload G-code from PrusaSlicer and print!
```

---

## Installation & Configuration

### Prerequisites
- **Python 3.9+** (macOS comes with this)
- **USB Cable** to Ender-3 V2 (must be working—see Troubleshooting if flaky)

### Install OctoPrint (One-Time Only)

```bash
cd ~
python3 -m venv octoprint-env
source octoprint-env/bin/activate
pip install octoprint
```

### Configuration File

**Location:** `~/Library/Application Support/OctoPrint/config.yaml`

**Key Settings** (added for mriscoc firmware compatibility):

```yaml
serial:
  sendChecksumWithUnknownCommands: false
  neverSendChecksums: true
  receiveAll: true
```

**Why:** mriscoc firmware doesn't handle Marlin line checksums well. Disabling them prevents "Device not configured" errors.

---

## Printer Profile Setup

When you first run OctoPrint, complete the wizard with these settings:

### General
- **Name:** Ender 3 V2
- **Model:** Creality Ender-3 V2

### Print Bed & Build Volume
- **Form Factor:** Rectangular
- **Origin:** Lower Left
- **Heated Bed:** ✅ Checked
- **Dimensions:** X=220mm, Y=220mm, Z=250mm

### Axes (Manual Control Speeds)
- **X:** 6000 mm/min
- **Y:** 6000 mm/min
- **Z:** 200 mm/min
- **E:** 300 mm/min

### Hotend & Extruder
- **Nozzle Diameter:** 0.4mm
- **Number of Extruders:** 1
- **Default Extrusion Length:** 5mm

### Serial Connection
- **Port:** `/dev/tty.usbserial-*` (auto-detected; use the `tty.*` variant, not `cu.*`)
- **Baud Rate:** 115200
- **Printer Profile:** Ender 3 V2

---

## PrusaSlicer Integration

### One-Click Printing from PrusaSlicer

**Step 1: Get API Key**
1. Go to `http://localhost:5001`
2. Click ⚙️ Settings (top right)
3. Click **API** in left sidebar
4. Copy the **Global API Key**

**Step 2: Configure PrusaSlicer**
1. Open PrusaSlicer
2. Go to **Preferences** (Mac: `PrusaSlicer` > `Preferences`)
3. Click **Printers** in left sidebar
4. Find your printer, click ⚙️ (edit)
5. Look for **Physical Printers** or **OctoPrint** settings
6. Fill in:
   - **Host:** `127.0.0.1:5001` (or `localhost:5001`)
   - **API Key:** (paste from step 1)
   - **Printer Profile:** Ender 3 V2

**Step 3: Print**
1. Slice a model in PrusaSlicer
2. Look for **"Send to Printer"** button (or similar)
3. Click it → file uploads and prints automatically

---

## Running OctoPrint

### Start the Server

```bash
~/Documents/3D_PRINTING/MINDCUBBY-3D/scripts/start-octoprint.sh
```

This script:
- ✅ Activates Python virtual environment
- ✅ Prevents macOS from sleeping (uses `caffeinate -i`)
- ✅ Runs OctoPrint on port 5001
- ✅ Keeps running until you press `Ctrl+C`

### Stop the Server

Press `Ctrl+C` in the terminal window.

### Access OctoPrint

- **Local:** `http://localhost:5001`
- **Network:** `http://<your-mac-ip>:5001`
- **mDNS (if available):** `http://daniels-mbp.local:5001`

---

## Known Issues & Fixes

### Issue: "Device not configured" or Connection Hangs

**Causes:**
1. **Faulty USB cable** (most common)
2. **macOS USB security** blocking access
3. **mriscoc firmware** not handling checksums properly
4. **Cura holding the port** (two apps can't share USB at once)

**Fixes:**
1. **Try a new USB cable** first (USB cables fail frequently)
2. **Approve USB Access** in macOS:
   - When connecting, macOS may prompt "Allow USB?"
   - Click **"Allow"** or **"Trust"**
3. **Update Serial Config** (see Configuration File section above)
4. **Close Cura completely** before connecting in OctoPrint
5. **Restart printer:** Unplug USB, wait 10s, plug back in

### Issue: Port 5000 Already in Use (Address Already in Use)

**Cause:** macOS AirPlay Receiver uses port 5000 by default.

**Fix:** OctoPrint is already configured to use port 5001. If you want to use 5000 instead:
1. Disable AirPlay Receiver: **System Settings** > **General** > **AirDrop & Handoff** > Uncheck **AirPlay Receiver**
2. Or keep using port 5001 (recommended for this setup)

### Issue: mriscoc Firmware Not Responding

**Symptoms:** OctoPrint connects briefly, then times out and goes "Offline after error"

**Fix:** The serial checksum bypass in `config.yaml` should handle this. If it persists:
1. Try baud rate **250000** instead of 115200
2. Check firmware version: `M115` in OctoPrint terminal
3. Verify BLTouch is responding: `M401` then `M402` in terminal

---

## Moving to a Dedicated Server (Optional)

For 24/7 printing without keeping your Mac awake:

### Option 1: Raspberry Pi (Recommended)
- **Cost:** $35-50
- **Power:** ~5W (24/7 is cheap)
- **Setup:** Install OctoPi (pre-configured Raspberry Pi OS + OctoPrint)
- **Download:** [octopi.octoprint.org](https://octoprint.octoprint.org/download/)

### Option 2: Old Linux Computer
- **Cost:** Free (repurpose old laptop/desktop)
- **Power:** Higher than Pi, but still less than Mac
- **Setup:** Install Docker + OctoPrint container

### Option 3: Keep on Mac
- **Pro:** No new hardware
- **Con:** Mac must stay on 24/7, uses more power than Pi

**Next Steps (when ready):**
1. Move USB cable to new server
2. Update PrusaSlicer host to new server's IP (e.g., `192.168.1.100:5001`)
3. Restart OctoPrint on new server
4. Stop running it on Mac

---

## Useful OctoPrint Features

### Terminal Tab
- Send G-code commands directly to printer
- Test mesh leveling: `G29`
- Disable steppers: `M84`
- Check firmware: `M115`

### Files Tab
- Upload G-code files
- Print, pause, resume from web interface
- Monitor print progress in real-time

### Plugins (Settings > Plugin Manager)
- **Bed Level Visualizer** - Visual 3D map of bed mesh (great for debugging leveling issues)
- **Themeify** - Dark mode
- **Material Settings** - Store filament profiles

### Timelapse (Settings > Timelapse)
- Captures photos at each layer
- Creates timelapse video of your print
- Requires USB webcam

---

## Maintenance

### Regular Tasks
- ✅ Keep USB cable in good condition (inspect for damage)
- ✅ Monitor bed adhesion (re-level PEI bed if prints lift)
- ✅ Check filament dry box (PETG absorbs moisture)
- ✅ Clean nozzle before long prints

### Updates
- **OctoPrint:** Check **Settings** > **Software Update** for new versions
- **Python:** Update when macOS offers system updates
- **Firmware:** mriscoc updates available at [github.com/mriscoc/Ender3V2S1](https://github.com/mriscoc/Ender3V2S1)

---

## Debugging Checklist

If something stops working:

1. ✅ Is the printer **powered on**?
2. ✅ Is the USB cable **plugged in firmly** on both ends?
3. ✅ Did you click **"Allow"** when macOS asked about USB?
4. ✅ Is **Cura closed** (or any other serial app)?
5. ✅ Did you **restart the printer** (power cycle 10s)?
6. ✅ Did you **restart OctoPrint** (Ctrl+C, run script again)?
7. ✅ Is the **PEI bed clean** (can you see finger smudges)?
8. ✅ Did you **test in terminal** with `timeout 5 cat /dev/tty.usbserial-*`?

If still stuck, check OctoPrint logs: **Settings** > **Logging** > **octoprint.log**

---

## References

- **OctoPrint Docs:** [docs.octoprint.org](https://docs.octoprint.org)
- **PrusaSlicer:** [prusa3d.com/en/prusaslicer](https://www.prusa3d.com/en/prusaslicer/)
- **mriscoc Firmware:** [github.com/mriscoc/Ender3V2S1](https://github.com/mriscoc/Ender3V2S1)
- **Ender-3 V2 Wiki:** Community resources and troubleshooting

---

**Last Updated:** November 29, 2025  
**Status:** ✅ Working (mriscoc 2.1.3 + OctoPrint 1.11.4)
