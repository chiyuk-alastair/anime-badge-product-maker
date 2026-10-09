# Anime Badge Product Maker

[![校验 Skill](https://github.com/chiyuk-alastair/anime-badge-product-maker/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/chiyuk-alastair/anime-badge-product-maker/actions/workflows/validate-skill.yml)
[![许可证：MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Codex-Agent%20Skill-111827)](skills/anime-badge-product-maker/SKILL.md)

[English](README.md) | 简体中文

这是一个可复用的 Codex Skill：只需要一张动漫实体手办图、GK 图、截图或效果图，就能制作一套前后一致的三张商品图：

1. 圆形徽章画稿；
2. 真实马口铁实体徽章效果图；
3. 由清理后的原手办背景、同一个实体徽章以及文案 `马口铁胸针谷子` 组成的商品图。

整个流程最重视一致性：用户当前上传的手办是唯一依据；实体徽章必须使用已确认的徽章画稿；最终商品图必须复用已确认的实体徽章，不能重新画一个相似的圆形图案代替。

## 主要特点

- 单张图片即可启动完整流程。
- 明确检查人物身份、肢体归属和手部结构。
- 自动区分并去除截图 UI、平台痕迹、卖家文字、价格、水印和无关杂物。
- 人物名字和底座上真实存在的人名刻字默认保留。
- 保留实体徽章的金属边、弧面、厚度、反光、透视和接触阴影。
- 三个固定产物，逐阶段检查后再继续。
- 每阶段最多两轮针对性修正，避免无限重试或把不合格结果说成合格。
- 提供本地校验脚本和 GitHub Actions 自动校验。

## 固定产物

| 文件 | 说明 |
| --- | --- |
| `01-badge-art.png` | 根据当前手办参考制作的圆形动漫徽章画稿。 |
| `02-badge-mockup.png` | 将已确认画稿放入真实马口铁徽章后的实体效果图。 |
| `03-badge-sales-image.png` | 清理后的手办背景 + 同一个实体徽章 + `马口铁胸针谷子`。 |

清理后的背景图和透明徽章抠图属于中间素材，只有用户明确要求或审核需要时才单独交付。

## 安装

克隆仓库后，请完整复制 Skill 文件夹。不要只复制 `SKILL.md`，因为流程还会使用参考规则、界面元数据和默认实体徽章素材。

PowerShell（更新时可以安全地重复执行）：

```powershell
git clone https://github.com/chiyuk-alastair/anime-badge-product-maker.git
.\anime-badge-product-maker\scripts\install-skill.ps1
```

Bash（更新时可以安全地重复执行）：

```bash
git clone https://github.com/chiyuk-alastair/anime-badge-product-maker.git
bash anime-badge-product-maker/scripts/install-skill.sh
```

安装脚本会优先使用 `CODEX_HOME`，未设置时使用标准的 `~/.codex` 目录。更新已有仓库时，请先在仓库内运行 `git pull --ff-only`，再重新运行安装脚本。两个脚本都会把 Skill 内容合并到现有目标目录，不会再套出第二层同名目录。

如 Codex 没有马上识别新 Skill，请刷新或重启 Codex。

## 使用方法

上传一张当前要制作的手办图，然后调用：

```text
使用 $anime-badge-product-maker，把这张实体手办图按完整流程制作成两张徽章图和一张背景图+实体徽章商品图。
```

除非图片里存在多个可能的主体，或不同参考图之间存在身份冲突，否则 Skill 会直接开始，不会反复追问。

## 背景清理规则

最终背景会保留真实手办或效果图中的造型、姿势、材质、涂装、服装、配件、能力特效、陪衬角色和底座；移除手机/应用控件、平台界面、卖家宣传、价格、优惠券、水印、工作室标记、版本标签以及无关生活杂物。

明确的人物名字或底座上真实存在的人名刻字应保留。作品标题、Logo 和宣传文案默认移除，除非用户明确要求保留。

完整判断表见[背景清理规则](skills/anime-badge-product-maker/references/source-cleanup.md)。

## 质量门槛

每个阶段在进入下一阶段前都必须检查。硬性门槛包括：

- 人物身份和解剖结构；
- 画稿与实体徽章的一致性；
- 实体徽章的真实感；
- 原手办的保真度与背景清理质量；
- 最终商品图是否使用同一个实体徽章；
- `马口铁胸针谷子` 七个字是否完全正确。

完整项目见[质量检查清单](skills/anime-badge-product-maker/references/quality-checklist.md)。

## 项目结构

```text
anime-badge-product-maker/
├── .github/                         自动校验与贡献模板
├── scripts/
│   ├── install-skill.ps1            可重复执行的 PowerShell 安装器
│   ├── install-skill.sh             可重复执行的 Bash 安装器
│   └── validate_repo.py             无第三方依赖的仓库校验器
├── skills/anime-badge-product-maker/
│   ├── SKILL.md                     Skill 入口与完整工作流
│   ├── agents/openai.yaml           Codex 界面元数据
│   ├── assets/default-blank-badge.png
│   └── references/                  背景清理规则和质量门槛
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── SUPPORT.md
└── LICENSE
```

## 校验

使用 Python 3.9 或更高版本运行：

```bash
python scripts/validate_repo.py
```

校验器会检查必需文件、YAML frontmatter、Skill 命名、界面元数据、资源链接、PNG 素材、三个固定产物名、准确文案、工作流依赖固定方式，以及是否误提交了未批准图片。

如需逐字节比对已安装副本和仓库中的 Skill，可运行：

```bash
python scripts/validate_repo.py --installed-skill /path/to/.codex/skills/anime-badge-product-maker
```

GitHub Actions 会在每次推送和 Pull Request 时同时在 Windows 与 Linux 上执行仓库校验和重复安装测试。

## 隐私与仓库边界

本仓库不会收录用户上传的图片、历史手办照片、生成的人物图、卖家账号、平台截图或工作室水印。仓库中的 PNG 只是一个通用空白实体徽章素材，只用于承载已经确认的徽章画稿。

## 限制

- 产物属于视觉设计和商品预览，不会自动成为可直接生产的印刷文件。
- 真正生产仍需徽章厂商提供直径、出血、安全区、分辨率和色彩配置要求。
- 原图分辨率过低或主体遮挡严重时，人物身份和肢体准确度会受限。
- 原图失效或无法读取时，Skill 会要求重新上传，不会靠记忆伪造背景。

## 参与贡献

欢迎提交问题和有针对性的改进。发起 Pull Request 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，参与项目即表示同意遵守[行为准则](CODE_OF_CONDUCT.md)。

安全问题请按 [SECURITY.md](SECURITY.md) 私下报告，不要公开提交 Issue。一般使用帮助见 [SUPPORT.md](SUPPORT.md)。

## 许可证

本项目使用 [MIT License](LICENSE)。
