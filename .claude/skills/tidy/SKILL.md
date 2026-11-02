---
name: tidy
description: Occasional review of notes already in Concepts/, finding drift in links, MOCs, areas and metadata and proposing fixes. Use only when the user asks to tidy, review or clean up existing notes. For new notes in Inbox/, use the organize skill.
---

# Tidy existing notes

Propose first, and change nothing until the user approves. Never reword, translate, summarize or add to a note's text. Never commit.

## Steps

1. Run `python _System/organize.py` (or `py` if `python` is missing), then `python _System/organize.py --report`.
2. Read `_System/index.md`. Do not read the whole vault.
3. Unless the user named a scope, review the report and all areas. Open a note only when the index cannot settle a decision.
4. Look for:
   - Items in the report.
   - MOC subtopics that have grown too large or no longer fit.
   - Duplicates, and notes that could be merged or split.
   - Older notes that should link to newer ones.
   - An `area` or `status` that no longer fits.
   - `needs-intro` or `todo` tags that no longer apply.
5. List the proposed changes, grouped by area and then by note, each with a one-line reason. Stop there and wait for approval.
6. Apply only what was approved, then run `python _System/organize.py` again.
7. Report what changed, and what was left for later.

## Rules

- May change: metadata, `## Related`, MOCs and file names (updating links to a renamed note).
- Merges and splits move the user's existing text as written, and only with explicit approval for that note.
- Never delete a note without explicit approval for that note. Send approved deletions to the Recycle Bin.
- Links go only in `## Related`, never in the text. MOCs are the exception.
- Tags go only in the `tags` field.
