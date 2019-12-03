#ifndef DAY3_H
#define DAY3_H

#include "../utils.h"

#include <algorithm>
#include <sstream>
#include <math.h>
#include <limits>

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
            for(int i = 1; i <= value; i++)
            {
                lastPoint.y += 1;
                outputList.push_back(lastPoint);
            }
        }
        else if(direction == DIR_DOWN)
        {
            for(int i = 1; i <= value; i++)
            {
                lastPoint.y -= 1;
                outputList.push_back(lastPoint);
            }
        }
        else if(direction == DIR_RIGHT)
        {
            for(int i = 1; i <= value; i++)
            {
                lastPoint.x += 1;
                outputList.push_back(lastPoint);
            }
        }
        else if(direction == DIR_LEFT)
        {
            for(int i = 1; i <= value; i++)
            {
                lastPoint.x -= 1;
                outputList.push_back(lastPoint);
            }
        }

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
                intersectionPoints.push_back(point);
            }
        }
    }
    return intersectionPoints;
}

int CalculateManhattenDistance(const std::vector<Vector2>& intersectionPoints)
{
    int distance = INT_MAX;
    for(auto point : intersectionPoints)
    {
        int length = abs(point.x) + abs(point.y);
        if(length < distance)
            distance = length;
    }

    return distance;
}

void RunProblemOne()
{
    std::vector<std::string> strLines;
    GetFileContent("day3/input.txt", strLines);
    auto lineOne = CreateLineFromString(strLines[0]);
    auto lineTwo = CreateLineFromString(strLines[1]);
    auto intersectionPoints = FindIntersectionPoints(lineOne, lineTwo);
    int distance = CalculateManhattenDistance(intersectionPoints);
    std::cout << "Manhatten distance is " << distance << std::endl;
}

void RunProblemTwo()
{

}

#endif