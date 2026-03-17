"""
MkDocs hook that processes [@key] BibTeX citations in two modes:

- **Numbered mode** (page contains ``\\bibliography``):
  [@key] → compact [N] link; \\bibliography → full numbered reference list.
- **Inline mode** (no ``\\bibliography``):
  [@key] on its own line → full formatted entry rendered in place.
"""

import re
from html import escape
from pathlib import Path

from pybtex.database import BibliographyData, Entry, parse_file
from pybtex.style.formatting.plain import Style as PlainStyle
from pybtex.backends.html import Backend as HtmlBackend

_bib_cache = {}
_style = PlainStyle()
_backend = HtmlBackend()

INLINE_RE = re.compile(r'^\[@([\w]+)\]$', re.MULTILINE)
ANY_CITE_RE = re.compile(r'\[@([\w]+)\]')

LINK_FIELDS = {'url', 'pdf', 'doi'}


def on_page_markdown(markdown, page, config, files):
    bib_data = _get_bib_data(config)
    if not bib_data:
        return markdown

    if '\\bibliography' in markdown:
        return _process_numbered(markdown, bib_data)

    if INLINE_RE.search(markdown):
        return _process_inline(markdown, bib_data)

    return markdown


# ---------------------------------------------------------------------------
# Numbered mode  (research page style)
# ---------------------------------------------------------------------------

def _process_numbered(markdown, bib_data):
    """Replace [@key] with [N] links and \\bibliography with the full list."""
    citation_order = []
    key_to_num = {}

    def replace_ref(match):
        key = match.group(1)
        if key not in bib_data.entries:
            return match.group(0)
        if key not in key_to_num:
            n = len(citation_order) + 1
            key_to_num[key] = n
            citation_order.append(key)
        n = key_to_num[key]
        return f'<a class="citation-ref" href="#ref-{key}">[{n}]</a>'

    markdown = ANY_CITE_RE.sub(replace_ref, markdown)

    bib_html_parts = []
    for key in citation_order:
        n = key_to_num[key]
        entry = bib_data.entries[key]
        bib_html_parts.append(_format_numbered_entry(n, key, entry))

    bib_html = (
        '<div class="bibliography">\n'
        + "\n".join(bib_html_parts)
        + "\n</div>\n"
    )
    markdown = re.sub(r'^\\bibliography\s*$', bib_html, markdown, flags=re.MULTILINE)
    return markdown


def _format_numbered_entry(n, key, entry):
    body = _render_pybtex(key, entry)
    fields = entry.fields
    links = _make_links(fields)

    links_html = ""
    if links:
        links_html = ' ' + ' '.join(links)

    return (
        f'<div class="publication" id="ref-{key}">\n'
        f'  <p><strong>[{n}]</strong> {body}{links_html}</p>\n'
        f'</div>'
    )


# ---------------------------------------------------------------------------
# Inline mode  (publications page style)
# ---------------------------------------------------------------------------

def _process_inline(markdown, bib_data):
    """Replace standalone [@key] lines with full formatted entries."""

    def replace_citation(match):
        key = match.group(1)
        if key not in bib_data.entries:
            return match.group(0)
        return _format_inline_entry(key, bib_data.entries[key])

    return INLINE_RE.sub(replace_citation, markdown)


def _format_inline_entry(key, entry):
    body = _render_pybtex(key, entry)
    fields = entry.fields
    links = _make_links(fields)

    links_html = ""
    if links:
        links_html = (
            '<div class="publication-links">'
            + " ".join(links)
            + "</div>"
        )

    return (
        f'<div class="publication">\n'
        f"  <p>{body}</p>\n"
        f"  {links_html}\n"
        f"</div>\n"
    )


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _get_bib_data(config):
    docs_dir = config.get('docs_dir', '')
    if docs_dir in _bib_cache:
        return _bib_cache[docs_dir]

    bib_file = Path(docs_dir) / 'publications.bib'
    if not bib_file.exists():
        _bib_cache[docs_dir] = None
        return None

    bib_data = parse_file(str(bib_file))
    _bib_cache[docs_dir] = bib_data
    return bib_data


def _render_pybtex(key, entry):
    """Format an entry with pybtex plain style, stripping link fields."""
    fields = entry.fields
    stripped = {k: v for k, v in fields.items() if k not in LINK_FIELDS}
    stripped_entry = Entry(entry.type, fields=stripped, persons=entry.persons)

    bib = BibliographyData(entries={key: stripped_entry})
    formatted = _style.format_bibliography(bib)

    for fmt_entry in formatted:
        return fmt_entry.text.render(_backend)
    return ""


def _make_links(fields):
    links = []
    url = fields.get('url', '') or fields.get('pdf', '')
    doi = fields.get('doi', '')
    if url:
        links.append(f'<a href="{escape(url)}">PDF</a>')
    if doi:
        doi_url = doi if doi.startswith('http') else f'https://doi.org/{doi}'
        links.append(f'<a href="{escape(doi_url)}">DOI</a>')
    return links
