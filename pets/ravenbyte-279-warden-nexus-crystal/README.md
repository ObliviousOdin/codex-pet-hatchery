# Warden Nexus Crystal

<p align="center">
  <img src="previews/ravenbyte-279-warden-nexus-crystal-showcase.gif" width="360" alt="Warden Nexus Crystal stitched multi-motion showcase">
</p>

**A crystal-class Ravenbyte familiar that keeps nexus work moving during long coding runs.**

Warden Nexus Crystal is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around crystal tripod familiar with facet armor and lint sparks, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Warden Nexus Crystal brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-279-warden-nexus-crystal-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-279-warden-nexus-crystal-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-279-warden-nexus-crystal-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-279-warden-nexus-crystal-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-279-warden-nexus-crystal-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-279-warden-nexus-crystal-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-279-warden-nexus-crystal-waiting.gif) |
| Running | ![Running](previews/ravenbyte-279-warden-nexus-crystal-running.gif) |
| Review | ![Review](previews/ravenbyte-279-warden-nexus-crystal-review.gif) |

Full contact sheet:

![Warden Nexus Crystal contact sheet](previews/ravenbyte-279-warden-nexus-crystal-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-279-warden-nexus-crystal
```

Or from anywhere with Git:

```bash
PET=ravenbyte-279-warden-nexus-crystal; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-279-warden-nexus-crystal/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-279-warden-nexus-crystal-showcase.gif
  ravenbyte-279-warden-nexus-crystal-idle.gif
  ravenbyte-279-warden-nexus-crystal-running-right.gif
  ravenbyte-279-warden-nexus-crystal-running-left.gif
  ravenbyte-279-warden-nexus-crystal-waving.gif
  ravenbyte-279-warden-nexus-crystal-jumping.gif
  ravenbyte-279-warden-nexus-crystal-failed.gif
  ravenbyte-279-warden-nexus-crystal-waiting.gif
  ravenbyte-279-warden-nexus-crystal-running.gif
  ravenbyte-279-warden-nexus-crystal-review.gif
  ravenbyte-279-warden-nexus-crystal-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from crystal tripod familiar with facet armor and lint sparks, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
