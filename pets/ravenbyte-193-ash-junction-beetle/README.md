# Ash Junction Beetle

<p align="center">
  <img src="previews/ravenbyte-193-ash-junction-beetle-showcase.gif" width="360" alt="Ash Junction Beetle stitched multi-motion showcase">
</p>

**A beetle-class Ravenbyte familiar that keeps junction work moving during long coding runs.**

Ash Junction Beetle is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around antenna beetle slab robot with code-shell wing plates, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Ash Junction Beetle brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-193-ash-junction-beetle-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-193-ash-junction-beetle-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-193-ash-junction-beetle-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-193-ash-junction-beetle-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-193-ash-junction-beetle-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-193-ash-junction-beetle-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-193-ash-junction-beetle-waiting.gif) |
| Running | ![Running](previews/ravenbyte-193-ash-junction-beetle-running.gif) |
| Review | ![Review](previews/ravenbyte-193-ash-junction-beetle-review.gif) |

Full contact sheet:

![Ash Junction Beetle contact sheet](previews/ravenbyte-193-ash-junction-beetle-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-193-ash-junction-beetle
```

Or from anywhere with Git:

```bash
PET=ravenbyte-193-ash-junction-beetle; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-193-ash-junction-beetle/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-193-ash-junction-beetle-showcase.gif
  ravenbyte-193-ash-junction-beetle-idle.gif
  ravenbyte-193-ash-junction-beetle-running-right.gif
  ravenbyte-193-ash-junction-beetle-running-left.gif
  ravenbyte-193-ash-junction-beetle-waving.gif
  ravenbyte-193-ash-junction-beetle-jumping.gif
  ravenbyte-193-ash-junction-beetle-failed.gif
  ravenbyte-193-ash-junction-beetle-waiting.gif
  ravenbyte-193-ash-junction-beetle-running.gif
  ravenbyte-193-ash-junction-beetle-review.gif
  ravenbyte-193-ash-junction-beetle-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from antenna beetle slab robot with code-shell wing plates, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
