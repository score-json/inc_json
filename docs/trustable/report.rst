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
   * - :doc:`assertions/TA-BEHAVIOURS`
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
   * - :doc:`assertions/TA-MISBEHAVIOURS`
     - Prohibited misbehaviours for json library are identified, and mitigations are specified, verified and validated based on analysis.
     - 0.00
   * - TA-RELEASES
     - Construction of json library releases is fully repeatable and the results are fully reproducible, with any exceptions documented and justified.
     - 0.00
   * - TA-SUPPLY_CHAIN
     - All sources for json library and tools are mirrored in our controlled environment.
     - 0.00
   * - :doc:`assertions/TA-TESTS`
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
   * - :doc:`tenets/TT-CHANGES`
     - Json library is actively maintained, with regular updates to dependencies, and changes are verified to prevent regressions.
     - 0.00
   * - :doc:`tenets/TT-CONFIDENCE`
     - Confidence in json library is measured by analysing actual performance in tests and in production.
     - 0.00
   * - :doc:`tenets/TT-CONSTRUCTION`
     - Tools are provided to build json library from trusted sources (also provided) with full reproducibility.
     - 0.00
   * - :doc:`tenets/TT-EXPECTATIONS`
     - Documentation is provided, specifying what json library is expected to do, and what it must not do, and how this is verified.
     - 0.00
   * - :doc:`tenets/TT-PROVENANCE`
     - All inputs (and attestations for claims) for json library are provided with known provenance.
     - 0.00
   * - :doc:`tenets/TT-RESULTS`
     - Evidence is provided to demonstrate that json library does what it is supposed to do, and does not do what it must not do.
     - 0.00


Assumptions of Use
###################

.. list-table:: Assumptions of Use
   :widths: 15 85
   :header-rows: 1

   * - Id
     - Summary
   * - AoU-01
     - Problems with nlohmann_json's implementation identified during testing are reported to the upstream nlohmann_json project.
   * - AoU-02
     - The build environment used for nlohmann_json in an integrating system is supplied with consistent dependencies.
   * - AoU-03
     - The integrator has Integrator-controlled mirrors of the dependencies.
   * - AoU-04
     - The system is built with the S-Core bazel build pipeline.
   * - AoU-05
     - Exceptions are properly handled or turned off:

       Context:

       - All exceptions (``json::parse_error``, ``json::invalid_iterator``, ``json::type_error``, ``json::out_of_range``, ``json::other_error``) inherit from ``json::exception``.
       - The nlohman_json library uses ``JSON_TRY``, ``JSON_CATCH``, etc., macros instead of the exception keywords ``try``, ``catch``, etc., which may be overwritten to suppress exceptions.
       - Each keyword can be individually overwritten (e.g. ``#define JSON_THROW(exception) std::abort()``) or all keywords can be changed by setting ``#define JSON_NOEXCEPTION`` to suppress exceptions.
       - Alternatively, the ``accept`` function may be used to check JSON validity, as it only throws an exception for an empty input. In the case of invalid JSON, ``false`` is returned, and no exception occurs. The ``parse`` function also has a parameter ``allow_exceptions`` to turn off parse error exceptions.
       - See:
        - `nlohman_json: JSON_NOEXCEPTION Macro <https://json.nlohmann.me/api/macros/json_noexception/>`_
        - `nlohman_json: Switch Off Exceptions <https://json.nlohmann.me/home/exceptions/#switch-off-exceptions>`_

   * - AoU-06
     - Input is encoded as UTF-8 (as required by RFC8259) and in case other string formats are used, it is expected that the parse or dump function may throw an exception.
   * - AoU-07
     - Brace initialization (e.g. json j{true};) is not used with the types basic_json, json, or ordered_json unless you want to create an object or array.
   * - AoU-08
     - If the input is no valid JSON, exceptions are expected during parsing with default parameters.
