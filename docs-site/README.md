# Vibe Coding: Zero to Ship - Documentation Site

This is the interactive documentation website for the Vibe Coding: Zero to Ship guide, built with [Docusaurus](https://docusaurus.io/).

## Local Development

### Prerequisites
- Node.js version 20.0 or above
- npm (comes with Node.js)

### Installation

```bash
npm install
```

### Running Locally

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

The site will be available at `http://localhost:3000/`

### Building for Production

```bash
npm run build
```

This command generates static content into the `build` directory. The output can be served using any static hosting service.

### Testing the Build Locally

```bash
npm run serve
```

This command serves the production build locally so you can test it before deploying.

## Deployment

### Deploy to Vercel

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Docusaurus site"
   git push
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will auto-detect the Docusaurus framework
   - Click "Deploy"

3. **Automatic Deployments:**
   - Every push to main branch will trigger automatic deployment
   - Preview deployments for pull requests

### Deploy to Netlify

1. **Push to GitHub** (same as above)

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub and select your repository
   - Build settings:
     - Build command: `npm run build`
     - Publish directory: `build`
   - Click "Deploy site"

## Project Structure

```
docs-site/
├── docs/                       # Documentation content
│   ├── intro.md               # Landing page
│   ├── pathways.md            # Learning pathways
│   ├── quick-start.md         # Quick start guide
│   ├── chapters/              # Main guide chapters
│   │   ├── 01-introduction.md
│   │   ├── 02-understanding-apps.md
│   │   ├── 03-choosing-stack.md
│   │   ├── 04-tutorial.md
│   │   ├── 05-building-blocks.md
│   │   ├── 06-debugging.md
│   │   ├── 07-testing.md
│   │   └── 08-whats-next.md
│   ├── micro-guides/          # Quick reference guides
│   │   ├── deploy-in-10-minutes.md
│   │   ├── fix-5-common-errors.md
│   │   ├── auth-quick-reference.md
│   │   ├── debugging-checklist.md
│   │   └── idea-to-live-url.md
│   └── glossary.md            # Terminology reference
├── src/                       # React components and CSS
├── static/                    # Static assets
├── docusaurus.config.ts       # Site configuration
├── sidebars.ts               # Sidebar navigation
├── vercel.json               # Vercel deployment config
└── package.json              # Dependencies and scripts

```

## Features

- **Mermaid Diagrams:** Full support for Mermaid diagrams in markdown
- **Syntax Highlighting:** Code blocks with syntax highlighting for all languages
- **Dark Mode:** Automatic dark mode based on user preference
- **Mobile Responsive:** Works great on all device sizes
- **Search:** Built-in search functionality (can be enhanced with Algolia)
- **Navigation:** Organized sidebar with chapters and quick references
- **Fast:** Static site generation for blazing fast loading

## Customization

### Updating Content

All documentation content is in markdown files under the `docs/` directory. Edit these files to update the content.

### Modifying Navigation

Edit `sidebars.ts` to change the navigation structure.

### Changing Site Config

Edit `docusaurus.config.ts` to modify:
- Site title and tagline
- URL and base URL
- Header and footer links
- Theme settings
- Plugin configuration

### Styling

Edit `src/css/custom.css` to customize colors and styles.

## Troubleshooting

### Build Fails

1. Clear the cache:
   ```bash
   rm -rf .docusaurus build node_modules
   npm install
   npm run build
   ```

2. Check for broken links in markdown files
3. Ensure all referenced images and files exist

### Local Server Won't Start

1. Kill any process using port 3000:
   ```bash
   lsof -ti:3000 | xargs kill
   ```

2. Try a different port:
   ```bash
   npm start -- --port 3001
   ```

### Mermaid Diagrams Not Rendering

Make sure you're using proper Mermaid syntax and that the `@docusaurus/theme-mermaid` plugin is installed.

## Contributing

When adding new documentation:

1. Create or edit markdown files in `docs/`
2. Add frontmatter with `id`, `title`, and `sidebar_position`
3. Update `sidebars.ts` if adding new sections
4. Test locally with `npm start`
5. Build to verify no errors: `npm run build`

## Support

- **Documentation Issues:** Open an issue in the main repository
- **Docusaurus Help:** Visit [docusaurus.io/docs](https://docusaurus.io/docs)
- **Community:** Join the Build to Launch newsletter at [buildtolaunch.substack.com](https://buildtolaunch.substack.com)

## License

This documentation site is part of the Vibe Coding: Zero to Ship guide, released under MIT License.
