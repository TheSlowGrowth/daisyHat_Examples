cmake_policy(SET CMP0048 NEW)
project (daisyHatExamples)
cmake_minimum_required(VERSION 3.19)

include(CTest)

# include libDaisy and daisyHat
add_subdirectory(lib/libDaisy)
set(LIBDAISY_DIR lib/libDaisy)
add_subdirectory(lib/daisyHat)

# include the tests
add_subdirectory(tests)