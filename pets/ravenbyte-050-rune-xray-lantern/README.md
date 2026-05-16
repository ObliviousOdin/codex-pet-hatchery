# Rune Xray Lantern

<p align="center">
  <img src="previews/ravenbyte-050-rune-xray-lantern-showcase.gif" width="360" alt="Rune Xray Lantern stitched multi-motion showcase">
</p>

**A lantern-class Ravenbyte familiar that keeps xray work moving during long coding runs.**

Rune Xray Lantern is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around floating lantern stack spirit with tiny build lights, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Rune Xray Lantern brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-050-rune-xray-lantern-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-050-rune-xray-lantern-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-050-rune-xray-lantern-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-050-rune-xray-lantern-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-050-rune-xray-lantern-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-050-rune-xray-lantern-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-050-rune-xray-lantern-waiting.gif) |
| Running | ![Running](previews/ravenbyte-050-rune-xray-lantern-running.gif) |
| Review | ![Review](previews/ravenbyte-050-rune-xray-lantern-review.gif) |

Full contact sheet:

![Rune Xray Lantern contact sheet](previews/ravenbyte-050-rune-xray-lantern-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-050-rune-xray-lantern
```

Or from anywhere with Git:

```bash
PET=ravenbyte-050-rune-xray-lantern; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-050-rune-xray-lantern/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-050-rune-xray-lantern-showcase.gif
  ravenbyte-050-rune-xray-lantern-idle.gif
  ravenbyte-050-rune-xray-lantern-running-right.gif
  ravenbyte-050-rune-xray-lantern-running-left.gif
  ravenbyte-050-rune-xray-lantern-waving.gif
  ravenbyte-050-rune-xray-lantern-jumping.gif
  ravenbyte-050-rune-xray-lantern-failed.gif
  ravenbyte-050-rune-xray-lantern-waiting.gif
  ravenbyte-050-rune-xray-lantern-running.gif
  ravenbyte-050-rune-xray-lantern-review.gif
  ravenbyte-050-rune-xray-lantern-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from floating lantern stack spirit with tiny build lights, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
