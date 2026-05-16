# Frost Yield Serpent

<p align="center">
  <img src="previews/ravenbyte-198-frost-yield-serpent-showcase.gif" width="360" alt="Frost Yield Serpent stitched multi-motion showcase">
</p>

**A serpent-class Ravenbyte familiar that keeps yield work moving during long coding runs.**

Frost Yield Serpent is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around serpent ribbon automaton that coils around flaky tests, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Frost Yield Serpent brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-198-frost-yield-serpent-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-198-frost-yield-serpent-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-198-frost-yield-serpent-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-198-frost-yield-serpent-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-198-frost-yield-serpent-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-198-frost-yield-serpent-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-198-frost-yield-serpent-waiting.gif) |
| Running | ![Running](previews/ravenbyte-198-frost-yield-serpent-running.gif) |
| Review | ![Review](previews/ravenbyte-198-frost-yield-serpent-review.gif) |

Full contact sheet:

![Frost Yield Serpent contact sheet](previews/ravenbyte-198-frost-yield-serpent-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-198-frost-yield-serpent
```

Or from anywhere with Git:

```bash
PET=ravenbyte-198-frost-yield-serpent; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-198-frost-yield-serpent/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-198-frost-yield-serpent-showcase.gif
  ravenbyte-198-frost-yield-serpent-idle.gif
  ravenbyte-198-frost-yield-serpent-running-right.gif
  ravenbyte-198-frost-yield-serpent-running-left.gif
  ravenbyte-198-frost-yield-serpent-waving.gif
  ravenbyte-198-frost-yield-serpent-jumping.gif
  ravenbyte-198-frost-yield-serpent-failed.gif
  ravenbyte-198-frost-yield-serpent-waiting.gif
  ravenbyte-198-frost-yield-serpent-running.gif
  ravenbyte-198-frost-yield-serpent-review.gif
  ravenbyte-198-frost-yield-serpent-contact-sheet.png
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
