# Gilles Degottex's Academic Website

A modern, static website built with **MkDocs** and the **Material theme** for Gilles Degottex's research portfolio.

## Overview

This website replaces the previous WordPress-based site with a modern, fast, and secure static site generator. The site includes:

- **Homepage**: Introduction, contact information, and quick links
- **Research**: Detailed research timeline and interests
- **Publications**: Complete bibliography with BibTeX support and PDF links
- **Tools**: Documentation for COVAREP, DFasma, and FMIT
- **Misc Subjects**: Author posting guidelines and listening tests

## Technology Stack

- **MkDocs**: Static site generator for Python
- **Material Theme**: Modern, responsive theme with dark/light mode
- **MkDocs BibTeX Plugin**: Bibliography management
- **Markdown**: Content format
- **BibTeX**: Academic bibliography format

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### Option 1: Using Conda (Recommended)

```bash
# Create a new conda environment
conda create -n gilles-website python=3.11
conda activate gilles-website

# Install dependencies
pip install mkdocs mkdocs-material mkdocs-bibtex
```

### Option 2: Using pip

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install mkdocs mkdocs-material mkdocs-bibtex
```

## Development

### Start Development Server

```bash
mkdocs serve
```

The site will be available at `http://localhost:8000/`

### Build Static Site

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## Project Structure

```
gillesdegottex.eu/
├── mkdocs.yml              # Main configuration file
├── README.md               # This file
├── docs/                   # Content directory
│   ├── index.md            # Homepage
│   ├── research.md         # Research page
│   ├── publications.md     # Publications page
│   ├── publications.bib    # BibTeX bibliography
│   ├── tools.md            # Tools overview
│   ├── tools/
│   │   ├── covarep.md      # COVAREP documentation
│   │   ├── dfasma.md       # DFasma documentation
│   │   └── fmit.md         # FMIT documentation
│   ├── misc/
│   │   ├── author-posting.md
│   │   └── listening-tests.md
│   ├── stylesheets/
│   │   └── extra.css       # Custom CSS
│   ├── javascripts/
│   │   └── extra.js        # Custom JavaScript
│   └── pdf/                # PDF papers
└── overrides/              # Theme overrides (optional)
```

## Configuration

The main configuration file is [`mkdocs.yml`](mkdocs.yml). Key settings include:

- **Theme**: Material with teal color scheme
- **Plugins**: Search and BibTeX
- **Navigation**: Tab-based navigation with sections
- **Social Links**: Google Scholar, ORCID, Email

## Deployment

### Option 1: GitHub Pages

1. Push the repository to GitHub
2. Go to repository settings > Pages
3. Select the `gh-pages` branch (or main branch with `/docs` directory)
4. Enable GitHub Actions for automatic deployment

### Option 2: Netlify

1. Push the repository to GitHub/GitLab/Bitbucket
2. Import the repository in Netlify
3. Configure build settings:
   - Build command: `mkdocs build`
   - Publish directory: `site`
4. Deploy

### Option 3: Manual Deployment

1. Build the site: `mkdocs build`
2. Upload the contents of the `site/` directory to your web server

### Option 4: Read the Docs

1. Create an account at [readthedocs.org](https://readthedocs.org)
2. Import your GitHub repository
3. Configure the project to use MkDocs
4. Deploy

## Updating Content

### Adding a New Page

1. Create a new Markdown file in the `docs/` directory
2. Add the page to the `nav` section in `mkdocs.yml`
3. Build and deploy the site

### Adding a New Publication

1. Add the BibTeX entry to `docs/publications.bib`
2. Update `docs/publications.md` if needed
3. Place the PDF in `docs/pdf/` (optional)
4. Build and deploy the site

### Custom Styling

Add custom CSS to `docs/stylesheets/extra.css`

### Custom JavaScript

Add custom JavaScript to `docs/javascripts/extra.js`

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Automatic theme switching based on system preferences
- **Search**: Full-text search across all pages
- **BibTeX Integration**: Automatic bibliography formatting
- **PDF Links**: Direct links to publication PDFs
- **Social Links**: Quick access to Google Scholar, ORCID, and email
- **Fast Loading**: Static site with no server-side processing
- **SEO Friendly**: Semantic HTML and proper metadata

## License

This website is licensed under the MIT License.

## Credits

- **MkDocs**: [https://www.mkdocs.org/](https://www.mkdocs.org/)
- **Material Theme**: [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- **MkDocs BibTeX**: [https://github.com/michaeljoseph/mkdocs-bibtex](https://github.com/michaeljoseph/mkdocs-bibtex)

## Support

For questions or issues, please contact: gilles.degottex@gmail.com
