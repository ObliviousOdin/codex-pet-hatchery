# Tundra Beacon Kite

<p align="center">
  <img src="previews/ravenbyte-180-tundra-beacon-kite-showcase.gif" width="360" alt="Tundra Beacon Kite stitched multi-motion showcase">
</p>

**A kite-class Ravenbyte familiar that keeps beacon work moving during long coding runs.**

Tundra Beacon Kite is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crescent kite drone with asymmetric review wing, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Tundra Beacon Kite brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-180-tundra-beacon-kite-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-180-tundra-beacon-kite-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-180-tundra-beacon-kite-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-180-tundra-beacon-kite-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-180-tundra-beacon-kite-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-180-tundra-beacon-kite-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-180-tundra-beacon-kite-waiting.gif) |
| Running | ![Running](previews/ravenbyte-180-tundra-beacon-kite-running.gif) |
| Review | ![Review](previews/ravenbyte-180-tundra-beacon-kite-review.gif) |

Full contact sheet:

![Tundra Beacon Kite contact sheet](previews/ravenbyte-180-tundra-beacon-kite-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-180-tundra-beacon-kite
```

Or from anywhere with Git:

```bash
PET=ravenbyte-180-tundra-beacon-kite; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-180-tundra-beacon-kite/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-180-tundra-beacon-kite-showcase.gif
  ravenbyte-180-tundra-beacon-kite-idle.gif
  ravenbyte-180-tundra-beacon-kite-running-right.gif
  ravenbyte-180-tundra-beacon-kite-running-left.gif
  ravenbyte-180-tundra-beacon-kite-waving.gif
  ravenbyte-180-tundra-beacon-kite-jumping.gif
  ravenbyte-180-tundra-beacon-kite-failed.gif
  ravenbyte-180-tundra-beacon-kite-waiting.gif
  ravenbyte-180-tundra-beacon-kite-running.gif
  ravenbyte-180-tundra-beacon-kite-review.gif
  ravenbyte-180-tundra-beacon-kite-contact-sheet.png
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
