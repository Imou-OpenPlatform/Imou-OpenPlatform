import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_README = """# Imou Open Platform

**[English](#english)** | **[简体中文](#zh-hans)**

<a id="english"></a>

👋 Hi. This is the official Imou account on GitHub.

We publish the Home Assistant integration for Imou devices, and the Python library that integration uses. Pick a repo below and take a look.

## 📦 Repositories

- 🏠 [Imou Life](https://github.com/Imou-OpenPlatform/Imou-Home-Assistant) — the Home Assistant integration, installed through HACS
- 🐍 [pyimouapi](https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api) — the Python library used by that integration

## 💬 Questions

Open an issue on the repository your question is about. We'll see it.

<a id="zh-hans"></a>

# 乐橙开放平台

👋 你好，这是乐橙在 GitHub 上的官方账号。

我们在这里发布乐橙设备的 Home Assistant 集成，以及这个集成使用的 Python 库。下面两个仓库，挑一个进去看看就行。

## 📦 仓库

- 🏠 [Imou Life](https://github.com/Imou-OpenPlatform/Imou-Home-Assistant) — Home Assistant 集成，通过 HACS 安装
- 🐍 [pyimouapi](https://github.com/Imou-OpenPlatform/Py-Imou-Open-Api) — 这个集成使用的 Python 库

## 💬 问题

到对应仓库开个 Issue 就好，我们看得到。
"""


class ProfileReadmeTest(unittest.TestCase):
    def test_readme_matches_the_approved_page(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(text, EXPECTED_README)


if __name__ == "__main__":
    unittest.main()
