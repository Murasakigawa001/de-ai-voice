#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Removing the AI register from academic prose

Single-file distribution of the "de-ai-voice" skill. Running this script writes a ready-to-use
SKILL.md that can be dropped into a skills directory.

Usage
  python de_ai_voice.py                 write ./de-ai-voice/SKILL.md
  python de_ai_voice.py --dir PATH      write PATH/de-ai-voice/SKILL.md
  python de_ai_voice.py --print         print the skill to standard output
  python de_ai_voice.py --check         verify that the embedded text is complete

No third-party packages are required. Python 3.8 or later.
"""

import argparse
import os
import sys

NAME = "de-ai-voice"

CONTENT = r"""---
name: de-ai-voice
description: Turns AI-drafted or AI-sounding academic prose back into writing that reads as human, while keeping the author's own voice. Trigger when the user says "reduce the AI feel", "it reads like ChatGPT", "make it sound like me", "add some life to this", "clean it before the detector", or submits a paper, report or book chapter for a language-level final pass. Works for English and Chinese humanities, social science and medical writing. Not for cutting length (use condense-to-limit), mechanical style-sheet revision (use manuscript-revision), or writing from scratch (use ima-report).
---

# Pulling the prose back to a human hand

The goal is not to evade a detector. It is to make the text read as though a person wrote it. These two aims often pull in opposite directions: tuning to detector feedback makes sentences stiffer. So the criterion is single: read it aloud, and ask whether a person would say it.

## 1. What the AI register actually is

It is not fancy vocabulary. It is the tendency of every choice to land on the statistical middle: generic wording, stopping at the category level, uniformly positive and vague tone, insistence on importance, reporting volume instead of making an argument, vague attribution, layered defensive hedging, argument that can be resequenced without loss, formulaic rhetoric, rigid paragraph architecture, citations stretched beyond what they support, and interchangeable examples.

The homogenisation is measurable. Lexical diversity in LLM output is markedly lower than in human writing; LLM-assisted research writing shifts toward complex syntax, longer words and lower lexical variety. So "make it sound more formal" is usually the move that deepens the problem.

Detectors cannot serve as acceptance criteria. OpenAI withdrew its own classifier for low accuracy, reporting 26% detection of AI text and a 9% false-positive rate on human text; across 91 TOEFL essays by non-native writers, seven detectors produced a mean false-positive rate of 61.22%. Pressing text toward a "green" score degrades the writing.

Do not avoid your field's technical vocabulary. Prose made entirely of general words is itself a trace.

## 2. Hard rules

1. **Specific before abstract.** Every abstract claim must be able to name a person, a year, a number or a quotation. If it cannot, the sentence does not go in.
2. **Claims of importance need at least two of four**: object, scope, period, source. Otherwise delete.
3. **One hedge per uncertainty.** State a limitation once. Never stack "may" with "cannot be generalised" and "further research is needed".
4. **No unsolicited disclaimers or reader guidance**, unless the body contains a specific contested point that the disclaimer actually informs.
5. **Attribute to named sources.** A single source is "one study". Do not manufacture a panel of reviewers for one view; do not use "several studies show" to cover one or two.
6. **Citations support only what they support.** Do not turn a finding in a specific population into a claim about everyone; do not turn correlation into causation. A footnote is not evidence that the sentence is warranted.
7. **The argument must survive testing.** Apply the deletion test and the reordering test to every paragraph. If a sentence can be cut or moved without loss, either give it an explicit joint role or cut it.
8. **Banned constructions**: "not X but Y"; "not only X but also Y" without real escalation; "it is worth noting"; "in a sense"; "for this very reason"; "this also shows" without a prior judgement; paragraphs opening with "Moreover", "Furthermore", "In addition", "At the same time".
9. **No three-part lists for rhythm, no closing that summarises and then gestures at the future.** A conclusion recovers evidence already presented; it does not speculate about benefits.
10. **No mechanical bold, no bullet lists in place of prose, no numbered fragments where a paragraph belongs.** Lists only when the material is genuinely a list.
11. **No em dashes anywhere.** Insertions take commas or a new sentence. Range dashes (2016–2024) are a different mark and may stay.
12. **Name a term once, then keep it.** Synonym rotation is allowed only when the referent changes, never to avoid repetition.
13. **Vary sentence length.** Alternate long subordinate sentences with short stops. After revising, check: three consecutive sentences within 20% of each other in length is a trace.
14. **Cut adjectives.** An evaluative adjective without a source becomes a statement of fact.
15. **Depth over breadth.** More evidence on a narrower question beats more topics and more words.

## 3. Beyond the fifteen

**Language hygiene.** Remove copula avoidance (serves as, stands as, represents standing in for is or has), false ranges (from X to Y where X and Y are not on a continuum), synonym rotation, filler phrases, authority rhetoric ("the real question is", "essentially", "at its core"), roadmap announcements ("let us look at", "what you need to know"), fragmentary headings, flattering tone, chatbot residue, knowledge-cutoff disclaimers, empty positive conclusions, emoji.

**No strong adverbs on mechanism claims.** Systematically, necessarily, must, in fact are standing in for evidence. Use markers such as "in our reading", "we take this to be", and hand the judgement back to the author.

**Delete formulaic openings and closings.** "In recent years", "with the development of", "in summary" carry no information. If the sentence stands without them, they were the problem.

**Make vagueness concrete.** "Related research shows" becomes author, year, sample size, effect size. "Has certain limitations" becomes "uses twelve cases and controls for no covariates".

**After each citation, add a sentence of your own that turns.** But, yet, however are the most direct markers of critical reading. Let the argument spiral: A, but A has a boundary, so B, but B raises C.

**Mark missing data as missing; never invent.** Write limitations in a plain, specific, unheroic voice.

**Abstracts**: no universal opening, no evaluation that is too perfect. **Conclusions**: no recapitulation, no forced elevation; state what was done and where it stops.

**Three failure modes to avoid**: swapping words only, piling on first person, over-colloquialising. All three increase the machine feel.

## 4. Voice: calibrate before writing

Before revising, read a sample of the author's own text and record: sentence-length pattern, register of vocabulary, how paragraphs open, punctuation habits, verbal tics, transition habits. Then replace your defaults with theirs. If they write short, do not produce long. If they use a plain word, do not upgrade it to a term.

Clean writing with no voice is as visible as AI filler. The signs: every sentence built the same way, neutral reporting with no judgement, no admission of uncertainty, no first person where one belongs, no trace of a person. The remedy is to react to facts rather than report them, to alternate rhythm, to admit complexity, and to allow a aside or a half-formed thought.

**English paragraphs** open on the object at hand, not on a count ("first", "second"). Do not break a parallel into a string of identically shaped short sentences. Do not reach for formulaic connectives.

**Chinese prose** has its own markers of a human hand, and they are worth keeping when the text is Chinese. Put a comma after a time adverbial (the words for "this year", "then", "in the past"). Put a comma after a turn or a causal connective (the words for "but", "so", "though"). Use a short sentence to hand the topic over before explaining it. Let a verb take a small filler that gives the sentence a beat. Use colloquial quantifiers for degree ("many", "a little", "somewhat more") rather than the formal words for "more" or "substantially". Admit the old practice first, then turn with the phrase for "but later". Keep one layer of meaning per sentence. Drop empty modifiers such as "quietly". Write "more attentive to" rather than its emphatic variant. Close by folding the point into a concrete action, not an overall verdict. Chinese paragraphs run continuously, without bullets, quotation marks, colons or dashes.

## 5. Method and record

Four steps: read the author's original and their marks, noting sentence length and vocabulary; revise against the rules; run a second audit listing what was changed and why; record the basis of each change in one row of a change log.

Four rules of record-keeping: version 0 is only added to, never overwritten; decisions carry dates; every revision keeps the original sentence and the reason; decisions are logged as decision, source, effect. One table with four columns: version, change, reason, basis.

Trimming: splitting a long sentence does not reduce length; only deleting a sentence does. Work through generic deletion strings (It should be noted that, It is worth noting that, In other words, As noted above, as discussed below) sentence by sentence. If deleting breaks the connection, replace it with a short connective (Yet, Thus, By contrast), not a rewritten sentence.

Five checks before delivery: count names, years, page numbers and quotations, and flag any that are zero; find sentences that could be deleted without loss; scan for banned constructions; find sentences about significance, impact or prospects that carry no source; verify the scope of every citation.

Then a second audit: ask of the draft, "where does this obviously read as AI", list the residue, revise once more, and report which patterns were removed.

## 6. House style follows the venue

House style is not a constant. It is an input to the task. The same manuscript sent to a different journal needs spelling, citation, heading case, abstract structure and length recalculated.

**Ask the venue first.** Confirm the target journal or outlet, read its author guidelines, and settle each item:

| Item | What to settle | Typical divergence |
|---|---|---|
| Spelling | British / American / author's own | -ise versus -ize, -our versus -or, -re versus -er, analyse versus analyze |
| Citation | author-date / superscript numerals / footnotes | Chicago author-date, AMA numerals, Vancouver, APA |
| Heading case | Title Case / sentence case | Chicago and AMA use Title Case; Elsevier and most British journals use sentence case |
| Abstract | structured / unstructured, word limit | 250 versus 300 words, whether headings are wanted |
| Keywords | maximum number | 3 to 6 |
| Tables and captions | title position, note prefix | Note. / NOTE: / no prefix |
| References | required / dispensable | most journals require them |

**Report conflicts rather than resolving them alone.** If the author asks for Chicago title case while the journal uses sentence case, state the conflict and let the author decide. The same applies when house rules collide with the venue.

**Do not itemise style matters.** Report only those that change appearance or eligibility (spelling, citation, headings, length); follow the venue's default for the rest.

**Write rules as value rules, not as one journal's template.** Say "spelling follows the target journal: British journals use -ise or Oxford -ize, American journals use -ize, one system throughout", not "use Oxford spelling".

## 7. Cite only what can be verified

When adding references:

1. Decide the citation points first. Methodological statements (estimation, data source), empirical facts (prevalence, expenditure), and policy texts need support; your own estimates do not.
2. Verify each entry to the point of location: authors, title, journal, year, volume, pages, DOI or document number. If no DOI, verify a PMID or an agency page. If neither, do not cite.
3. Match scope to the sentence. A review of trials in one country cannot support a claim about prevalence elsewhere; it can support the existence of trial evidence.
4. Deliver a verification list: number, the sentence it supports, and a retrieval identifier, so the author can check each one.
5. Prefer fewer. Eight verified references beat thirty assembled ones. When nothing reliable exists, say so; do not fill the gap.

## 8. Fix the style sheet before editing

Names, translated terms, number rules (numerals above ten or numerals throughout), italic range, first-use expansion of abbreviations, spelling system: settle these in a table first, or the revision will be internally inconsistent by the halfway point.

## 9. Arbitration

Two kinds of advice to reject: shuffling sentence order to beat a detector; inserting obscure references unrelated to the argument.

Where a guideline lists something as an AI trace but it collides with the author's established style (title case, quotation form, semicolons), follow the author's ruling and say so rather than deciding silently.

Two things to report unprompted: gaps that the material cannot fill, and conflicts between a rule and the house style, resolved by the author.
"""


def check():
    problems = []
    if not CONTENT.startswith("---"):
        problems.append("missing YAML header")
    if "name: " + NAME not in CONTENT:
        problems.append("name in YAML header does not match")
    if "description:" not in CONTENT:
        problems.append("missing description in YAML header")
    sections = [l for l in CONTENT.splitlines() if l.startswith("## ")]
    if len(sections) < 5:
        problems.append("expected at least 5 sections, found %d" % len(sections))
    if len(CONTENT) < 6000:
        problems.append("content looks truncated (%d characters)" % len(CONTENT))
    return problems, len(sections)


def write(target_dir):
    out_dir = os.path.join(target_dir, NAME)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "SKILL.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(CONTENT)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Install the %s skill." % NAME)
    ap.add_argument("--dir", default=".", help="parent directory for the skill folder")
    ap.add_argument("--print", dest="do_print", action="store_true", help="print the skill text")
    ap.add_argument("--check", action="store_true", help="verify the embedded text")
    args = ap.parse_args(argv)

    if args.do_print:
        sys.stdout.write(CONTENT)
        return 0

    problems, n_sections = check()
    if args.check:
        if problems:
            print("FAIL")
            for p in problems:
                print("  -", p)
            return 1
        print("OK  %s  %d characters, %d sections" % (NAME, len(CONTENT), n_sections))
        return 0

    if problems:
        print("warning: " + "; ".join(problems), file=sys.stderr)
    path = write(args.dir)
    print("written:", os.path.abspath(path))
    print("next: put the folder %s into your skills directory." % NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
