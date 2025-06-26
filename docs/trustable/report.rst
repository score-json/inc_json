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
.. _report:

Report
==========================

Each item in a Trustable Graph is scored with a number between 0 and 1. The score represents aggregated organizational confidence in a given Statement, with larger numbers corresponding to higher confidence.


Compliance for TA
###################

.. list-table:: Compliance for TA
   :widths: 25 50 25
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - TA-ANALYSIS
     - Collected data from tests and monitoring of deployed software is analysed according to specified objectives.
     - 0.00
   * - :doc:`tenets/TT-EXPECTATIONS/TA-BEHAVIOURS`
     - Expected or required behaviours for json library are identified, specified, verified and validated based on analysis.
     - 0.00
   * - TA-CONFIDENCE
     - Confidence in json library is measured based on results of analysis.
     - 0.00
   * - TA-CONSTRAINTS
     - Constraints on adaptation and deployment of json library are specified.
     - 0.00
   * - TA-DATA
     - Data is collected from tests, and from monitoring of deployed software, according to specified objectives.
     - 0.00
   * - TA-FIXES
     - Known bugs or misbehaviours are analysed and triaged, and critical fixes or mitigations are implemented or applied.
     - 0.00
   * - TA-INDICATORS
     - Advance warning indicators for misbehaviours are identified, and monitoring mechanisms are specified, verified and validated based on analysis.
     - 0.00
   * - TA-INPUTS
     - All inputs to json library are assessed, to identify potential risks and issues.
     - 0.00
   * - TA-ITERATIONS
     - All constructed iterations of json library include source code, build instructions, tests, results and attestations.
     - 0.00
   * - TA-METHODOLOGIES
     - Manual methodologies applied for json library by contributors, and their results, are managed according to specified objectives.
     - 0.00
   * - :doc:`tenets/TT-EXPECTATIONS/TA-MISBEHAVIOURS`
     - Prohibited misbehaviours for json library are identified, and mitigations are specified, verified and validated based on analysis.
     - 0.00
   * - TA-RELEASES
     - Construction of json library releases is fully repeatable and the results are fully reproducible, with any exceptions documented and justified.
     - 0.00
   * - TA-SUPPLY_CHAIN
     - All sources for json library and tools are mirrored in our controlled environment.
     - 0.00
   * - :doc:`tenets/TT-CONSTRUCTION/TA-TESTS`
     - All tests for json library, and its build and test environments, are constructed from controlled/mirrored sources and are reproducible, with any exceptions documented.
     - 0.00
   * - TA-UPDATES
     - Json library components, configurations and tools are updated under specified change and configuration management controls.
     - 0.00
   * - TA-VALIDATION
     - All specified tests are executed repeatedly, under defined conditions in controlled environments, according to specified objectives.
     - 0.00

Compliance for TRUSTABLE
##########################

.. list-table:: Compliance for TRUSTABLE
   :widths: 25 50 25
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - TRUSTABLE-SOFTWARE
     - This release of json library is Trustable.
     - 0.00

Compliance for TT
###################

.. list-table:: Compliance for TT
   :widths: 25 50 25
   :header-rows: 1

   * - Item
     - Summary
     - Score
   * - :doc:`tenets/TT-CHANGES/index`
     - Json library is actively maintained, with regular updates to dependencies, and changes are verified to prevent regressions.
     - 0.00
   * - :doc:`tenets/TT-CONFIDENCE/index`
     - Confidence in json library is measured by analysing actual performance in tests and in production.
     - 0.00
   * - :doc:`tenets/TT-CONSTRUCTION/index`
     - Tools are provided to build json library from trusted sources (also provided) with full reproducibility.
     - 0.00
   * - :doc:`tenets/TT-EXPECTATIONS/index`
     - Documentation is provided, specifying what json library is expected to do, and what it must not do, and how this is verified.
     - 0.00
   * - :doc:`tenets/TT-PROVENANCE/index`
     - All inputs (and attestations for claims) for json library are provided with known provenance.
     - 0.00
   * - :doc:`tenets/TT-RESULTS/index`
     - Evidence is provided to demonstrate that json library does what it is supposed to do, and does not do what it must not do.
     - 0.00
