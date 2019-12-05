cmake_minimum_required(VERSION 3.10)

# set the project name
project(AOC_2019)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

file(GLOB aoc2019_SRC
    "main.cpp",
    "setup.h",
    "utils.h",
    "day1/day1.h",
    "day2/day2.h",
    "day2/intprogram.h",
    "day3/day3.h",
    "day4/day4.h",
    "day5/day5.h",
    "day5/intprogram.h"
)

# add the executable
add_executable(AOC_2019 ${aoc2019_SRC})

set( INPUT_FILES
 day1/input.txt
 day2/input.txt
 day3/input.txt
 day5/input.txt
)

foreach( file_i ${INPUT_FILES})
        add_custom_command(
                TARGET AOC_2019 POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                        ${CMAKE_SOURCE_DIR}/${file_i}
                        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Debug/${file_i})

        add_custom_command(
                TARGET AOC_2019 POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                        ${CMAKE_SOURCE_DIR}/${file_i}
                        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/Release/${file_i})
endforeach( file_i )