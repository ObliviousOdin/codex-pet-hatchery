<p align="center">
  <img src="assets/hero/ravenbyte-familiars-hero.gif" width="100%" alt="Ravenbyte Familiars hero animation: tiny robot companions working, reviewing, and rejoicing around a minimalist industrial console">
</p>

<p align="center">
  <strong>Tiny mythic coding companions for Codex-compatible and Open Design pet import workflows.</strong><br>
  Original animated familiars packaged with <code>pet.json</code> and <code>spritesheet.webp</code>.
</p>

<p align="center">
  <a href="#familiars">Familiars</a> ·
  <a href="#one-command-install">Install</a> ·
  <a href="#package-format">Package format</a> ·
  <a href="#variation-standard">Variation standard</a> ·
  <a href="#development-and-verification">Development</a>
</p>

---

## What this is

**Ravenbyte Familiars** is an **ObliviousOdin** sprite collection for long coding nights: raven-dark, rune-lit, wild-hearted little machines and spirits that can be imported through **Settings → Pets → Import Codex sprite**.

The repo is intentionally practical: each familiar ships as a complete import package, with animation previews, a per-familiar README, deterministic generation artifacts, and validation scripts.

## Design direction

The header animation is the visual north star: calm industrial product discipline, precise panels, useful machines, and tiny companions that make the workbench feel alive. The collection should feel premium and restrained, not childish or corporate.

| Principle | Meaning here |
| --- | --- |
| Useful first | Every familiar has a real importable package, not just preview art. |
| Less, but better | Strong silhouettes, few accents, readable motion at `64×64`. |
| More than idle | README cards use stitched showcase GIFs that move through idle, run, jump, review, fail, and wave states. |
| Original mythology | Broad mecha/spirit/adventure energy, no copied characters or logos. |
| Built to verify | `pet.json`, spritesheet dimensions, previews, showcase GIFs, and visual variation are checked before publishing. |

## Brand palette

| Token | Hex | Use |
| --- | --- | --- |
| Void Black | `#080A0F` | deep background |
| Raven Ink | `#111827` | panels and outlines |
| Bone White | `#E8E0D0` | readable text and masks |
| Rune Gold | `#D6A84F` | mythic accent |
| Plasma Cyan | `#62E6FF` | code energy and motion |
| Signal Ember | `#FF7A45` | warnings, failed states, sparks |

## Familiars

Each card below is a **stitched multi-motion showcase**, not a single idle loop. It cycles through several real rows from the import spritesheet so the README better reflects how each familiar behaves in Open Design.

<table>
<tr>
<td width="33%" align="center" valign="top">
  <a href="pets/kageframe-rx07/README.md"><img src="pets/kageframe-rx07/previews/kageframe-rx07-showcase.gif" width="240" alt="Kageframe RX-07 stitched multi-motion showcase"></a><br>
  <strong>Kageframe RX-07</strong><br>
  <sub>A chibi shadow-mecha shinobi that reviews code with a plasma scarf.</sub><br>
  <a href="pets/kageframe-rx07/README.md">README</a> · <a href="pets/kageframe-rx07/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/shuriken-byte-zero/README.md"><img src="pets/shuriken-byte-zero/previews/shuriken-byte-zero-showcase.gif" width="240" alt="Shuriken Byte Zero stitched multi-motion showcase"></a><br>
  <strong>Shuriken Byte Zero</strong><br>
  <sub>A stealthy robot courier with spinning debug shuriken drones.</sub><br>
  <a href="pets/shuriken-byte-zero/README.md">README</a> · <a href="pets/shuriken-byte-zero/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/ronin-build-fox/README.md"><img src="pets/ronin-build-fox/previews/ronin-build-fox-showcase.gif" width="240" alt="Ronin Build Fox stitched multi-motion showcase"></a><br>
  <strong>Ronin Build Fox</strong><br>
  <sub>A fox-masked build guardian with tiny servo tails and CI charms.</sub><br>
  <a href="pets/ronin-build-fox/README.md">README</a> · <a href="pets/ronin-build-fox/spritesheet.webp">spritesheet</a>
</td>
</tr>
<tr>
<td width="33%" align="center" valign="top">
  <a href="pets/compiler-oni-mini/README.md"><img src="pets/compiler-oni-mini/previews/compiler-oni-mini-showcase.gif" width="240" alt="Compiler Oni Mini stitched multi-motion showcase"></a><br>
  <strong>Compiler Oni Mini</strong><br>
  <sub>A tiny red oni bot that bonks failing tests with a foam kanabo.</sub><br>
  <a href="pets/compiler-oni-mini/README.md">README</a> · <a href="pets/compiler-oni-mini/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/moonbase-tanuki-dev/README.md"><img src="pets/moonbase-tanuki-dev/previews/moonbase-tanuki-dev-showcase.gif" width="240" alt="Moonbase Tanuki Dev stitched multi-motion showcase"></a><br>
  <strong>Moonbase Tanuki Dev</strong><br>
  <sub>A sleepy rover-tanuki with a leaf antenna and lunar debug pouches.</sub><br>
  <a href="pets/moonbase-tanuki-dev/README.md">README</a> · <a href="pets/moonbase-tanuki-dev/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/karakuri-patch-cat/README.md"><img src="pets/karakuri-patch-cat/previews/karakuri-patch-cat-showcase.gif" width="240" alt="Karakuri Patch Cat stitched multi-motion showcase"></a><br>
  <strong>Karakuri Patch Cat</strong><br>
  <sub>A wooden clockwork cat automaton that bats TODOs into shape.</sub><br>
  <a href="pets/karakuri-patch-cat/README.md">README</a> · <a href="pets/karakuri-patch-cat/spritesheet.webp">spritesheet</a>
</td>
</tr>
<tr>
<td width="33%" align="center" valign="top">
  <a href="pets/lotus-firewall-monk/README.md"><img src="pets/lotus-firewall-monk/previews/lotus-firewall-monk-showcase.gif" width="240" alt="Lotus Firewall Monk stitched multi-motion showcase"></a><br>
  <strong>Lotus Firewall Monk</strong><br>
  <sub>A cyber-monk bot that reviews diffs behind shield-petal armor.</sub><br>
  <a href="pets/lotus-firewall-monk/README.md">README</a> · <a href="pets/lotus-firewall-monk/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/nebula-courier-mech/README.md"><img src="pets/nebula-courier-mech/previews/nebula-courier-mech-showcase.gif" width="240" alt="Nebula Courier Mech stitched multi-motion showcase"></a><br>
  <strong>Nebula Courier Mech</strong><br>
  <sub>A star-courier micro-mech that sprints commits through hyperspace.</sub><br>
  <a href="pets/nebula-courier-mech/README.md">README</a> · <a href="pets/nebula-courier-mech/spritesheet.webp">spritesheet</a>
</td>
<td width="33%" align="center" valign="top">
  <a href="pets/ramen-debug-drone/README.md"><img src="pets/ramen-debug-drone/previews/ramen-debug-drone-showcase.gif" width="240" alt="Ramen Debug Drone stitched multi-motion showcase"></a><br>
  <strong>Ramen Debug Drone</strong><br>
  <sub>A noodle-shop hover drone that serves hot fixes in a tiny bowl.</sub><br>
  <a href="pets/ramen-debug-drone/README.md">README</a> · <a href="pets/ramen-debug-drone/spritesheet.webp">spritesheet</a>
</td>
</tr>
<tr>
<td width="33%" align="center" valign="top">
  <a href="pets/samurai-cache-crab/README.md"><img src="pets/samurai-cache-crab/previews/samurai-cache-crab-showcase.gif" width="240" alt="Samurai Cache Crab stitched multi-motion showcase"></a><br>
  <strong>Samurai Cache Crab</strong><br>
  <sub>A side-stepping armor crab that guards build artifacts and cache hits.</sub><br>
  <a href="pets/samurai-cache-crab/README.md">README</a> · <a href="pets/samurai-cache-crab/spritesheet.webp">spritesheet</a>
</td>
</tr>
</table>

Each familiar includes the same import-critical animation states:

<table>
<tr>
<td><code>idle</code></td><td><code>running-right</code></td><td><code>running-left</code></td>
<td><code>waving</code></td><td><code>jumping</code></td><td><code>failed</code></td>
<td><code>waiting</code></td><td><code>running</code></td><td><code>review</code></td>
</tr>
</table>

`running-left` is mirrored from `running-right` only for genuinely symmetric familiars.

## One-command install

From any machine with Python 3 and Git:

```bash
PET=kageframe-rx07; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Then import the generated sprite package in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Choose:

```text
${CODEX_HOME:-$HOME/.codex}/pets/kageframe-rx07/spritesheet.webp
```

The metadata file is next to it:

```text
${CODEX_HOME:-$HOME/.codex}/pets/kageframe-rx07/pet.json
```

## Hatch a familiar manually

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/hatch_pet.py --pet ronin-build-fox --root .
python scripts/validate_all.py
git diff --check
```

The hatch script performs the deterministic pipeline:

1. stores the intended image-generation prompt in `generated/imagegen-prompt.json`,
2. creates or extracts a base look into `generated/base.png`,
3. composes row strips under `generated/strips/`,
4. builds `spritesheet.webp`,
5. writes `pet.json`,
6. validates dimensions and animation rows,
7. exports contact sheets plus per-state GIF/MP4 previews,
8. renders a stitched multi-motion `previews/<pet>-showcase.gif`,
9. packages the familiar into `${CODEX_HOME:-$HOME/.codex}/pets/<pet-name>/`.

To regenerate README media after adding familiars:

```bash
python scripts/render_showcase_gifs.py
python scripts/render_readme_hero.py
python scripts/sync_readme.py
```

## Package format

Each familiar directory is self-contained:

```text
pets/<pet-name>/
  README.md
  pet.json
  spritesheet.webp
  previews/
    <pet-name>-showcase.gif
    <pet-name>-contact-sheet.png
    <pet-name>-idle.gif
    ...
  generated/
    base.png
    imagegen-prompt.json
    strips/
      idle.png
      running-right.png
      running-left.png
      waving.png
      jumping.png
      failed.png
      waiting.png
      running.png
      review.png
```

The current spritesheet layout is `384×576`: six `64×64` frames per row and nine animation rows.

## Variation standard

A new familiar should not look like the previous familiar with different colors. Before publishing, check:

- silhouette overlap against existing familiars is not too high,
- head/body plan changes materially,
- motion language changes materially,
- at least one signature prop or creature feature is obvious at `64×64`,
- failed/waiting/review states are readable,
- README showcase cycles through multiple visibly different motions,
- no generated art claims to be a copyrighted character.

`python scripts/validate_all.py` includes a silhouette-overlap check and requires stitched showcase GIFs to catch clone-like or under-presented pets.

## Familiar ideas queued

Future hatches should rotate body plans instead of making the same mecha repeatedly:

- **Nebula Courier Mech** — courier robot with launch-thruster running animations.
- **Lotus Firewall Monk** — meditating cyber-monk bot with shield-petal review frames.
- **Samurai Cache Crab** — side-stepping armor crab with cache-crystal claws.
- **Ramen Debug Drone** — noodle-shop hover drone that serves hot fixes in a tiny bowl.
- **Origami Test Heron** — folded-paper cyber-heron that pecks flaky tests.

## Development and verification

```bash
python scripts/validate_all.py
python scripts/render_showcase_gifs.py
python scripts/render_readme_hero.py
python scripts/sync_readme.py
git diff --check
```

Before publishing a new familiar, check:

- `pet.json` exists and points to `spritesheet.webp`.
- All required animation rows exist.
- The root README links to the familiar README and shows aligned stitched showcase GIFs.
- GIF/MP4 previews are generated.
- The familiar installs into `${CODEX_HOME:-$HOME/.codex}/pets/<pet-name>/`.
- The new familiar is structurally distinct from earlier familiars.

## Project status

Early collection. The current familiars are usable now. New familiars are added as reviewable commits with validated packages.
