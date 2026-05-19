# Zephyr Zenith Mask

<p align="center">
  <img src="previews/ravenbyte-378-zephyr-zenith-mask-showcase.gif" width="360" alt="Zephyr Zenith Mask stitched multi-motion showcase">
</p>

**A mask-class Ravenbyte familiar that keeps zenith work moving during long coding runs.**

Zephyr Zenith Mask is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around split-mask imp familiar with two-tone review face, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Zephyr Zenith Mask brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-378-zephyr-zenith-mask-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-378-zephyr-zenith-mask-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-378-zephyr-zenith-mask-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-378-zephyr-zenith-mask-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-378-zephyr-zenith-mask-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-378-zephyr-zenith-mask-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-378-zephyr-zenith-mask-waiting.gif) |
| Running | ![Running](previews/ravenbyte-378-zephyr-zenith-mask-running.gif) |
| Review | ![Review](previews/ravenbyte-378-zephyr-zenith-mask-review.gif) |

Full contact sheet:

![Zephyr Zenith Mask contact sheet](previews/ravenbyte-378-zephyr-zenith-mask-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-378-zephyr-zenith-mask
```

Or from anywhere with Git:

```bash
PET=ravenbyte-378-zephyr-zenith-mask; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-378-zephyr-zenith-mask/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-378-zephyr-zenith-mask-showcase.gif
  ravenbyte-378-zephyr-zenith-mask-idle.gif
  ravenbyte-378-zephyr-zenith-mask-running-right.gif
  ravenbyte-378-zephyr-zenith-mask-running-left.gif
  ravenbyte-378-zephyr-zenith-mask-waving.gif
  ravenbyte-378-zephyr-zenith-mask-jumping.gif
  ravenbyte-378-zephyr-zenith-mask-failed.gif
  ravenbyte-378-zephyr-zenith-mask-waiting.gif
  ravenbyte-378-zephyr-zenith-mask-running.gif
  ravenbyte-378-zephyr-zenith-mask-review.gif
  ravenbyte-378-zephyr-zenith-mask-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from split-mask imp familiar with two-tone review face, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
