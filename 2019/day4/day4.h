#ifndef DAY4_H
#define DAY4_H

#include "../utils.h"
#include <stack>

std::stack<int> SplitNumber(int number)
{
    std::stack<int> splitDigits;
    while(number > 0)
    {
        int digit = number % 10;
        number /= 10;
        splitDigits.push(digit);
    }
    return splitDigits;
}

std::vector<int> GetPossiblePasswordsInRange(int min, int max)
{
    std::vector<int> possiblePaswords;
    for(int password = min; password <= max; password++)
    {
        auto splitDigits = SplitNumber(password);
        int lastDigit = -1;
        bool doubleDigits = false, increasingDigits = true;
        while(!splitDigits.empty())
        {
            int digit = splitDigits.top();

            if(digit < lastDigit)
            {
                increasingDigits = false;
                break;
            }

            if(digit == lastDigit)
            {
                doubleDigits = true;
            }

            splitDigits.pop();
            lastDigit = digit;
        }

        if(doubleDigits && increasingDigits)
        {
            possiblePaswords.push_back(password);
        }
    }

    return possiblePaswords;
}

void RunProblemOne()
{
    int minPassword = 156218;
    int maxPassword = 652527;

    auto passwords = GetPossiblePasswordsInRange(minPassword, maxPassword);
    std::cout << "There are " << passwords.size() << " different passwords" << std::endl;
}

void RunProblemTwo()
{

}

#endif