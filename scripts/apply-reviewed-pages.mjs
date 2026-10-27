import fs from 'node:fs';
import path from 'node:path';

const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));

export function applyReviewedPages(root, renderPage) {
  const manifest = path.join(root, 'content/reviewed-pages.json');
  if (!fs.existsSync(manifest)) return 0;
  const entries = JSON.parse(fs.readFileSync(manifest, 'utf8'));
  if (!Array.isArray(entries)) throw new Error('Reviewed pages must be an array.');
  const seen = new Set();
  const host = fs.readFileSync(path.join(root, 'CNAME'), 'utf8').trim();
  if (!/^[a-z0-9.-]+$/i.test(host)) throw new Error('Invalid site domain.');
  for (const entry of entries) {
    if (!/^\/(?:[a-z0-9]+(?:-[a-z0-9]+)*\/)+$/.test(entry.route) || seen.has(entry.route)) {
      throw new Error(`Invalid or duplicate reviewed route: ${entry.route}`);
    }
    seen.add(entry.route);
    const destination = path.join(root, entry.route.slice(1), 'index.html');
    if (!fs.existsSync(destination)) throw new Error(`Route is outside the existing atlas: ${entry.route}`);
    if (!/^content\/[a-z0-9/_.-]+\.html$/.test(entry.source) || entry.source.split('/').includes('..')) {
      throw new Error(`Invalid content source: ${entry.source}`);
    }
    if (typeof entry.title !== 'string' || !entry.title || typeof entry.description !== 'string' || !entry.description) {
      throw new Error(`Missing reviewed metadata: ${entry.route}`);
    }
    const body = fs.readFileSync(path.join(root, entry.source), 'utf8');
    if (!body.trim() || (body.match(/<h1\b/g) || []).length !== 1) throw new Error(`Expected one H1: ${entry.source}`);
    const canonical = `https://${host}${entry.route}`;
    let html = renderPage(escapeHtml(entry.title), body)
      .replace('<html lang="nl">', '<html lang="nl-BE">')
      .replace('<body>', `<body class="${entry.route.startsWith('/kasteel/') ? 'reviewed-castle' : 'reviewed-province'}"><a class="skip-to-content" href="${entry.route}#main-content">Naar de inhoud</a>`)
      .replace('<main>', '<main id="main-content">')
      .replaceAll('<img src="assets/logo.svg" alt="">', '<img src="assets/logo.svg" alt="" width="42" height="42">')
      .replace('data-nav>', 'data-nav id="primary-navigation" aria-label="Hoofdnavigatie">')
      .replace('data-menu aria-label="Menu"', 'data-menu aria-controls="primary-navigation" aria-label="Menu"')
      .replace(/<meta name="description" content="[^"]*">/, `<meta name="description" content="${escapeHtml(entry.description)}">`)
      .replace('Conceptatlas · praktische data wacht op verificatie', 'Erfgoedatlas · raadpleeg de bron voor actuele bezoekuren');
    let additions = `<link rel="canonical" href="${canonical}">`;
    if (entry.stylesheet) {
      if (!/^assets\/[a-z0-9-]+\.css$/.test(entry.stylesheet) || !fs.existsSync(path.join(root, entry.stylesheet))) {
        throw new Error(`Invalid stylesheet: ${entry.stylesheet}`);
      }
      additions += `<link rel="stylesheet" href="/${entry.stylesheet}">`;
    }
    additions += `<meta property="og:type" content="website"><meta property="og:title" content="${escapeHtml(entry.title)}"><meta property="og:description" content="${escapeHtml(entry.description)}"><meta property="og:url" content="${canonical}"><meta name="twitter:card" content="summary">`;
    if (entry.schema) additions += `<script type="application/ld+json">${JSON.stringify(entry.schema).replace(/</g, '\\u003c')}</script>`;
    html = html.replace('</head>', `${additions}</head>`);
    // Give informational pages the same right-hand section navigation as castle
    // details. Keep every article section and its semantic headings intact.
    if (!entry.route.startsWith('/kasteel/')) {
      const jumps = html.match(/<nav class="visit-jumps" aria-label="Op deze pagina">([\\s\\S]*?)<\\/nav>/);
      const articleOpen = /<article class="province-guide(?: [^"]*)?">/;
      if (jumps && articleOpen.test(html)) {
        const links = [...jumps[1].matchAll(/<a href="#([^"]+)">([\\s\\S]*?)<\\/a>/g)];
        const articleStart = html.search(articleOpen);
        const articleEnd = html.lastIndexOf('</article>');
        const valid = links.length > 0 && links.every(([, id]) => html.includes('id="' + id + '"'));
        if (valid && articleEnd > articleStart) {
          const nav = '<aside class="information-aside" aria-label="Navigatie binnen dit artikel"><div class="information-toc"><span class="eyebrow">Op deze pagina</span><nav aria-label="Spring naar onderdelen">' +
            links.map(([, id, label]) => '<a href="' + entry.route + '#' + id + '">' + label + '<span aria-hidden="true">→</span></a>').join('') +
            '</nav></div></aside>';
          html = html.replace(jumps[0], '');
          html = html.replace(articleOpen, match => match + '<div class="information-layout"><div class="information-content">');
          const close = html.lastIndexOf('</article>');
          html = html.slice(0, close) + '</div>' + nav + '</div>' + html.slice(close);
        }
      }
    }
    fs.writeFileSync(destination, html);
  }
  return entries.length;
}
