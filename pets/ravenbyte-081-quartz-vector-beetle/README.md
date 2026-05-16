# Quartz Vector Beetle

<p align="center">
  <img src="previews/ravenbyte-081-quartz-vector-beetle-showcase.gif" width="360" alt="Quartz Vector Beetle stitched multi-motion showcase">
</p>

**A beetle-class Ravenbyte familiar that keeps vector work moving during long coding runs.**

Quartz Vector Beetle is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around antenna beetle slab robot with code-shell wing plates, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Quartz Vector Beetle brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-081-quartz-vector-beetle-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-081-quartz-vector-beetle-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-081-quartz-vector-beetle-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-081-quartz-vector-beetle-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-081-quartz-vector-beetle-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-081-quartz-vector-beetle-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-081-quartz-vector-beetle-waiting.gif) |
| Running | ![Running](previews/ravenbyte-081-quartz-vector-beetle-running.gif) |
| Review | ![Review](previews/ravenbyte-081-quartz-vector-beetle-review.gif) |

Full contact sheet:

![Quartz Vector Beetle contact sheet](previews/ravenbyte-081-quartz-vector-beetle-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-081-quartz-vector-beetle
```

Or from anywhere with Git:

```bash
PET=ravenbyte-081-quartz-vector-beetle; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-081-quartz-vector-beetle/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-081-quartz-vector-beetle-showcase.gif
  ravenbyte-081-quartz-vector-beetle-idle.gif
  ravenbyte-081-quartz-vector-beetle-running-right.gif
  ravenbyte-081-quartz-vector-beetle-running-left.gif
  ravenbyte-081-quartz-vector-beetle-waving.gif
  ravenbyte-081-quartz-vector-beetle-jumping.gif
  ravenbyte-081-quartz-vector-beetle-failed.gif
  ravenbyte-081-quartz-vector-beetle-waiting.gif
  ravenbyte-081-quartz-vector-beetle-running.gif
  ravenbyte-081-quartz-vector-beetle-review.gif
  ravenbyte-081-quartz-vector-beetle-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from antenna beetle slab robot with code-shell wing plates, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
