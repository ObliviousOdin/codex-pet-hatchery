# Origami Test Heron

<p align="center">
  <img src="previews/origami-test-heron-showcase.gif" width="360" alt="Origami Test Heron stitched multi-motion showcase">
</p>

**A folded-paper cyber-heron that pecks flaky tests until they settle.**

Origami Test Heron is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around origami bird robot with folded white armor and blue circuit seams, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Origami Test Heron brings a distinct motion language to Ravenbyte Familiars: folded-paper wing tilts, long-leg test pecks, jump glides, flaky-test alert sparks, and precise review scans.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/origami-test-heron-idle.gif) |
| Running Right | ![Running Right](previews/origami-test-heron-running-right.gif) |
| Running Left | ![Running Left](previews/origami-test-heron-running-left.gif) |
| Waving | ![Waving](previews/origami-test-heron-waving.gif) |
| Jumping | ![Jumping](previews/origami-test-heron-jumping.gif) |
| Failed | ![Failed](previews/origami-test-heron-failed.gif) |
| Waiting | ![Waiting](previews/origami-test-heron-waiting.gif) |
| Running | ![Running](previews/origami-test-heron-running.gif) |
| Review | ![Review](previews/origami-test-heron-review.gif) |

Full contact sheet:

![Origami Test Heron contact sheet](previews/origami-test-heron-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py origami-test-heron
```

Or from anywhere with Git:

```bash
PET=origami-test-heron; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/origami-test-heron/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  origami-test-heron-showcase.gif
  origami-test-heron-idle.gif
  origami-test-heron-running-right.gif
  origami-test-heron-running-left.gif
  origami-test-heron-waving.gif
  origami-test-heron-jumping.gif
  origami-test-heron-failed.gif
  origami-test-heron-waiting.gif
  origami-test-heron-running.gif
  origami-test-heron-review.gif
  origami-test-heron-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from origami bird robot with folded white armor and blue circuit seams, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
