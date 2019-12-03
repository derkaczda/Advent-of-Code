#if ADVENT_OF_CODE_2019_DAY == 1
    #include "day1/day1.h"
#endif

void PrintHeader(int numberOfDay)
{
    std::cout << "Advent of Code 2019" << "\n";
    std::cout << "Running Day " << numberOfDay << "\n";
    std::cout << "\n" << "\n";
}

void PrintProblemHeader(int problemNumber)
{
    std::cout << "Running Problem" << problemNumber << "\n";
    std::cout << "\n" << "\n";
}

void run()
{
    PrintHeader(ADVENT_OF_CODE_2019_DAY);
    if (PROBLEM == 1)
    {
        PrintProblemHeader(PROBLEM);
        RunProblemOne();
    }
    else if (PROBLEM == 2)
    {
        PrintProblemHeader(PROBLEM);
        RunProblemTwo();
    }
    else if(PROBLEM == 0)
    {
        PrintProblemHeader(1);
        RunProblemOne();
        PrintProblemHeader(2);
        RunProblemTwo();
    }
    getchar();
}