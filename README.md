# Anime Badge Product Maker

[![Validate skill](https://github.com/chiyuk-alastair/anime-badge-product-maker/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/chiyuk-alastair/anime-badge-product-maker/actions/workflows/validate-skill.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Codex-Agent%20Skill-111827)](skills/anime-badge-product-maker/SKILL.md)

English | [简体中文](README.zh-CN.md)

A reusable Codex skill that turns **one anime collectible-figure photo, GK photo, screenshot, or effect render** into a consistent three-image product set:

1. circular badge artwork;
2. a photoreal physical tinplate button-badge mockup;
3. a matching sales image built from the cleaned source figure, the exact physical badge, and the copy `马口铁胸针谷子`.

The workflow is designed around continuity: the uploaded figure is the source of truth, the mockup must reuse the approved badge art, and the final sales image must reuse the approved physical badge rather than redraw it.

## Highlights

- One-image input for the full workflow.
- Explicit character-identity, anatomy, and ownership checks.
- Screenshot cleanup that removes platform UI, seller traces, prices, watermarks, and unrelated clutter.
- Character names and genuine base inscriptions are preserved when they are part of the source.
- Physical badge realism: metal rim, dome, thickness, reflections, perspective, and contact shadow.
- Fixed, reviewable outputs with stage-by-stage hard gates.
- A correction limit that prevents endless silent retries or false claims of success.
- Repository validation in local development and GitHub Actions.

## Outputs

| File | Purpose |
| --- | --- |
| `01-badge-art.png` | Square circular anime artwork derived from the current figure reference. |
| `02-badge-mockup.png` | The approved artwork printed on a photoreal physical tinplate badge. |
| `03-badge-sales-image.png` | Cleaned figure background plus the exact physical badge and `马口铁胸针谷子`. |

The cleaned background and transparent badge cutout are intermediate assets. They are returned only when requested or needed for review.

## Installation

Clone the repository and copy the complete skill directory. Do not copy `SKILL.md` by itself because the workflow also uses its references, UI metadata, and physical badge asset.

PowerShell:

```powershell
git clone https://github.com/chiyuk-alastair/anime-badge-product-maker.git
Copy-Item -Recurse -Force `
  .\anime-badge-product-maker\skills\anime-badge-product-maker `
  "$env:USERPROFILE\.codex\skills\anime-badge-product-maker"
```

Bash:

```bash
git clone https://github.com/chiyuk-alastair/anime-badge-product-maker.git
cp -R anime-badge-product-maker/skills/anime-badge-product-maker \
  "${CODEX_HOME:-$HOME/.codex}/skills/anime-badge-product-maker"
```

Restart or refresh Codex after installation if the skill is not discovered immediately.

## Usage

Attach one current figure image and invoke:

```text
Use $anime-badge-product-maker to turn this figure image into the complete badge product set.
```

Chinese invocation:

```text
使用 $anime-badge-product-maker，把这张实体手办图按完整流程制作成两张徽章图和一张背景图+实体徽章商品图。
```

The skill proceeds without unnecessary questions unless the source contains competing subjects or contradictory identity evidence.

## Source cleanup policy

The final background keeps the actual figure or render, including pose, material, paint, accessories, effects, companion motifs, and display base. It removes phone/app controls, marketplace UI, seller copy, prices, coupons, watermarks, studio marks, version labels, and unrelated household clutter.

A clearly identified character name or genuine name inscription on the base is preserved. Franchise logos and promotional copy are removed by default unless the user asks to keep them.

See [source cleanup rules](skills/anime-badge-product-maker/references/source-cleanup.md) for the full decision table.

## Quality gates

Every stage is reviewed before the next stage begins. Hard gates cover:

- character identity and anatomy;
- art-to-mockup consistency;
- physical badge realism;
- source fidelity and cleanup;
- exact reuse of the physical badge in the sales image;
- exact Chinese copy `马口铁胸针谷子`.

See the [quality checklist](skills/anime-badge-product-maker/references/quality-checklist.md).

## Repository layout

```text
anime-badge-product-maker/
├── .github/                         Project automation and contribution templates
├── scripts/validate_repo.py         Dependency-free repository validator
├── skills/anime-badge-product-maker/
│   ├── SKILL.md                     Skill entry point and workflow
│   ├── agents/openai.yaml           Codex UI metadata
│   ├── assets/default-blank-badge.png
│   └── references/                  Cleanup rules and quality gates
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── SUPPORT.md
└── LICENSE
```

## Validation

Run the repository validator with Python 3.9 or newer:

```bash
python scripts/validate_repo.py
```

It checks required files, frontmatter, skill naming, UI metadata, resource links, the PNG asset, required output names, exact sales copy, and accidental inclusion of generated customer images.

When the official Codex `skill-creator` validator is available, also run:

```text
quick_validate.py skills/anime-badge-product-maker
```

GitHub Actions runs the dependency-free validator on every push and pull request.

## Privacy and repository scope

This repository intentionally contains no customer uploads, historical source photographs, generated character outputs, seller handles, marketplace screenshots, or studio marks. The included PNG is a generic blank physical badge asset used only as an edit target.

## Limitations

- Results are visual designs and product previews, not automatically print-ready manufacturing files.
- Production output still requires the vendor's diameter, bleed, safe-area, resolution, and color-profile specifications.
- A low-resolution or heavily occluded source may limit identity and anatomy fidelity.
- The skill does not infer a missing or expired source from memory; it asks for a fresh attachment.

## Contributing

Bug reports and focused improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

For security-sensitive reports, follow [SECURITY.md](SECURITY.md) instead of opening a public issue. General help is covered by [SUPPORT.md](SUPPORT.md).

## License

Released under the [MIT License](LICENSE).
