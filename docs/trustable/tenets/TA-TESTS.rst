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

All tests for the json-library, along with their build and test environments, are constructed from controlled/mirrored sources and are reproducible, with any exceptions documented.

Supported Requests
------------------

TT-CONSTRUCTION

Supporting Items
----------------

None

References
----------

None

Fallacies
---------

None

Guidance
--------

This assertion is satisfied to the extent that we:

- have implemented all of the tests specified in :doc:`TA-BEHAVIOURS`
- have implemented fault inductions specified in :doc:`TA-MISBEHAVIOURS`
- have implemented or integrated test tooling and environments for these
- can demonstrate that all of these are constructed from:
  - change-managed sources (see TA-UPDATES)
  - mirrored sources (see TA-SUPPLY_CHAIN)

All of the above must ensure that test results are retroactively reproducible, which is easily achieved through automated end-to-end test execution alongside necessary environment setups. Note that with non-deterministic software, exact results may not be reproducible, but high-level takeaways and exact setup should still be possible.


Evidence
--------

Test Overview (TBD)
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: List of Tests and Descriptions
   :header: "Test Name", "Description"
   :widths: 30, 70

   "array.cpp", "Tests functionality related to JSON arrays, including creation, manipulation, and serialization."
   "binary.cpp", "Focuses on binary formats and operations, testing correct encoding and decoding processes."
   "boolean.cpp", "Tests handling of boolean values, ensuring correct parsing and behavior within JSON structures."
   "class_parser.cpp", "Examines custom parser class to validate flexible parsing."
   "cmake_support.cpp", "Tests related to CMake configuration of the JSON library."
   "comments.cpp", "Tests JSON comments, ensuring they are handled correctly according to specifications."
   "conversions.cpp", "Checks conversion routines between JSON and native C++ types."
   "exceptions.cpp", "Verifies exception handling within JSON parsing and manipulation scenarios."
   "fuzzer.cpp", "Evaluates fuzz testing, aiming at robustness with random input data."
   "iterators.cpp", "Tests iterator behaviors and functionalities for traversing JSON elements."
   "json_pointer.cpp", "Assesses JSON pointer operations, ensuring accurate navigation and access of nested elements."
   "json_sax.cpp", "Tests streaming parsing via SAX (Simple API for XML-like streaming functionality)."
   "macros.cpp", "Checks the functionality of macro definitions and their impact on JSON operations."
   "memory.cpp", "Tests memory usage and garbage collection within JSON operations."
   "object.cpp", "Examines JSON object manipulations, including key-value pair handling."
   "operators.cpp", "Tests various operators used for JSON objects and values, ensuring correct logical and arithmetic operations."
   "parser.cpp", "Focuses on parsing mechanisms, testing the robustness and accuracy of converting strings to JSON objects."
   "serialization.cpp", "Evaluates the serialization process, ensuring JSON structures are correctly transformed to text."
   "types.cpp", "Tests the handling of different JSON value types."
   "unit-algorithmus.cpp", "Tests various STL algorithms applied on JSON data, ensuring they behave as expected."
   "utf8.cpp", "Assesses UTF-8 encoding and decoding processes, ensuring compliance with character encoding standards."

Fault inductions (TBD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is a list of fault inductions designed to test the robustness and reliability of a JSON library:

1. **Invalid JSON Format**:
   Attempt to parse malformed JSON strings that do not adhere to the standard JSON syntax, such as missing braces, brackets, or quotation marks.

2. **Non-UTF-8 Encodings**:
   Feed the parser data in encodings other than UTF-8, such as UTF-16 or ISO-8859-1, to test how encoding errors are handled.

3. **Extremely Large JSON**:
   Provide JSON files or strings that are significantly larger than typical sizes to test memory handling and performance.

4. **Deeply Nested JSON Structures**:
   Use JSON strings with excessive nesting levels to test recursion limits or stack overflows.

5. **Circular References**:
   Attempt to create objects with circular references, which are non-standard in JSON, to test detection of such anomalies.

6. **Special Character Handling**:
   Test JSON strings that contain special characters or escape sequences to ensure correct parsing and encoding.

7. **Boundary Value Inputs**:
   Use JSON inputs with values at or beyond expected minimum and maximum limits, such as boundary numbers for integer types.

8. **Unexpected Data Types**:
   Provide invalid or unexpected data types within JSON (such as functions or undefined symbols) and verify proper error detection and handling.

9. **Concurrent Access**:
   Induce faults by performing concurrent access to JSON parsing and manipulation, testing thread safety and potential race conditions.

10. **SAX Parsing Faults**:
    For libraries supporting SAX (streaming APIs), present streaming data with interruptions or unexpected terminations.

11. **Inconsistent Data Types**:
    Use JSON structures with inconsistent data types across similar keys or arrays, testing robustness in type checking.

12. **Memory Leak Induction**:
    Monitor specifically for scenarios that may expose potential memory leaks during heavy or repeated JSON operations.

13. **Randomized Inputs**:
    Leverage fuzz testing by feeding random and unpredictable JSON data to observe how the system responds to uncertain inputs.


Test Environments for Software Testing (TBD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following list outlines various test environments used to ensure comprehensive testing coverage:

1. **Development Environment**:
   A setup similar to the development environment, often using local machines or virtual machines with appropriate development tools and libraries to test initial versions of the software.

2. **Staging Environment**:
   An environment that mimics the production setting, allowing for testing in conditions that closely simulate real-world usage before full deployment.

3. **Production Environment**:
   The live environment where real user data and interactions occur, used for testing with particular caution, often under controlled conditions.

4. **Continuous Integration (CI) Environment**:
   Automated testing setup integrated with CI pipelines, ensuring regular tests are executed with each code change submission.

5. **Cross-Platform Testing Environment**:
   Environments configured for testing across multiple operating systems and hardware configurations, such as Windows, macOS, Linux, and mobile platforms.

6. **Cloud-Based Environment**:
   Remote servers or services in the cloud that simulate production conditions, allowing scalability and diverse configurations for tests.

7. **Virtualized Environment**:
   Use of virtual machines or containerization (e.g., Docker) to replicate various deployment scenarios, ensuring isolated and repeatable tests.

8. **Browser-Based Environment**:
   Testing setups designed for web applications, focusing on various browsers and versions to check compatibility and performance.

9. **Mobile Device Environment**:
   Configurations designed to test mobile applications across different devices, operating systems, screen sizes, and network conditions.

10. **Security Testing Environment**:
    Specialized setup to test security features and vulnerabilities, often isolated to prevent any real-world security implications.

11. **Load Testing Environment**:
    Configurations that simulate high-traffic conditions to test performance, scalability, and reliability under stress.

12. **Usability Testing Environment**:
    Environments focused on the user experience, often involving real or simulated end-user interactions to assess usability.

This diversity in test environments helps in ensuring that software systems are robust, performant, compatible, and secure across various real-world scenarios.


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
