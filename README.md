# copier-templates

Authored Copier templates for new project spinup in this ecosystem.

## Layout

- `copier_code_template/` — Python code project template (migrated from the retired `copier-workspace` repo)
- `copier_paper_template/` — LaTeX scientific paper template (migrated from the retired `copier-paper-workspace` repo)

Each template root is independently usable:

    copier copy --trust /home/dcl3nd/dev/copier-templates/copier_code_template /home/dcl3nd/dev/{new-code-project}
    copier copy --trust /home/dcl3nd/dev/copier-templates/copier_paper_template /home/dcl3nd/dev/{new-paper-project}

The user-facing orchestration skill is `/copier-copy` in the agentic-workspace runtime; see that skill body for the route-selection flow.

Authoritative design reference: `library/prompts/workspaces/projects/copier-templates/copier templates architecture.md` in the agentic-workspace repo.

## Release discipline

Templates share a single tag sequence (e.g., `v0.1.0`, `v0.2.0`, ...). Tag from this repo's root; Copier resolves the tag across both template roots.
