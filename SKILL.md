# Musical Instrument Design — CNC Workshop Knowledge Base

## Owner
Tony Koop — San Jose, CA. 17+ years building Native American style flutes (153 builds). 
Expanding into world instruments, percussion, and strings via CNC router + lathe at Maker Nexus makerspace (Sunnyvale).
GitHub: tonykoop (tongue-drum repo planned). SolidWorks CAD user.

---

## 1. Acoustic Physics Models

### 1A. Open-Open Pipe (most flutes)
- **Formula:** `f = c / (2 × L_eff)`
- **End correction:** `ΔL ≈ 0.6 × radius` at each open end
- **Speed of sound:** `c = 331.3 × √(1 + T/273.15)` m/s; at 68°F ≈ 343 m/s ≈ 13,552 in/s
- **Used by:** NAF, Irish Flute, Shakuhachi, Tin Whistle, Fujara, Kena/Quena, Moseño, Pinkullo, Tarka, Xiao family
- **Hole positioning:** Each open hole shortens effective length to that hole's position
- **Key formula for hole distance from end:** `dist = acoustic_length × (fund_freq / hole_freq)`
  - This is an approximation; Tony's empirical K2 corrections refine it

### 1B. Stopped Pipe (closed at one end)
- **Formula:** `f = c / (4 × L_eff)` — sounds one octave LOWER than open pipe of same length
- **Harmonics:** Odd only (1st, 3rd, 5th) — gives characteristic hollow tone
- **End correction:** Only at the open end
- **Used by:** Duduk (reed closes one end), Siku/Zampoña (pan flute, closed bottom), Didgeridoo (lips close mouthpiece)
- **Duduk specifics:** root note = key_name − 3 semitones; body_length ≈ 2412/freq inches
- **Pan flute tube:** `L = c/(4f) − 0.82 × bore_diameter` (bore correction)
- **Didgeridoo:** 2nd resonance at 3f ("toot"), 3rd at 5f; blank = theoretical + 6" overshoot

### 1C. Cantilever Beam (tongue drums)
- **Formula:** `f = K × t / L²`
- **K constant:** `K = (1.875²)/(2π) × √(E/(12ρ)) / 0.0254` (imperial: t in inches, L in inches → f in Hz)
- **Key insight:** Width affects volume/sustain but NOT frequency. Length is dominant (L² in denominator).
- **Material K values (imperial):**
  - Padauk: 24,438 | Wenge: 27,103 | Hard Maple: 26,887 | Cherry: 27,275
  - Black Walnut: 27,734 | White Oak: 25,419 | Baltic Birch Ply: 24,389
  - Mahogany: 26,314 | Western Red Cedar: 29,013
- **Tongue length from target freq:** `L = √(K × t / f)`

### 1D. Free-Free Beam (marimba, xylophone)
- **Same Euler-Bernoulli theory** but different boundary conditions
- **λ₁ = 4.730** (vs 1.875 for cantilever)
- **K_marimba = K_tongue × (4.730/1.875)² ≈ K_tongue × 6.36**
- **Padauk K_marimba ≈ 155,502**
- **Node positions:** 22.4% and 77.6% from each end (drill cord holes here)
- **Arch undercut:** Parabolic CNC cut on underside lowers pitch without shortening bar
  - `center_thickness = edge_thickness × (target_freq / flat_bar_freq)²`
  - Minimum center: 0.25" for structural integrity
- **Xylophone vs Marimba:** Xylo has no arch, shorter/harder bars, tuned to 12th overtone (3:1)
- **Resonator tubes:** Quarter-wave closed pipe `L_tube = c/(4f) − 0.82 × bore`

### 1E. Helmholtz Resonator (Resonant Box capstone)
- **Formula:** `f = (c/2π) × √(A_neck / (V_chamber × L_neck))`
- **A_neck** = slit_width × tongue_width (rectangular neck opening)
- **V_chamber** = π × (pocket_Ø/2)² × pocket_depth
- **L_neck** = soundboard thickness
- **Coupling condition:** Helmholtz freq within ±20% of tongue freq → "✓ Coupled"
- **Pocket diameter for coupling:** `Ø = 2 × √(V_needed / (π × depth))` where `V_needed = A_neck / (f² × L_neck × (2π/c)²)`

### 1F. Vibrating String — Mersenne-Taylor (harps, guitars, kora, ngoni)
- **Formula:** `f = (1/2L) × √(T/μ)` where μ = linear density (mass/length)
- **For round monofilament:** `μ = ρ × π × (d/2)²`
- **Gauge from target tension:** `d = 2 × √(T × g / (ρ × π × 4L²f²))` (g = 386.4 in/s²)
- **Critical insight — %Breaking is INDEPENDENT of diameter:**
  `%break = ρ × 4L²f² / (σ_break × g) × 100`
  This depends only on material density, string length, and frequency — NOT gauge.
- **Nylon:** ρ = 0.04155 lb/in³, σ_break = 44,600 psi
- **Practical limits:** Treble strings run 50-70% breaking; bass at 10-30%
- **Harp string lengths:** NOT linear — follow neck curve designed to keep %breaking safe
- **Kora:** 21 strings, string lengths ~22-79cm, Mersenne-Taylor applies same as harp
- **Ngoni:** 6-18 strings, pentatonic, shorter string range

---

## 2. Scale & Hole Patterns

### Common Scales (semitone offsets from fundamental/root)
| Scale | Offsets | Instruments |
|-------|---------|-------------|
| Pentatonic Minor | +3, +5, +7, +8, +10, +12 | NAF (6 holes) |
| Double Harmonic (Arabic) | +1, +4, +5, +7, +8, +11, +12 | NAF Arabic mode (7 holes) |
| Diatonic Major | +2, +4, +5, +7, +9, +11, +12 | Irish Flute, Quena, Tin Whistle, Moseño, Pinkullo, Tarka (6-7 holes) |
| Shakuhachi Pentatonic | +3, +5, +7, +10, +12 | Shakuhachi (5 holes) |
| Xiao 8-hole Chromatic | +2, +3, +4, +5, +7, +9, +10, +11 | All 3 Xiao variants (8 holes) |
| Duduk Natural Minor | +2, +3, +5, +7, +8, +10, +12, +14, +15 | Duduk family (9 holes) |
| Fujara Pentatonic | +3, +5, +7 | Fujara (3 holes + overtones) |
| Siku Diatonic (split) | Arka: 0,4,7,10,14,17,21 / Ira: 2,5,9,12,16,19 | Siku/Zampoña (13 tubes) |

### Naming Conventions
- **NAF/most flutes:** Key = fundamental (all closed)
- **Xiao:** Key = 4th hole note (root + 5 semitones). "G xiao" has root D.
- **Duduk:** Key = root + 3 semitones. "A duduk" has root F#.
- **Siku:** Key = 4th note of the combined scale (usually the major key name)

---

## 3. Tony's Empirical Corrections (NAF-specific)

### K2 Correction by Bore Diameter
| Bore (in) | K2 Calc | K2 NAF (Tony's) | Correction |
|-----------|---------|-----------------|------------|
| ≥1.125 | Formula | +1.0 to +1.6% | Model underestimates |
| 0.875 | Formula | +0.4% | Crossover (neutral) |
| ≤0.75 | Formula | −0.7 to −6.0% | Model overestimates |

### Chamber-to-Bore Ratio
- Sweet spot: 17:1 to 21:1 across all NAF keys
- Formula: acoustic_length / bore_ID

### NAF Build Data (153 flutes)
- Keys range A3 to Bb5
- Common failures: "Death on Router", "Exploded on lathe", "TSH too big", finger holes too large
- Common woods: Walnut, Maple, Cherry, Cedar, Oak, Padauk, Poplar, Mahogany
- Revenue from 153 builds: ~$1,180

---

## 4. Workbook Structure (Flutes-AI.xlsx — 34 sheets)

### Sheet Categories
1. **Original/Legacy (8):** CNC Flute Dimensions, Low to High Range, Pivot Table 2, Built, Price Calculator, Customers, Mode 1&4 Pent., Wolfram Export
2. **World Flute Design Tables (12):** Irish Flute, Shakuhachi, Tin Whistle, Fujara, Tuning Reference, Kena-Kenacho, Xiao Family, Duduk Family, Moseño, Andean Duct Flutes, Siku-Zampoña, Didgeridoo
3. **Percussion Design Tables (4):** Tongue Drum, Marimba, Xylophone, Resonant Box (capstone hybrid)
4. **Stringed Instruments BOM+Method (6):** Electric Guitar Bodies, Electric Violin, Floor Harp, Whamola Bass, Ukulele, Acoustic Violin
5. **Drums BOM+Method (3):** Segmented Ashiko, CNC Guitar Bodies, Segmented Conga
6. **Index (1):** Cross-reference to Instrument Workshop Master v3.xlsx

### Design Sheet Standard Layout
- Rows 1-2: Title + subtitle
- Rows 3-5: Key headers (note, piano key, instrument-specific naming)
- Physical dimensions section (bore, wall, blank size) — often color-coded by variant
- Acoustic calculations section (formulas referencing inputs)
- Scale/hole table (note names, frequencies via formula, diameter as blue input, distance as formula)
- Blue cells (#0000FF font, #D6E4F0 bg) = user inputs
- All other values = formulas referencing inputs

### BOM+Method Sheet Standard Layout
- Title block
- Design inputs (blue cells)
- BOM table: #, Item, Qty, Size/Notes
- Build Method: numbered steps organized into phases
- Design Notes at bottom

---

## 5. Related Workbooks & Files

### Instrument Workshop Master v3.xlsx (16 sheets)
- Master Catalog (260+ rows), CAD/CNC Library (120+ rows), Production Log (240+ rows)
- Materials Inventory, BOM Budget, Training Plan (Maker Nexus), Roadmap
- DoE Studies for tongue drum key tuning (3 phases planned)
- Cross-referenced via catalog IDs (TNG-001, ASH-001, LEG-DES-001, etc.)

### Source Data Files
- Didgeridoos.xlsx: 24-key stopped-pipe design (imported to Didgeridoo sheet)
- Segmented Conga.xlsx: 34-ring × 20-segment cut list (imported)
- Large Djembe Pattern 3.xlsx: 29-ring × 16-segment ashiko (imported)
- Guitar PDFs: FenderJazzBass.pdf (11p, detailed routes), GibsonLesPaul59-ver10full.pdf (1p, Catto Rev10), Fender62stratocaster-blueprint.pdf (1p, graphical)

### Wolfram Cloud
- Notebook: Flutes_Acoustic_Model (scaffolded, not yet executed)
- 9 sections: Intro → Acoustic Theory → Core Functions → Tone Hole Model → Interactive Widget → Empirical Validation → Residual Analysis → Design Table Generator → Discussion
- Handoff document: wolfram-notebook-setup-handoff.md

---

## 6. Pending / Next Builds

### Queued instruments (user requested):
1. **Kora** — 21-string West African harp-lute. Segmented bowl (replaces calabash), goatskin head, notched bridge, Mersenne-Taylor string schedule. Electric version with piezo pickup. Bowl: 35-50cm diameter, 25cm deep. Neck: 120-130cm. String lengths: 22-79cm.
2. **Ngoni (Kamele N'goni)** — 6-18 string West African rhythm harp. Smaller segmented bowl (~25-45cm), goatskin, pentatonic tuning (D-F-G-A-C pattern). Donso (6-string hunter's) and Kamele (10-12 modern) variants.
3. **Stave Lute/Oud** — Bowl-back construction from 14-21 thin ribs (70-75cm × 2.5-4cm × 2.8mm each) bent over a CNC-routed mold. Oud: fretless, 11 strings. Lute: fretted, 6-13 courses.
4. **Steam Bending Reference** — Wood bendability chart, minimum radii by species/thickness, steam box specifications.

### Key dimensions from research:
- **Kora bowl:** 16" diameter head, 10.25" deep (Havlena build); full-size 51.5cm diameter, 25cm deep
- **Kora neck:** 49" long × 3/4" × 2" (Havlena); traditional 120-130cm
- **Kora strings:** shortest 12.5" / longest 33.25" (Havlena); full-size 22-79cm
- **Kora tuning:** F3-D6 diatonic, 11 strings left hand + 10 strings right hand
- **Ngoni bowl:** 10-18" diameter depending on size; Kaypacha model: 32cm (small) or 45cm (large)
- **Ngoni strings:** nylon 0.5-1.6mm gauges; pentatonic D-F-G-A-C-D-F-G repeating
- **Oud ribs:** 14-21 pieces, 75cm × 2.5-4cm × 2.8mm thick (Sofianos supplier specs)
- **Lute ribs:** Same dimensions, 70cm length; end clasp + reinforcing strips

---

## 7. CNC & Shop Capabilities

### Available Tools (Maker Nexus + Tony's home shop)
- ShopBot CNC router (Maker Nexus)
- Wood lathe (12"+ swing for drums; needs 15"+ for conga belly)
- Table saw, band saw, jointer/planer, drum sander
- Epilog laser cutter (templates, engraving)
- SolidWorks CAD (parametric design tables)

### CNC Patterns Used
- **Flip jig with datum pins:** For 2-sided routing (guitar cavities, resonant box chambers)
- **Miter sled:** For segmented drum rings (11.25° ashiko, 9° conga)
- **Split-blank:** For didgeridoo (rip, route bore in halves, re-glue)
- **Profile routing:** For guitar body perimeters with tabs
- **3D surfacing:** For Les Paul carved top, Strat contours, marimba arch undercuts

### Standard CNC Bits Referenced
- 1/8" upcut spiral (tongue slits, fine detail)
- 1/4" downcut spiral (pickup cavities, pockets)
- 1/2" downcut spiral (perimeter profiles, neck pockets)
- 3/4" ball-end (3D surfacing, marimba arches, guitar contours)
- 3/4" flat-bottom (Helmholtz chamber pockets)