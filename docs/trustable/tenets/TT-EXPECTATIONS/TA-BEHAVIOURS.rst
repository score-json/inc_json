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

.. _ta_behaviours:

TA-BEHAVIOURS
#############

Overview
--------

The TA-BEHAVIORS documentation provides a comprehensive guide to the assessment and testing of expected behaviors within the Trustable Software Framework. This section outlines the objectives, methodologies, and outcomes related to trust assessment. Further reading can be found `here <https://codethinklabs.gitlab.io/trustable/trustable/doorstop/TA.html#ta-behaviours>`_.

Objectives
----------

- Define clear behavior expectations for the software.
- Assess and verify compliance with established trust criteria.
- Document the procedures for testing and validation of behaviors.

Methodology
-----------

1. **Behavior Identification**
   - Document the intended behaviors of the software components.
   - Align behaviors with trust criteria.

2. **Assessment Procedures**
   - Design tests to evaluate each behavior.
   - Specify input conditions, expected outcomes, and test cases.

3. **Validation and Verification**
   - Execute tests and document results.
   - Validate test effectiveness by analyzing outcomes.

Expectations
----------------

The following expectations outline the critical behaviors and properties the Niels Lohmann JSON library is expected to provide and maintain:

1. **Correctness of JSON Parsing**:
   - Expectation: The library must correctly parse valid JSON data into the corresponding internal data structures.
   - Verification Strategy: Functional testing with various JSON datasets, including edge cases.

2. **Robust Error Handling**:
   - Expectation: The library must gracefully handle errors in JSON input with appropriate exception throwing and error messages.
   - Verification Strategy: Unit testing with malformed JSON inputs to ensure proper error handling.

3. **High Performance and Efficiency**:
   - Expectation: The library should perform operations such as parsing, serialization, and manipulation efficiently without unnecessary overhead.
   - Verification Strategy: Performance testing and benchmarks compared to other libraries.

4. **Memory Management and Leak Prevention**:
   - Expectation: The library must manage memory efficiently and prevent leaks, especially during intensive operations.
   - Verification Strategy: Testing using Valgrind and Clang Sanitizers to detect memory leaks.

5. **Comprehensive Documentation and Usability**:
   - Expectation: Documentation should be clear and comprehensive, ensuring users can effectively utilize the library's functionalities.
   - Verification Strategy: Documentation reviews and user feedback loops.

6. **Continuous Fuzz Testing**:
   - Expectation: The library should withstand various fuzz test scenarios without breaking or exhibiting vulnerabilities.
   - Verification Strategy: Integration with Google OSS-Fuzz for continuous fuzz testing.

7. **Standards Compliance**:
   - Expectation: The library must adhere to JSON standards and best practices defined by the Core Infrastructure Initiative (CII).
   - Verification Strategy: Regular audits and code reviews for compliance.

Evidence and Confidence Scoring
-------------------------------

- **Evidence**: Test results, documentation reviews, and continuous integration reports provide concrete evidence of expectation fulfillment.
- **Confidence Scoring**: High confidence in correctness and performance, supported by extensive test coverage and continuous maintenance.

Checklist for Expectations
--------------------------

- **Evolution of Expectations**: Regular updates based on user feedback and technological advances.
- **Comprehensiveness**: Continuous reviews ensure all critical requirements are covered.
- **Manipulation Considerations**: Transparent processes minimize information manipulation risks.
- **Discovery of New Expectations**: Ongoing analysis to identify emerging expectations.
- **Coverage Assessment**: All defined expectations have corresponding tests, with identified areas for improvement in coverage.

Test Cases
----------

### unit-algorithms.cpp

This section provides examples of testing the expected behaviors of software components using the Nlohmann JSON library's parsing capabilities. The file contains comprehensive test cases demonstrating the use of JSON in conjunction with Standard Template Library (STL) algorithms.

.. code-block:: c++

    // JSON for Modern C++ (version 3.12.0)
    // SPDX-License-Identifier: MIT

    #include "doctest_compatibility.h"
    #include <algorithm>
    #include <nlohmann/json.hpp>
    using nlohmann::json;

    TEST_CASE("algorithms")
    {
        json j_array = {13, 29, 3, {{"one", 1}, {"two", 2}}, true, false, {1, 2, 3}, "foo", "baz"};
        json j_object = {{"one", 1}, {"two", 2}};

        SECTION("non-modifying sequence operations")
        {
            SECTION("std::all_of")
            {
                CHECK(std::all_of(j_array.begin(), j_array.end(), [](const json & value)
                {
                    return !value.empty();
                }));
                CHECK(std::all_of(j_object.begin(), j_object.end(), [](const json & value)
                {
                    return value.type() == json::value_t::number_integer;
                }));
            }

            SECTION("std::any_of")
            {
                CHECK(std::any_of(j_array.begin(), j_array.end(), [](const json & value)
                {
                    return value.is_string() && value.get<std::string>() == "foo";
                }));
                CHECK(std::any_of(j_object.begin(), j_object.end(), [](const json & value)
                {
                    return value.get<int>() > 1;
                }));
            }

            SECTION("std::none_of")
            {
                CHECK(std::none_of(j_array.begin(), j_array.end(), [](const json & value)
                {
                    return value.empty();
                }));
                CHECK(std::none_of(j_object.begin(), j_object.end(), [](const json & value)
                {
                    return value.get<int>() <= 0;
                }));
            }

            SECTION("std::for_each")
            {
                SECTION("reading")
                {
                    int sum = 0;
                    std::for_each(j_array.cbegin(), j_array.cend(), [&sum](const json & value)
                    {
                        if (value.is_number())
                        {
                            sum += static_cast<int>(value);
                        }
                    });
                    CHECK(sum == 45);
                }

                SECTION("writing")
                {
                    auto add17 = [](json & value)
                    {
                        if (value.is_array())
                        {
                            value.push_back(17);
                        }
                    };
                    std::for_each(j_array.begin(), j_array.end(), add17);
                    CHECK(j_array[6] == json({1, 2, 3, 17}));
                }
            }

            SECTION("sorting operations")
            {
                json j_ordered;
                std::sort(j_array.begin(), j_array.end());
                CHECK(j_array == json({false, true, 3, 13, 29, {{"one", 1}, {"two", 2}}, {1, 2, 3}, "baz", "foo"}));
            }
        }
    }

### unit-allocator.cpp

This section includes tests that focus on memory allocation behavior to ensure expected allocation operations using custom allocators. The tests explore scenarios with a `bad_allocator` and `my_allocator` within the Nlohmann JSON context.

.. code-block:: c++

    // JSON for Modern C++ (supporting code)
    // version 3.12.0

    #include "doctest_compatibility.h"
    #define JSON_TESTS_PRIVATE
    #include <nlohmann/json.hpp>
    using nlohmann::json;

    namespace
    {
    template<class T>
    struct bad_allocator : std::allocator<T>
    {
        // Constructor
        bad_allocator() = default;
        template<class U> bad_allocator(const bad_allocator<U>&) { }

        // Throwing construct method
        template<class... Args>
        void construct(T* /*unused*/, Args&& ...) // NOLINT(cppcoreguidelines-missing-std-forward)
        {
            throw std::bad_alloc();
        }

        template <class U>
        struct rebind
        {
            using other = bad_allocator<U>;
        };
    }

    TEST_CASE("bad_alloc")
    {
        SECTION("bad_alloc")
        {
            using bad_json = nlohmann::basic_json<std::map, std::vector, std::string, bool,
                                                  std::int64_t, std::uint64_t, double, bad_allocator>;

            // Check bad_alloc with basic_json object creation
            CHECK_THROWS_AS(bad_json(bad_json::value_t::object), std::bad_alloc&);
        }
    }

    namespace
    {
    bool next_construct_fails = false;
    bool next_destroy_fails = false;
    bool next_deallocate_fails = false;

    template<class T>
    struct my_allocator : std::allocator<T>
    {
        template<class... Args>
        void construct(T* p, Args&& ... args)
        {
            if (next_construct_fails)
            {
                next_construct_fails = false;
                throw std::bad_alloc();
            }

            ::new (reinterpret_cast<void*>(p)) T(std::forward<Args>(args)...);
        }

        void deallocate(T* p, std::size_t n)
        {
            if (next_deallocate_fails)
            {
                next_deallocate_fails = false;
                throw std::bad_alloc();
            }

            std::allocator<T>::deallocate(p, n);
        }

        void destroy(T* p)
        {
            if (next_destroy_fails)
            {
                next_destroy_fails = false;
                throw std::bad_alloc();
            }

            static_cast<void>(p); // fix MSVC's C4100 warning
            p->~T();
        }

        template <class U>
        struct rebind
        {
            using other = my_allocator<U>;
        };
    }

    template<class T>
    void my_allocator_clean_up(T* p)
    {
        assert(p != nullptr);
        my_allocator<T> alloc;
        alloc.destroy(p);
        alloc.deallocate(p, 1);
    }

    TEST_CASE("controlled bad_alloc")
    {
        using my_json = nlohmann::basic_json<std::map, std::vector, std::string, bool,
                                             std::int64_t, std::uint64_t, double, my_allocator>;

        SECTION("class json_value")
        {
            SECTION("json_value(value_t)")
            {
                SECTION("object")
                {
                    next_construct_fails = false;
                    auto t = my_json::value_t::object;
                    CHECK_NOTHROW(my_allocator_clean_up(my_json::json_value(t).object));
                    next_construct_fails = true;
                    CHECK_THROWS_AS(my_json::json_value(t), std::bad_alloc&);
                }
                SECTION("array")
                {
                    next_construct_fails = false;
                    auto t = my_json::value_t::array;
                    CHECK_NOTHROW(my_allocator_clean_up(my_json::json_value(t).array));
                    next_construct_fails = true;
                    CHECK_THROWS_AS(my_json::json_value(t), std::bad_alloc&);
                }
                SECTION("string")
                {
                    next_construct_fails = false;
                    auto t = my_json::value_t::string;
                    CHECK_NOTHROW(my_allocator_clean_up(my_json::json_value(t).string));
                    next_construct_fails = true;
                    CHECK_THROWS_AS(my_json::json_value(t), std::bad_alloc&);
                }
            }
            SECTION("json_value(const string_t&)")
            {
                next_construct_fails = false;
                const my_json::string_t v("foo");
                CHECK_NOTHROW(my_allocator_clean_up(my_json::json_value(v).string));
                next_construct_fails = true;
                CHECK_THROWS_AS(my_json::json_value(v), std::bad_alloc&);
            }
        }

        SECTION("class basic_json")
        {
            SECTION("basic_json(const CompatibleObjectType&)")
            {
                next_construct_fails = false;
                const std::map<std::string, std::string> v {{"foo", "bar"}};
                CHECK_NOTHROW(my_json(v));
                next_construct_fails = true;
                CHECK_THROWS_AS(my_json(v), std::bad_alloc&);
            }
            SECTION("basic_json(const CompatibleArrayType&)")
            {
                next_construct_fails = false;
                const std::vector<std::string> v {"foo", "bar", "baz"};
                CHECK_NOTHROW(my_json(v));
                next_construct_fails = true;
                CHECK_THROWS_AS(my_json(v), std::bad_alloc&);
            }
            SECTION("basic_json(const typename string_t::value_type*)")
            {
                next_construct_fails = false;
                CHECK_NOTHROW(my_json("foo"));
                next_construct_fails = true;
                CHECK_THROWS_AS(my_json("foo"), std::bad_alloc&);
            }
            SECTION("basic_json(const std::string&)")
            {
                next_construct_fails = false;
                const std::string s("foo");
                CHECK_NOTHROW(my_json(s));
                next_construct_fails = true;
                CHECK_THROWS_AS(my_json(s), std::bad_alloc&);
            }
        }
    }

    namespace
    {
    template<class T>
    struct allocator_no_forward : std::allocator<T>
    {
        allocator_no_forward() = default;

        template <class U>
        allocator_no_forward(allocator_no_forward<U>) {}

        template <class U>
        struct rebind
        {
            using other = allocator_no_forward<U>;
        }

        template <class... Args>
        void construct(T* p, const Args& ... args) noexcept(noexcept(::new (reinterpret_cast<void*>(p)) T(args...)))
        {
            ::new (static_cast<void*>(p)) T(args...);
        }
    }

    TEST_CASE("bad my_allocator::construct")
    {
        SECTION("my_allocator::construct doesn't forward")
        {
            using bad_alloc_json = nlohmann::basic_json<std::map, std::vector, std::string, bool,
                                                        std::int64_t, std::uint64_t, double, allocator_no_forward>;

            bad_alloc_json j;
            j["test"] = bad_alloc_json::array_t();
            j["test"].push_back("should not leak");
        }
    }

Results
-------

- Documented outcomes of behavior testing.
- Analysis of discrepancies between expected and actual behavior.
- Recommendations for improvement.

Conclusion
----------

The TA-BEHAVIORS framework ensures that software meets trustability standards by systematically assessing and documenting expected behaviors. Through continuous validation and verification, the framework supports the development of reliable and secure software.
