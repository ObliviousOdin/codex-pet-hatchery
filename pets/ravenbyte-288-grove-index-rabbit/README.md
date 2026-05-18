# Grove Index Rabbit

<p align="center">
  <img src="previews/ravenbyte-288-grove-index-rabbit-showcase.gif" width="360" alt="Grove Index Rabbit stitched multi-motion showcase">
</p>

**A rabbit-class Ravenbyte familiar that keeps index work moving during long coding runs.**

Grove Index Rabbit is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around scaffold rabbit bot with long signal ears, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Grove Index Rabbit brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-288-grove-index-rabbit-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-288-grove-index-rabbit-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-288-grove-index-rabbit-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-288-grove-index-rabbit-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-288-grove-index-rabbit-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-288-grove-index-rabbit-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-288-grove-index-rabbit-waiting.gif) |
| Running | ![Running](previews/ravenbyte-288-grove-index-rabbit-running.gif) |
| Review | ![Review](previews/ravenbyte-288-grove-index-rabbit-review.gif) |

Full contact sheet:

![Grove Index Rabbit contact sheet](previews/ravenbyte-288-grove-index-rabbit-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-288-grove-index-rabbit
```

Or from anywhere with Git:

```bash
PET=ravenbyte-288-grove-index-rabbit; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-288-grove-index-rabbit/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-288-grove-index-rabbit-showcase.gif
  ravenbyte-288-grove-index-rabbit-idle.gif
  ravenbyte-288-grove-index-rabbit-running-right.gif
  ravenbyte-288-grove-index-rabbit-running-left.gif
  ravenbyte-288-grove-index-rabbit-waving.gif
  ravenbyte-288-grove-index-rabbit-jumping.gif
  ravenbyte-288-grove-index-rabbit-failed.gif
  ravenbyte-288-grove-index-rabbit-waiting.gif
  ravenbyte-288-grove-index-rabbit-running.gif
  ravenbyte-288-grove-index-rabbit-review.gif
  ravenbyte-288-grove-index-rabbit-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from scaffold rabbit bot with long signal ears, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
