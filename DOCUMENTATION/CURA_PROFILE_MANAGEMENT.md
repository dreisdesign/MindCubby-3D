# Cura Profile Management Best Practices

## Overview
Cura profiles control everything: nozzle temp, speed, infill, layer height, etc. Good organization prevents mistakes and makes switching between print types seamless.

---

## Profile Hierarchy (Recommended Structure)

### Level 1: Base/Material Profiles
These are **foundational** - don't modify these often.

```
Base Profiles (one per material):
├── PLA_Base
│   ├── Nozzle: 200°C
│   ├── Bed: 60°C
│   ├── Speed: 50 mm/s
│   └── Infill: 20%
├── PETG_Base
│   ├── Nozzle: 240°C
│   ├── Bed: 75°C
│   ├── Speed: 40 mm/s
│   └── Infill: 20%
└── TPU_Base
    ├── Nozzle: 230°C
    ├── Bed: 50°C
    ├── Speed: 25 mm/s
    └── Infill: 10%
```

### Level 2: Use-Case Profiles (Inherit from Base)
These **extend** base profiles for specific purposes.

```
USE CASE PROFILES (inherit from base):
├── PLA_Fast (based on PLA_Base)
│   └── Override: Speed 60 mm/s, Infill 10%
├── PLA_Quality (based on PLA_Base)
│   └── Override: Speed 30 mm/s, Layer Height 0.1mm, Infill 30%
├── PLA_Flexible (based on PLA_Base)
│   └── Override: Infill 30%, Line Width 0.5mm
├── PETG_Strong (based on PETG_Base)
│   └── Override: Infill 40%, Wall Thickness +0.4mm
├── PETG_PrintInPlace (based on PETG_Base)
│   └── Override: Speed 35 mm/s, Layer Height 0.15mm
└── TPU_Stretchy (based on TPU_Base)
    └── Override: Infill 5%, Retraction reduced
```

---

## Profile Naming Convention

**Format**: `MATERIAL_PURPOSE_MODIFIER`

### Good Names:
- ✅ `PLA_Fast_Prototype` - Clear material, purpose, and use
- ✅ `PETG_PrintInPlace_Clip` - Specific for clip models
- ✅ `TPU_Stretchy_Low` - Material + property + intensity
- ✅ `PLA_Quality_HighDetail` - Purpose + descriptor

### Bad Names:
- ❌ `Profile1`, `Test`, `New_Profile` - Meaningless
- ❌ `PLA_v2`, `PETG_v3` - Version confusion
- ❌ `Fast`, `Good`, `Custom` - Ambiguous

---

## Best Practices for Profile Organization

### 1. **Start Conservative, Then Tweak**
```
❌ DON'T: Create 20 custom profiles randomly
✅ DO:
   1. Start with 3 base profiles (one per material)
   2. Print 3-5 test objects with each base
   3. Only then create use-case variants (Fast, Quality, etc.)
   4. Keep use-case profiles ≤ 5 per material
```

### 2. **Document Your Tweaks**
Create a profile log (optional, but helpful):

```
Profile: PETG_PrintInPlace_Clip
Created: 2025-11-09
Base: PETG_Base
Changes Made:
  - Speed: 40mm/s → 35mm/s (reduces vibration in thin parts)
  - Layer Height: 0.2mm → 0.15mm (better detail for moving hinge)
  - Nozzle Pressure: Standard → +10% (more extrusion for durability)
Result: [Success/Failed] - [notes]
```

### 3. **Use Inheritance, Not Duplication**
- ✅ Create use-case profile based on material base (uses inheritance)
- ❌ Don't copy-paste entire base profile and modify

**Why?** If you improve PLA_Base later (found better temps), all profiles inheriting from it auto-update.

### 4. **Keep Base Profiles Pure**
```
PLA_Base = Production Baseline
├── Never tweak for specific prints
├── Only update if you find universally better settings
└── Document why you changed it

PLA_Fast = For quick iteration
├── Tweak freely for speed
├── Only inherits from PLA_Base
└── Never used as base for other profiles
```

### 5. **Organize by Material, Then by Purpose**
In Cura's profile dropdown, you'll see:
```
PLA
├── PLA_Base ⭐ (don't use directly, use as base only)
├── PLA_Fast
├── PLA_Quality
├── PLA_Flexible
PETG
├── PETG_Base ⭐
├── PETG_PrintInPlace_Clip
├── PETG_Strong
TPU
├── TPU_Base ⭐
└── TPU_Stretchy
```

---

## Profile Settings You'll Commonly Tweak

### For Speed Optimization
```
Speed Profiles:
├── FAST: Travel 150mm/s, Print 60mm/s, First Layer 30mm/s
├── NORMAL: Travel 120mm/s, Print 40mm/s, First Layer 25mm/s
└── QUALITY: Travel 100mm/s, Print 30mm/s, First Layer 20mm/s
```

### For Quality/Detail
```
Quality Profiles:
├── STANDARD: Layer 0.2mm, Nozzle 0.4mm lines
├── DETAILED: Layer 0.1mm, Nozzle 0.3mm lines
└── ULTRA: Layer 0.05mm, Nozzle 0.2mm lines (slow!)
```

### For Strength/Durability
```
Strength Profiles:
├── LIGHT: Infill 10%, Walls 2
├── NORMAL: Infill 20%, Walls 3
└── STRONG: Infill 30%+, Walls 4+, 100% top/bottom
```

### For Flexible/Articulated Parts
```
Flexible Profiles:
├── NORMAL_PETG: 20% infill, standard retraction
├── PRINT_IN_PLACE: 30% infill, reduced retraction (-0.5mm), slower speed
└── HINGES_MOVING: 40% infill, no retraction, 35mm/s speed
```

---

## Workflow: Creating a New Use-Case Profile

### Step 1: Identify the Need
"I'm printing a clip with moving hinge in PETG"

### Step 2: Check Existing Profiles
- Do I have `PETG_PrintInPlace`? ✓ Use it
- If not, create based on `PETG_Base`

### Step 3: Create Profile (In Cura)
1. Select `PETG_Base` as your active profile
2. Go to **Settings → Printer → Manage Printers**
3. Select your printer
4. **Create Profile from Current** (or duplicate PETG_Base)
5. Name it: `PETG_PrintInPlace_Clip`
6. Save

### Step 4: Tweak for Your Use Case
Common tweaks for print-in-place:
```
- Infill: 20% → 30% (more flexible but stronger)
- Speed: 40mm/s → 35mm/s (cleaner hinge movement)
- Retraction Distance: 5mm → 4mm (reduce stringing)
- Min Layer Time: 10s (prevent overheating thin parts)
```

### Step 5: Test & Document
1. Print a test piece
2. Note what worked/what needs adjustment
3. Add to MODELS/README.md print history
4. Update profile if needed

### Step 6: Save & Commit (Optional)
If you export profiles to files for backup:
```bash
# Export profile
Cura → File → Export Profile → PETG_PrintInPlace_Clip.curaprofile
# Commit to repo
git add _cura-profile/PETG_PrintInPlace_Clip.curaprofile
git commit -m "Add: PETG_PrintInPlace_Clip profile (30% infill, 35mm/s)"
```

---

## Red Flags: When NOT to Create New Profiles

❌ **Don't create a new profile if:**
- You only changed ONE setting (use profile variants or modifiers instead)
- You're tweaking for one specific model (use Cura's Per-Model Settings)
- The change is temporary/experimental (test it first!)

✅ **Do create a new profile when:**
- You've tested 3+ prints and found consistent improvements
- The change is material-based (different material = new profile)
- Multiple models will use these settings

---

## Managing Profile Bloat

If you end up with 20+ profiles:

### Clean Up Strategy:
1. **Audit**: List all profiles and mark which you actually use
2. **Consolidate**: Can 3 similar profiles merge into 1 base + 1 variant?
3. **Archive**: Move unused profiles to `_archive_profiles` (Cura backup)
4. **Document**: Keep a list of what each profile is for

---

## Backup & Restore Profiles

### Export (Backup)
```
Cura → File → Export Profile
Saves as: MyProfile.curaprofile (can commit to repo)
```

### Import (Restore)
```
Cura → File → Import Profile
Select: MyProfile.curaprofile
Cura automatically adds it to your profile list
```

### Why Backup?
- Sync profiles across computers
- Share optimized profiles with others
- Version control your tuning work

---

## Profile Optimization Workflow (Recommended)

```
Week 1: Create Base Profiles
├── Test PLA_Base on 5 prints
├── Test PETG_Base on 5 prints
└── Test TPU_Base on 5 prints
   → Document results

Week 2-3: Create Use-Case Profiles
├── Create PLA_Fast (if needed)
├── Create PETG_PrintInPlace (if printing clips)
├── Test each on 2-3 prints
└── Document changes & results

Week 4+: Maintain & Optimize
├── Use profiles as-is
├── Only modify if problem discovered
├── Log all tweaks
└── Share working profiles with repo
```

---

## Quick Reference: What Changes Per Use Case

| Use Case | Speed ↓ | Infill ↑ | Layer Height ↓ | Walls ↑ |
|----------|---------|---------|-----------------|---------|
| **Fast Prototype** | 60 mm/s | 10% | 0.3mm | 2 |
| **Standard Print** | 40 mm/s | 20% | 0.2mm | 3 |
| **High Quality** | 30 mm/s | 20% | 0.1mm | 3 |
| **Flexible/Hinges** | 35 mm/s | 30% | 0.2mm | 3 |
| **Strong/Durable** | 35 mm/s | 30%+ | 0.2mm | 4 |

---

## Summary

✅ **DO:**
- Create 1 base profile per material (PLA, PETG, TPU)
- Create use-case profiles inheriting from base (Fast, Quality, PrintInPlace)
- Name profiles descriptively (Material_Purpose)
- Test before creating new profiles
- Document tweaks and results
- Keep profiles ≤ 8 total (3 base + 5 use-case max)

❌ **DON'T:**
- Create profiles randomly without testing
- Have 20+ profiles (you won't use them all)
- Modify base profiles frequently
- Copy-paste instead of using inheritance
- Forget to document changes

