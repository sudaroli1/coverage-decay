# LaTeX source — Computers & Security submission

The manuscript in `elsarticle`, Elsevier's own class. Margins, type area, front
matter and reference style come from the class, so they are correct by
construction rather than by hand.

**The prose is unchanged from `paper/mywriting_paper.docx`.** Nothing was
shortened, rephrased or reordered in the conversion. Cutting to the journal's
limit has deliberately not been attempted here; `WORD_BUDGET.txt` measures where
the words are so that the decision can be made deliberately.

## Files

    main.tex          class options, front matter, abstract, keywords
    body.tex          Sections 1-8, back matter and Appendix A
    references.bib    20 entries
    WORD_BUDGET.txt   words per subsection, and the gap to the limit
    elsarticle.cls    LOCAL SHIM ONLY — delete before building for real
    elsarticle-harv.bst  ditto

## Building on Overleaf

1. New Project → Templates → search **elsarticle** → *Elsevier Article
   (elsarticle) Template*.
2. Delete the template's `main.tex` and `elsarticle.cls` if present.
3. Upload `main.tex`, `body.tex`, `references.bib`, and the seven figure PDFs
   from `results/` (`fig_cumulative.pdf`, `fig3_persistence.pdf`,
   `fig4_null_coverage.pdf`, `fig_anchor.pdf`, `fig_ruleage.pdf`,
   `fig_sharetrend.pdf`, `fig_timeline.pdf`).
4. If the figures sit beside `main.tex` rather than in a sibling `results/`,
   change `../results/` to `` in the seven `\includegraphics` lines.
5. Recompile. Overleaf runs BibTeX automatically.

**Do not upload `elsarticle.cls` or `elsarticle-harv.bst`.** They are stand-ins
written for this sandbox, which cannot reach CTAN, and exist only so the source
could be typechecked. Overleaf ships the genuine class and style; the shims
would override them and produce the wrong layout.

## Class options

Set on line 12 of `main.tex`:

    preprint,12pt              single column — the normal submission format
    review,12pt                double spaced with line numbers, for referees
    final,5p,times,twocolumn   the published two-column look, for a page estimate

Submit with `preprint`. Use `final,5p` only to see what the article will look
like in print.

## Notes on the conversion

- The three rule excerpts are `lstlisting` inside a `listing` float, numbered
  separately from figures and tables, as they were in the Word file.
- Figure 4 (the anchor bar) and Figure 7 (the single-rule timeline) are
  `figure*` so they span both columns under the two-column option. The rest are
  in-column.
- Citations are `\citep` and `\citet` against `references.bib` — 43 in total,
  all 20 entries cited, none undefined.
- Section labels exist for every section and for the subsections the prose
  refers to, so cross-references renumber themselves if a section is cut.
- The delta quantities of Section 4.2 are set as mathematics.

## Outstanding

- Abstract is **289 words** against the journal's 250-word limit.
- Whole document is about **15,971 words**. See `WORD_BUDGET.txt`.
- Five overfull boxes, all in long verbatim lines inside the listings. Harmless
  in the shim build; check them again once the real class is in use.
