# CONTRIBUTING.md

Thank you for your interest in contributing to Space Leaf Corp — Digital Sea. This document explains how to contribute code, documentation, designs, simulations, and governance proposals in a way that keeps safety, transparency, and stewardship front and center.

## Code of Conduct
All contributors must follow the project Code of Conduct in `governance/CODE_OF_CONDUCT.md`. Be respectful, constructive, and safety minded. Report violations to the Stewardship Board.

## Ways to Contribute
- **Issues**: Report bugs, propose features, or start design discussions. Use clear titles and include reproducible steps or sketches.
- **Pull Requests**: Submit fixes, features, tests, or documentation improvements via PRs.
- **Designs and Diagrams**: Add to `/concepts/` with clear captions and versioned files.
- **Simulations**: Add runnable prototypes to `/simulations/` with usage instructions and test data.
- **Governance Proposals**: Submit charter, funding, or policy proposals to `/governance/` and tag them `proposal/`.

## Getting Started
1. Fork the repository and create a feature branch named `feat/<short-description>` or `fix/<short-description>`.
2. Run tests locally and ensure linting passes.
3. Open a pull request against `main` with a clear description, motivation, and test plan.

## Branching and Pull Request Guidelines
- Base branches on `main`.
- Keep PRs focused and small when possible.
- Include tests for new behavior and update documentation.
- Use descriptive commit messages. Follow this format:
  - `feat: short description`
  - `fix: short description`
  - `docs: short description`
  - `chore: short description`
- Link related issue numbers in the PR description.

## Issue Templates and Labels
- Use labels: `bug`, `enhancement`, `proposal`, `design`, `security`, `documentation`.
- For design proposals include diagrams, rationale, and safety analysis.

## Testing and Continuous Integration
- Add unit tests for logic and simulation scripts.
- CI runs on every PR and must pass before merging.
- Include reproducible examples for simulation scripts.

## Security Sensitive Changes
- Security related code or protocol changes must reference `SECURITY.md` and follow the responsible disclosure process.
- Major protocol or funding changes require Stewardship Board review before merging.

## Licensing and Copyright
- Contributions are licensed under the repository MIT License.
- Do not submit third party code without appropriate license and attribution.

## Stewardship Board Review
- Changes that affect funding, charter access, or public deployments require a Stewardship Board signoff. See `governance/STEWARDSHIP_BOARD.md`.

## Documentation Standards
- Document APIs, simulation parameters, and governance changes.
- Add usage examples and expected outputs for simulation scripts.

## How to Propose a Partnership or Funding Change
- Create a governance proposal in `/governance/` with `proposal/` prefix.
- Include draft partnership agreement, scope of work, and financial impact.
- The Stewardship Board will review and publish minutes in `/governance/board_minutes/`.

## Contact and Questions
- For general contribution questions open an issue tagged `help wanted`.
- For security issues follow `SECURITY.md`.

Thank you for helping build the Digital Sea responsibly.
