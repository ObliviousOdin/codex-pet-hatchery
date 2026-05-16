# Cipher Patch Crawler

<p align="center">
  <img src="previews/ravenbyte-195-cipher-patch-crawler-showcase.gif" width="360" alt="Cipher Patch Crawler stitched multi-motion showcase">
</p>

**A crawler-class Ravenbyte familiar that keeps patch work moving during long coding runs.**

Cipher Patch Crawler is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around multi-leg crawler bridge familiar for dependency paths, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Cipher Patch Crawler brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-195-cipher-patch-crawler-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-195-cipher-patch-crawler-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-195-cipher-patch-crawler-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-195-cipher-patch-crawler-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-195-cipher-patch-crawler-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-195-cipher-patch-crawler-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-195-cipher-patch-crawler-waiting.gif) |
| Running | ![Running](previews/ravenbyte-195-cipher-patch-crawler-running.gif) |
| Review | ![Review](previews/ravenbyte-195-cipher-patch-crawler-review.gif) |

Full contact sheet:

![Cipher Patch Crawler contact sheet](previews/ravenbyte-195-cipher-patch-crawler-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-195-cipher-patch-crawler
```

Or from anywhere with Git:

```bash
PET=ravenbyte-195-cipher-patch-crawler; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-195-cipher-patch-crawler/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-195-cipher-patch-crawler-showcase.gif
  ravenbyte-195-cipher-patch-crawler-idle.gif
  ravenbyte-195-cipher-patch-crawler-running-right.gif
  ravenbyte-195-cipher-patch-crawler-running-left.gif
  ravenbyte-195-cipher-patch-crawler-waving.gif
  ravenbyte-195-cipher-patch-crawler-jumping.gif
  ravenbyte-195-cipher-patch-crawler-failed.gif
  ravenbyte-195-cipher-patch-crawler-waiting.gif
  ravenbyte-195-cipher-patch-crawler-running.gif
  ravenbyte-195-cipher-patch-crawler-review.gif
  ravenbyte-195-cipher-patch-crawler-contact-sheet.png
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
