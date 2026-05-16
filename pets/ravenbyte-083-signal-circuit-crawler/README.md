# Signal Circuit Crawler

<p align="center">
  <img src="previews/ravenbyte-083-signal-circuit-crawler-showcase.gif" width="360" alt="Signal Circuit Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps circuit work moving during long coding runs.**

Signal Circuit Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Signal Circuit Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-083-signal-circuit-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-083-signal-circuit-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-083-signal-circuit-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-083-signal-circuit-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-083-signal-circuit-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-083-signal-circuit-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-083-signal-circuit-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-083-signal-circuit-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-083-signal-circuit-crawler-review.gif) |

Full contact sheet:

![Signal Circuit Crawler contact sheet](previews/ravenbyte-083-signal-circuit-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-083-signal-circuit-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-083-signal-circuit-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-083-signal-circuit-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-083-signal-circuit-crawler-showcase.gif
  ravenbyte-083-signal-circuit-crawler-idle.gif
  ravenbyte-083-signal-circuit-crawler-running-right.gif
  ravenbyte-083-signal-circuit-crawler-running-left.gif
  ravenbyte-083-signal-circuit-crawler-waving.gif
  ravenbyte-083-signal-circuit-crawler-jumping.gif
  ravenbyte-083-signal-circuit-crawler-failed.gif
  ravenbyte-083-signal-circuit-crawler-waiting.gif
  ravenbyte-083-signal-circuit-crawler-running.gif
  ravenbyte-083-signal-circuit-crawler-review.gif
  ravenbyte-083-signal-circuit-crawler-contact-sheet.png
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
