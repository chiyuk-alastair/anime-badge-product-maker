# Contributing

Thank you for improving Anime Badge Product Maker. Contributions should make the workflow more reliable, easier to understand, or easier to validate without weakening source fidelity.

## Before opening an issue

- Confirm the behavior is reproducible with the current `main` branch.
- Remove personal information, seller handles, watermarks, and private customer images.
- Describe the observable failure and the stage where it occurs.
- Do not upload copyrighted character source material unless you have the right to share it publicly.

Use the bug template for reproducible failures and the feature template for focused improvements. General usage questions belong in the support channel described in [SUPPORT.md](SUPPORT.md).

## Pull requests

1. Keep the change scoped to one clear problem.
2. Preserve the one-image default workflow and the three output contract unless the proposal explicitly changes the public interface.
3. Keep `SKILL.md` concise enough to load efficiently; move conditional detail into `references/`.
4. Never add customer uploads, generated customer deliverables, seller/platform screenshots, credentials, or private data.
5. Update English and Chinese documentation when public behavior changes.
6. Add an entry under `Unreleased` in [CHANGELOG.md](CHANGELOG.md).
7. Run `python scripts/validate_repo.py` before submitting.

## Instruction quality

Prefer rules that address a demonstrated, repeatable failure. Avoid adding broad restrictions from a single unusual example. Instructions should state observable outcomes and meaningful invariants rather than prescribing unnecessary implementation details.

## Commit messages

Use short imperative subjects, for example:

```text
Clarify character-name preservation
Add badge cutout edge checks
Fix broken documentation link
```

## License

By contributing, you agree that your contribution is licensed under the project's [MIT License](LICENSE).
