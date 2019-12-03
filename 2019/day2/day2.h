#ifndef DAY2_H
#define DAY2_H

#include "intprogram.h" 

void RunProblemOne()
{
    int answer = RunProgram(12, 2);
    std::cout << "Value at position 0 after program halts: " << answer << std::endl;
}

void RunProblemTwo()
{
    int needed_result = 19690720;
    bool found = false;
    int noun,verb;
    for(noun = 0; noun <= 99; noun++)
    {
        for(verb = 0; verb <= 99; verb++)
        {
            int answer = RunProgram(noun, verb);
            if (answer == needed_result)
            {
                found = true;
                break;
            }
        }

        if (found)
            break;
    }

    std::cout << "The noun is: " << noun << " the verb is: " << verb << std::endl;
    std::cout << "100*noun + verb is: " << (100 * noun) + verb << std::endl;
}

#endif