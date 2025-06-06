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

load("@rules_license//rules:license.bzl", "license")

package(
    default_applicable_licenses = [":license"],
)

exports_files([
    "LICENSE.MIT",
])

license(
    name = "license",
    license_kinds = ["@rules_license//licenses/spdx:MIT"],
    license_text = "LICENSE.MIT",
)

cc_library(
    name = "json",
    hdrs = ["include/main.cpp"],
    includes = ["include"],
    visibility = ["//visibility:public"],
    alwayslink = True,
)
