1) Alec Radford and Amanda Lee

2) It's python, numpy is the only current dependency

3) The current example will create random functions of the form:
y = mx + b and find the parameters via tabu search

4) Example output from a run on my computer:

Current function: y = -6674x + 3135

SOLUTION FOUND
Found slope -6674
Found offset 3135
In 185317 checks
In 4.64 seconds
Efficiency Ratio: 539.62

Current function: y = -944x + -9428

SOLUTION FOUND
Found slope -944
Found offset -9428
In 108636 checks
In 2.70 seconds
Efficiency Ratio: 920.51

Current function: y = 3220x + -8095

SOLUTION FOUND
Found slope 3220
Found offset -8095
In 162133 checks
In 4.06 seconds
Efficiency Ratio: 616.78

Current function: y = -5135x + 3848

SOLUTION FOUND
Found slope -5135
Found offset 3848
In 159799 checks
In 3.99 seconds
Efficiency Ratio: 625.79

Current function: y = -7054x + 9759

SOLUTION FOUND
Found slope -7054
Found offset 9759
In 267105 checks
In 6.85 seconds
Efficiency Ratio: 374.38

Current function: y = -4993x + 6594

SOLUTION FOUND
Found slope -4993
Found offset 6594
In 186916 checks
In 4.76 seconds
Efficiency Ratio: 535.00

Current function: y = -9568x + -5027

SOLUTION FOUND
Found slope -9568
Found offset -5027
In 160408 checks
In 4.05 seconds
Efficiency Ratio: 623.41

Current function: y = 4026x + -6664

SOLUTION FOUND
Found slope 4026
Found offset -6664
In 164526 checks
In 4.15 seconds
Efficiency Ratio: 607.81

Current function: y = 7573x + -5372

SOLUTION FOUND
Found slope 7573
Found offset -5372
In 230214 checks
In 5.85 seconds
Efficiency Ratio: 434.38

Current function: y = -9951x + 4886

SOLUTION FOUND
Found slope -9951
Found offset 4886
In 279882 checks
In 7.10 seconds
Efficiency Ratio: 357.29

5) Tabu search is a really elegant augmentation of our original local random stochastic search code which provides a convergence garuntee (in worst case it degenerates to brute force search) and is a great optimization heuristic to get out of local minimum which was the problem we encountered before.

The way it works is it remembers its history of hypothesis it has visited before and will never choose to transition to a hypothesis it has visited before. Thus, whenever a local minimum is encountered, it will visit all locations in that minima thus "filling it" and spilling out to visit other areas that it has not visited before.

The efficiency ratio is a number of hypothesis evalutations tabu search took to find the underlying function compared to brute force search of the current function space. Tabu search can work on an unbounded space, but I'm currently generating functions on a bounded domain of -10k to 10k for time reasons. The average efficiency ratio is 500 right now which should only go up as the functions we can learn become more complex and the search space begins to exponentially grow.

6) We now need to expand the complexity of functions to be learned and start looking into alternative ways to learn them besides search solutions.