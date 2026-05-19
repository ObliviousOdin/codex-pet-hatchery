# Violet Nexus Serpent

<p align="center">
  <img src="previews/ravenbyte-374-violet-nexus-serpent-showcase.gif" width="360" alt="Violet Nexus Serpent stitched multi-motion showcase">
</p>

**A serpent-class Ravenbyte familiar that keeps nexus work moving during long coding runs.**

Violet Nexus Serpent is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around serpent ribbon automaton that coils around flaky tests, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Violet Nexus Serpent brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-374-violet-nexus-serpent-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-374-violet-nexus-serpent-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-374-violet-nexus-serpent-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-374-violet-nexus-serpent-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-374-violet-nexus-serpent-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-374-violet-nexus-serpent-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-374-violet-nexus-serpent-waiting.gif) |
| Running | ![Running](previews/ravenbyte-374-violet-nexus-serpent-running.gif) |
| Review | ![Review](previews/ravenbyte-374-violet-nexus-serpent-review.gif) |

Full contact sheet:

![Violet Nexus Serpent contact sheet](previews/ravenbyte-374-violet-nexus-serpent-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-374-violet-nexus-serpent
```

Or from anywhere with Git:

```bash
PET=ravenbyte-374-violet-nexus-serpent; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-374-violet-nexus-serpent/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-374-violet-nexus-serpent-showcase.gif
  ravenbyte-374-violet-nexus-serpent-idle.gif
  ravenbyte-374-violet-nexus-serpent-running-right.gif
  ravenbyte-374-violet-nexus-serpent-running-left.gif
  ravenbyte-374-violet-nexus-serpent-waving.gif
  ravenbyte-374-violet-nexus-serpent-jumping.gif
  ravenbyte-374-violet-nexus-serpent-failed.gif
  ravenbyte-374-violet-nexus-serpent-waiting.gif
  ravenbyte-374-violet-nexus-serpent-running.gif
  ravenbyte-374-violet-nexus-serpent-review.gif
  ravenbyte-374-violet-nexus-serpent-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from serpent ribbon automaton that coils around flaky tests, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
