#ifndef DAY1_H
#define DAY1_H

#include "../utils.h"

int GetModuleFuelFromLine(const std::string& line)
{
    int moduleMass = std::stoi(line);
    return (moduleMass / 3) - 2;
}

void RunDay()
{
    std::vector<std::string> lines;
    bool result = GetFileContent("day1/input.txt", lines);

    if(!result)
    {
        std::cerr << "Reading file went wrong" << std::endl;
    }

    int totalFuel = 0;
    for(std::string& line : lines)
    {
        std::cout << line << std::endl;
        int fuel = GetModuleFuelFromLine(line);
        totalFuel += fuel;
    }

    std::cout << "Total amount of fuel needed: " << totalFuel << std::endl;
}

#endif