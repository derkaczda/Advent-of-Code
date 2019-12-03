#ifndef DAY3_H
#define DAY3_H

#include "../utils.h"

#include <algorithm>
#include <sstream>

#define DIR_UP "U"
#define DIR_DOWN "D"
#define DIR_RIGHT "R"
#define DIR_LEFT "L"

struct Vector2
{
    Vector2(int _x, int _y) : x(_x), y(_y) {}
    int x;
    int y;
};

std::vector<std::string> SplitString(std::string& string)
{
    std::replace(string.begin(), string.end(), ',', ' ');

    std::stringstream ss(string);
    std::string temp;
    std::vector<std::string> strVector;
    while(ss >> temp)
        strVector.push_back(temp);
    return strVector;
}

std::vector<Vector2> CreateLineFromString(std::string& strLine)
{
    auto directionList = SplitString(strLine);
    auto lastPoint = Vector2(0,0);
    std::vector<Vector2> outputList;
    for(std::string dir : directionList)
    {
        std::string direction = dir.substr(0, 1);
        int value = std::stoi(dir.substr(1, std::string::npos));
        
        if(direction == DIR_UP)
        {
            lastPoint.y += value;
        }
        else if(direction == DIR_DOWN)
        {
            lastPoint.y -= value;
        }
        else if(direction == DIR_RIGHT)
        {
            lastPoint.x += value;
        }
        else if(direction == DIR_LEFT)
        {
            lastPoint.x -= value;
        } 
        outputList.push_back(lastPoint);
    }
    return outputList;
}

std::vector<Vector2> FindIntersectionPoints(const std::vector<Vector2>& lineOne, const std::vector<Vector2>& lineTwo)
{
    std::vector<Vector2> intersectionPoints;
    for(Vector2 point : lineOne)
    {
        for(Vector2 pointTwo : lineTwo)
        {
            if(point.x == pointTwo.x && point.y == pointTwo.y)
            {
                std::cout << "intersection" << std::endl;
                intersectionPoints.push_back(point);
            }
        }
    }
    return intersectionPoints;
}

void RunProblemOne()
{
    std::vector<std::string> strLines;
    GetFileContent("day3/input.txt", strLines);
    auto lineOne = CreateLineFromString(strLines[0]);
    auto lineTwo = CreateLineFromString(strLines[1]);
    auto intersectionPoints = FindIntersectionPoints(lineOne, lineTwo);
    for(auto point : intersectionPoints)
    {
        std::cout << point.x << " " << point.y << std::endl;
    }

}

void RunProblemTwo()
{

}

#endif