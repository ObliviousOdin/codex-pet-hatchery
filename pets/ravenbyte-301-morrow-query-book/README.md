# Morrow Query Book

<p align="center">
  <img src="previews/ravenbyte-301-morrow-query-book-showcase.gif" width="360" alt="Morrow Query Book stitched multi-motion showcase">
</p>

**A book-class Ravenbyte familiar that keeps query work moving during long coding runs.**

Morrow Query Book is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around open-book golem companion with diff-page armor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Morrow Query Book brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-301-morrow-query-book-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-301-morrow-query-book-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-301-morrow-query-book-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-301-morrow-query-book-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-301-morrow-query-book-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-301-morrow-query-book-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-301-morrow-query-book-waiting.gif) |
| Running | ![Running](previews/ravenbyte-301-morrow-query-book-running.gif) |
| Review | ![Review](previews/ravenbyte-301-morrow-query-book-review.gif) |

Full contact sheet:

![Morrow Query Book contact sheet](previews/ravenbyte-301-morrow-query-book-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-301-morrow-query-book
```

Or from anywhere with Git:

```bash
PET=ravenbyte-301-morrow-query-book; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-301-morrow-query-book/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-301-morrow-query-book-showcase.gif
  ravenbyte-301-morrow-query-book-idle.gif
  ravenbyte-301-morrow-query-book-running-right.gif
  ravenbyte-301-morrow-query-book-running-left.gif
  ravenbyte-301-morrow-query-book-waving.gif
  ravenbyte-301-morrow-query-book-jumping.gif
  ravenbyte-301-morrow-query-book-failed.gif
  ravenbyte-301-morrow-query-book-waiting.gif
  ravenbyte-301-morrow-query-book-running.gif
  ravenbyte-301-morrow-query-book-review.gif
  ravenbyte-301-morrow-query-book-contact-sheet.png
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
