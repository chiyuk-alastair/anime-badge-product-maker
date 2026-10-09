#!/usr/bin/env bash
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
project_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
source_dir="$project_root/skills/anime-badge-product-maker"

if [ ! -f "$source_dir/SKILL.md" ]; then
  printf 'Skill source was not found at: %s\n' "$source_dir" >&2
  exit 1
fi

codex_home=${1:-${CODEX_HOME:-"$HOME/.codex"}}
target="$codex_home/skills/anime-badge-product-maker"

mkdir -p "$target"
cp -R "$source_dir"/. "$target"/

printf 'Installed anime-badge-product-maker to: %s\n' "$target"
