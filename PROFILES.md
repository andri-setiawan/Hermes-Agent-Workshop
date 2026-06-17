# Hermes Profiles

![profiles](screenshots/10_hermes_profiles_docs.png)

Create purpose-specific isolated profiles:

```bash
# Create profiles
hermes profile create research --clone-from default
hermes profile create slr --clone-from default
hermes profile create writing --clone-from default

# List profiles
hermes profile list

# View a profile
hermes profile show research

# Switch
hermes profile use research
```

## Profile Structure
Each profile lives at `~/.hermes/profiles/<name>/` with:
- `config.yaml`
- `.env`
- `skills/`
- `sessions/`
- `memories/`

## Use Case
- `research` — Scopus skills, SLR workflows, paper reading
- `writing` — Academic paper drafting, de-AI-fy tools
- `slr` — Systematic literature review toolsets only
