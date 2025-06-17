load("@rules_cc//cc:defs.bzl", "cc_library")
load("@rules_cc//cc:cc_test.bzl", "cc_test")

genrule(
    name = "generate_test_data_hpp",
    outs = ["test_data.hpp"],
    cmd = "echo '#define TEST_DATA_DIRECTORY \"json_test_data\"' > $@",
)

cc_library(
    name = "test_data_header",
    hdrs = [
        "make_test_data_available.hpp",
        "test_data_header.hpp",
        "test_data.hpp",
        "test_utils.hpp",
    ],
    deps = [":generate_test_data_hpp"],
    includes = ["."],
    visibility = ["//visibility:public"],
)

cc_test(
    name = "all_nlohmann_tests",
    srcs = glob([
        "unit*.cpp",
    ], exclude = [
        "unit-32bit.cpp",
    ]) + select({
        "@platforms//cpu:x86_32": ["unit-32bit.cpp"],  # Only include on 32-bit x86
        "//conditions:default": [],
    }),
    deps = [
        ":test_data_header",
        "//nlohmann_json/single_include/nlohmann:nlohmann_json",
        "//nlohmann_json/tests/thirdparty/doctest:doctest_compatibility",
        "//nlohmann_json/tests/thirdparty/doctest:doctest",
        "//nlohmann_json/tests/thirdparty/fifo_map:fifo_map",

    ],
    data = glob(["json_test_data/**"]),
    copts = [
        '-DTEST_DATA_DIRECTORY="json_test_data"',
    ],
    includes = [
        ".",
    ],
)
