#if ADVENT_OF_CODE_2019_DAY == 1
    #include "day1/day1.h"
#endif

void PrintHeader(int numberOfDay)
{
    std::cout << "Advent of Code 2019" << "\n";
    std::cout << "Running Day " << numberOfDay << "\n";
    std::cout << "\n" << "\n";
}

void run()
{
    PrintHeader(ADVENT_OF_CODE_2019_DAY);
    RunDay();
    getchar();
}