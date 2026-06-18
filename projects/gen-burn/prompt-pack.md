# Woodworking Gen-Burn Prompt Pack

> **Version:** 1.0  
> **Authored by:** Sonnet (Issue #3)  
> **Feeds:** agy hero/step stories (#4), b-roll motion loops (#5)  
> **Validated on:** Walnut Segmented Bowl (Turning) + Oak Picture Frame (Joinery)

---

## Template

Every project entry uses the following schema. All fields are required before handing off to agy.

```yaml
project_type: <woodturning | beehive | coffee_table | picture_frame>
slug: <kebab-case identifier, e.g. walnut-bowl-segmented>

wood_species:        # list 2–4 species used (primary first)
joinery_method:      # e.g. "segmented glue-up", "mortise & tenon", "box joint", "rabbet"
finish_stages:       # ordered list: raw / sanded / oiled / waxed / lacquered / poly
lighting_setup:      # one of: side-raking | overhead-diffuse | window-natural | studio-3pt | golden-hour
style_tokens:
  camera: <angle description>
  dof: <shallow | mid | deep>
  background: <description>
  mood: <descriptor>

hero_prompts:        # 3–5 image prompts
  - id: H1
    prompt: "..."
  - id: H2
    prompt: "..."
  ...

step_set:            # 4–6 numbered step illustrations
  - step: 1
    label: "<short label>"
    prompt: "..."
  ...

broll_loops:         # 2–3 motion loop descriptions for video gen
  - id: B1
    label: "<short label>"
    description: "..."
    motion_type: <pan | push-in | orbit | static-with-action | time-lapse>
    duration_sec: <4 | 6 | 8>
  ...
```

### Style Token Glossary

| Token | Allowed Values |
|---|---|
| camera | overhead flat-lay, 45-degree three-quarter, worm's-eye low-angle, eye-level profile, close-up macro |
| dof | shallow (f/1.8–f/2.8), mid (f/5.6–f/8), deep (f/11–f/16) |
| background | workshop bench raw pine, charcoal seamless paper, warm linen textile, outdoor grass/stone, white infinity cove |
| mood | intimate-craft, bold-product, rustic-workshop, minimal-gallery, earthy-organic |
| lighting_setup | side-raking (reveals grain texture), overhead-diffuse (soft, even), window-natural (directional with shadows), studio-3pt (clean product), golden-hour (warm ambient) |

### Variant Count Guidelines

| Slot | Min | Max | Notes |
|---|---|---|---|
| Hero images per project | 3 | 5 | Vary species + finish stage |
| Step illustrations per project | 4 | 6 | Show build arc start → finish |
| B-roll loops per project | 2 | 3 | Mix motion types |
| Worked example coverage | 2 | 2 | 1 turning + 1 joinery minimum |

---

## Project: Woodturning

```yaml
project_type: woodturning
slug: generic-turning

wood_species: [walnut, maple, cherry, padauk]
joinery_method: "lathe-turned; no joinery — form through rotation"
finish_stages: [raw_blank, rough_turned, finish_turned, sanded_400, danish_oil, wax_buffed]
lighting_setup: side-raking
style_tokens:
  camera: 45-degree three-quarter
  dof: shallow
  background: workshop bench raw pine
  mood: intimate-craft
```

### Hero Image Prompts

**H1 — Walnut Bowl, Finish Turned, Side-Raking Light**
```
Product photograph of a hand-turned walnut bowl on a worn pine workbench, freshly finish-turned with tool marks still faintly visible on the interior, dramatic raking side light from the left casting long shadows that reveal the end-grain figure, shallow depth of field with the rim sharp and the interior falling into soft bokeh, warm amber tones, 45-degree three-quarter view, mood: intimate workshop craft, no props
```

**H2 — Maple Vase, Wax-Buffed Final Finish, Overhead**
```
Flat-lay overhead photograph of a tall maple vase form, freshly hand-turned and wax-buffed to a satin sheen, white infinity cove background, studio overhead diffuse lighting with a single fill card, creamy figured maple grain with faint curly figure, deep depth of field f/11, clean minimal-gallery mood, centered composition with subtle drop shadow
```

**H3 — Cherry Platter, Danish Oil Stage, Natural Window Light**
```
45-degree three-quarter view of a wide cherry platter resting on a linen cloth, mid-oiling stage — one half still dry-sanded showing pale wood, the other half freshly wiped with danish oil showing deep amber-red grain, directional window light from the right with soft shadow, mid depth of field f/5.6, rustic-workshop mood, hands not shown
```

**H4 — Padauk Pepper Mill, Turned Pair, Studio 3-Point**
```
Studio product photograph of a matched pair of padauk and maple pepper mills on a charcoal seamless background, both lathe-turned with crisp coves and beads, padauk showing its vivid red-orange heartwood, studio 3-point lighting — key at 45 degrees, fill opposite, rim light behind, shallow dof f/2.8 on the front mill, bold-product mood
```

**H5 — Segmented Walnut/Maple Bowl, Gallery Shot**
```
Eye-level profile photograph of a segmented bowl with alternating dark walnut and light maple rings, finished to a high gloss with spray lacquer, charcoal seamless paper background, overhead-diffuse soft box, the reflection of the bowl visible on the lacquer surface, deep depth of field, minimal-gallery mood, centered symmetrical composition
```

### Step Illustration Set

**Step 1 — Blank Preparation**
```
Close-up macro photograph on a pine workbench: a rough bandsaw-cut bowl blank of walnut, approximately 8 inches diameter and 4 inches thick, freshly cut with visible saw marks on the face, bark edge on one side, end grain showing annual rings, harsh overhead workshop fluorescent light, deep dof, no hands, label area at bottom for "Step 1: Prepare Blank"
```

**Step 2 — Mounting on Lathe**
```
Eye-level photograph showing a walnut bowl blank mounted on a lathe faceplate with four wood screws visible, lathe tailstock brought up for support, workshop background with tool rack softly out of focus, side-raking light, mid dof f/5.6, intimate-craft mood
```

**Step 3 — Rough Turning Exterior**
```
45-degree three-quarter view of a bowl blank being rough-turned on the lathe — visible tool marks spiraling around the cylinder, wood shavings piled on the lathe bed below, a bowl gouge positioned at the rest (tool only, no hands required), raking workshop light from the left, warm incandescent color temperature, mid dof
```

**Step 4 — Hollowing the Interior**
```
Overhead close-up of the lathe chuck with the bowl blank reversed, a swept-back bowl gouge entering the interior — shavings curling away, the hollow form emerging with thick walls still to be refined, side-raking light casting the shadow of the gouge into the hollow, shallow dof on the cutting edge, intimate-craft mood
```

**Step 5 — Sanding Through Grits**
```
Macro close-up of hands (gloved, partial frame) holding a folded sheet of sandpaper against the spinning interior of a walnut bowl, lathe running, fine dust haze visible in backlight, 220-grit stage, surface showing emerging smoothness, window-natural light, shallow dof f/2.0
```

**Step 6 — First Oil Coat Applied**
```
45-degree three-quarter view of the finished-turned walnut bowl sitting off the lathe on a linen cloth, a folded shop rag dark with danish oil resting beside it, the bowl surface half-oiled showing the dramatic color shift — pale dry wood on left, rich dark amber on right, golden-hour warm light, mid dof, earthy-organic mood
```

### B-Roll Loop Descriptions

**B1 — Shavings Cascade**
```yaml
id: B1
label: Shavings cascade off spinning bowl
description: >
  Low-angle close-up, lathe spinning at medium RPM, a bowl gouge making a light finishing pass on the exterior of a walnut bowl — thin translucent shavings curl and cascade off the tool in slow motion (120fps playback at 24), backlit by a single warm tungsten source, dark workshop background, shavings catching the light like ribbon. Loop point: seamless cut between tool entering and exiting the cut.
motion_type: static-with-action
duration_sec: 6
```

**B2 — Orbital Turntable Reveal**
```yaml
id: B2
label: Slow orbit around finished bowl
description: >
  Camera on a motorized turntable slowly orbiting 360 degrees around a completed wax-buffed walnut bowl on a charcoal paper surface, studio diffuse overhead light, camera at 30-degree elevation, shallow dof so only the near face is sharp as it passes — emphasizes the figure and form from all angles. Speed: one full revolution in 8 seconds.
motion_type: orbit
duration_sec: 8
```

**B3 — Oil Application Wipe**
```yaml
id: B3
label: Danish oil absorbed into grain
description: >
  Tight macro push-in on the surface of a walnut bowl as a danish-oil-soaked rag is slowly drawn across the frame from left to right — the grain dramatically deepens in color behind the rag as the oil absorbs in real time, side-raking light reveals the texture, 4K macro lens, very shallow dof, warm ambient. Loop: rag exits right, cut back to dry surface on left.
motion_type: push-in
duration_sec: 4
```

---

## Project: Beehive

```yaml
project_type: beehive
slug: generic-beehive

wood_species: [western_red_cedar, pine, spruce]
joinery_method: "box joint (finger joint) at box corners; rabbet for top/bottom ledges; butt-joint with screws for supers"
finish_stages: [raw_lumber, cut_and_jointed, assembled_dry, painted_exterior, primed_only]
lighting_setup: golden-hour
style_tokens:
  camera: eye-level profile
  dof: mid
  background: outdoor grass/stone
  mood: rustic-workshop
```

### Hero Image Prompts

**H1 — Cedar Langstroth Hive, Golden Hour, Field Setting**
```
Eye-level profile photograph of a completed Western Red Cedar Langstroth beehive — two deep supers and one honey super — sitting on cinder-block stand in a wildflower meadow, golden-hour sunlight raking across the box joints at the corners highlighting the finger joint detail, natural weathered look with no paint, cedar showing silver-grey tone, mid dof f/8, bees visible as motion blur at the entrance, earthy-organic mood
```

**H2 — Hive Components Exploded Flat-Lay**
```
Overhead flat-lay on outdoor weathered cedar deck boards showing all Langstroth hive components separated and arranged in assembly order — bottom board, deep super 1, deep super 2, honey super, inner cover, telescoping outer cover, frames with foundation — all raw unfinished pine, diffuse overcast sky lighting from above, deep dof f/16, minimal-gallery mood, labels not shown
```

**H3 — Box Joint Corner Detail, Studio**
```
Macro close-up of the corner box joint on a cedar hive super, alternating finger joints interlocked and glued, fresh sanding marks visible across the end grain, studio overhead-diffuse light, shallow dof f/2.8 so only the outermost joint face is sharp, white background softly out of focus, bold-product mood
```

**H4 — Painted White Hive, Garden Setting**
```
45-degree three-quarter view of a painted white Langstroth hive in a backyard garden setting, bright mid-morning natural light, white paint slightly chalky suggesting weathering, cherry blossoms or garden flowers softly bokeh in the background, mid dof f/5.6, intimate-craft mood
```

### Step Illustration Set

**Step 1 — Milling Lumber to Width**
```
Eye-level photograph of a table saw with a cedar board being ripped to the correct hive-box width — blade guard in place, push stick visible, workshop background, overhead fluorescent lighting, mid dof, rustic-workshop mood, no hands required in frame
```

**Step 2 — Cutting Box Joints**
```
Close-up of a router table or table-saw box-joint jig with a pine hive-box side piece being indexed through — finger joints freshly cut, sawdust on the table surface, side-raking workshop light highlighting the joint geometry, shallow dof on the joint, intimate-craft mood
```

**Step 3 — Dry-Fitting the Box**
```
45-degree overhead view of a hive super box being dry-fitted — four sides interlocked without glue, clamps lightly holding, pine or cedar, workshop bench background, mid dof, showing the rabbet ledge on the interior for frame rest, natural window light
```

**Step 4 — Glue-Up and Clamping**
```
Workshop bench scene: a hive box clamped with four bar clamps after glue-up, glue squeeze-out visible at the box joint lines, square sitting on top to verify, cedar or pine, warm incandescent work light, mid dof f/5.6, intimate-craft mood
```

**Step 5 — Painting Exterior**
```
Eye-level photograph of a finished hive box being painted white with a 4-inch brush — bristles loaded with exterior latex paint, one side freshly painted white against the raw wood of the adjacent face, outdoor setting on a sawhorse, natural light, mid dof, rustic-workshop mood
```

### B-Roll Loop Descriptions

**B1 — Morning Hive Entrance Time-Lapse**
```yaml
id: B1
label: Bees entering and exiting at dawn
description: >
  Time-lapse, camera locked on tripod at ground level, framing the landing board and entrance of a white Langstroth hive in a garden, 30-second real-time compressed to 4 seconds — bees streaming in and out, golden morning light raking across the entrance, dew on the nearby grass, shallow dof so bees are the sharpest element. Loop: seamless morning → activity → morning.
motion_type: time-lapse
duration_sec: 4
```

**B2 — Box Joint Assembly Push-In**
```yaml
id: B2
label: Finger joints sliding together
description: >
  Macro push-in: two sides of a cedar hive box being pressed together at the corner, finger joints aligning and interlocking in slow motion — the grain of the wood filling the frame, side-raking workshop light catching each finger as it seats, shallow dof, no glue (dry-fit), sound design cue: satisfying wood-on-wood click. Duration 6 seconds, loop at the moment both faces are flush.
motion_type: push-in
duration_sec: 6
```

**B3 — Frame Wiring Close-Up**
```yaml
id: B3
label: Frame wire tensioning
description: >
  Static close-up with action: hands threading beeswax foundation into a wooden frame and pressing the wires into the wax — warm light from a single work lamp, macro lens, very shallow dof on the wire and wax surface, cedar frame blurred in background. 8-second loop with a continuous motion of smoothing the foundation flat.
motion_type: static-with-action
duration_sec: 8
```

---

## Project: Coffee Table

```yaml
project_type: coffee_table
slug: generic-coffee-table

wood_species: [white_oak, black_walnut, hard_maple, ash]
joinery_method: "mortise & tenon (apron-to-leg); breadboard ends with elongated mortise; loose-wedge through-tenon accent"
finish_stages: [rough_sawn, dimensioned, joinery_cut, dry_fitted, glued_assembled, sanded_180, sanded_220, oil_finish, poly_topcoat]
lighting_setup: window-natural
style_tokens:
  camera: 45-degree three-quarter
  dof: mid
  background: warm linen textile
  mood: bold-product
```

### Hero Image Prompts

**H1 — White Oak Coffee Table, Natural Oil, Living Room Context**
```
45-degree three-quarter lifestyle photograph of a white oak coffee table in a modern living room, herringbone or rift-sawn ray-fleck visible in the oak surface, finished with hardwax oil — satin sheen that catches the natural window light from the right, tapered legs with visible through-tenon wedges at the top, a single art book and small plant as props, mid dof f/5.6, warm afternoon window light, bold-product mood
```

**H2 — Walnut Table, High Contrast, Dark Background**
```
Product photograph of a black walnut coffee table against a deep charcoal background, studio 3-point lighting — key light at 45 degrees skimming the surface to reveal grain figure, the walnut showing rich chocolate brown to purple-black heartwood variation, hand-rubbed oil finish, tapered legs, clean minimal-gallery mood, deep dof f/11, no props
```

**H3 — Mortise-and-Tenon Detail, Side Light**
```
Close-up macro of the apron-to-leg joint on a white oak coffee table, the through-tenon protruding slightly past the leg face with a contrasting walnut wedge driven in, side-raking light emphasizing the grain transition between apron and leg, shallow dof f/2.0, warm linen cloth softly out of focus in background, intimate-craft mood
```

**H4 — Breadboard End Detail, Natural Light**
```
Eye-level profile shot of the short end of a coffee table, focusing on the breadboard end connection — the breadboard piece slightly proud of the tabletop face, figure-8 fastener slots visible on underside (optional), natural window light, ray-fleck oak surface catching the light, mid dof, warm workshop linen background, bold-product mood
```

**H5 — Ash Table, Raw Workshop Context**
```
45-degree overhead view of an ash coffee table top resting on sawhorses in a workshop, surface at the 220-grit final sanding stage — orbital sander sitting on the bench in background, ash showing open pore texture and cathedral grain, harsh overhead shop light with a warm tungsten practical lamp adding fill, deep dof, rustic-workshop mood
```

### Step Illustration Set

**Step 1 — Dimensioning Lumber**
```
Workshop scene: a white oak board passing through a thickness planer — machine in foreground, shavings ejecting from the discharge chute, the board surface showing the freshly planed face, overhead workshop fluorescent light, mid dof, rustic-workshop mood
```

**Step 2 — Laying Out Mortise Locations**
```
Close-up overhead of a table leg blank on a bench, a marking gauge scribing the mortise outline — pencil lines visible, the leg held in a bench vise, natural window light, shallow dof on the marking gauge pin, intimate-craft mood
```

**Step 3 — Chopping Mortises**
```
Eye-level workshop photograph of a leg clamped to a bench with a hollow-chisel mortiser positioned over it, mortise cavity half-excavated, clean chisel walls visible, oak shavings in the cavity, side-raking light, mid dof, rustic-workshop mood
```

**Step 4 — Cutting Tenons at the Table Saw**
```
45-degree view of a table saw with a tenoning jig holding an apron board vertically, the blade making the cheek cut on a white oak tenon — sawdust at the blade, workshop background with tool rack, mid dof, bold-product mood
```

**Step 5 — Dry-Fitting the Base**
```
Workshop bench overview: all four legs and aprons of a coffee table base dry-fitted and standing upright without glue — the through-tenons visible at the top of each leg, a square sitting on the apron to check for square, natural window light, deep dof, intimate-craft mood
```

**Step 6 — Final Oiled Surface**
```
Macro close-up of a white oak tabletop surface after the first coat of hardwax oil — the grain deeply saturated, ray-fleck silver and gold visible, the surface reflecting soft window light, a wadded oil-soaked cloth at the edge of frame, shallow dof f/2.0, golden-hour warm tone, earthy-organic mood
```

### B-Roll Loop Descriptions

**B1 — Planer Shavings Ribbon**
```yaml
id: B1
label: Continuous ribbon shaving from planer
description: >
  Low-angle close-up at the outfeed side of a thickness planer: a white oak board emerging with a continuous ribbon shaving curling upward off the cutterhead, backlit by a warm work light so the shaving glows translucent amber. Camera locked, 120fps playback. 6-second loop: board exits frame, cut seamless to the moment the next pass begins.
motion_type: static-with-action
duration_sec: 6
```

**B2 — Through-Tenon Wedge Drive**
```yaml
id: B2
label: Walnut wedge driven into through-tenon
description: >
  Macro static shot: a through-tenon protruding from an oak leg, a contrasting walnut wedge being tapped in with a wooden mallet in slow motion — each mallet blow causing the wedge to advance slightly, the oak grain around the mortise showing slight compression stress. Side-raking light, very shallow dof on the wedge face. 4-second loop.
motion_type: static-with-action
duration_sec: 4
```

**B3 — Surface Grain Reveal Pan**
```yaml
id: B3
label: Camera pans across oiled oak surface
description: >
  Slow lateral pan at tabletop height across the surface of a finished white oak coffee table, side-raking golden-hour light from the right — the ray-fleck and open grain structure catching the light as the camera moves left to right, shallow dof so only the leading edge is sharp, warm linen background. 8-second loop, smooth motorized slider move.
motion_type: pan
duration_sec: 8
```

---

## Project: Picture Frame

```yaml
project_type: picture_frame
slug: generic-picture-frame

wood_species: [white_oak, walnut, maple, cherry, poplar_painted]
joinery_method: "45-degree mitered corners with spline or biscuit reinforcement; rabbet on interior edge for glazing/backing"
finish_stages: [raw_moulding, profile_routed, mitered, glued_assembled, sanded_220, stained_or_painted, finish_coated]
lighting_setup: overhead-diffuse
style_tokens:
  camera: overhead flat-lay
  dof: deep
  background: warm linen textile
  mood: minimal-gallery
```

### Hero Image Prompts

**H1 — Walnut Frame, Miter Detail, White Background**
```
Overhead flat-lay of a completed walnut picture frame on white seamless paper, the miter joint at the lower-right corner closest to camera — book-matched grain across the miter line, high-gloss lacquer finish showing a deep reflection of the studio softbox above, no glazing or art inside, shadow subtle on left, deep dof f/16, minimal-gallery mood, bold-product style
```

**H2 — Oak Frame with Art, Lifestyle Setting**
```
45-degree three-quarter view of a white oak picture frame hanging on a white plaster wall, holding a botanical watercolor print, ray-fleck pattern in the oak moulding catching directional natural window light from the left, warm afternoon sunlight, the frame casting a gentle shadow on the wall, mid dof f/5.6, minimal-gallery mood
```

**H3 — Spline Miter Exploded View, Workshop**
```
Workshop bench flat-lay showing an oak picture frame at the mitered corner glue-up stage — two frame sticks at a perfect 45-degree meeting, a thin walnut spline sitting in the glue-covered slot, a band clamp loosely surrounding the assembly, wood glue squeeze-out visible, overhead-diffuse bench light, mid dof, intimate-craft mood
```

**H4 — Cherry Frame, Golden-Hour Glow**
```
Eye-level profile of a cherry picture frame propped against a linen-covered surface, the warm cherry tone catching golden-hour light from the right — the profile moulding casting shadows that reveal the ogee curve, danish oil finish bringing out the warm red tones of the cherry, shallow dof f/2.8, earthy-organic mood
```

### Step Illustration Set

**Step 1 — Routing the Moulding Profile**
```
Workshop photograph of a router table with a cherry or oak board being run past an ogee or cove bit, the profile emerging along the edge — router fence visible, bit guard in place, profile clearly showing on the trailing portion of the board, overhead-diffuse shop light, mid dof, rustic-workshop mood
```

**Step 2 — Routing the Rabbet**
```
Close-up eye-level of the router table with the board flipped to cut the glazing rabbet on the interior edge — rabbet bit visible, the L-shaped channel freshly cut in the oak, shavings on the table surface, side-raking workshop light, shallow dof on the rabbet corner, intimate-craft mood
```

**Step 3 — Mitering at the Chop Saw**
```
45-degree view of a compound miter saw with a picture frame moulding stick clamped at 45 degrees, the blade in the down position having just completed the cut — two freshly cut miter faces visible, sawdust on the base, workshop background, overhead shop light, mid dof, rustic-workshop mood
```

**Step 4 — Spline Slot on Router Table**
```
Macro close-up of the mitered corner of a picture frame being run across a slot-cutting bit on the router table, the slot appearing centered in the miter face — bit visible, the thin slot just created, oak grain on the miter face, side-raking light, shallow dof, intimate-craft mood
```

**Step 5 — Glue-Up with Band Clamp**
```
Workshop bench overhead view of a picture frame mid-glue-up: all four corners mitered, splines inserted with glue, a band clamp (ratchet strap or frame clamp) wrapped around the full assembly drawing all four corners tight simultaneously — glue squeeze-out at each miter, linen cloth protecting the bench, overhead-diffuse light, deep dof, intimate-craft mood
```

**Step 6 — Finish Coat Application**
```
Close-up macro of a soft brush applying a final lacquer or varnish coat to the moulding profile of an assembled walnut frame — the brush loaded with finish, the profile catching a wet gloss reflection, the grain fully raised and filled, overhead-diffuse studio light, shallow dof on the brush tip, minimal-gallery mood
```

### B-Roll Loop Descriptions

**B1 — Miter Cut Dust Burst**
```yaml
id: B1
label: Slow-motion miter saw cut through oak moulding
description: >
  Front-angle close-up of a miter saw blade descending through an oak picture frame moulding at 45 degrees — 120fps so the sawdust cloud fans out in slow motion, the blade teeth visible, the two cut faces separating perfectly flat. Backlit by a single warm work lamp so the dust cloud glows. 4-second loop at the cut moment.
motion_type: static-with-action
duration_sec: 4
```

**B2 — Corner Squeeze-Out Wipe**
```yaml
id: B2
label: Glue squeeze-out wiped from miter corner
description: >
  Macro push-in on a freshly glued walnut miter corner held in a clamp: a damp cloth being used to wipe the PVA glue squeeze-out — the glue smearing and being removed to reveal the tight miter line, warm bench lamp, very shallow dof, slow deliberate hand motion. 6-second loop.
motion_type: push-in
duration_sec: 6
```

**B3 — Frame Reflection Turntable**
```yaml
id: B3
label: Lacquered frame orbiting on turntable
description: >
  Camera locked low at 20-degree elevation, a completed high-gloss lacquered walnut picture frame on a slow motorized turntable — overhead studio softbox reflects as a white highlight stripe that travels around the frame as it rotates, the grain and miter joints cycling into view. 8-second full rotation loop.
motion_type: orbit
duration_sec: 8
```

---

## Worked Example A: Walnut Segmented Bowl (Turning)

> **Validates:** Woodturning template  
> **Wood species:** Black walnut (primary), hard maple (accent rings)  
> **Joinery:** Segmented ring glue-up (24 segments per ring, 8 rings), face-plate mounted, no traditional joinery  
> **Finish stage progression:** rough blank → rough turned → finish turned → 400-grit sanded → danish oil × 3 coats → paste wax  
> **Lighting setup:** side-raking for texture reveals; studio-3pt for final hero

---

### Hero Images — Walnut Segmented Bowl

**H1 — Mid-Turn, Shavings Flying, Workshop Atmosphere**
```
Product/process photograph: a walnut segmented bowl on the lathe mid-turning, the alternating dark walnut and light maple rings just starting to emerge as the tool removes the rough exterior — lathe in background slightly out of focus, workshop bench visible, dramatic side-raking light from the LEFT at roughly 15 degrees from horizontal, casting deep shadow into the shaving pile below, the bowl diameter approximately 10 inches, 45-degree three-quarter camera angle, mid depth of field f/5.6, warm tungsten workshop light at 3200K, mood: intimate workshop craft, photorealistic, not illustrated
```

**H2 — Finish-Turned Dry, Before Oil**
```
Studio still-life photograph of a finish-turned walnut and maple segmented bowl resting on a worn pine workbench — the ring pattern clearly defined: alternating wide dark walnut rings and narrow maple accent rings, surface at 400-grit final sand showing a satin matte appearance, dramatic single side-raking light revealing the slight tooling marks and the open end-grain of each walnut segment, bowl approximately 4 inches tall × 10 inches diameter, 45-degree three-quarter view, shallow dof f/2.8 keeping the near rim sharp and the far side soft, mood: intimate craft, warm 3000K ambient
```

**H3 — First Oil Coat, Half-and-Half Reveal**
```
Workshop bench photograph of the walnut segmented bowl sitting on a folded shop rag — exactly half the exterior has been wiped with danish oil (showing dramatic deep walnut chocolate and warm maple cream contrast) while the other half remains dry (pale and flat), the oil boundary line running diagonally across the bowl, single natural window light from the right at 45 degrees, mid dof f/5.6, the danish oil rag beside the bowl, warm afternoon color temperature, earthy-organic mood, photorealistic
```

**H4 — Final Wax-Buffed Hero, Dark Background**
```
High-end product photograph of the completed walnut-and-maple segmented bowl after three danish oil coats and paste wax — the surface has a warm satin glow, walnut showing its full chocolate-to-purple variation, maple cream-white in sharp contrast, studio 3-point lighting setup: key light 45-degree camera-right at f/16 equivalent output, fill at 1/4 power opposite, narrow rim light behind to separate bowl from charcoal seamless background, deep dof f/11, bowl centered, minimal-gallery mood, fine art product photography aesthetic
```

**H5 — Overhead Flat-Lay, Linen Background**
```
Overhead flat-lay of the completed segmented bowl on a warm natural linen cloth, the ring pattern creating a spiral/rosette visual when viewed from directly above — walnut and maple rings concentric, the interior hollow visible, overhead-diffuse studio lighting with two equal softboxes flanking, no shadows, deep dof f/16, centered composition, minimal-gallery mood, the wood grain of each segment visible in the walnut sections
```

---

### Step Illustrations — Walnut Segmented Bowl

**Step 1 — Segment Cutting**
```
Workshop overhead close-up on a table saw sled: a walnut board being crosscut into trapezoid segments for ring assembly — the sled angled at 7.5 degrees (for 24-segment rings), fresh cut end-grain visible on the forward segment, sawdust on the sled surface, overhead shop fluorescent light, mid dof f/8, no hands needed, intimate-craft mood, label space for "Step 1: Cut 24 segments per ring"
```

**Step 2 — Ring Glue-Up**
```
Workshop bench top-down photograph: 24 walnut trapezoid segments arranged in a ring on a flat surface with rubber band clamps or a hose clamp drawing them together, PVA glue visible at the segment joints, the ring approximately 10 inches outer diameter, one maple accent strip visible at the near side ready to be incorporated into the next ring, overhead-diffuse bench lamp, deep dof, intimate-craft mood, label: "Step 2: Glue up ring assembly"
```

**Step 3 — Ring Sanding Flat on Disk Sander**
```
Eye-level close-up of a glued walnut ring being pressed flat against the face of a large disk sander — the ring face being trued flat for stacking, sawdust at the sander bed, the alternating segment end-grain pattern visible on the ring face, workshop background, mid dof, side-raking shop light, rustic-workshop mood, label: "Step 3: True ring faces flat"
```

**Step 4 — Stack and Glue Rings**
```
Workshop bench 45-degree view of 6 walnut rings stacked and clamped into a rough bowl form — rings glued and alternating with thin maple accent rings, bar clamps top and bottom drawing them together, the segmented pattern visible on the exterior of the stack, wood glue squeeze-out between rings, pine bench background, mid dof f/5.6, intimate-craft mood, label: "Step 4: Stack and glue all rings"
```

**Step 5 — Rough Turning Exterior**
```
Lathe in-action photograph: the stacked bowl blank mounted on a faceplate, being rough-turned with a bowl gouge — the exterior being brought to a round cylinder, tool marks spiraling the surface, walnut and maple bands starting to emerge through the rough exterior, workshop background, side-raking light, mid dof, warm tungsten ambient, label: "Step 5: Rough turn to round"
```

**Step 6 — Final Finish Turn and Interior Hollow**
```
45-degree workshop photograph of the bowl on the lathe at the finish-turning stage — exterior nearly final form showing crisp ring transitions, the interior being hollowed with a swept-back bowl gouge entering the cavity, fine shavings curling, the wall thickness now approximately 1/4 inch visible at the rim, side-raking light catching the segmented pattern, shallow dof on the rim, intimate-craft mood, label: "Step 6: Finish turn and hollow interior"
```

---

### B-Roll Loops — Walnut Segmented Bowl

**B1 — Segment Pattern Reveal (Turntable)**
```yaml
id: B1
label: Segmented pattern revealed as bowl rotates
description: >
  Camera locked at 30-degree elevation, 45 degrees to the side — the completed walnut-maple segmented bowl on a slow turntable, 8-second full rotation. Studio side light at 20 degrees raking across the surface. As the bowl rotates, the alternating dark walnut and pale maple segments catch the light differently — dark faces going matte, light faces going bright. The segment joints create a subtle geometric shadow network that travels across the surface. Shallow dof f/2.8 on the nearest face. Minimal-gallery mood.
motion_type: orbit
duration_sec: 8
```

**B2 — Shavings Off the Segmented Blank**
```yaml
id: B2
label: First cuts revealing the ring pattern
description: >
  Static close-up at lathe height — a bowl gouge making a light roughing cut across the glued-up segmented blank, the blade crossing from the rough exterior into the emerging ring pattern. Each pass of the gouge reveals another layer of walnut and maple. Filmed at 120fps, played back at 24fps — shavings hang in slow motion. Backlit with a single warm tungsten spot so the shavings glow translucent. 6-second loop.
motion_type: static-with-action
duration_sec: 6
```

**B3 — Oil Absorption Macro**
```yaml
id: B3
label: Danish oil soaking into walnut end-grain segments
description: >
  Extreme macro on the end-grain surface of one walnut segment on the bowl exterior as a drop of danish oil is placed and begins to absorb — the open pores of the walnut visibly drinking the oil, color deepening from pale tan to dark chocolate in real time, side-raking light, very shallow dof so only the oil droplet and immediate grain are sharp. 4-second loop: droplet placed, absorbed, color deepened, cut to next droplet.
motion_type: static-with-action
duration_sec: 4
```

---

## Worked Example B: Oak Picture Frame (Joinery)

> **Validates:** Picture Frame template  
> **Wood species:** White oak (primary), thin walnut spline inlay at corners  
> **Joinery:** 45-degree mitered corners with 1/8" walnut spline reinforcement; 3/8" rabbet on interior for glazing/backing  
> **Finish stage progression:** raw oak moulding → profile routed → rabbet routed → mitered → spline slotted → glued with band clamp → 220-grit sanded → fumed ammonia darkening → hardwax oil finish  
> **Lighting setup:** overhead-diffuse for flat-lay steps; window-natural for lifestyle hero

---

### Hero Images — Oak Picture Frame

**H1 — Ammonia-Fumed Oak Frame, Lifestyle Wall Shot**
```
Lifestyle photograph of a white oak picture frame hanging on a white-painted plaster wall — the oak moulding ammonia-fumed to a medium grey-brown tone that emphasizes the ray-fleck silver pattern, the frame holding a simple black-and-white architectural photograph, directional natural window light from the camera-left wall casting a soft shadow to the right of the frame, the moulding profile an ogee curve approximately 1.5 inches wide, frame size approximately 11×14 inches, mid dof f/5.6, minimal-gallery mood, afternoon light 4500K
```

**H2 — Spline Miter Corner Macro**
```
Extreme close-up macro of one mitered corner of the white oak picture frame after final finishing — the 45-degree miter line running diagonally through frame, the thin walnut spline visible as a 1/8-inch dark stripe centered on the miter, ammonia-fumed oak showing silvery ray-fleck at the miter face, hardwax oil giving a low-sheen glow, overhead-diffuse studio light, shallow dof f/1.8 so only the spline is sharp, bold-product mood, charcoal seamless background
```

**H3 — Frame Flat-Lay Components, Pre-Assembly**
```
Overhead flat-lay on warm linen cloth: all four picture frame sticks already mitered and profiled but not yet glued — arranged as a square with corners touching but not clamped, the rabbet channel visible on interior edges, walnut splines sitting in the slots at each corner, thin gaps at the miter joints, overhead-diffuse soft studio light, deep dof f/16, minimal-gallery mood, label space at bottom
```

**H4 — Frame with Glazing Installed, Studio Product**
```
Studio product photograph of the completed oak frame with glazing (glass or acrylic) installed in the rabbet — the glass catching a soft overhead reflection, the fumed oak moulding contrasting with the silvery glass surface, frame standing upright propped on a small easel on a charcoal surface, studio 3-point lighting, mid dof f/8, bold-product mood, the moulding profile casting a subtle shadow onto the glass surface
```

---

### Step Illustrations — Oak Picture Frame

**Step 1 — Routing the Moulding Profile**
```
Workshop photograph at router table: a white oak board (1.5 inches wide × 3/4 inch thick) being run past an ogee router bit, the profile emerging cleanly on the top edge — bit guard in place, router fence set, the profile shape an S-curve ogee, fresh oak shavings curling away, overhead-diffuse shop light, mid dof, rustic-workshop mood, label: "Step 1: Route moulding profile"
```

**Step 2 — Routing the Glazing Rabbet**
```
Close-up at router table: the profiled oak moulding board flipped on its side, a straight bit cutting the glazing rabbet — the L-shaped channel 3/8" deep × 3/8" wide on the inside back edge, the profile face down on the router table surface, rabbet emerging cleanly, side-raking workshop light, shallow dof, intimate-craft mood, label: "Step 2: Route interior rabbet"
```

**Step 3 — Mitering Corners at Chop Saw**
```
Workshop 45-degree view: a compound miter saw with the oak moulding piece clamped, blade at 45 degrees, a fresh cut face visible — the mitered end showing the ogee profile in cross-section, the rabbet corner on the interior edge of the miter face, sawdust on the saw base, overhead shop light, mid dof, rustic-workshop mood, label: "Step 3: Miter all four corners at 45°"
```

**Step 4 — Cutting Spline Slots**
```
Macro close-up at router table: the mitered end of an oak frame piece being held vertically against a fence, a slot-cutting bit creating the 1/8-inch slot centered in the 45-degree miter face — the slot visible as a dark line in the warm oak miter face, shallow dof, side-raking workshop light, intimate-craft mood, label: "Step 4: Slot miter faces for walnut spline"
```

**Step 5 — Glue-Up with Band Clamp**
```
Workshop bench overhead-angle photograph: the four oak frame pieces arranged as a square with all four walnut splines seated in the glue-covered slots, a ratchet band clamp wrapped around the entire frame tightening all four corners simultaneously — glue squeeze-out at each miter corner, a square tool resting beside the frame to verify geometry, linen cloth on bench, overhead-diffuse light, mid dof f/8, intimate-craft mood, label: "Step 5: Glue up all four corners simultaneously"
```

**Step 6 — Fumed Finish and Final Coat**
```
Workshop bench still-life: the assembled oak frame resting flat on a folded linen cloth, the ammonia-fumed tone making the oak a warm grey-brown with vivid silver ray-fleck showing, a small jar of hardwax oil and a folded applicator pad beside the frame, window light from the right, mid dof f/5.6, the moulding profile casting an interior shadow, earthy-organic mood, label: "Step 6: Fume with ammonia + hardwax oil finish"
```

---

### B-Roll Loops — Oak Picture Frame

**B1 — Ammonia Fuming Color Change Time-Lapse**
```yaml
id: B1
label: Oak darkening under ammonia fumes
description: >
  Time-lapse overhead view of an oak picture frame moulding stick inside a fuming tent (plastic bag or bin, edges visible), the surface visibly transitioning from pale creamy raw oak to warm grey-brown over 4 hours of real time compressed to 4 seconds — the ray-fleck pattern emerging as the tannins react, overhead-diffuse light, deep dof. Cut loop: start pale, end fumed, seamless return.
motion_type: time-lapse
duration_sec: 4
```

**B2 — Spline Seated in Corner**
```yaml
id: B2
label: Walnut spline pressed into oak miter slot
description: >
  Macro push-in: two mitered oak frame pieces meeting at a corner, a thin walnut spline being pressed into the glue-coated slot with thumb pressure — the dark walnut spline centering itself in the pale oak miter faces, glue squeeze-out appearing along the slot edges. Very shallow dof on the spline tip, side-raking warm bench lamp, 6-second loop at the moment the spline seats fully flush.
motion_type: push-in
duration_sec: 6
```

**B3 — Ray-Fleck Surface Pan**
```yaml
id: B3
label: Camera slides across fumed oak surface revealing ray-fleck
description: >
  Slow lateral slider pan at tabletop level across the face of the completed oak frame moulding after fuming and oil finish — the camera moving left to right, side-raking window light from the right causing the silver ray-fleck medullary rays to alternately light up and dim as the angle changes. Very shallow dof f/2.0 on the leading edge of the frame face. 8-second loop on a smooth motorized slider.
motion_type: pan
duration_sec: 8
```

---

## Agy Handoff Notes

### For Issue #4 (Hero/Step Images)
- Use the `hero_prompts` and `step_set` sections from each project.
- Append global style suffix to every prompt: `photorealistic, Canon R5 equivalent quality, no AI artifacts, no text overlays, no watermarks`
- For hero images, specify final output size: `landscape 3:2 for full-bleed, or 4:5 for social`
- For step illustrations, specify: `square 1:1, consistent light direction across all steps in a set`

### For Issue #5 (B-Roll Motion Loops)
- Use the `broll_loops` sections from each project.
- All loops should specify: `ProRes 4444, 4K UHD 3840×2160, 24fps output (slow-motion source at 120fps where noted)`
- Color grade target: `warm neutral, slightly lifted blacks, no blue cast, matching Kodak Portra 400 film reference`
- Loop validation: test seamless loop point before final delivery

### Prompt Injection Pattern
For any gen-burn pipeline consuming this pack, the recommended prompt structure is:

```
{hero_prompt_text}, {style_tokens.camera} angle, {style_tokens.dof} depth of field, {style_tokens.background} background, {style_tokens.mood} mood, photorealistic, no text, no watermark, 4K
```

Example fully-assembled prompt:
```
Product photograph of a hand-turned walnut bowl on a worn pine workbench, freshly finish-turned with tool marks still faintly visible on the interior, dramatic raking side light from the left casting long shadows that reveal the end-grain figure, 45-degree three-quarter angle, shallow depth of field f/2.8, workshop bench raw pine background, intimate-craft mood, photorealistic, no text, no watermark, 4K
```
