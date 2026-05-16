# Lumen Index Manta

<p align="center">
  <img src="previews/ravenbyte-140-lumen-index-manta-showcase.gif" width="360" alt="Lumen Index Manta stitched multi-motion showcase">
</p>

**A manta-class Ravenbyte familiar that keeps index work moving during long coding runs.**

Lumen Index Manta is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around manta glider bot with quiet night-shift wings, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Lumen Index Manta brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-140-lumen-index-manta-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-140-lumen-index-manta-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-140-lumen-index-manta-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-140-lumen-index-manta-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-140-lumen-index-manta-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-140-lumen-index-manta-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-140-lumen-index-manta-waiting.gif) |
| Running | ![Running](previews/ravenbyte-140-lumen-index-manta-running.gif) |
| Review | ![Review](previews/ravenbyte-140-lumen-index-manta-review.gif) |

Full contact sheet:

![Lumen Index Manta contact sheet](previews/ravenbyte-140-lumen-index-manta-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-140-lumen-index-manta
```

Or from anywhere with Git:

```bash
PET=ravenbyte-140-lumen-index-manta; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-140-lumen-index-manta/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-140-lumen-index-manta-showcase.gif
  ravenbyte-140-lumen-index-manta-idle.gif
  ravenbyte-140-lumen-index-manta-running-right.gif
  ravenbyte-140-lumen-index-manta-running-left.gif
  ravenbyte-140-lumen-index-manta-waving.gif
  ravenbyte-140-lumen-index-manta-jumping.gif
  ravenbyte-140-lumen-index-manta-failed.gif
  ravenbyte-140-lumen-index-manta-waiting.gif
  ravenbyte-140-lumen-index-manta-running.gif
  ravenbyte-140-lumen-index-manta-review.gif
  ravenbyte-140-lumen-index-manta-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from manta glider bot with quiet night-shift wings, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
