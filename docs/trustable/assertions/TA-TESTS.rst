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

.. _ta-tests:

TA-TESTS
#############

Overview
--------

TA-TESTS is a component of the Trustable Software Framework dedicated to ensuring the integrity and reproducibility of all tests related to the json library and its associated build and test environments. This section emphasizes constructing tests from controlled and mirrored sources, documenting any exceptions, and ensuring retroactive reproducibility of test results. TA-TESTS validates the implementation of specified tests and fault inductions, integrates test tooling and environments, and guarantees that all components operate within a controlled setup. Through automated end-to-end test execution, the framework aims to consistently achieve reproducible results, bolstering confidence in the testing process and software reliability. Further reading can be found `here <https://codethinklabs.gitlab.io/trustable/trustable/doorstop/TA.html#ta-tests>`_.


Guidance
--------

This assertion is satisfied to the extent that we:

- have implemented all of the tests specified in :doc:`../TT-EXPECTATIONS/TA-BEHAVIOURS`
- have implemented fault inductions specified in :doc:`../TT-EXPECTATIONS/TA-MISBEHAVIOURS`
- have implemented or integrated test tooling and environments for these
- can demonstrate that all of these are constructed from:
  - change-managed sources (see TA-UPDATES)
  - mirrored sources (see TA-SUPPLY_CHAIN)

All of the above must ensure that test results are retroactively reproducible, which is easily achieved through automated end-to-end test execution alongside necessary environment setups. Note that with non-deterministic software, exact results may not be reproducible, but high-level takeaways and exact setup should still be possible.


Evidence
--------

Test Overview
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: List of Tests and Descriptions
   :header: "Test Name", "Description"
   :widths: 25, 75

   "fuzzer-driver_afl.cpp", "Tests integration with AFL (American Fuzzy Lop) fuzzer for discovering edge cases and vulnerabilities in JSON parsing."
   "fuzzer-parse_bjdata.cpp", "Focuses on parsing BJData, a binary format related to JSON-capable of handling similar data structures."
   "fuzzer-parse_bson.cpp", "Examines the parsing of BSON (Binary JSON) data to ensure reliable and accurate conversion."
   "fuzzer-parse_cbor.cpp", "Tests CBOR (Concise Binary Object Representation), ensuring correct parsing and handling of binary data."
   "fuzzer-parse_json.cpp", "Evaluates the JSON parsing functionality with fuzzing to test the robustness against malformed inputs."
   "fuzzer-parse_msgpack.cpp", "Focuses on MessagePack, a binary format, and tests its parsing for consistency with JSON structures."
   "fuzzer-parse_ubjson.cpp", "Tests UBJSON (Universal Binary JSON), ensuring accurate parsing of its structured binary data."
   "make_test_data_available.hpp", "Provides utilities and functions to set up and manage test data within the test environment."
   "test_utils.hpp", "Contains utility functions and helpers that are shared across different tests for JSON functionalities."
   "unit-32bit.cpp", "Ensures compatibility and correct behavior of the JSON library when used on 32-bit systems."
   "unit-algorithms.cpp", "Tests various STL algorithms applied on JSON data, ensuring they work correctly with JSON structures."
   "unit-allocator.cpp", "Examines custom memory allocation strategies within the JSON library."
   "unit-alt-string.cpp", "Tests alternative string handling mechanisms and their integration within JSON functionality."
   "unit-assert_macro.cpp", "Verifies the behavior of assertion macros used throughout the JSON library."
   "unit-binary_formats.cpp", "Tests across different binary formats supported by the library, such as CBOR and MessagePack."
   "unit-bjdata.cpp", "Focuses on BJData handling, ensuring correct parsing and functionality."
   "unit-bson.cpp", "Evaluates BSON format behavior and its integration within the JSON library."
   "unit-byte_container_with_subtype.cpp", "Examines containers with specific byte subtypes, ensuring they work seamlessly."
   "unit-capacity.cpp", "Tests the capacity management functionalities in JSON objects."
   "unit-cbor.cpp", "Focuses specifically on the CBOR format, ensuring its correct interpretation."
   "unit-class_const_iterator.cpp", "Tests constant iterators in JSON structures for correct traversal."
   "unit-class_iterator.cpp", "Tests general iterator functionalities within JSON structures."
   "unit-class_lexer.cpp", "Examines lexer functionalities that parse JSON text into tokens."
   "unit-class_parser.cpp", "Evaluates parser behavior, including new options like trailing commas."
   "unit-class_parser_diagnostic_positions.cpp", "Tests parser diagnostics related to the position of errors in JSON text."
   "unit-comparison.cpp", "Verifies comparison operations between JSON objects and values."
   "unit-concepts.cpp", "Tests C++ concepts employed within the JSON library for compatibility and correctness."
   "unit-constructor1.cpp", "Examines JSON construction from various data types."
   "unit-constructor2.cpp", "Further tests construction robustness, handling edge cases and diverse input types."
   "unit-convenience.cpp", "Tests convenience methods provided by the JSON library for ease of use."
   "unit-conversions.cpp", "Validates conversion routines between JSON objects and various C++ types."
   "unit-custom-base-class.cpp", "Tests the inheritance and customization options for JSON objects."
   "unit-deserialization.cpp", "Ensures deserialization routines work correctly across different formats."
   "unit-diagnostic-positions-only.cpp", "Focuses on diagnostics output to help identify parsing issues."
   "unit-diagnostic-positions.cpp", "Comprehensive tests on diagnostic outputs related to parsing."
   "unit-diagnostics.cpp", "A broader suite for diagnostics functionality throughout the library."
   "unit-disabled_exceptions.cpp", "Verifies behavior when exceptions are disabled within JSON operations."
   "unit-element_access1.cpp", "Tests access patterns on JSON elements, validating methods for retrieval."
   "unit-element_access2.cpp", "Extends element access testing, including multi-level deep accesses."
   "unit-hash.cpp", "Evaluates hashing mechanisms and performance within JSON operations."
   "unit-inspection.cpp", "Tests inspection capabilities, allowing introspection within JSON structures."
   "unit-items.cpp", "Validates methods for iterating and accessing items in JSON containers."
   "unit-iterators1.cpp", "Tests specific iterator patterns for JSON arrays and objects."
   "unit-iterators2.cpp", "Examines advanced iterator functionality, handling complex data traversal."
   "unit-iterators3.cpp", "Comprehensive iterator tests across all types of JSON data."
   "unit-json_patch.cpp", "Ensures JSON Patch operations modify JSON objects correctly."
   "unit-json_pointer.cpp", "Tests JSON Pointer operations, ensuring they accurately retrieve nested values."
   "unit-large_json.cpp", "Examines parsing and performance with exceptionally large JSON documents."
   "unit-locale-cpp.cpp", "Tests JSON parsing behavior across different locales."
   "unit-merge_patch.cpp", "Validates Merge Patch functionality, ensuring correct application of patches."
   "unit-meta.cpp", "Tests metadata handling and integration within JSON structures."
   "unit-modifiers.cpp", "Validates modifier operations like insertions and deletions on JSON objects."
   "unit-msgpack.cpp", "Tests MessagePack format handling, ensuring it converts accurately to/from JSON."
   "unit-no-mem-leak-on-adl-serialize.cpp", "Confirms serialization does not cause memory leaks due to ADL (argument-dependent lookup)."
   "unit-noexcept.cpp", "Tests that operations marked as noexcept do not throw exceptions under any circumstances."
   "unit-ordered_json.cpp", "Ensures ordered JSON objects maintain expected key order during operations."
   "unit-ordered_map.cpp", "Tests ordered maps used within the JSON library."
   "unit-pointer_access.cpp", "Verifies correct behavior of pointer-based JSON access."
   "unit-readme.cpp", "Tests examples and functionalities mentioned in the README documentation."
   "unit-reference_access.cpp", "Tests reference-based access patterns for JSON data."
   "unit-regression1.cpp", "Verifies previous bug fixes to ensure they don't reappear (regression testing)."
   "unit-regression2.cpp", "Further regression tests to maintain stability after updates."
   "unit-serialization.cpp", "Tests serialization processes, ensuring correct conversion from JSON to text."
   "unit-testsuites.cpp", "Comprehensive test suites combining various JSON functionalities."
   "unit-to_chars.cpp", "Evaluates performance and correctness of 'to_chars' conversions."
   "unit-type_traits.cpp", "Tests C++ type traits used within the JSON library for compatibility."
   "unit-ubjson.cpp", "Verifies UBJSON format handling and conversion processes."
   "unit-udl.cpp", "Tests User-Defined Literals (UDLs) for creating JSON objects from literals."
   "unit-udt.cpp", "Tests User-Defined Types (UDTs) for seamless compatibility with JSON functionalities."
   "unit-udt_macro.cpp", "Evaluates macros for working with User-Defined Types in JSON."
   "unit-unicode1.cpp", "Tests handling of various Unicode characters and encodings."
   "unit-unicode2.cpp", "Extends Unicode handling, ensuring correct parsing and representation."
   "unit-unicode3.cpp", "Comprehensive tests for Unicode support throughout the library."
   "unit-unicode4.cpp", "Ensures compatibility and correct behavior with complex Unicode sequences."
   "unit-unicode5.cpp", "Further tests for edge cases in Unicode handling."
   "unit-user_defined_input.cpp", "Verifies support for user-defined input types and their integration with JSON parsing."
   "unit-windows_h.cpp", "Tests integration of JSON functionalities within a Windows environment."
   "unit-wstring.cpp", "Tests handling and conversion of wide strings within JSON operations."
   "unit.cpp", "General tests covering various aspects of JSON's core functionalities."


Fault inductions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive list of fault inductions is essential for testing the robustness and reliability of the JSON library. These fault inductions are designed to simulate various error conditions and edge cases that the library may encounter in real-world scenarios. You can find the list of fault inductions in the :doc:`../TT-EXPECTATIONS/TA-MISBEHAVIOURS` section of the Trustable Software Framework documentation.


Test Environments for Software Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Niels Lohmann JSON library employs rigorous testing methodologies to ensure software reliability and high quality:

1. **Unit Testing**:
   The library is heavily unit-tested, achieving 100% code coverage, including exceptional behavior scenarios. This ensures that each component functions correctly in isolation.

2. **Memory Leak Detection**:
   Valgrind and Clang Sanitizers are utilized to verify that there are no memory leaks within the codebase, providing stability and reliability.

3. **Fuzz Testing**:
   Google OSS-Fuzz performs continuous fuzz testing against all parsers 24/7. This process has effectively executed billions of test cases, identifying vulnerabilities through random and malformed input data.

4. **Quality Assurance**:
   The project adheres to the Core Infrastructure Initiative (CII) best practices to maintain high-quality standards. This involves comprehensive policies and documentation aimed at preserving the software's integrity and security.


Construction Configuration and Results (TBD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Construction Configuration**

The construction configuration outlines the setup and parameters used in building and testing the software system. This is crucial for ensuring consistency and reproducibility across different test environments. Key aspects include:

1. **Build Tools and Version**:
   - **Compiler**: GCC version X.Y.Z or equivalent
   - **Build System**: CMake or Bazel, version X.Y
   - **Dependencies**: Specific versions of libraries and frameworks, e.g., Boost 1.75 or JSON for Modern C++ 3.11

2. **Environment Setup**:
   - **Operating System**: Ubuntu 20.04, Windows 10, or macOS Catalina
   - **Hardware Requirements**: Minimum RAM, CPU specifications necessary for running tests
   - **Network Configuration**: Proxy settings, firewall configurations for connecting and testing in a networked setup

3. **Configuration Management**:
   - **Source Control**: Git repository at specific branch or commit; utilizing version control best practices
   - **Build Scripts**: Automated scripts for setting up and performing builds
   - **Virtualization/Containers**: Docker images or VMs for isolated testing environments

4. **Testing Tools**:
   - **Test Frameworks**: Unit testing using Catch2, integration testing with custom test suites
   - **Automation Tools**: Jenkins for CI/CD, Selenium for browser-based tests

**Construction Results**

The results section provides an overview of the outcomes from the construction phase, emphasizing the process's success and areas for potential improvements. Key results might include:

1. **Build Success Rate**:
   - Percentage of successful builds compared to attempted builds over a defined period
   - Metrics related to build failure reasons and resolutions

2. **Test Coverage**:
   - Percentage of code covered by tests; ideally aiming for 80% or higher
   - Identification of areas with insufficient coverage and plans for additional tests

3. **Performance Benchmarks**:
   - Execution times, resource utilization metrics from tests
   - Comparison to baseline figures and expected targets

4. **Error and Issue Tracking**:
   - Summary of bugs found during test phases; categorized by severity and type
   - Steps taken to resolve critical issues

5. **Reproducibility Assurance**:
   - Confirmation that results can be replicated in different environments or setups
   - Documentation of any deviations and corrective measures

This structured approach helps ensure all phases of construction and testing are thoroughly documented and reviewed, supporting both ongoing development efforts and future audits.

Confidence Scoring
------------------

Confidence scoring for TA-TESTS is based on the presence of tests and our confidence in their implementation and construction.

Checklist
---------

- How confident are we that we've implemented all of the specified tests?
- How confident are we that we've implemented all of the specified fault inductions?
- How confident are we that we have test tooling and environments enabling us to execute these tests and fault inductions?
- How confident are we that all test components are taken from within our controlled environment?
- How confident are we that all of the test environments we are using are also under our control?
