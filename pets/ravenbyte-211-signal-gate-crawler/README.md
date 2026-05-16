# Signal Gate Crawler

<p align="center">
  <img src="previews/ravenbyte-211-signal-gate-crawler-showcase.gif" width="360" alt="Signal Gate Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps gate work moving during long coding runs.**

Signal Gate Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Signal Gate Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-211-signal-gate-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-211-signal-gate-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-211-signal-gate-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-211-signal-gate-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-211-signal-gate-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-211-signal-gate-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-211-signal-gate-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-211-signal-gate-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-211-signal-gate-crawler-review.gif) |

Full contact sheet:

![Signal Gate Crawler contact sheet](previews/ravenbyte-211-signal-gate-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-211-signal-gate-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-211-signal-gate-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-211-signal-gate-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-211-signal-gate-crawler-showcase.gif
  ravenbyte-211-signal-gate-crawler-idle.gif
  ravenbyte-211-signal-gate-crawler-running-right.gif
  ravenbyte-211-signal-gate-crawler-running-left.gif
  ravenbyte-211-signal-gate-crawler-waving.gif
  ravenbyte-211-signal-gate-crawler-jumping.gif
  ravenbyte-211-signal-gate-crawler-failed.gif
  ravenbyte-211-signal-gate-crawler-waiting.gif
  ravenbyte-211-signal-gate-crawler-running.gif
  ravenbyte-211-signal-gate-crawler-review.gif
  ravenbyte-211-signal-gate-crawler-contact-sheet.png
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
