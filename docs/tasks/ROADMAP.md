# Roadmap

Milestones in dependency order. M01–M16 follow PLAN.md 16 one to one (M03 rewritten for project folders, ADR 0005);
M17–M21 cover screens designed after PLAN.md was written; M22–M24 are PLAN.md milestones 17–19.

Each milestone file holds its goal, specification pointers, designs, acceptance criteria and tasks. Before starting a
milestone, run the `daisy-plan-milestone` skill to refine its tasks against the spec (tasks converted from PLAN.md
are one line each and get their _Needs_ and _Done when_ filled in then).

| #   | Milestone                                                                  | Designs                                                 | Tasks | File                                                                                             |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------ |
| M00 | Project setup and toolchain                                                | all repo                                                | 9     | [M00-project-setup-and-toolchain.md](M00-project-setup-and-toolchain.md)                         |
| M01 | Clean document and core editor loop                                        | D-03, D-04 (shell frame only)                           | 14    | [M01-clean-document-and-core-editor-loop.md](M01-clean-document-and-core-editor-loop.md)         |
| M02 | Selection and manipulation                                                 | D-05–D-11, D-19                                         | 12    | [M02-selection-and-manipulation.md](M02-selection-and-manipulation.md)                           |
| M03 | Projects on disk, saving and Home                                          | D-01, D-02, D-02b, D-46, D-52                           | 12    | [M03-projects-on-disk-saving-and-home.md](M03-projects-on-disk-saving-and-home.md)               |
| M04 | Element creation tools and text editing                                    | D-12, D-13, D-17, D-18, D-41, D-42, D-43                | 14    | [M04-element-creation-tools-and-text-editing.md](M04-element-creation-tools-and-text-editing.md) |
| M05 | Layers and document hierarchy                                              | D-24, D-25                                              | 11    | [M05-layers-and-document-hierarchy.md](M05-layers-and-document-hierarchy.md)                     |
| M06 | Properties architecture                                                    | D-04, D-20                                              | 14    | [M06-properties-architecture.md](M06-properties-architecture.md)                                 |
| M07 | Layout and spacing                                                         | D-14, D-15, Layout-Advanced                             | 12    | [M07-layout-and-spacing.md](M07-layout-and-spacing.md)                                           |
| M08 | Typography and appearance                                                  | D-35 Radius, D-39, D-47                                 | 13    | [M08-typography-and-appearance.md](M08-typography-and-appearance.md)                             |
| M09 | Assets and media                                                           | D-17, D-26                                              | 11    | [M09-assets-and-media.md](M09-assets-and-media.md)                                               |
| M10 | Preview and export                                                         | D-29, D-30, D-55                                        | 11    | [M10-preview-and-export.md](M10-preview-and-export.md)                                           |
| M11 | Responsive editing                                                         | D-22, D-23                                              | 12    | [M11-responsive-editing.md](M11-responsive-editing.md)                                           |
| M12 | States and transitions                                                     | D-21                                                    | 10    | [M12-states-and-transitions.md](M12-states-and-transitions.md)                                   |
| M13 | Advanced CSS and positioning                                               | D-16, D-19                                              | 11    | [M13-advanced-css-and-positioning.md](M13-advanced-css-and-positioning.md)                       |
| M14 | Animation                                                                  | D-28, D-28b                                             | 10    | [M14-animation.md](M14-animation.md)                                                             |
| M15 | Custom code and attributes                                                 | D-27, D-27b                                             | 12    | [M15-custom-code-and-attributes.md](M15-custom-code-and-attributes.md)                           |
| M16 | Full element library and accessibility                                     | D-18, D-42, D-25                                        | 12    | [M16-full-element-library-and-accessibility.md](M16-full-element-library-and-accessibility.md)   |
| M17 | Pages and project settings                                                 | D-31, D-31b, D-44, D-44b, D-45, D-54                    | 6     | [M17-pages-and-project-settings.md](M17-pages-and-project-settings.md)                           |
| M18 | Design system                                                              | D-36, D-36b, D-36c, D-02b step 3                        | 6     | [M18-design-system.md](M18-design-system.md)                                                     |
| M19 | Reusable content: shared parts, components, collections, interactive parts | D-53, D-56, D-56b, D-57, D-57b, D-58, D-58b             | 8     | [M19-reusable-content-shared-parts.md](M19-reusable-content-shared-parts.md)                     |
| M20 | Menus, search, preferences, shortcuts and themes                           | D-38, D-40, D-48, D-49, D-50, D-51, D-33, D-33b–d, D-34 | 8     | [M20-menus-search-preferences-shortcuts-and.md](M20-menus-search-preferences-shortcuts-and.md)   |
| M21 | MCP server for AI apps                                                     | D-59, D-59b, D-59c                                      | 9     | [M21-mcp-server-for-ai-apps.md](M21-mcp-server-for-ai-apps.md)                                   |
| M22 | History, versions and project files                                        | D-32, D-32b                                             | 11    | [M22-history-versions-and-project-files.md](M22-history-versions-and-project-files.md)           |
| M23 | Performance and editor accessibility                                       | —                                                       | 10    | [M23-performance-and-editor-accessibility.md](M23-performance-and-editor-accessibility.md)       |
| M24 | Release 1.0: polish, signing and distribution                              | all boards                                              | 12    | [M24-release-1-0-polish-signing-and.md](M24-release-1-0-polish-signing-and.md)                   |

## Release stages

| Stage                                   | After | Audience                       |
| --------------------------------------- | ----- | ------------------------------ |
| Internal alpha                          | M03   | the owner: build, save, reopen |
| Public alpha (unsigned, `beta` channel) | M10   | testers: real pages, export    |
| Beta (signed)                           | M16   | early users                    |
| 1.0                                     | M24   | everyone                       |
