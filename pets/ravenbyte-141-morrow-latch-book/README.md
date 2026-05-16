# Morrow Latch Book

<p align="center">
  <img src="previews/ravenbyte-141-morrow-latch-book-showcase.gif" width="360" alt="Morrow Latch Book stitched multi-motion showcase">
</p>

**A book-class Ravenbyte familiar that keeps latch work moving during long coding runs.**

Morrow Latch Book is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around open-book golem companion with diff-page armor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Morrow Latch Book brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-141-morrow-latch-book-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-141-morrow-latch-book-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-141-morrow-latch-book-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-141-morrow-latch-book-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-141-morrow-latch-book-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-141-morrow-latch-book-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-141-morrow-latch-book-waiting.gif) |
| Running | ![Running](previews/ravenbyte-141-morrow-latch-book-running.gif) |
| Review | ![Review](previews/ravenbyte-141-morrow-latch-book-review.gif) |

Full contact sheet:

![Morrow Latch Book contact sheet](previews/ravenbyte-141-morrow-latch-book-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-141-morrow-latch-book
```

Or from anywhere with Git:

```bash
PET=ravenbyte-141-morrow-latch-book; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-141-morrow-latch-book/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-141-morrow-latch-book-showcase.gif
  ravenbyte-141-morrow-latch-book-idle.gif
  ravenbyte-141-morrow-latch-book-running-right.gif
  ravenbyte-141-morrow-latch-book-running-left.gif
  ravenbyte-141-morrow-latch-book-waving.gif
  ravenbyte-141-morrow-latch-book-jumping.gif
  ravenbyte-141-morrow-latch-book-failed.gif
  ravenbyte-141-morrow-latch-book-waiting.gif
  ravenbyte-141-morrow-latch-book-running.gif
  ravenbyte-141-morrow-latch-book-review.gif
  ravenbyte-141-morrow-latch-book-contact-sheet.png
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
