# Template execution contract

## Reference

- Retained reference: `/Users/david/Downloads/Copy of Digital Minds Research Sprint submission template.docx`
- SHA-256: `37aa16880555b45fd73fb9019a4a7ba157c34d60eba5d7cd038d6620be647f6c`
- Rendered pages: 5
- Sections: 1
- Render evidence: `/Users/david/Documents/ChatGPT/doom_codex/.tmp/final_submission/template-reference-render/`
- Style evidence: `/Users/david/Documents/ChatGPT/doom_codex/.tmp/final_submission/template-style-evidence.json`
- Content-control inventory: empty

The retained reference is read-only. The final DOCX must be a different file.

## Page system

- US Letter portrait: 8.5 × 11 inches (`12240 × 15840` DXA).
- Margins: 1 inch on every side (`1440` DXA).
- Header and footer distance: 0.5 inch (`720` DXA).
- One section, `NEW_PAGE`, no first-page or odd/even variants.
- No running header or footer. The title footnote is ordinary template content, not footer furniture.
- Main report target: a four-page substantive spine, optionally followed by a short conclusion/data page, then references and appendix/LLM disclosure; total must stay within the venue's 4–8 page envelope.

## Typography and recurring roles

- Embedded family and visual authority: Old Standard TT.
- `Title`: Old Standard TT, 20 pt, bold, centered, single-spaced, 7.2 pt after.
- `Heading 2`: Old Standard TT, 16 pt, regular, dark gray, 12.7 pt before and no after-space in the source; retain its centered numbered-section treatment.
- `Heading 3`: Old Standard TT, 14 pt, regular, `#434343`, 10.2 pt before and 4 pt after.
- Body: source `normal` style, Old Standard TT, approximately 11 pt, justified, single-spaced. Final builder may set the inherited normal style explicitly to Old Standard TT 10.5 pt to keep the four-page main-text budget, but may not introduce a second font system.
- Captions: Old Standard TT 9 pt, justified, 4 pt before/after, kept with the preceding figure.
- References: Old Standard TT 9 pt with 0.18-inch hanging indent.
- Keep section headings with the following paragraph. Avoid orphan captions and single-line carryovers.

## Lists and tables

- The source contains real numbering definitions and five table styles. Preserve `word/numbering.xml` unchanged.
- The title/author/abstract block is the first top-level table, full content width (`9360` DXA), centered, fixed layout, with horizontal rules.
- The author grid is nested inside that table. Retain a single centered author cell and remove unused author rows/cells without changing the outer title component.
- The yellow instruction table is guidance-only and must be removed.
- No body table is required; results are better represented by two figures and compact prose.
- Any list in the final document must use a real Word list definition. Do not type Unicode bullets into body text.

## Components

- First-page title block: reuse the source title table and its top/bottom rules.
- Author block: replace the middle author slot with `David Fraile Navarro` and `Independent Researcher`; clear the unused five slots; retain `With / Apart Research`.
- Abstract: replace the italicized 150–250-word guidance inside the nested abstract table. Keep the `Abstract` heading and constrained inset width.
- Body sections: reuse the template's centered `Heading 2` and left-aligned `Heading 3` patterns.
- Figures: two centered PNGs, maximum width 6.15 inches, with descriptive captions directly below.
- Footnote: preserve the template's Digital Minds Research Sprint footnote and relationship.

## Content flow and slot map

| Stable locator | Purpose | Capacity/action |
|---|---|---|
| `word/document.xml`, first top-level `w:tbl`, first row | Project title | Rewrite in place; preserve table geometry and rule |
| Same table, nested author grid containing `Author name 1` | Author metadata | Rewrite/clear placeholders; keep one centered author |
| Same table, nested table containing `Summarize your project...` | Abstract | Rewrite with 150–250 words |
| Second top-level `w:tbl`, yellow fill | Instructions | Remove entirely |
| Body paragraphs styled `Heading 2`, from `1. Introduction` onward | Main sections | Replace guidance with final report sections; clone the same heading pattern where needed |
| Guidance paragraphs under each section | Editorial prompts | Remove entirely |
| `References` onward | Back matter | Rewrite; may begin on a new page |
| `Appendix (optional)` and `LLM Usage Statement` | Deviations and disclosure | Rewrite and retain as back matter |

## Package preservation inventory

All parts are preserve-only except `word/document.xml`, `word/_rels/document.xml.rels` (new figure relationships only), `[Content_Types].xml` (PNG declaration if needed), and added `word/media/*` figure parts.

| Part | Bytes | SHA-256 | Class |
|---|---:|---|---|
| `word/footnotes.xml` | 3457 | `22bc3ede8ce874888d5c31b666d9c32687149c7fc8fb6f2d3f07c60486c2c8a7` | preserve |
| `word/_rels/footnotes.xml.rels` | 386 | `22c61659fc9a2894f268f6374b77a3256fbab422d526861483feba3a9a261594` | preserve |
| `word/numbering.xml` | 11522 | `17b764b10bafb4b1ad14856f3fdc493e2199bb6bbe5f9e60f74bcd5753f55795` | preserve |
| `word/settings.xml` | 2152 | `26f2853fde05b88d4b0a9da0bb016d56a896901f60c9272dddf33c3f3fa61e4a` | preserve |
| `word/fontTable.xml` | 2045 | `41f6cd0d5be3467d325ce77d754cf1432b548fab1f478eb0a3aeb896ba206752` | preserve |
| `word/_rels/fontTable.xml.rels` | 590 | `9badf90f7dd1a2e38e307c16f6d2dd7eead417b354beb9154b1f3f51d8bea361` | preserve |
| `word/styles.xml` | 6423 | `10c66367541c8c212714639d98f88a860ca5c203d9b95ac4dbee0b30b81d6821` | preserve unless explicit body-size patch is required |
| `word/document.xml` | 85461 | `a2b0f40f5d1b8a0dc03c1518e313bc9f1d63d0200252a824f4e1494470888a71` | editable |
| `word/_rels/document.xml.rels` | 1145 | `a2f6cbe07732bdbe4d2be656ac1f274c0de4eb99db3e39bf11328ab355a84906` | editable: add figures only |
| `_rels/.rels` | 298 | `1cc87395d4a229f21c23af406724de12dd9454071925f983e4b648a7b2be8cc5` | preserve |
| `word/fonts/OldStandardTT-regular.ttf` | 242700 | `cf759c9617e8d9a74ccc3fcdc8670a25d1e016e6e4cf55c378e79f70bf45520b` | preserve |
| `word/fonts/OldStandardTT-bold.ttf` | 260156 | `fcd2340207253ef61a6a02694b9a43cd54159867518edfd4788b0916f1fc92a3` | preserve |
| `word/fonts/OldStandardTT-italic.ttf` | 267016 | `722168792ee2dda09d07ab6443bdd4743469b86e3d233e5bf8e96e3951afb98c` | preserve |
| `word/theme/theme1.xml` | 7643 | `b2295d3198893d2c03f5e584c749a15751b798aefdcd9bee2889f13903d68cb2` | preserve |
| `[Content_Types].xml` | 1368 | `d0ae6f5b5cdb2f37a7d642baadd62ae6cd7d35e4be63274f9f43388b6bc90df5` | editable only for figures |

## Fidelity gates

- Reference SHA must remain unchanged.
- Final must remain one Letter/portrait section with one-inch margins.
- Embedded Old Standard TT fonts, footnotes, numbering, theme, and relationships not needed for figures must survive.
- No guidance text or author placeholders may remain.
- Introduction through discussion must occupy four pages; conclusion and data availability may use a short fifth page before References.
- All figure labels must be legible at 100% zoom; no clipping, overlap, broken tables, or stranded headings.
- Render every final page and compare against the reference for unexplained changes to the title block and page geometry.
