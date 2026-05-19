# Frost Event Serpent

<p align="center">
  <img src="previews/ravenbyte-358-frost-event-serpent-showcase.gif" width="360" alt="Frost Event Serpent stitched multi-motion showcase">
</p>

**A serpent-class Ravenbyte familiar that keeps event work moving during long coding runs.**

Frost Event Serpent is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around serpent ribbon automaton that coils around flaky tests, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Frost Event Serpent brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-358-frost-event-serpent-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-358-frost-event-serpent-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-358-frost-event-serpent-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-358-frost-event-serpent-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-358-frost-event-serpent-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-358-frost-event-serpent-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-358-frost-event-serpent-waiting.gif) |
| Running | ![Running](previews/ravenbyte-358-frost-event-serpent-running.gif) |
| Review | ![Review](previews/ravenbyte-358-frost-event-serpent-review.gif) |

Full contact sheet:

![Frost Event Serpent contact sheet](previews/ravenbyte-358-frost-event-serpent-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-358-frost-event-serpent
```

Or from anywhere with Git:

```bash
PET=ravenbyte-358-frost-event-serpent; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-358-frost-event-serpent/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-358-frost-event-serpent-showcase.gif
  ravenbyte-358-frost-event-serpent-idle.gif
  ravenbyte-358-frost-event-serpent-running-right.gif
  ravenbyte-358-frost-event-serpent-running-left.gif
  ravenbyte-358-frost-event-serpent-waving.gif
  ravenbyte-358-frost-event-serpent-jumping.gif
  ravenbyte-358-frost-event-serpent-failed.gif
  ravenbyte-358-frost-event-serpent-waiting.gif
  ravenbyte-358-frost-event-serpent-running.gif
  ravenbyte-358-frost-event-serpent-review.gif
  ravenbyte-358-frost-event-serpent-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from serpent ribbon automaton that coils around flaky tests, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
