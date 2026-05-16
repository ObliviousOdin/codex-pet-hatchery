# Lotus Firewall Monk

<p align="center">
  <img src="previews/lotus-firewall-monk-showcase.gif" width="360" alt="Lotus Firewall Monk stitched multi-motion showcase">
</p>

**A cyber-monk bot that reviews diffs behind shield-petal armor.**

Lotus Firewall Monk is an original Codex-compatible coding familiar by **ObliviousOdin**. It combines a tall incense-core monk bot, orbiting lotus shield petals, prayer-bead firewall nodes, and cross-legged hover motion into a readable `64×64` sprite companion. The familiar is an original design and does not copy any named character, logo, costume, or insignia.

## Personality

Lotus Firewall Monk is the repo's calm merge guardian:

- hovering in idle with shield-petal breathing motion,
- gliding through run states with firewall petals held wide,
- waving with a soft scan-arc blessing,
- jumping in a floating lotus lift,
- cracking into alert sparks when a check fails,
- waiting with patient beacon dots and prayer-node pulses,
- reviewing code like a quiet sentinel behind a diff shield.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/lotus-firewall-monk-idle.gif) |
| Running right | ![Running right](previews/lotus-firewall-monk-running-right.gif) |
| Running left | ![Running left](previews/lotus-firewall-monk-running-left.gif) |
| Waving | ![Waving](previews/lotus-firewall-monk-waving.gif) |
| Jumping | ![Jumping](previews/lotus-firewall-monk-jumping.gif) |
| Failed | ![Failed](previews/lotus-firewall-monk-failed.gif) |
| Waiting | ![Waiting](previews/lotus-firewall-monk-waiting.gif) |
| Running | ![Running](previews/lotus-firewall-monk-running.gif) |
| Review | ![Review](previews/lotus-firewall-monk-review.gif) |

Full contact sheet:

![Lotus Firewall Monk contact sheet](previews/lotus-firewall-monk-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py lotus-firewall-monk
```

Or from anywhere with Git:

```bash
PET=lotus-firewall-monk; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/lotus-firewall-monk/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  lotus-firewall-monk-showcase.gif
  lotus-firewall-monk-idle.gif
  lotus-firewall-monk-running-right.gif
  lotus-firewall-monk-running-left.gif
  lotus-firewall-monk-waving.gif
  lotus-firewall-monk-jumping.gif
  lotus-firewall-monk-failed.gif
  lotus-firewall-monk-waiting.gif
  lotus-firewall-monk-running.gif
  lotus-firewall-monk-review.gif
  lotus-firewall-monk-contact-sheet.png
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
- Symmetric design: yes
- `running-left`: mirrored from `running-right` because the shield-petal monk silhouette is intentionally symmetric
- Author: `ObliviousOdin`

## Design notes

The design is intentionally original. It uses broad visual language from lotus petals, firewall shields, quiet cyber-monks, prayer beads, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
