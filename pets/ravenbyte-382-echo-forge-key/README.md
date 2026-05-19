# Echo Forge Key

<p align="center">
  <img src="previews/ravenbyte-382-echo-forge-key-showcase.gif" width="360" alt="Echo Forge Key stitched multi-motion showcase">
</p>

**A key-class Ravenbyte familiar that keeps forge work moving during long coding runs.**

Echo Forge Key is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around asymmetric key guardian with unlock beam, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Echo Forge Key brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-382-echo-forge-key-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-382-echo-forge-key-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-382-echo-forge-key-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-382-echo-forge-key-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-382-echo-forge-key-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-382-echo-forge-key-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-382-echo-forge-key-waiting.gif) |
| Running | ![Running](previews/ravenbyte-382-echo-forge-key-running.gif) |
| Review | ![Review](previews/ravenbyte-382-echo-forge-key-review.gif) |

Full contact sheet:

![Echo Forge Key contact sheet](previews/ravenbyte-382-echo-forge-key-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-382-echo-forge-key
```

Or from anywhere with Git:

```bash
PET=ravenbyte-382-echo-forge-key; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-382-echo-forge-key/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-382-echo-forge-key-showcase.gif
  ravenbyte-382-echo-forge-key-idle.gif
  ravenbyte-382-echo-forge-key-running-right.gif
  ravenbyte-382-echo-forge-key-running-left.gif
  ravenbyte-382-echo-forge-key-waving.gif
  ravenbyte-382-echo-forge-key-jumping.gif
  ravenbyte-382-echo-forge-key-failed.gif
  ravenbyte-382-echo-forge-key-waiting.gif
  ravenbyte-382-echo-forge-key-running.gif
  ravenbyte-382-echo-forge-key-review.gif
  ravenbyte-382-echo-forge-key-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from asymmetric key guardian with unlock beam, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
