# Glyph Event Crystal

<p align="center">
  <img src="previews/ravenbyte-263-glyph-event-crystal-showcase.gif" width="360" alt="Glyph Event Crystal stitched multi-motion showcase">
</p>

**A crystal-class Ravenbyte familiar that keeps event work moving during long coding runs.**

Glyph Event Crystal is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crystal tripod familiar with facet armor and lint sparks, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Glyph Event Crystal brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-263-glyph-event-crystal-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-263-glyph-event-crystal-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-263-glyph-event-crystal-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-263-glyph-event-crystal-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-263-glyph-event-crystal-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-263-glyph-event-crystal-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-263-glyph-event-crystal-waiting.gif) |
| Running | ![Running](previews/ravenbyte-263-glyph-event-crystal-running.gif) |
| Review | ![Review](previews/ravenbyte-263-glyph-event-crystal-review.gif) |

Full contact sheet:

![Glyph Event Crystal contact sheet](previews/ravenbyte-263-glyph-event-crystal-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-263-glyph-event-crystal
```

Or from anywhere with Git:

```bash
PET=ravenbyte-263-glyph-event-crystal; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-263-glyph-event-crystal/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-263-glyph-event-crystal-showcase.gif
  ravenbyte-263-glyph-event-crystal-idle.gif
  ravenbyte-263-glyph-event-crystal-running-right.gif
  ravenbyte-263-glyph-event-crystal-running-left.gif
  ravenbyte-263-glyph-event-crystal-waving.gif
  ravenbyte-263-glyph-event-crystal-jumping.gif
  ravenbyte-263-glyph-event-crystal-failed.gif
  ravenbyte-263-glyph-event-crystal-waiting.gif
  ravenbyte-263-glyph-event-crystal-running.gif
  ravenbyte-263-glyph-event-crystal-review.gif
  ravenbyte-263-glyph-event-crystal-contact-sheet.png
generated/
  base.png
  imagegen-prompt.json
  strips/*.png
```

## Sprite metadata

- Frame size: `64×64`
- Frames per row: `6`
- Rows: `9`
- Spritesheet: `384×576`
- Symmetric design: no
- `running-left`: drawn as a separate row because this familiar has side-specific details
- Author: `ObliviousOdin`

## Design notes

The design is intentionally original. It uses broad visual language from crystal tripod familiar with facet armor and lint sparks, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
