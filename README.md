# Icon-First Design

A reusable AI skill that encourages purposeful use of real icons from Lucide, Tabler, Heroicons, Phosphor, Fluent UI System Icons, Solar Icons, and Material Symbols.

## Contents

- `SKILL.md` — main behavior and instructions
- `references/` — library selection and usage guidance
- `assets/` — place for optional supporting visual assets
- `scripts/` — basic package validation helper

## Key behavior

The AI should proactively use icons when they improve clarity or visual design, even when icons were not explicitly requested. A clear instruction such as "don't add icons" overrides the default for that output.

## Validation

Run:

```bash
python scripts/validate_skill.py
```
