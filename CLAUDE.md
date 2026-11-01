# CLAUDE.md

Project rules for Claude Code in this repository.

## Project summary

A FastMCP server with five arithmetic tools: `add`, `subtract`, `divide`, `power`, and `fraction`. A CLI for demos is planned in issue #2. It does not exist yet.

## Precedence

The user's global `CLAUDE.md` still applies. This file wins on project topics such as the model, the stack, and the workflow. This file cannot remove a global data privacy rule or a global file protection.

## Commit rule

Format: `type: short description`. Example: `feat: add an MCP client CLI for the demo`.

| Type | Use for |
|---|---|
| `feat` | A new capability for the user |
| `fix` | A defect repair |
| `chore` | Dependencies, configuration, or tidying. The user sees no new behaviour |
| `docs` | Documentation only |
| `refactor` | The structure changes. The behaviour stays the same |

## Branch rule

Format: `type/short-description`, with the same types. Example: `feat/mcp-client-cli`.

Use lower case and hyphens. Each PR has one branch.

## Push rule

1. Do not push directly to `main`. Raise a PR.
2. Do not force push.
3. Confirm with the user before each push.

## Commands

Set up the project:

```bash
uv sync
```

Run the server over stdio:

```bash
uv run fastmcp run mcp_server_01.py
```

Run the server over SSE at `http://127.0.0.1:8000/sse`:

```bash
uv run python mcp_server_01.py
```

Run the checks. These tools are not project dependencies yet, so use `uvx`:

```bash
uvx black --check .
```

```bash
uvx ruff check .
```

```bash
uvx pytest
```

`uvx pytest` runs in an isolated environment without `fastmcp`. It fails when a test imports the project. Add `pytest` as a dev dependency and use `uv run pytest` when the first test is added.

## LLM model

Planned in issue #3. No LLM code exists yet. Use `claude-haiku-5-5`. The task is short tool selection with simple arithmetic, so a small model is sufficient.

## API-first exception

The planned CLI will call the MCP server directly, with no FastAPI layer. The MCP server is already the API, and the goal is a CLI demo.

## Secrets

Real keys go in `.env` only. `.env` never goes to git. `.env.example` holds names and empty values only.

## Definition of done

1. Format passes.
2. Lint passes.
3. Tests pass.
4. `changelog.md` is updated for each changed file.
5. `/code-review` has run, and the findings went to the user.
6. The user approved the findings.

## Known open issues

GitHub tracks planned work: https://github.com/skolvankar/my-first-mcp-server/issues

These findings have no tracking issue:

1. **Blocker for issues #1, #2, and #3:** `pytest` stops with exit code 4 when the project path contains `[` or `]`. The error is "path cannot contain [] parametrization". Each issue requires `pytest` to pass. Move the project to a path without these characters before you start these issues.
2. `black --check` fails. `black` would reformat `mcp_server_01.py`.
3. `pyproject.toml` sets Python `>=3.10`. The global floor is `>=3.11`.
4. `uv.lock` is not in git.
5. `README.md` shows a Windows username and a local folder path.
6. `README.md` gives a venv and pip setup. This file gives a uv setup.
7. The project has no tests yet.
8. `black`, `ruff`, and `pytest` are not project dependencies.
