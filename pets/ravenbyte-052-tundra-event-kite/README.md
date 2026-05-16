# Tundra Event Kite

<p align="center">
  <img src="previews/ravenbyte-052-tundra-event-kite-showcase.gif" width="360" alt="Tundra Event Kite stitched multi-motion showcase">
</p>

**A kite-class Ravenbyte familiar that keeps event work moving during long coding runs.**

Tundra Event Kite is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crescent kite drone with asymmetric review wing, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Tundra Event Kite brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-052-tundra-event-kite-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-052-tundra-event-kite-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-052-tundra-event-kite-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-052-tundra-event-kite-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-052-tundra-event-kite-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-052-tundra-event-kite-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-052-tundra-event-kite-waiting.gif) |
| Running | ![Running](previews/ravenbyte-052-tundra-event-kite-running.gif) |
| Review | ![Review](previews/ravenbyte-052-tundra-event-kite-review.gif) |

Full contact sheet:

![Tundra Event Kite contact sheet](previews/ravenbyte-052-tundra-event-kite-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-052-tundra-event-kite
```

Or from anywhere with Git:

```bash
PET=ravenbyte-052-tundra-event-kite; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-052-tundra-event-kite/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-052-tundra-event-kite-showcase.gif
  ravenbyte-052-tundra-event-kite-idle.gif
  ravenbyte-052-tundra-event-kite-running-right.gif
  ravenbyte-052-tundra-event-kite-running-left.gif
  ravenbyte-052-tundra-event-kite-waving.gif
  ravenbyte-052-tundra-event-kite-jumping.gif
  ravenbyte-052-tundra-event-kite-failed.gif
  ravenbyte-052-tundra-event-kite-waiting.gif
  ravenbyte-052-tundra-event-kite-running.gif
  ravenbyte-052-tundra-event-kite-review.gif
  ravenbyte-052-tundra-event-kite-contact-sheet.png
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
