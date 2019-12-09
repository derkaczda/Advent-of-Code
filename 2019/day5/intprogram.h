#ifndef INTPROGRAM_H
#define INTPROGRAM_H

#include "../utils.h"

#include <algorithm>
#include <sstream>
#include <stack>

#define OPCODE_ADD 1
#define OPCODE_MUL 2
#define OPCODE_END 99
#define OPCODE_SAVE 3
#define OPCODE_OUTPUT 4

#define MODE_POSITION 0
#define MODE_IMMEDIATE 1

class IntProgram
{
private:
    struct InstructionParameter
    {
        int value;
        int mode;
    };
    struct Instruction
    {
        int opcode;
        InstructionParameter params[3];
        int parameterSize;
    };
public:

    IntProgram(const std::string& filepath)
    {
        m_ProgramSource = filepath;
        m_InstructionPointer = 0;
        LoadProgram();
    }

    void Run()
    {
        bool programRunning = true;
        while(programRunning)
        {
            LoadNextInstruction();
            IntProgram::PrintInstruction(m_CurrentInstruction);
            //std::cout << "Instruction opcode: " << m_CurrentInstruction.opcode << " parameters " << m_CurrentInstruction.parameterSize << std::endl;
            programRunning = false;

            if(m_CurrentInstruction.opcode == OPCODE_ADD)
            {
                int valueOne = GetParameterValue(m_CurrentInstruction.params[0]);
                int valueTwo = GetParameterValue(m_CurrentInstruction.params[1]);
                int savePosition = m_CurrentInstruction.params[2].value;
                m_Memory[savePosition] = valueOne + valueTwo;
            }
            else if(m_CurrentInstruction.opcode == OPCODE_MUL)
            {
                int valueOne = GetParameterValue(m_CurrentInstruction.params[0]);
                int valueTwo = GetParameterValue(m_CurrentInstruction.params[1]);
                int savePosition = m_CurrentInstruction.params[2].value;
                m_Memory[savePosition] = valueOne * valueTwo;
            }
            else if(m_CurrentInstruction.opcode == OPCODE_END)
            {
                programRunning = false;
                continue;
            }

            m_InstructionPointer += m_CurrentInstruction.parameterSize;
        }  
    }

public:

    static void PrintInstruction(const Instruction& instruction)
    {
        std::string opcode;
        if(instruction.opcode == OPCODE_MUL)
            opcode = "MUL";
        else if(instruction.opcode == OPCODE_ADD)
            opcode = "ADD";
        else if(instruction.opcode == OPCODE_END)
            opcode = "END";
        else if(instruction.opcode == OPCODE_OUTPUT)
            opcode = "OUTPUT";
        else if(instruction.opcode == OPCODE_SAVE)
            opcode = "SAVE";
        else
            opcode = "UNKNOWN";

        std::cout << "OPCODE: " << opcode << std::endl;

        for(int i = 0; i < instruction.parameterSize; i++)
        {
            std::string mode;
            if (instruction.params[i].mode == MODE_POSITION)
                mode = "POSITION";
            else if(instruction.params[i].mode == MODE_IMMEDIATE)
                mode = "IMMEDIATE";
            else
                mode = "UNKNOWN";
            
            std::cout << "PARAM " << i;
            std::cout << " MODE: " << mode << " VALUE: " << instruction.params[i].value << std::endl;
        }
        
    }

private:

    void LoadProgram()
    {
        std::vector<std::string> lines;
        bool result = GetFileContent(m_ProgramSource, lines);

        if(!result)
        {
            std::cerr << "Reading file went wrong" << std::endl;
        }

        std::string program = lines[0];
        std::replace(program.begin(), program.end(), ',', ' ');

        std::stringstream ss(program);
        int temp;
        while(ss >> temp)
            m_Memory.push_back(temp);
    }

    std::vector<int> SplitNumber(int number)
    {
        std::vector<int> splitDigits;
        while(number > 0)
        {
            int digit = number % 10;
            number /= 10;
            splitDigits.push_back(digit);
        }
        return splitDigits;
    }

    void LoadNextInstruction()
    {
        auto splitDigits = SplitNumber(m_Memory[m_InstructionPointer]);
        int parameterCount = 0;
        for(int i = 0; i < splitDigits.size(); i++)
        {
            if(i == 0)
            {
                m_CurrentInstruction.opcode = splitDigits[i];
            }
            else
            {
                InstructionParameter param;
                param.mode = splitDigits[i];
                param.value = m_Memory[m_InstructionPointer + parameterCount + 1];
                m_CurrentInstruction.params[parameterCount] = param;
                parameterCount++;
            }  
        }
        m_CurrentInstruction.parameterSize = parameterCount;
    }

    int GetParameterValue(InstructionParameter parameter)
    {
        if(parameter.mode == MODE_IMMEDIATE)
            return parameter.value;
        else if(parameter.mode == MODE_POSITION)
            return m_Memory[parameter.value];
    }

private:
    std::string m_ProgramSource;
    std::vector<int> m_Memory;
    int m_InstructionPointer;
    Instruction m_CurrentInstruction;
    
};

// struct Instruction
// {
//     struct InstructionParameter
//     {
//         int value;
//         int mode;
//     };
//     int opcode;
//     std::vector<InstructionParameter> params;
//     // int arg1;
//     // int arg2;
//     // int dest;
// };

// void CreateProgramMemory(std::vector<int>& memory)
// {
//     std::vector<std::string> lines;
//     bool result = GetFileContent("day5/input.txt", lines);

//     if(!result)
//     {
//         std::cerr << "Reading file went wrong" << std::endl;
//     }

//     std::string program = lines[0];
//     std::replace(program.begin(), program.end(), ',', ' ');

//     std::stringstream ss(program);
//     int temp;
//     while(ss >> temp)
//         memory.push_back(temp);
// }

// void IncreaseProgramCounter(int& programCounter)
// {
//     programCounter += 4;
// }

// Instruction GetInstruction(const std::vector<int>&memory, const int& programCounter)
// {
//     Instruction inst;

//     // inst.opcode = memory[programCounter];
//     // inst.arg1 = memory[programCounter + 1];
//     // inst.arg2 = memory[programCounter + 2];
//     // inst.dest = memory[programCounter + 3];
//     return inst;
// }

// int RunProgram(int noun, int verb)
// {
//     std::vector<int> memory;
//     CreateProgramMemory(memory);

//     // Fix program
//     memory[1] = noun;
//     memory[2] = verb;

//     int programCounter = 0;
//     bool programRunning = true;
//     while(programRunning)
//     {
//         Instruction inst = GetInstruction(memory, programCounter);
//         if(inst.opcode == OPCODE_ADD)
//         {
//             memory[inst.dest] = memory[inst.arg1] + memory[inst.arg2];
//         }
//         else if(inst.opcode == OPCODE_MUL)
//         {
//             memory[inst.dest] = memory[inst.arg1] * memory[inst.arg2];
//         }
//         else if(inst.opcode == OPCODE_END)
//         {
//             programRunning = false;
//             continue;
//         }

//         IncreaseProgramCounter(programCounter);
//     }

//     return memory[0];
// }

#endif