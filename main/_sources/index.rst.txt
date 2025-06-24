..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

.. _library_description:

NLOHMANN JSON LIBRARY
=============================

This module is dedicated to implementing the Trustable Software Framework for the Niels Lohmann JSON Library. Initially, it emphasizes ensuring the reliability and correctness of the library's parsing functionality. The Niels Lohmann JSON Library is recognized for its efficient and straightforward approach to JSON parsing, manipulation, and serialization within modern C++ applications, aiming to provide developers with a flexible and robust tool for managing JSON data structures. The framework seeks to enhance these capabilities, aligning them with rigorous software quality standards to ensure dependable JSON processing across diverse applications.

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
--------

This repository provides the aspired setup for projects using **C++** and **Bazel** as a build system.

.. toctree::
   :maxdepth: 1
   :glob:

   introduction/index.rst
   trustable/index.rst
   trustable/tenets/index.rst
   Eclipse <https://projects.eclipse.org/projects/automotive.score>

Requirements
------------

.. stkh_req:: Correct JSON Parsing
   :id: stkh_req__json_parsing_accuracy__core_lib
   :status: valid
   :safety: QM
   :reqtype: Functional
   :rationale: Ensure the library accurately parses JSON strings into their corresponding data structures, accommodating both common and edge cases.

.. stkh_req:: Efficient Serialization
   :id: stkh_req__serialization_efficiency__core_lib
   :status: valid
   :safety: QM
   :reqtype: Functional
   :rationale: Guarantee that the library performs serialization operations swiftly, minimizing processing time and resource consumption.

.. stkh_req:: Comprehensive Testing
   :id: stkh_req__test_coverage__testing_module
   :status: valid
   :safety: QM
   :reqtype: Non-Functional
   :rationale: Achieve 100% test coverage in unit and integration tests, including verification against memory leaks using tools like Valgrind and Clang Sanitizers.

.. stkh_req:: Fuzz Testing Compliance
   :id: stkh_req__fuzz_testing__testing_module
   :status: valid
   :safety: QM
   :reqtype: Non-Functional
   :rationale: Integrate continuous fuzz testing to detect vulnerabilities, executing extensive test scenarios as part of a broader security strategy.

.. stkh_req:: Adherence to Apache License 2.0
   :id: stkh_req__license_compliance__core_lib
   :status: valid
   :safety: QM
   :reqtype: Legal
   :rationale: Ensure all aspects of the library, including contributions and modifications, adhere to the terms specified under the Apache License Version 2.0.



Project Layout
--------------

This module includes the following top-level structure:

- `nlohmann_json/include/`: C++ source code for the NLOHMANN JSON library
- `nlohmann_json/tests/`: Unit and integration tests
- `docs/`: Documentation using `docs-as-code`
- `.github/workflows/`: CI/CD pipelines

Quick Start
-----------

To build the module:

.. code-block:: bash

   bazel build

To run tests:

.. code-block:: bash

   git submodule init
   git submodule update
   bazel test //nlohmann_json/tests/src:all_nlohmann_tests --test_output=all

To update the documentation:

.. code-block:: bash

   bazel run //docs:incremental
   python3 -m http.server --directory _build

To generate LaTeX documentation:

.. code-block:: bash

   apt-get install texlive texlive-latex-extra texlive-fonts-recommended
   sphinx-build -b latex . _build/latex
   cd _build/latex
   pdflatex nlohmannjsonlibrary.tex
