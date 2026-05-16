# Zephyr Relay Mask

<p align="center">
  <img src="previews/ravenbyte-122-zephyr-relay-mask-showcase.gif" width="360" alt="Zephyr Relay Mask stitched multi-motion showcase">
</p>

**A mask-class Ravenbyte familiar that keeps relay work moving during long coding runs.**

Zephyr Relay Mask is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around split-mask imp familiar with two-tone review face, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Zephyr Relay Mask brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-122-zephyr-relay-mask-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-122-zephyr-relay-mask-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-122-zephyr-relay-mask-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-122-zephyr-relay-mask-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-122-zephyr-relay-mask-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-122-zephyr-relay-mask-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-122-zephyr-relay-mask-waiting.gif) |
| Running | ![Running](previews/ravenbyte-122-zephyr-relay-mask-running.gif) |
| Review | ![Review](previews/ravenbyte-122-zephyr-relay-mask-review.gif) |

Full contact sheet:

![Zephyr Relay Mask contact sheet](previews/ravenbyte-122-zephyr-relay-mask-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-122-zephyr-relay-mask
```

Or from anywhere with Git:

```bash
PET=ravenbyte-122-zephyr-relay-mask; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-122-zephyr-relay-mask/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-122-zephyr-relay-mask-showcase.gif
  ravenbyte-122-zephyr-relay-mask-idle.gif
  ravenbyte-122-zephyr-relay-mask-running-right.gif
  ravenbyte-122-zephyr-relay-mask-running-left.gif
  ravenbyte-122-zephyr-relay-mask-waving.gif
  ravenbyte-122-zephyr-relay-mask-jumping.gif
  ravenbyte-122-zephyr-relay-mask-failed.gif
  ravenbyte-122-zephyr-relay-mask-waiting.gif
  ravenbyte-122-zephyr-relay-mask-running.gif
  ravenbyte-122-zephyr-relay-mask-review.gif
  ravenbyte-122-zephyr-relay-mask-contact-sheet.png
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
