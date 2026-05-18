# Tundra Engine Kite

<p align="center">
  <img src="previews/ravenbyte-276-tundra-engine-kite-showcase.gif" width="360" alt="Tundra Engine Kite stitched multi-motion showcase">
</p>

**A kite-class Ravenbyte familiar that keeps engine work moving during long coding runs.**

Tundra Engine Kite is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crescent kite drone with asymmetric review wing, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Tundra Engine Kite brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-276-tundra-engine-kite-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-276-tundra-engine-kite-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-276-tundra-engine-kite-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-276-tundra-engine-kite-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-276-tundra-engine-kite-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-276-tundra-engine-kite-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-276-tundra-engine-kite-waiting.gif) |
| Running | ![Running](previews/ravenbyte-276-tundra-engine-kite-running.gif) |
| Review | ![Review](previews/ravenbyte-276-tundra-engine-kite-review.gif) |

Full contact sheet:

![Tundra Engine Kite contact sheet](previews/ravenbyte-276-tundra-engine-kite-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-276-tundra-engine-kite
```

Or from anywhere with Git:

```bash
PET=ravenbyte-276-tundra-engine-kite; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-276-tundra-engine-kite/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-276-tundra-engine-kite-showcase.gif
  ravenbyte-276-tundra-engine-kite-idle.gif
  ravenbyte-276-tundra-engine-kite-running-right.gif
  ravenbyte-276-tundra-engine-kite-running-left.gif
  ravenbyte-276-tundra-engine-kite-waving.gif
  ravenbyte-276-tundra-engine-kite-jumping.gif
  ravenbyte-276-tundra-engine-kite-failed.gif
  ravenbyte-276-tundra-engine-kite-waiting.gif
  ravenbyte-276-tundra-engine-kite-running.gif
  ravenbyte-276-tundra-engine-kite-review.gif
  ravenbyte-276-tundra-engine-kite-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from crescent kite drone with asymmetric review wing, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
