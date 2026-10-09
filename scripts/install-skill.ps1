[CmdletBinding()]
param(
    [string]$CodexHome = ""
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $projectRoot "skills\anime-badge-product-maker"

if (-not (Test-Path -LiteralPath (Join-Path $source "SKILL.md") -PathType Leaf)) {
    throw "Skill source was not found at: $source"
}

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    if (-not [string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
        $CodexHome = $env:CODEX_HOME
    }
    else {
        $CodexHome = Join-Path $env:USERPROFILE ".codex"
    }
}

$skillsRoot = Join-Path $CodexHome "skills"
$target = Join-Path $skillsRoot "anime-badge-product-maker"

New-Item -ItemType Directory -Force -Path $target | Out-Null
Get-ChildItem -LiteralPath $source -Force |
    Copy-Item -Destination $target -Recurse -Force

Write-Output "Installed anime-badge-product-maker to: $target"
