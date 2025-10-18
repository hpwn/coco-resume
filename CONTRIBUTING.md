# Contributing to Coco Resume

Thanks for your interest in contributing! This project uses a pnpm + Turbo
monorepo. The following guidelines will help you get started.

## Development workflow

1. Install dependencies with `pnpm install`.
2. Run `pnpm -w build` to make sure everything compiles.
3. Use `pnpm -w lint`, `pnpm -w typecheck`, and `pnpm -w test` to validate your
   changes.

## Commit messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) spec.
Use `pnpm dlx commitlint` if you want to validate a commit message locally.

## Code style

- Format code with Prettier using `pnpm format`.
- Lint with ESLint using `pnpm -w lint`.
- Add tests alongside code where possible.

## Communication

For questions, open a GitHub issue or reach out to
[maintainers@coco-resume.dev](mailto:maintainers@coco-resume.dev).
