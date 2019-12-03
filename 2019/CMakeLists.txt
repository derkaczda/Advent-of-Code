cmake_minimum_required(VERSION 3.10)

# set the project name
project(AOC_2019)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

file(GLOB aoc2019_SRC
    "main.cpp",
    "setup.h",
    "utils.h",
    "day1/day1.h"
)

# add the executable
add_executable(AOC_2019 ${aoc2019_SRC})

add_custom_command(
        TARGET AOC_2019 POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_SOURCE_DIR}/day1/input.txt
                ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Debug/day1/input.txt)

add_custom_command(
        TARGET AOC_2019 POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_SOURCE_DIR}/day1/input.txt
                ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Release/day1/input.txt)