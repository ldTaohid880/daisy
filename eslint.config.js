// Flat config. Package boundaries are checked by scripts/check-deps.ts;
// this file enforces code rules that apply everywhere.
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import reactHooks from 'eslint-plugin-react-hooks';
import prettier from 'eslint-config-prettier';
import globals from 'globals';

export default tseslint.config(
  { ignores: ['**/dist/**', '**/out/**', '**/coverage/**', '**/release/**', 'design-src/**', '**/*.d.ts'] },
  js.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  {
    languageOptions: {
      parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
    },
    rules: {
      '@typescript-eslint/consistent-type-imports': 'error',
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-non-null-assertion': 'error',
      'no-console': ['error', { allow: ['warn', 'error'] }],
      eqeqeq: ['error', 'always'],
      // ADR 0011 allows pure logic as static methods on a class.
      '@typescript-eslint/no-extraneous-class': ['error', { allowStaticOnly: true }],
    },
  },
  // Pure packages: no DOM, no Node, no React. They must run anywhere.
  {
    files: ['packages/{di,model,css,html,export,ipc}/src/**/*.ts'],
    languageOptions: { globals: {} },
    rules: {
      'no-restricted-globals': ['error', 'window', 'document', 'navigator', 'process', 'require', 'Buffer'],
      'no-restricted-imports': [
        'error',
        { patterns: ['node:*', 'fs', 'path', 'react', 'react-dom', 'electron'] },
      ],
    },
  },
  // Renderer-side packages: never touch Node or Electron directly. Use window.daisy (preload).
  {
    files: ['packages/{renderer,ui,editor}/src/**/*.{ts,tsx}', 'apps/desktop/src/renderer/**/*.{ts,tsx}'],
    languageOptions: { globals: { ...globals.browser } },
    plugins: { 'react-hooks': reactHooks },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            'node:*',
            'fs',
            'path',
            'electron',
            '@daisy/project-fs',
            '@daisy/mcp-server',
            '@daisy/native',
          ],
        },
      ],
    },
  },
  // Node-side packages and the Electron main process.
  {
    files: [
      'packages/{project-fs,mcp-server,native}/src/**/*.ts',
      'packages/native/scripts/**/*.ts',
      'apps/desktop/src/{main,preload}/**/*.ts',
      'scripts/**/*.ts',
      '.claude/hooks/*.ts',
    ],
    languageOptions: { globals: { ...globals.node } },
    rules: {
      'no-restricted-imports': [
        'error',
        { patterns: ['react', 'react-dom', '@daisy/editor', '@daisy/ui', '@daisy/renderer'] },
      ],
    },
  },
  // ADR 0011: classes first. Logic lives in classes; module-level functions are not allowed in .ts files.
  // In .tsx only React components (Capitalised) and hooks (use…) may be functions.
  {
    files: ['**/*.ts'],
    ignores: ['**/*.config.ts', '**/*.d.ts'],
    rules: {
      'no-restricted-syntax': [
        'error',
        {
          selector:
            'Program > FunctionDeclaration, Program > ExportNamedDeclaration > FunctionDeclaration, Program > ExportDefaultDeclaration > FunctionDeclaration',
          message: 'Daisy is class-based (ADR 0011): make this a method of a class.',
        },
        {
          selector:
            'Program > VariableDeclaration > VariableDeclarator > :matches(ArrowFunctionExpression, FunctionExpression), Program > ExportNamedDeclaration > VariableDeclaration > VariableDeclarator > :matches(ArrowFunctionExpression, FunctionExpression)',
          message: 'Daisy is class-based (ADR 0011): make this a method of a class.',
        },
      ],
    },
  },
  {
    files: ['**/*.tsx'],
    rules: {
      'no-restricted-syntax': [
        'error',
        {
          selector:
            'Program > FunctionDeclaration[id.name!=/^(use[A-Z]|[A-Z])/], Program > ExportNamedDeclaration > FunctionDeclaration[id.name!=/^(use[A-Z]|[A-Z])/]',
          message: 'Only React components and hooks may be functions (ADR 0011). Put logic in a class.',
        },
      ],
    },
  },
  {
    files: ['**/*.test.{ts,tsx}', '**/e2e/**/*.ts'],
    rules: { '@typescript-eslint/no-non-null-assertion': 'off', 'no-restricted-syntax': 'off' },
  },
  { files: ['**/*.{js,mjs,cjs}'], ...tseslint.configs.disableTypeChecked },
  // Per-package Vitest configs sit outside each package's tsconfig (which covers src only).
  { files: ['**/vitest.config.ts', '**/vitest.browser.config.ts'], ...tseslint.configs.disableTypeChecked },
  prettier,
);
