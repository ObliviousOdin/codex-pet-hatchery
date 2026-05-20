# Obsidian Zenith Jelly

<p align="center">
  <img src="previews/ravenbyte-399-obsidian-zenith-jelly-showcase.gif" width="360" alt="Obsidian Zenith Jelly stitched multi-motion showcase">
</p>

**A jelly-class Ravenbyte familiar that keeps zenith work moving during long coding runs.**

Obsidian Zenith Jelly is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around bell jellyfish familiar with dangling trace tendrils, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Obsidian Zenith Jelly brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-399-obsidian-zenith-jelly-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-399-obsidian-zenith-jelly-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-399-obsidian-zenith-jelly-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-399-obsidian-zenith-jelly-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-399-obsidian-zenith-jelly-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-399-obsidian-zenith-jelly-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-399-obsidian-zenith-jelly-waiting.gif) |
| Running | ![Running](previews/ravenbyte-399-obsidian-zenith-jelly-running.gif) |
| Review | ![Review](previews/ravenbyte-399-obsidian-zenith-jelly-review.gif) |

Full contact sheet:

![Obsidian Zenith Jelly contact sheet](previews/ravenbyte-399-obsidian-zenith-jelly-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-399-obsidian-zenith-jelly
```

Or from anywhere with Git:

```bash
PET=ravenbyte-399-obsidian-zenith-jelly; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-399-obsidian-zenith-jelly/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-399-obsidian-zenith-jelly-showcase.gif
  ravenbyte-399-obsidian-zenith-jelly-idle.gif
  ravenbyte-399-obsidian-zenith-jelly-running-right.gif
  ravenbyte-399-obsidian-zenith-jelly-running-left.gif
  ravenbyte-399-obsidian-zenith-jelly-waving.gif
  ravenbyte-399-obsidian-zenith-jelly-jumping.gif
  ravenbyte-399-obsidian-zenith-jelly-failed.gif
  ravenbyte-399-obsidian-zenith-jelly-waiting.gif
  ravenbyte-399-obsidian-zenith-jelly-running.gif
  ravenbyte-399-obsidian-zenith-jelly-review.gif
  ravenbyte-399-obsidian-zenith-jelly-contact-sheet.png
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
