# Signal Zenith Crawler

<p align="center">
  <img src="previews/ravenbyte-019-signal-zenith-crawler-showcase.gif" width="360" alt="Signal Zenith Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps zenith work moving during long coding runs.**

Signal Zenith Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Signal Zenith Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-019-signal-zenith-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-019-signal-zenith-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-019-signal-zenith-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-019-signal-zenith-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-019-signal-zenith-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-019-signal-zenith-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-019-signal-zenith-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-019-signal-zenith-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-019-signal-zenith-crawler-review.gif) |

Full contact sheet:

![Signal Zenith Crawler contact sheet](previews/ravenbyte-019-signal-zenith-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-019-signal-zenith-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-019-signal-zenith-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-019-signal-zenith-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-019-signal-zenith-crawler-showcase.gif
  ravenbyte-019-signal-zenith-crawler-idle.gif
  ravenbyte-019-signal-zenith-crawler-running-right.gif
  ravenbyte-019-signal-zenith-crawler-running-left.gif
  ravenbyte-019-signal-zenith-crawler-waving.gif
  ravenbyte-019-signal-zenith-crawler-jumping.gif
  ravenbyte-019-signal-zenith-crawler-failed.gif
  ravenbyte-019-signal-zenith-crawler-waiting.gif
  ravenbyte-019-signal-zenith-crawler-running.gif
  ravenbyte-019-signal-zenith-crawler-review.gif
  ravenbyte-019-signal-zenith-crawler-contact-sheet.png
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
