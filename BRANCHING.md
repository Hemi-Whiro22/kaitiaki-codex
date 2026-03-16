# Branching strategy

A lightweight, clear workflow suitable for small teams:

- main: always deployable. Protected branch.
- feature/\*: work on features or fixes. PR into main.
- docs/_, chore/_: maintenance docs and chores.
- release/\* (optional): version prep if you need CHANGELOGs or manual QA.

Recommended flow:

1. Create a branch: `git checkout -b feature/short-description`
2. Commit small, focused changes.
3. Open a PR to `main`, require at least one review.
4. Rebase or merge — either is fine for this repo; keep history readable.
5. Delete the branch after merge.

Notes:

- Tag releases from `main` like `v0.1.0` when you deploy.
- Add CI: typecheck/build and secret scan on PRs.
- Keep `.env.*` and keys out of git; use `.env.example` for docs.
