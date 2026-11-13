# Architecture decision records

One file per decision, numbered. Create with `pnpm new:adr "Title"`. An ADR that changes PLAN.md must name the sections it supersedes, and PLAN.md gets a pointer to it.

- [0001. Desktop app on Electron](0001-desktop-app-on-electron.md)
- [0002. pnpm workspaces and Turborepo monorepo](0002-pnpm-workspaces-and-turborepo-monorepo.md)
- [0003. Internal packages are consumed as TypeScript source](0003-internal-packages-are-consumed-as-typescript-source.md)
- [0004. GitHub Actions for CI/CD; GitHub Releases for distribution](0004-github-actions-for-ci-cd-github-releases-for-distribution.md)
- [0005. Projects are folders on disk](0005-projects-are-folders-on-disk.md)
- [0006. Daisy is an MCP server; changes go through renderer commands](0006-daisy-is-an-mcp-server-changes-go-through-renderer-commands.md)
- [0007. Open source under MIT](0007-open-source-under-mit.md)
- [0008. Toolchain versions](0008-toolchain-versions.md)
- [0009. Agent-native development](0009-agent-native-development.md)
- [0010. Preview in an isolated Electron session](0010-preview-in-an-isolated-electron-session.md)
- [0011. Classes and dependency injection](0011-classes-and-dependency-injection.md)
- [0015. No fallbacks; the native addon is required](0015-no-fallbacks-the-native-addon-is-required.md)
- [0014. No Go or standalone C++; C++ only as the Node addon](0014-no-go-or-standalone-cpp-c-only-as-the-node-addon.md)
- [0013. Native addons with Node-API and cmake-js](0013-native-addons-with-node-api-and-cmake-js.md)
- [0012. Go, C++ and Python alongside TypeScript](0012-go-cpp-and-python-alongside-typescript.md)
