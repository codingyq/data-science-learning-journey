# Tips — Collapsible `<details>` in GitHub Markdown

Quick pro-tips so it always works smoothly:

- Put a **blank line** before `<details>` and after `</summary>`.
- Keep the **`<summary>` on one line** (no headings/lists inside it).
- Use **`open`** to expand by default: `<details open>`.
- Nested `<details>` are allowed, but don’t overdo it (harder to read).
- Local previews (PyCharm/VS Code) may not toggle; **GitHub will**.

## Copy-paste template
```markdown
<details>
<summary><b>Section title</b> (n/m)</summary>

…content…

</details>
