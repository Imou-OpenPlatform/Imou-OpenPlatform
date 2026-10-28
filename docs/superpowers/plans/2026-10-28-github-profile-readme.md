# GitHub Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the official Imou GitHub profile README so https://github.com/Imou-OpenPlatform shows it.

**Architecture:** One `README.md` in the repository whose name matches the GitHub user `Imou-OpenPlatform`. A unittest locks that file to the approved text. Pushing `main` to `Imou-OpenPlatform/Imou-OpenPlatform` is what makes GitHub render the profile.

**Tech Stack:** Markdown, Python unittest, GitHub CLI (`gh`) authenticated as `Imou-OpenPlatform`.

## Global Constraints

- This is the official Imou account introduction, not the Imou Life project README.
- Repository name is `Imou-OpenPlatform/Imou-OpenPlatform`. The profile file is `README.md` at the repository root.
- English and Chinese state the same facts. The top of the page links `#english` and `#zh-hans`.
- Say this is the official Imou account on GitHub (乐橙在 GitHub 上的官方账号).
- Link only these repositories: `https://github.com/Imou-OpenPlatform/Imou-Home-Assistant` and `https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api`.
- Imou Life is the Home Assistant integration, installed through HACS. pyimouapi is the Python library that integration uses.
- Questions go to an issue on the repository the question is about.
- Do not add install steps, a feature list, decrypt-library instructions, configuration docs, a star history chart, stat badges, tech-stack badges, a personal name, a job title, or any biography that is not on the account.
- The committed `README.md` bytes match the page in `docs/superpowers/specs/2026-10-28-github-profile-readme-design.md`.

---

### Task 1: Profile README

**Files:**
- Create: `README.md`
- Test: `tests/test_readme.py`

**Interfaces:**
- Consumes: the page block in `docs/superpowers/specs/2026-10-28-github-profile-readme-design.md`
- Produces: repository-root `README.md` whose text equals `EXPECTED_README` in `tests/test_readme.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_readme.py`:

```python
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_README = """# Imou Open Platform

**[English](#english)** | **[简体中文](#zh-hans)**

<a id="english"></a>

This is the official Imou account on GitHub. We publish the Home Assistant integration for Imou devices, and the Python library that integration uses.

## Repositories

- [Imou Life](https://github.com/Imou-OpenPlatform/Imou-Home-Assistant) — the Home Assistant integration, installed through HACS
- [pyimouapi](https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api) — the Python library used by that integration

## Questions

Open an issue on the repository your question is about.

<a id="zh-hans"></a>

# 乐橙开放平台

这是乐橙在 GitHub 上的官方账号。我们发布乐橙设备的 Home Assistant 集成，以及这个集成使用的 Python 库。

## 仓库

- [Imou Life](https://github.com/Imou-OpenPlatform/Imou-Home-Assistant) — Home Assistant 集成，通过 HACS 安装
- [pyimouapi](https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api) — 这个集成使用的 Python 库

## 问题

请到对应仓库开 Issue。
"""


class ProfileReadmeTest(unittest.TestCase):
    def test_readme_matches_the_approved_page(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(text, EXPECTED_README)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run from `/home/open/projects/Imou-OpenPlatform`:

```bash
python3 -m unittest tests/test_readme.py
```

Expected: FAIL because `README.md` does not exist (`FileNotFoundError`).

- [ ] **Step 3: Write the profile page**

Create `README.md` with the same characters as `EXPECTED_README`, including the final newline.

- [ ] **Step 4: Run the test to verify it passes**

```bash
python3 -m unittest tests/test_readme.py
```

Expected: `OK`.

- [ ] **Step 5: Commit**

```bash
git add README.md tests/test_readme.py
git commit -m "$(cat <<'EOF'
docs: add the official GitHub profile README

EOF
)"
```

### Task 2: Publish the profile repository

**Files:**
- Modify: none
- Test: `gh repo view` against `Imou-OpenPlatform/Imou-OpenPlatform`

**Interfaces:**
- Consumes: `README.md` committed on local `main` by Task 1
- Produces: public repository `Imou-OpenPlatform/Imou-OpenPlatform` whose default branch `main` contains that `README.md`

- [ ] **Step 1: Confirm the local page still matches**

Run from `/home/open/projects/Imou-OpenPlatform`:

```bash
python3 -m unittest tests/test_readme.py
```

Expected: `OK`.

- [ ] **Step 2: Create the GitHub repository and push `main`**

`gh` must already be authenticated as `Imou-OpenPlatform`. Do not force-push. Do not change git config.

```bash
gh repo create Imou-OpenPlatform/Imou-OpenPlatform --public --source=. --remote=origin --push
```

Expected: the command prints the new repository URL `https://github.com/Imou-OpenPlatform/Imou-OpenPlatform`.

- [ ] **Step 3: Verify GitHub is serving this README**

```bash
gh repo view Imou-OpenPlatform/Imou-OpenPlatform --json name,url,defaultBranchRef --jq '{name,url,branch:.defaultBranchRef.name}'
gh api repos/Imou-OpenPlatform/Imou-OpenPlatform/readme --jq .content | base64 -d | python3 -c "import sys; t=sys.stdin.read(); assert t.startswith('# Imou Open Platform\n'); assert 'This is the official Imou account on GitHub' in t; assert '这是乐橙在 GitHub 上的官方账号' in t; assert 'https://github.com/Imou-OpenPlatform/Imou-Home-Assistant' in t; assert 'https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api' in t; print('profile readme ok')"
```

Expected: `name` is `Imou-OpenPlatform`, `url` is `https://github.com/Imou-OpenPlatform/Imou-OpenPlatform`, `branch` is `main`, and the second command prints `profile readme ok`.

https://github.com/Imou-OpenPlatform then shows that same page.
