#ifndef DAY2_H
#define DAY2_H

#include "../utils.h"

#include <algorithm>
#include <sstream>

#define OPCODE_ADD 1
#define OPCODE_MUL 2
#define OPCODE_END 99

struct Instruction
{
    int opcode;
    int arg1;
    int arg2;
    int dest;
};

void CreateProgramMemory(std::vector<int>& memory)
{
    std::vector<std::string> lines;
    bool result = GetFileContent("day2/input.txt", lines);

    if(!result)
    {
        std::cerr << "Reading file went wrong" << std::endl;
    }

    std::string program = lines[0];
    std::replace(program.begin(), program.end(), ',', ' ');

    std::stringstream ss(program);
    int temp;
    while(ss >> temp)
        memory.push_back(temp);
}

void IncreaseProgramCounter(int& programCounter)
{
    programCounter += 4;
}

Instruction GetInstruction(const std::vector<int>&memory, const int& programCounter)
{
    Instruction inst;
    inst.opcode = memory[programCounter];
    inst.arg1 = memory[programCounter + 1];
    inst.arg2 = memory[programCounter + 2];
    inst.dest = memory[programCounter + 3];
    return inst;
}

int RunProgram(int noun, int verb)
{
    std::vector<int> memory;
    CreateProgramMemory(memory);

    // Fix program
    memory[1] = noun;
    memory[2] = verb;

    int programCounter = 0;
    bool programRunning = true;
    while(programRunning)
    {
        Instruction inst = GetInstruction(memory, programCounter);
        if(inst.opcode == OPCODE_ADD)
        {
            memory[inst.dest] = memory[inst.arg1] + memory[inst.arg2];
        }
        else if(inst.opcode == OPCODE_MUL)
        {
            memory[inst.dest] = memory[inst.arg1] * memory[inst.arg2];
        }
        else if(inst.opcode == OPCODE_END)
        {
            programRunning = false;
            continue;
        }

        IncreaseProgramCounter(programCounter);
    }

    return memory[0];
} 

void RunProblemOne()
{
    int answer = RunProgram(12, 2);
    std::cout << "Value at position 0 after program halts: " << answer << std::endl;
}

void RunProblemTwo()
{

}

#endif