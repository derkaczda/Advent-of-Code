#ifndef INSTRUCTION_H
#define INSTRUCTION_H

#include <string>
#include <vector>
#include <iostream>

#define MODE_POSITION 0
#define MODE_IMMEDIATE 1

struct InstructionParameter
{
    int value;
    int mode;
};

class Instruction
{
public:
    Instruction(const std::string& name, 
                int opcode, int paramLength)
        : m_opcode(opcode), m_paramLength(paramLength),
          m_Name(name)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) = 0;

    void SetParameterAtPosition(int position, InstructionParameter param)
    {
        params[position] = param;
    }

    int GetOpcode() { return m_opcode; }
    int GetParamLength() { return m_paramLength; }

    InstructionParameter GetParameter(int number) {return params[number];}

protected:
    int GetParameterValueAtPosition(int pos, const std::vector<int>& memory)
    {
        return params[pos].mode == MODE_IMMEDIATE ? params[pos].value : memory[params[pos].value];
    }

private:
    std::string m_Name;
    int m_opcode;
    int m_paramLength;
protected:
    InstructionParameter params[3];
};

class AddInstruction : public Instruction
{
public:
    AddInstruction()
        : Instruction("ADD", 1, 3)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        int valueOne = GetParameterValueAtPosition(0, memory);
        int valueTwo = GetParameterValueAtPosition(1, memory);
        int savePos = GetParameterValueAtPosition(2, memory);
        memory[savePos] = valueOne + valueTwo;
        return true;
    }
};

class EndInstruction : public Instruction
{
public:
    EndInstruction()
        : Instruction("END", 99, 0)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        return false;
    }
};

class MultiplyInstruction : public Instruction
{
public:
    MultiplyInstruction()
        : Instruction("MUL", 2, 3)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        int valueOne = GetParameterValueAtPosition(0, memory);
        int valueTwo = GetParameterValueAtPosition(1, memory);
        int savePos = GetParameterValueAtPosition(2, memory);
        memory[savePos] = valueOne * valueTwo;
        return true;
    }
};

class SaveInstruction : public Instruction
{
public:
    SaveInstruction()
        : Instruction("SAVE", 3, 1)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        std::cout << "Input number: ";
        int input;
        std::cin >> input;
        memory[GetParameterValueAtPosition(0, memory)] = input;
        return true;
    }
};

class OutputInstruction : public Instruction
{
public:
    OutputInstruction()
        : Instruction("OUTPUT", 4, 1)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        std::cout << "OUTPUT: " << memory[GetParameterValueAtPosition(0, memory)] << std::endl;
        return true;
    }
};

#endif
