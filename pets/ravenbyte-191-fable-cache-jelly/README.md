# Fable Cache Jelly

<p align="center">
  <img src="previews/ravenbyte-191-fable-cache-jelly-showcase.gif" width="360" alt="Fable Cache Jelly stitched multi-motion showcase">
</p>

**A jelly-class Ravenbyte familiar that keeps cache work moving during long coding runs.**

Fable Cache Jelly is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around bell jellyfish familiar with dangling trace tendrils, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Fable Cache Jelly brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-191-fable-cache-jelly-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-191-fable-cache-jelly-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-191-fable-cache-jelly-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-191-fable-cache-jelly-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-191-fable-cache-jelly-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-191-fable-cache-jelly-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-191-fable-cache-jelly-waiting.gif) |
| Running | ![Running](previews/ravenbyte-191-fable-cache-jelly-running.gif) |
| Review | ![Review](previews/ravenbyte-191-fable-cache-jelly-review.gif) |

Full contact sheet:

![Fable Cache Jelly contact sheet](previews/ravenbyte-191-fable-cache-jelly-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-191-fable-cache-jelly
```

Or from anywhere with Git:

```bash
PET=ravenbyte-191-fable-cache-jelly; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-191-fable-cache-jelly/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-191-fable-cache-jelly-showcase.gif
  ravenbyte-191-fable-cache-jelly-idle.gif
  ravenbyte-191-fable-cache-jelly-running-right.gif
  ravenbyte-191-fable-cache-jelly-running-left.gif
  ravenbyte-191-fable-cache-jelly-waving.gif
  ravenbyte-191-fable-cache-jelly-jumping.gif
  ravenbyte-191-fable-cache-jelly-failed.gif
  ravenbyte-191-fable-cache-jelly-waiting.gif
  ravenbyte-191-fable-cache-jelly-running.gif
  ravenbyte-191-fable-cache-jelly-review.gif
  ravenbyte-191-fable-cache-jelly-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from bell jellyfish familiar with dangling trace tendrils, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
