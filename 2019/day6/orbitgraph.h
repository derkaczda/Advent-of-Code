#ifndef ORBITGRAPH_H
#define ORBITGRAPH_H

#include "../utils.h"

#include <memory>
#include <algorithm>
#include <sstream>

struct OrbitObject
{
    std::string name;
    int orbitCount;
    OrbitObject* parent;
};

class OrbitGraph
{
public:
    OrbitGraph(const std::string& filepath)
    {
        std::vector<std::string> graphInput;
        LoadInput(filepath, graphInput);
        ConstructGraph(graphInput);
        CalculateOrbitCount();
    }

    int GetTotalOrbitCount() { return m_TotalOrbitCount; }

private:
    void LoadInput(const std::string& filepath, std::vector<std::string>& input)
    {
        bool result = GetFileContent(filepath, input);

        if(!result)
        {
            std::cerr << "Reading file went wrong" << std::endl;
        }
    }

    void ConstructGraph(const std::vector<std::string>& graphInput)
    {
        for(std::string input : graphInput)
        {
            std::string first = input.substr(0, 3);
            std::string second = input.substr(4, 3);
            auto parentObject = GetOrbitObjectByName(first);
            auto otherObject = GetOrbitObjectByName(second);
            
            if(parentObject == nullptr)
            {
                parentObject = new OrbitObject();
                parentObject->name = first;
                parentObject->parent = nullptr;
                m_OrbitObjects.push_back(parentObject);
            }

            if(otherObject == nullptr)
            {
                otherObject = new OrbitObject();
                otherObject->name = second;
                m_OrbitObjects.push_back(otherObject);
            }
            
            otherObject->parent = parentObject;
        }
    }

    OrbitObject* GetOrbitObjectByName(const std::string& name)
    {
        for(OrbitObject* obj : m_OrbitObjects)
        {
            if(obj->name == name)
                return obj;
        }

        return nullptr;
    }

    void CalculateOrbitCount()
    {
        m_TotalOrbitCount = 0;
        for(OrbitObject* obj : m_OrbitObjects)
        {
            int count = 0;
            OrbitObject* parent = obj->parent;
            while(parent != nullptr)
            {
                count++;
                parent = parent->parent;
            }

            obj->orbitCount = count;
            m_TotalOrbitCount += count;
        }
    }

private:
    std::vector<OrbitObject*> m_OrbitObjects;
    int m_TotalOrbitCount;
};

#endif