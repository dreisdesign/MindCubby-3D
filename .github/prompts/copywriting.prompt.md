---
agent: agent
---

# Generate Printables Listing Copy

## Overview

This prompt generates professional Printables listing copy from G-code specifications and user-provided copywriting details.

**Output:** A single, complete `.md` file ready to paste directly into Printables listing.

**Two workflow modes:**

### Mode 1: Interactive Collection (via Apple Shortcuts)
Use the **Printables-Copywriting-Wizard** Shortcut to collect copywriting info interactively, then the script appends it to generated specs.

### Mode 2: Direct Generation (from existing `.md` files)
When you already have specs in a `*_printables-description.md` file, provide the copywriting details directly and generate the full listing.

### Mode 3: Multi-Component Assembly (Recommended)
For modular designs (e.g., rolling pin with 3 parts), combine all component specs into a **single comprehensive listing** with assembly instructions. This generates one merged `.md` file, not three separate listings.

---

## PHASE 1: Gather/Provide Model Information

**For single-component models:**
Ensure the following information is available (either collected via Shortcuts or from existing documentation):

1. **Model Name** - Object/project name
2. **Primary Function** - What does it do?
3. **Key Features** - What makes it unique?
4. **Print Time** - Estimated time (extracted from G-code)
5. **Filament Used** - Weight in grams (extracted from G-code)
6. **Filament Type** - Material tested (PETG, PLA, etc.)
7. **Special Notes** - Critical printing tips or assembly requirements

**For multi-component assemblies:**
Provide specs for each component:
- Component name, print time, weight, filament
- Assembly order and fit details (snap-fit, threads, interlocking)
- Critical per-component notes (infill pattern, z-seam, orientation)
- Combined total time and weight

**For direct generation:** Provide this information clearly, or point to the existing `.md` file(s) containing specs.

---

## PHASE 2: Generate Copy Using Guidelines Below

**Output Format:**
Generate a **single, complete `.md` file** containing all four required sections (Title, Summary, Tags, Description). For multi-component designs, include:
- A merged **Print Settings** table showing all components and combined totals
- **Assembly Instructions** section with component list and step-by-step fit
- **Per-Component Printing Notes** explaining optimal settings for each part

This single `.md` file can be copy-pasted directly into the Printables listing.

AI Copywriting Guide for 3D Printables Models
Use this guide to generate copy for Printables listings, ensuring all output is technical, concise, and highly scannable.
1. Persona and Tone
Tone: Technical, direct, efficient, and enthusiastic about the print's utility.
Target Audience: 3D printing enthusiasts looking for a quick, reliable, and functional print.
Language to Avoid: "QVC" or overly dramatic/salesy language (e.g., "Tired of stale chips?", "Amazing new design").
Language to Use: Focus on specific metrics (20-Minute, 0.20 mm), key features (Print-in-Place, Strong Grip), and print quality (Tested, Optimized).
2. Required Output Structure
The output MUST contain four clearly labeled sections, matching the fields on the Printables submission page.
A. Model Name (Title)
Goal: Maximize searchability and highlight the top 2-3 most valuable features.
Format: [Time/Size] [Object Name] - [Mechanism/Design] - [Key Benefit/Material]
Example: 20-Minute Chip Clip - Print-in-Place (PIP) - Low Poly, Strong Grip
B. Summary (120 Characters Max)
Goal: Provide the core value proposition. Must be under 120 characters.
Content: Must mention key features (PIP, material, daily use) and core function/speed.
Example: **Low-poly, Print-in-Place** design for **daily use**. Delivers a **strong, self-sprung clip** in under **20 minutes**. **PETG tested.**
C. Tags (Space Separated)
Goal: Provide a comprehensive list including keywords for design, speed, material, and use-case.
Mandatory Inclusion: Include the short-form and long-form of the key design (pip, print-in-place).
Example: chip_clip clip printinplace print-in-place pip kitchen tool lowpoly fast_print quick_print petg tested spring no_support bag_clip food_storage
D. Description (Main Body Text)
Goal: Be highly scannable, using bolding and bullet points.
Anti-Redundancy Rule: Do not repeat the full feature name from the Title/Summary. Instead of just naming a feature (e.g., "Strong Grip"), briefly explain how it works or its benefit (e.g., "Low-poly geometry provides a robust, reliable closing force...").
1. Quick Facts Section
Use short, descriptive bullet points.
Each bullet point should address one category: Design, Speed, Function, Durability/Material.
2. Print Settings Table
Convert all raw data (Nozzle Temp, Layer Height, Print Time) into a clean Markdown table format.
Bold the key values (Filament, Supports, etc.).
3. Critical Printing Notes
List any essential tips for success (e.g., first layer adhesion, bed leveling requirements).
4. Community Note
Always include a brief, friendly note at the end encouraging users to share makes and provide feedback.
3. "Gold Standard" Example (Chip Clip)
# 1. Model Name (Title Field)

**20-Minute Chip Clip - Print-in-Place (PIP) - Low Poly, Strong Grip**

# 2. Summary (120 Characters Max Field)

**Low-poly, Print-in-Place** design for **daily use**. Delivers a **strong, self-sprung clip** in under **20 minutes**. **PETG tested.**

# 3. Tags (Space Separated Field)

chip_clip clip printinplace print-in-place pip kitchen tool lowpoly fast_print quick_print petg tested spring no_support bag_clip food_storage

# 4. Description (Main Body Text Field)

## Quick Facts

* **Design:** **Prints functional** with **zero assembly**; the spring mechanism is integral to the single-piece file.

* **Speed:** Go from download to a finished, usable clip in **under 20 minutes** (19m 50s estimated).

* **Function:** Low-poly geometry provides a **robust, reliable closing force** for bags and storage.

* **Durability:** Tested with **PETG** filament for superior hinge retention and long-term spring force.

## Print Settings (Tested on Ender-3 V2)

| **Setting** | **Value** |
| **Filament** | **PETG** (Recommended for spring retention) |
| Layer Height | 0.20 mm |
| Print Time | 19m 50s |
| Nozzle/Bed Temp | 218°C / 70°C |
| Supports | **None required** |

### Critical Printing Notes

* Ensure a **clean first layer** to prevent the spring mechanism from fusing.

* Optimized for **Ender-3 V2** with BLTouch.

**Community Note:** This is an open-source design intended for daily use. If you print one, please **share your make** and let me know if you have any feedback for future improvements!