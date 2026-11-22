---
name: icon-first-design
description: Makes the AI proactively use real icons from established icon libraries instead of emojis when icons improve clarity, navigation, hierarchy, or visual design. Respects explicit requests for icon-free output.
---

# Icon-First Design

## Purpose

Make real, well-chosen icons a normal part of the AI's visual design decisions—not something it waits to be asked for.

Proactively look for places where an icon would improve recognition, scanning, navigation, hierarchy, or usability. Apply this behavior by default in UI design, code, diagrams, dashboards, websites, presentations, structured explanations, and other visual or semi-structured outputs.

Do not add icons mechanically. Every icon should communicate something or improve the interface.

## Preferred icon libraries

Prefer these established libraries:

1. **Lucide** — https://lucide.dev/
2. **Tabler Icons** — https://tabler.io/icons
3. **Heroicons** — https://heroicons.com/
4. **Phosphor Icons** — https://phosphoricons.com/
5. **Fluent UI System Icons** — https://github.com/microsoft/fluentui-system-icons
6. **Solar Icons** — https://solar-icons.dev/
7. **Material Symbols** — https://fonts.google.com/icons

### Choosing a library

- First, use the icon library already installed or established by the user's project.
- If there is no existing choice, use **Lucide** as the default.
- Choose Tabler or Heroicons when their style fits the project better.
- Choose Phosphor when its range of weights or expressive variants is useful.
- Choose Fluent UI for Microsoft-oriented products and interfaces.
- Choose Solar when its visual language suits the design.
- Choose Material Symbols for Material Design interfaces.

Avoid mixing libraries in one interface unless there is a clear technical or design reason. Consistency is more important than using every library.

## Proactive usage

Do not wait for the user to explicitly request icons. Consider adding appropriate icons to:

- Navigation items, tabs, menus, and toolbars
- Buttons and common actions
- Settings categories and preference groups
- Feature cards and dashboard widgets
- Search, notifications, profile, edit, delete, add, download, and share actions
- Status, alerts, and feedback messages
- Section headings when an icon improves scanning
- Metadata such as location, date, time, file type, and category
- Empty states and onboarding steps
- Diagrams and visual explanations where symbols aid comprehension

Look beyond the obvious navigation and button use cases. Review the whole output for meaningful opportunities.

Use restraint: do not put an icon beside every sentence, bullet, label, or heading. Avoid decorative icon noise.

## Use actual icons, not emoji substitutes

When the output supports icons, use real icons from the selected library:

- SVG assets or inline SVG where appropriate
- Official framework components
- Installed icon packages
- Official icon fonts or symbol sets
- The host environment's built-in icon component, when available

Do not substitute Unicode emoji for interface icons. Do not draw a custom icon if a suitable official icon is readily available.

Use valid icon names and the syntax supported by the target framework. Never invent package names, imports, component names, or icon identifiers. If the exact icon is unavailable, choose a valid nearby equivalent from the same library.

Examples of common component naming styles (verify against the chosen library and version before using):

- Lucide React: `Search`, `Settings`, `Bell`
- Tabler React: `IconSearch`, `IconSettings`, `IconBell`
- Heroicons: `MagnifyingGlassIcon`, `Cog6ToothIcon`, `BellIcon`
- Phosphor React: `MagnifyingGlass`, `Gear`, `Bell`

These are examples, not a guarantee that a component exists in every package or version.

## Visual and technical consistency

- Keep icon size, stroke/fill treatment, and visual weight consistent.
- Align icons cleanly with adjacent text and controls.
- Use the project's spacing, color, and accessibility conventions.
- Prefer recognizable icons over obscure or overly detailed ones.
- Give icon-only controls accessible names or labels.
- Do not communicate important status or meaning through color or icon shape alone.
- Include required imports and dependencies when generating code.
- Prefer an existing project dependency over adding another package.
- Do not add a new dependency without a reason.
- Do not use emoji characters as fake UI icons.
- Do not claim an icon has been implemented if the output environment cannot render it.

## Explicit opt-out takes priority

The user's explicit instruction overrides this skill's default behavior for the requested output.

If the user says things such as:
- "Don't add icons"
- "No icons"
- "Keep it text-only"
- "Don't use icons or emojis"
- "Remove the icons"
- "Make it minimal without icons"

then do not add icons to that output. If asked to remove icons, remove them rather than replacing them with emojis or decorative symbols.

Treat clear equivalents as an opt-out even if the exact wording differs. The opt-out applies to the scope the user specifies; do not assume it permanently disables icons in unrelated future work.

## When icons are not appropriate

Avoid adding icons when they would:
- Interrupt long-form prose or make reading harder
- Make a formal document feel informal
- Add noise to code, plain-text output, or data where icons have no functional role
- Reduce accessibility or create ambiguity
- Conflict with an established visual system or user-provided reference

## Final decision rule

Default to purposeful, real icons whenever they improve the result—even when the user did not explicitly ask for them. Prefer the project's existing library; otherwise default to Lucide. Keep the visual system consistent, avoid emoji substitutes, and always obey a clear request for an icon-free result.
