import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  guideSidebar: [
    {
      type: 'category',
      label: 'Start Here',
      items: ['intro', 'pathways', 'quick-start'],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Chapters',
      items: [
        'chapters/01-introduction',
        'chapters/02-understanding-apps',
        'chapters/03-choosing-stack',
        'chapters/04-tutorial',
        'chapters/05-building-blocks',
        'chapters/06-debugging',
        'chapters/07-testing',
        'chapters/08-whats-next',
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Quick Reference',
      items: [
        'micro-guides/deploy-in-10-minutes',
        'micro-guides/fix-5-common-errors',
        'micro-guides/auth-quick-reference',
        'micro-guides/debugging-checklist',
        'micro-guides/idea-to-live-url',
      ],
      collapsed: true,
    },
    {
      type: 'category',
      label: 'Resources',
      items: ['glossary'],
      collapsed: true,
    },
  ],
};

export default sidebars;
