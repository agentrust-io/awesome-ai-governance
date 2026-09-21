"""Home page description for the list.

README.md is both this site's home page and the GitHub landing page, so it
cannot carry front matter without that showing on GitHub. Its first paragraph
is an argument, not a summary, so the home page uses site_description instead
of what hooks/seo.py would take. Runs before seo.py, which then leaves it alone.
"""


def on_page_markdown(markdown, page, config, files):
    if page.is_homepage and not page.meta.get('description'):
        page.meta['description'] = config['site_description']
    return markdown
