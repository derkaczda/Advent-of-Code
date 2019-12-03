#ifndef DAY1_H
#define DAY1_H

#include "../utils.h"

void ReadFileContent(std::vector<std::string>& lines)
{
    bool result = GetFileContent("day1/input.txt", lines);

    if(!result)
    {
        std::cerr << "Reading file went wrong" << std::endl;
    }
}

int GetModuleFuel(int moduleMass)
{
    return (moduleMass / 3) - 2;
}

int GetModuleFuelRecursive(int moduleMass)
{
    int fuel = GetModuleFuel(moduleMass);
    if (fuel <= 0)
        return 0;
    return fuel + GetModuleFuelRecursive(fuel);
}

int GetModuleFuelFromLine(const std::string& line)
{
    int moduleMass = std::stoi(line);
    return GetModuleFuel(moduleMass);
}

int GetCompleteModuleFuelFromLine(const std::string& line)
{
    int moduleMass = std::stoi(line);
    return GetModuleFuelRecursive(moduleMass);
}

void RunProblemOne()
{
    std::vector<std::string> lines;
    ReadFileContent(lines);

    int totalFuel = 0;
    for(std::string& line : lines)
    {
        int fuel = GetModuleFuelFromLine(line);
        totalFuel += fuel;
    }

    std::cout << "Total amount of fuel needed: " << totalFuel << std::endl;
}

void RunProblemTwo()
{
    std::vector<std::string> lines;
    ReadFileContent(lines);

    int totalFuel = 0;
    for(std::string& line : lines)
    {
        totalFuel += GetCompleteModuleFuelFromLine(line);
    }

    std::cout << "Total amount of fuel needed with fuel mass considered: " << totalFuel << std::endl;
}

#endif