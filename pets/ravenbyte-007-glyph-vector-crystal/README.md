# Glyph Vector Crystal

<p align="center">
  <img src="previews/ravenbyte-007-glyph-vector-crystal-showcase.gif" width="360" alt="Glyph Vector Crystal stitched multi-motion showcase">
</p>

**A crystal-class Ravenbyte familiar that keeps vector work moving during long coding runs.**

Glyph Vector Crystal is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crystal tripod familiar with facet armor and lint sparks, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Glyph Vector Crystal brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-007-glyph-vector-crystal-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-007-glyph-vector-crystal-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-007-glyph-vector-crystal-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-007-glyph-vector-crystal-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-007-glyph-vector-crystal-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-007-glyph-vector-crystal-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-007-glyph-vector-crystal-waiting.gif) |
| Running | ![Running](previews/ravenbyte-007-glyph-vector-crystal-running.gif) |
| Review | ![Review](previews/ravenbyte-007-glyph-vector-crystal-review.gif) |

Full contact sheet:

![Glyph Vector Crystal contact sheet](previews/ravenbyte-007-glyph-vector-crystal-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-007-glyph-vector-crystal
```

Or from anywhere with Git:

```bash
PET=ravenbyte-007-glyph-vector-crystal; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-007-glyph-vector-crystal/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-007-glyph-vector-crystal-showcase.gif
  ravenbyte-007-glyph-vector-crystal-idle.gif
  ravenbyte-007-glyph-vector-crystal-running-right.gif
  ravenbyte-007-glyph-vector-crystal-running-left.gif
  ravenbyte-007-glyph-vector-crystal-waving.gif
  ravenbyte-007-glyph-vector-crystal-jumping.gif
  ravenbyte-007-glyph-vector-crystal-failed.gif
  ravenbyte-007-glyph-vector-crystal-waiting.gif
  ravenbyte-007-glyph-vector-crystal-running.gif
  ravenbyte-007-glyph-vector-crystal-review.gif
  ravenbyte-007-glyph-vector-crystal-contact-sheet.png
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
