# Signal Diff Crawler

<p align="center">
  <img src="previews/ravenbyte-115-signal-diff-crawler-showcase.gif" width="360" alt="Signal Diff Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps diff work moving during long coding runs.**

Signal Diff Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Signal Diff Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-115-signal-diff-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-115-signal-diff-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-115-signal-diff-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-115-signal-diff-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-115-signal-diff-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-115-signal-diff-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-115-signal-diff-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-115-signal-diff-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-115-signal-diff-crawler-review.gif) |

Full contact sheet:

![Signal Diff Crawler contact sheet](previews/ravenbyte-115-signal-diff-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-115-signal-diff-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-115-signal-diff-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-115-signal-diff-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-115-signal-diff-crawler-showcase.gif
  ravenbyte-115-signal-diff-crawler-idle.gif
  ravenbyte-115-signal-diff-crawler-running-right.gif
  ravenbyte-115-signal-diff-crawler-running-left.gif
  ravenbyte-115-signal-diff-crawler-waving.gif
  ravenbyte-115-signal-diff-crawler-jumping.gif
  ravenbyte-115-signal-diff-crawler-failed.gif
  ravenbyte-115-signal-diff-crawler-waiting.gif
  ravenbyte-115-signal-diff-crawler-running.gif
  ravenbyte-115-signal-diff-crawler-review.gif
  ravenbyte-115-signal-diff-crawler-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from multi-leg crawler bridge familiar for dependency paths, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
