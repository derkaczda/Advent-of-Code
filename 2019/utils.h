#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <fstream>
#include <iostream>
#include <string>

bool GetFileContent(const std::string& filepath, std::vector<std::string>& lines)
{
    std::ifstream in(filepath.c_str());

    if(!in)
    {
        std::cerr << "Cannot open the File: " << filepath << std::endl;
        return false;
    }

    std::string str;
    while(std::getline(in, str))
    {
        if(str.size() > 0)
        {
            lines.push_back(str);
        }
    }

    in.close();
    return true;
}

#endif