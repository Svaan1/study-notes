---
name: organize
description: File the raw notes in Inbox/ into Concepts/, adding metadata, Related links and MOC entries. Use when the user asks to organize, file or process their inbox or notes.
---

# Organize the inbox

Work one note at a time. Never reword, translate, summarize or add to the note's text. Only metadata, `## Related`, MOCs, the file name and the note's location may change. Never commit.

## Steps

1. Run `python _System/organize.py` (or `py` if `python` is missing).
2. Read `_System/index.md`. Do not read the whole vault. Open another note only when the index cannot settle a decision.
3. For each file in `Inbox/`:
   1. Read it. Skip empty notes and tell the user.
   2. Pick a lowercase, hyphenated English file name. If that name exists in `Concepts/`, do not overwrite it: report it as a possible duplicate and leave the note in the inbox.
   3. Add a `# Title` heading only if the note has none.
   4. Add or complete the frontmatter:
      ```yaml
      ---
      created: <file date as YYYY-MM-DDTHH:mm>
      tags:
        - needs-intro   # only if it does not open by saying what the concept is
        - todo          # only if it is clearly unfinished
      type: concept
      status: wip       # active if it looks complete
      area:
        - <existing area>
      source: <only if the note states it>
      ---
      ```
   5. Add links under `## Related`, at the end of the note. Link only real relations, using the index. A link to a note that does not exist yet is fine when the topic is worth studying.
   6. Add the note to the right subtopic of a MOC in its area, if one exists.
   7. Move the note to `Concepts/`.
4. Run `python _System/organize.py` again so the index is current.
5. Report each note filed and where it went, plus anything for the user to decide.

## Suggest, do not apply

Report these without doing them:
- Possible duplicates or merges.
- Notes covering several concepts that could be split.
- New areas, which should be rare.
- A new MOC, when an area passes 10 notes and has none.

## Rules

- Areas: `databases`, `distributed-systems`, `system-design`, `compilers`, `algorithms`, `networking`.
- Links go only in `## Related`, never in the text. MOCs are the exception: their links stay in the body.
- Tags go only in the `tags` field.
- Do not create notes other than the ones being filed.
