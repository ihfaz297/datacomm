// Builds mid2-notes.html (the phone reader artifact) from the Mid-2 markdown files.
// Maths stays as TeX in the page and is typeset in the browser by KaTeX 0.16.47
// (script from cdnjs; its CSS and fonts are inlined because the artifact CSP blocks
// stylesheets and fonts from other hosts).
//
// Needs katex@0.16.47 and marked@12.0.2 installed somewhere, e.g.
//   cd <tmp> && npm i katex@0.16.47 marked@12.0.2
//   NODE_PATH=<tmp>/node_modules node DSP/study/_build_mid2_notes.js
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const HERE = __dirname;
const KATEX_DIR = path.dirname(require.resolve('katex/package.json'));
const KATEX_VERSION = require('katex/package.json').version;

const DOCS = [
  { id: 'plan', file: '00-mid2-battle-plan.md', tag: 'Start', label: 'Battle plan' },
  { id: 'q1', file: '20-T1-frequency-response.md', tag: 'Q1', label: 'Frequency response' },
  { id: 'q2', file: '21-T2-ztransform.md', tag: 'Q2', label: 'z-Transform' },
  { id: 'q3fast', file: '25-T3-in-30-minutes.md', tag: 'Q3', label: 'In 30 minutes' },
  { id: 'q3', file: '22-T3-frequency-analysis.md', tag: 'Q3', label: 'Frequency analysis' },
  { id: 'conv', file: '23-convolution-revise.md', tag: 'TT1', label: 'Convolution' },
  { id: 'traps', file: '24-traps-and-intuition.md', tag: 'Last', label: 'Traps' },
];

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function render(doc) {
  let src = fs.readFileSync(path.join(HERE, doc.file), 'utf8');
  // The VS Code preview hint makes no sense on the phone page.
  src = src.replace(/^> \*\*Reading these notes\.\*\*.*\n\n?/m, '');

  const math = [];
  // Display blocks: $$ on its own line, TeX, $$ on its own line.
  src = src.replace(/^\$\$[ \t]*\n([\s\S]*?)\n\$\$[ \t]*$/gm, (_, tex) => {
    math.push({ tex, display: true });
    return `MATHD${math.length - 1}X`;
  });
  // Inline $...$, leaving code spans alone.
  src = src.split('\n').map(line => line.split(/(`[^`]*`)/).map(part =>
    part.startsWith('`') ? part : part.replace(/\$([^$\n]+?)\$/g, (_, tex) => {
      math.push({ tex, display: false });
      return `MATHI${math.length - 1}X`;
    })
  ).join('')).join('\n');

  let html = marked.parse(src, { gfm: true });

  html = html
    .replace(/<p>MATHD(\d+)X<\/p>/g, (_, i) => `<div class="md">${esc(math[i].tex)}</div>`)
    .replace(/MATHD(\d+)X/g, (_, i) => `<div class="md">${esc(math[i].tex)}</div>`)
    .replace(/MATHI(\d+)X/g, (_, i) => `<span class="mi">${esc(math[i].tex)}</span>`);

  // Figures: inline the SVG from figs/ so its colours follow the page theme.
  html = html.replace(/<p><img src="figs\/([\w-]+)\.svg" alt="([^"]*)"\s*\/?><\/p>/g, (_, name) => {
    const svg = fs.readFileSync(path.join(HERE, 'figs', `${name}.svg`), 'utf8').trim();
    const w = svg.match(/viewBox="0 0 (\d+)/)[1];
    return `<figure class="fig" style="--figw:${w}px">${svg.replace(/ width="\d+" height="\d+"/, '')}</figure>`;
  });
  // Interactive widgets, marked in the markdown with an HTML comment.
  html = html.replace(/<!-- widget:pole-explorer -->/g, '<div class="pz-explorer"></div>');

  // Subtitle line under the title.
  html = html.replace(/(<h1>[\s\S]*?<\/h1>\s*)<p><em>([\s\S]*?)<\/em><\/p>/, '$1<p class="lede">$2</p>');
  // Errata call-outs get their own colour.
  html = html.replace(/<blockquote>\s*<p><strong>Your note/g, '<blockquote class="erratum">\n<p><strong>Your note');
  // Tables scroll inside their own box on a phone.
  html = html.replace(/<table>/g, '<div class="tablewrap"><table>').replace(/<\/table>/g, '</table></div>');
  // Mentions of the other files become tab links.
  for (const d of DOCS) {
    html = html.split(`<code>${d.file}</code>`).join(`<a href="#${d.id}" class="xref" data-goto="${d.id}">${d.tag === 'Start' || d.tag === 'Last' || d.tag === 'TT1' ? d.label : d.tag + ' · ' + d.label}</a>`);
  }
  // Section ids and a contents list built from the h2s.
  const toc = [];
  let n = 0;
  html = html.replace(/<h2>([\s\S]*?)<\/h2>/g, (_, inner) => {
    const id = `${doc.id}-s${++n}`;
    toc.push(`<li><a href="#${id}" data-jump="${id}">${inner}</a></li>`);
    return `<h2 id="${id}">${inner}</h2>`;
  });
  const tocHtml = `<details class="toc"><summary>Sections</summary><ol>${toc.join('')}</ol></details>`;
  html = html.replace(/(<p class="lede">[\s\S]*?<\/p>)/, `$1\n${tocHtml}`);
  if (!html.includes('class="toc"')) html = html.replace(/(<\/h1>)/, `$1\n${tocHtml}`);
  return html;
}

function katexCss() {
  let css = fs.readFileSync(path.join(KATEX_DIR, 'dist', 'katex.min.css'), 'utf8');
  css = css.replace(/url\(fonts\/([^)]+?)\.woff2\) format\("woff2"\)(?:,url\([^)]+\) format\("[^"]+"\))*/g, (_, name) => {
    const b64 = fs.readFileSync(path.join(KATEX_DIR, 'dist', 'fonts', `${name}.woff2`)).toString('base64');
    return `url(data:font/woff2;base64,${b64}) format("woff2")`;
  });
  return css;
}

const template = fs.readFileSync(path.join(HERE, '_mid2_notes_template.html'), 'utf8');
const tabs = DOCS.map(d =>
  `<button type="button" role="tab" id="tab-${d.id}" data-tab="${d.id}" aria-controls="doc-${d.id}"><span class="tag">${d.tag}</span>${d.label}</button>`
).join('\n      ');
const articles = DOCS.map(d =>
  `<article id="doc-${d.id}" role="tabpanel" aria-labelledby="tab-${d.id}" hidden>\n${render(d)}\n</article>`
).join('\n');

const out = template
  .replace('/*KATEX_CSS*/', () => katexCss())
  .replace('<!--TABS-->', () => tabs)
  .replace('<!--ARTICLES-->', () => articles)
  .replace(/KATEX_VERSION/g, KATEX_VERSION);

fs.writeFileSync(path.join(HERE, 'mid2-notes.html'), out);
console.log(`wrote mid2-notes.html (${(out.length / 1024).toFixed(0)} KB, KaTeX ${KATEX_VERSION})`);
