# Drift Yield Book

<p align="center">
  <img src="previews/ravenbyte-061-drift-yield-book-showcase.gif" width="360" alt="Drift Yield Book stitched multi-motion showcase">
</p>

**A book-class Ravenbyte familiar that keeps yield work moving during long coding runs.**

Drift Yield Book is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around open-book golem companion with diff-page armor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Drift Yield Book brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-061-drift-yield-book-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-061-drift-yield-book-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-061-drift-yield-book-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-061-drift-yield-book-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-061-drift-yield-book-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-061-drift-yield-book-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-061-drift-yield-book-waiting.gif) |
| Running | ![Running](previews/ravenbyte-061-drift-yield-book-running.gif) |
| Review | ![Review](previews/ravenbyte-061-drift-yield-book-review.gif) |

Full contact sheet:

![Drift Yield Book contact sheet](previews/ravenbyte-061-drift-yield-book-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-061-drift-yield-book
```

Or from anywhere with Git:

```bash
PET=ravenbyte-061-drift-yield-book; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-061-drift-yield-book/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-061-drift-yield-book-showcase.gif
  ravenbyte-061-drift-yield-book-idle.gif
  ravenbyte-061-drift-yield-book-running-right.gif
  ravenbyte-061-drift-yield-book-running-left.gif
  ravenbyte-061-drift-yield-book-waving.gif
  ravenbyte-061-drift-yield-book-jumping.gif
  ravenbyte-061-drift-yield-book-failed.gif
  ravenbyte-061-drift-yield-book-waiting.gif
  ravenbyte-061-drift-yield-book-running.gif
  ravenbyte-061-drift-yield-book-review.gif
  ravenbyte-061-drift-yield-book-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from open-book golem companion with diff-page armor, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
