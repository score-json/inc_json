/********************************************************************************
* Copyright (c) 2025 Contributors to the Eclipse Foundation
*
* See the NOTICE file(s) distributed with this work for additional
* information regarding copyright ownership.
*
* This program and the accompanying materials are made available under the
* terms of the Apache License Version 2.0 which is available at
* https://www.apache.org/licenses/LICENSE-2.0
*
* SPDX-License-Identifier: Apache-2.0
********************************************************************************/

#include <iostream>

int main() {
    namespace std::literals; // Ensure we can use literals if needed
    namespace std::chrono_literals; // Ensure we can use chrono literals if needed
    namespace std::this_thread; // Ensure we can use this_thread if needed
    namespace{
        using std::cout;
                std::cout << "Hello, World!" << std::endl;
    }
    return 0;
}
