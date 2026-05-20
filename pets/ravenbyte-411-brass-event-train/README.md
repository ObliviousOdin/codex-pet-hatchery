# Brass Event Train

<p align="center">
  <img src="previews/ravenbyte-411-brass-event-train-showcase.gif" width="360" alt="Brass Event Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps event work moving during long coding runs.**

Brass Event Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Brass Event Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-411-brass-event-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-411-brass-event-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-411-brass-event-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-411-brass-event-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-411-brass-event-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-411-brass-event-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-411-brass-event-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-411-brass-event-train-running.gif) |
| Review | ![Review](previews/ravenbyte-411-brass-event-train-review.gif) |

Full contact sheet:

![Brass Event Train contact sheet](previews/ravenbyte-411-brass-event-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-411-brass-event-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-411-brass-event-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-411-brass-event-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-411-brass-event-train-showcase.gif
  ravenbyte-411-brass-event-train-idle.gif
  ravenbyte-411-brass-event-train-running-right.gif
  ravenbyte-411-brass-event-train-running-left.gif
  ravenbyte-411-brass-event-train-waving.gif
  ravenbyte-411-brass-event-train-jumping.gif
  ravenbyte-411-brass-event-train-failed.gif
  ravenbyte-411-brass-event-train-waiting.gif
  ravenbyte-411-brass-event-train-running.gif
  ravenbyte-411-brass-event-train-review.gif
  ravenbyte-411-brass-event-train-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from tiny train familiar hauling hotfix cargo, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
