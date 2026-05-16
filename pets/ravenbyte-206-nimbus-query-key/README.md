# Nimbus Query Key

<p align="center">
  <img src="previews/ravenbyte-206-nimbus-query-key-showcase.gif" width="360" alt="Nimbus Query Key stitched multi-motion showcase">
</p>

**A key-class Ravenbyte familiar that keeps query work moving during long coding runs.**

Nimbus Query Key is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around asymmetric key guardian with unlock beam, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Nimbus Query Key brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-206-nimbus-query-key-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-206-nimbus-query-key-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-206-nimbus-query-key-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-206-nimbus-query-key-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-206-nimbus-query-key-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-206-nimbus-query-key-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-206-nimbus-query-key-waiting.gif) |
| Running | ![Running](previews/ravenbyte-206-nimbus-query-key-running.gif) |
| Review | ![Review](previews/ravenbyte-206-nimbus-query-key-review.gif) |

Full contact sheet:

![Nimbus Query Key contact sheet](previews/ravenbyte-206-nimbus-query-key-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-206-nimbus-query-key
```

Or from anywhere with Git:

```bash
PET=ravenbyte-206-nimbus-query-key; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-206-nimbus-query-key/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-206-nimbus-query-key-showcase.gif
  ravenbyte-206-nimbus-query-key-idle.gif
  ravenbyte-206-nimbus-query-key-running-right.gif
  ravenbyte-206-nimbus-query-key-running-left.gif
  ravenbyte-206-nimbus-query-key-waving.gif
  ravenbyte-206-nimbus-query-key-jumping.gif
  ravenbyte-206-nimbus-query-key-failed.gif
  ravenbyte-206-nimbus-query-key-waiting.gif
  ravenbyte-206-nimbus-query-key-running.gif
  ravenbyte-206-nimbus-query-key-review.gif
  ravenbyte-206-nimbus-query-key-contact-sheet.png
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
