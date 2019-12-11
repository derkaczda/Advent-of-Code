#ifndef INTPROGRAM_IMPROVED_H
#define INTPROGRAM_IMPROVED_H

#include "../utils.h"

#include "instruction.h"

#include <algorithm>
#include <sstream>
#include <stack>


class IntProgram
{
public:

    IntProgram(const std::string& sourcePath)
    {
        LoadProgram(sourcePath);

        m_Instructions.push_back(new AddInstruction());
        m_Instructions.push_back(new EndInstruction());
        m_Instructions.push_back(new MultiplyInstruction());
        m_Instructions.push_back(new SaveInstruction());
        m_Instructions.push_back(new OutputInstruction());
		m_Instructions.push_back(new JumpIfTrueInstruction());
		m_Instructions.push_back(new JumpIfFalseInstruction());
        m_Instructions.push_back(new LessThanInstruction());
        m_Instructions.push_back(new EqualInstruction());
    }

    void Run()
    {
        bool programRunning = true;
        while(programRunning)
        {
            Instruction* inst = NextInstruction();
            programRunning = inst->DoInstruction(m_Memory, m_InstructionPointer);
			//m_InstructionPointer += inst->GetParamLength() + 1;
        }
    }

private:

    void LoadProgram(const std::string& sourcePath)
    {
        std::vector<std::string> lines;
        bool result = GetFileContent(sourcePath, lines);

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

    Instruction* FindInstructionWithOpCode(int opcode, int opcodeTwo)
    {
		int code = opcode;
		if(opcodeTwo != 0)
			code = std::stoi(std::to_string(opcodeTwo) + std::to_string(opcode));

        for(Instruction* inst : m_Instructions)
        {
            if(inst->GetOpcode() == code)
                return inst;
        }
    }

    Instruction* NextInstruction()
    {
        auto splitDigits = SplitNumber(m_Memory[m_InstructionPointer]);
		Instruction* instruction;
		if (splitDigits.size() > 1)
			instruction = FindInstructionWithOpCode(splitDigits[0],splitDigits[1]);
		else
			instruction = FindInstructionWithOpCode(splitDigits[0], 0);
        for(int i = 0; i < instruction->GetParamLength(); i++)
        {
            InstructionParameter param;
            if(i + 2 >= splitDigits.size())
                param.mode = MODE_POSITION;
            else
                param.mode = splitDigits[i + 2];
            param.value = m_Memory[m_InstructionPointer + i + 1];
            instruction->SetParameterAtPosition(i, param);
        }
        return instruction;
    }

private:
    int m_InstructionPointer = 0;
    std::vector<int> m_Memory;
    std::vector<Instruction*> m_Instructions;
};

#endif