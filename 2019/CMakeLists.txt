cmake_minimum_required(VERSION 3.10)

# set the project name
project(AOC_2019)

file(GLOB aoc2019_SRC
    "main.cpp",
    "includeguards.h",
    "day1/day1.h"
)


# add the executable
add_executable(AOC_2019 ${aoc2019_SRC})