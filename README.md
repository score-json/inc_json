# NLOHMANN JSON LIBRARY (TSF)

This module is dedicated to implementing the Trustable Software Framework for the Niels Lohmann JSON Library. Initially, it emphasizes ensuring the reliability and correctness of the library's parsing functionality. The Niels Lohmann JSON Library is recognized for its efficient and straightforward approach to JSON parsing, manipulation, and serialization within modern C++ applications, aiming to provide developers with a flexible and robust tool for managing JSON data structures. The framework seeks to enhance these capabilities, aligning them with rigorous software quality standards to ensure dependable JSON processing across diverse applications.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)

## Overview

This repository provides the aspired setup for projects using **C++** and **Bazel** as a build system.

---

### 📂 Project Structure

| File/Folder                         | Description                                       |
| ----------------------------------- | ------------------------------------------------- |
| `README.md`                         | Short description & build instructions            |
| `nlohmann_json/include/`            | Include files for the module                      |
| `nlohmann_json/single_include/`     | Single Header Include file for the module         |
| `nlohmann_json/tests/`              | Unit tests (UT) and integration tests (IT)        |
| `docs/`                             | Documentation (Doxygen/ reStructuredText)         |
| `.github/workflows/`                | CI/CD pipelines                                   |
| `.vscode/`                          | Recommended VS Code settings                      |
| `.devcontainer/S-CORE/`             | Development containter, containing used packages  |
| `.bazelrc`, `MODULE.bazel`, `BUILD` | Bazel configuration & settings                    |
| `project_config.bzl`                | Project-specific metadata for Bazel macros        |
| `LICENSE.md`                        | Licensing information                             |
| `CONTRIBUTION.md`                   | Contribution guidelines                           |

---

## Quick Start

To build the module, run:

```bash
bazel build
```
To run tests, execute:

```bash
git submodule init
git submodule update
bazel test //nlohmann_json/tests/src:all_nlohmann_tests --test_output=all
```

To update the reStructuredText-documentation, follow these steps:

```bash
python3 -m venv venv && \
. venv/bin/activate && \
pip install sphinx==8.2.3 sphinx-design sphinx-needs sphinxcontrib.plantuml
cd docs
sphinx-build -b html . _build
python3 -m http.server --directory _build
```

or run (this will create SCORE-formated site):

```bash
bazel run //docs:incremental
python3 -m http.server --directory _build
```

To generate LaTeX documentation, use:
```bash
apt-get install texlive texlive-latex-extra texlive-fonts-recommended
sphinx-build -b latex . _build/latex
cd _build/latex
pdflatex nlohmannjsonlibrary.tex
```

Feel free to copy and use this Markdown format for your documentation purposes!
