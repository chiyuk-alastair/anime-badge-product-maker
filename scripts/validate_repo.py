#!/usr/bin/env python3
"""Validate the public skill repository without third-party dependencies."""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "anime-badge-product-maker"
SKILL_MD = SKILL_DIR / "SKILL.md"

REQUIRED_FILES = (
    ROOT / ".editorconfig",
    ROOT / ".gitattributes",
    ROOT / ".gitignore",
    ROOT / ".github" / "CODEOWNERS",
    ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml",
    ROOT / ".github" / "workflows" / "validate-skill.yml",
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "CHANGELOG.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "SECURITY.md",
    ROOT / "SUPPORT.md",
    SKILL_MD,
    SKILL_DIR / "README.md",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "assets" / "default-blank-badge.png",
    SKILL_DIR / "references" / "README.md",
    SKILL_DIR / "references" / "source-cleanup.md",
    SKILL_DIR / "references" / "quality-checklist.md",
)

REQUIRED_OUTPUTS = (
    "01-badge-art.png",
    "02-badge-mockup.png",
    "03-badge-sales-image.png",
)

GENERATED_OUTPUTS = set(REQUIRED_OUTPUTS) | {
    "cleaned-background.png",
    "badge-cutout.png",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    fields: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            fail(f"invalid frontmatter line: {raw_line!r}")
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def validate_png(path: Path) -> None:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"{path.relative_to(ROOT)} is not a valid PNG")
    width, height = struct.unpack(">II", data[16:24])
    if width < 512 or height < 512:
        fail(f"blank badge asset is too small: {width}x{height}")


def local_markdown_links(text: str) -> list[str]:
    links = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip().split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        links.append(target)
    return links


def validate_links() -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts or ".validation-deps" in markdown.parts:
            continue
        for target in local_markdown_links(read_text(markdown)):
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository in {markdown.relative_to(ROOT)}: {target}")
            if not resolved.exists():
                fail(f"broken link in {markdown.relative_to(ROOT)}: {target}")


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill_text = read_text(SKILL_MD)
    fields = parse_frontmatter(skill_text)
    if fields.get("name") != "anime-badge-product-maker":
        fail("frontmatter name must be anime-badge-product-maker")
    if not fields.get("description") or len(fields["description"]) > 1024:
        fail("frontmatter description must contain 1-1024 characters")
    if fields.get("license") != "MIT":
        fail("frontmatter license must be MIT")

    lower_skill = skill_text.lower()
    for placeholder in ("todo", "tbd", "replace me", "example skill"):
        if placeholder in lower_skill:
            fail(f"unfinished placeholder found in SKILL.md: {placeholder}")

    for output in REQUIRED_OUTPUTS:
        if output not in skill_text:
            fail(f"required output is not documented in SKILL.md: {output}")
    if "马口铁胸针谷子" not in skill_text:
        fail("exact sales copy is missing from SKILL.md")
    if "character name" not in lower_skill or "version labels" not in lower_skill:
        fail("source text classification rules are incomplete")
    if "prompt-only" not in lower_skill:
        fail("SKILL.md must forbid prompt-only completion")

    ui_text = read_text(SKILL_DIR / "agents" / "openai.yaml")
    for required in ("display_name:", "short_description:", "default_prompt:"):
        if required not in ui_text:
            fail(f"agents/openai.yaml is missing {required}")
    if "$anime-badge-product-maker" not in ui_text:
        fail("default_prompt must mention $anime-badge-product-maker")

    validate_png(SKILL_DIR / "assets" / "default-blank-badge.png")
    validate_links()

    accidental = [
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file() and path.name.lower() in GENERATED_OUTPUTS
    ]
    if accidental:
        fail("generated customer outputs must not be committed: " + ", ".join(map(str, accidental)))

    print("Repository validation passed.")


if __name__ == "__main__":
    main()
