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
		int savePos = params[2].value; //  (2, memory);
        memory[savePos] = valueOne + valueTwo;
        instructionPointer += GetParamLength() + 1;
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
		int savePos = params[2].value; //GetParameterValueAtPosition(2, memory);
        memory[savePos] = valueOne * valueTwo;
        instructionPointer += GetParamLength() + 1;
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
		int pos = params[0].value; //GetParameterValueAtPosition(0, memory);
        memory[pos] = input;
        instructionPointer += GetParamLength() + 1;
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
        std::cout << "OUTPUT: " << GetParameterValueAtPosition(0, memory) << std::endl;
        instructionPointer += GetParamLength() + 1;
        return true;
    }
};

class JumpIfTrueInstruction : public Instruction 
{
public:
    JumpIfTrueInstruction()
        : Instruction("JumpIfTrue", 5, 2)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        if(GetParameterValueAtPosition(0, memory) != 0)
            instructionPointer = GetParameterValueAtPosition(1, memory);
        else
            instructionPointer += GetParamLength() + 1;
        return true;
    }
};

class JumpIfFalseInstruction : public Instruction 
{
public:
    JumpIfFalseInstruction()
        : Instruction("JumpIfFalse", 6, 2)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        if(GetParameterValueAtPosition(0, memory) == 0)
            instructionPointer = GetParameterValueAtPosition(1, memory);
        else
            instructionPointer += GetParamLength() + 1;
        return true;
    }
};

class LessThanInstruction : public Instruction
{
public:
    LessThanInstruction()
        : Instruction("LessThan", 7, 3)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        int valueOne = GetParameterValueAtPosition(0, memory);
        int valueTwo = GetParameterValueAtPosition(1, memory);
        int savePos = params[2].value;
        int saveValue = 0;
        if(valueOne < valueTwo)
            saveValue = 1;
        memory[savePos] = saveValue;
        instructionPointer += GetParamLength() + 1;
        return true;
    }
};

class EqualInstruction : public Instruction
{
public:
    EqualInstruction()
        : Instruction("Equal", 8, 3)
    {}

    virtual bool DoInstruction(std::vector<int>& memory, int& instructionPointer) override
    {
        int valueOne = GetParameterValueAtPosition(0, memory);
        int valueTwo = GetParameterValueAtPosition(1, memory);
        int savePos = params[2].value;
        int saveValue = 0;
        if(valueOne == valueTwo)
            saveValue = 1;
        memory[savePos] = saveValue;
        instructionPointer += GetParamLength() + 1;
        return true;
    }
};



#endif
