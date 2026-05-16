# Rune Zenith Lantern

<p align="center">
  <img src="previews/ravenbyte-114-rune-zenith-lantern-showcase.gif" width="360" alt="Rune Zenith Lantern stitched multi-motion showcase">
</p>

**A lantern-class Ravenbyte familiar that keeps zenith work moving during long coding runs.**

Rune Zenith Lantern is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around floating lantern stack spirit with tiny build lights, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Rune Zenith Lantern brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-114-rune-zenith-lantern-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-114-rune-zenith-lantern-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-114-rune-zenith-lantern-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-114-rune-zenith-lantern-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-114-rune-zenith-lantern-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-114-rune-zenith-lantern-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-114-rune-zenith-lantern-waiting.gif) |
| Running | ![Running](previews/ravenbyte-114-rune-zenith-lantern-running.gif) |
| Review | ![Review](previews/ravenbyte-114-rune-zenith-lantern-review.gif) |

Full contact sheet:

![Rune Zenith Lantern contact sheet](previews/ravenbyte-114-rune-zenith-lantern-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-114-rune-zenith-lantern
```

Or from anywhere with Git:

```bash
PET=ravenbyte-114-rune-zenith-lantern; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-114-rune-zenith-lantern/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-114-rune-zenith-lantern-showcase.gif
  ravenbyte-114-rune-zenith-lantern-idle.gif
  ravenbyte-114-rune-zenith-lantern-running-right.gif
  ravenbyte-114-rune-zenith-lantern-running-left.gif
  ravenbyte-114-rune-zenith-lantern-waving.gif
  ravenbyte-114-rune-zenith-lantern-jumping.gif
  ravenbyte-114-rune-zenith-lantern-failed.gif
  ravenbyte-114-rune-zenith-lantern-waiting.gif
  ravenbyte-114-rune-zenith-lantern-running.gif
  ravenbyte-114-rune-zenith-lantern-review.gif
  ravenbyte-114-rune-zenith-lantern-contact-sheet.png
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
