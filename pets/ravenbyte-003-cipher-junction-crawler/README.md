# Cipher Junction Crawler

<p align="center">
  <img src="previews/ravenbyte-003-cipher-junction-crawler-showcase.gif" width="360" alt="Cipher Junction Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps junction work moving during long coding runs.**

Cipher Junction Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Cipher Junction Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-003-cipher-junction-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-003-cipher-junction-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-003-cipher-junction-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-003-cipher-junction-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-003-cipher-junction-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-003-cipher-junction-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-003-cipher-junction-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-003-cipher-junction-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-003-cipher-junction-crawler-review.gif) |

Full contact sheet:

![Cipher Junction Crawler contact sheet](previews/ravenbyte-003-cipher-junction-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-003-cipher-junction-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-003-cipher-junction-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-003-cipher-junction-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-003-cipher-junction-crawler-showcase.gif
  ravenbyte-003-cipher-junction-crawler-idle.gif
  ravenbyte-003-cipher-junction-crawler-running-right.gif
  ravenbyte-003-cipher-junction-crawler-running-left.gif
  ravenbyte-003-cipher-junction-crawler-waving.gif
  ravenbyte-003-cipher-junction-crawler-jumping.gif
  ravenbyte-003-cipher-junction-crawler-failed.gif
  ravenbyte-003-cipher-junction-crawler-waiting.gif
  ravenbyte-003-cipher-junction-crawler-running.gif
  ravenbyte-003-cipher-junction-crawler-review.gif
  ravenbyte-003-cipher-junction-crawler-contact-sheet.png
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
