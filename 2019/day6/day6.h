#ifndef DAY6_H
#define DAY6_H

#include "orbitgraph.h"

void RunProblemOne()
{
    OrbitGraph graph("day6/input.txt");
    std::cout << "Total orbit count is " << graph.GetTotalOrbitCount() << std::endl;
}

void RunProblemTwo()
{

}

#endif