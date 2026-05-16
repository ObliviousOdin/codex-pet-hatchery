# Obsidian Query Jelly

<p align="center">
  <img src="previews/ravenbyte-111-obsidian-query-jelly-showcase.gif" width="360" alt="Obsidian Query Jelly stitched multi-motion showcase">
</p>

**A jelly-class Ravenbyte familiar that keeps query work moving during long coding runs.**

Obsidian Query Jelly is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around bell jellyfish familiar with dangling trace tendrils, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Obsidian Query Jelly brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-111-obsidian-query-jelly-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-111-obsidian-query-jelly-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-111-obsidian-query-jelly-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-111-obsidian-query-jelly-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-111-obsidian-query-jelly-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-111-obsidian-query-jelly-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-111-obsidian-query-jelly-waiting.gif) |
| Running | ![Running](previews/ravenbyte-111-obsidian-query-jelly-running.gif) |
| Review | ![Review](previews/ravenbyte-111-obsidian-query-jelly-review.gif) |

Full contact sheet:

![Obsidian Query Jelly contact sheet](previews/ravenbyte-111-obsidian-query-jelly-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-111-obsidian-query-jelly
```

Or from anywhere with Git:

```bash
PET=ravenbyte-111-obsidian-query-jelly; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-111-obsidian-query-jelly/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-111-obsidian-query-jelly-showcase.gif
  ravenbyte-111-obsidian-query-jelly-idle.gif
  ravenbyte-111-obsidian-query-jelly-running-right.gif
  ravenbyte-111-obsidian-query-jelly-running-left.gif
  ravenbyte-111-obsidian-query-jelly-waving.gif
  ravenbyte-111-obsidian-query-jelly-jumping.gif
  ravenbyte-111-obsidian-query-jelly-failed.gif
  ravenbyte-111-obsidian-query-jelly-waiting.gif
  ravenbyte-111-obsidian-query-jelly-running.gif
  ravenbyte-111-obsidian-query-jelly-review.gif
  ravenbyte-111-obsidian-query-jelly-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from bell jellyfish familiar with dangling trace tendrils, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
