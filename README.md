# optimization_of_first_search
A maze searcher that first searches the area for a goal and then optimizes the known route to get there.

Intro:
An [n,n] sized maze is introduced to a solver. 
The solver will have a start position and will only know it has reached a goal when the goal is reached.
The solver can only move up, down, right and left.

Solution:
1. Let the solver roam freely, trying it's best to avoid going to places it has already been to.
  1.1 Small algorithm that looks if the solver has been to a neighbouring space alreadu.
2. Add a stepcount to each space the solver arrives at (all stepcounts = 0 at start). 
  2.1 This will be the smallest of the adjacent spaces stepcounts + 1.
3. When the goal is found, backtrack to the start from the goal by selecting each space's smallest adjacent neighbour's stepcount.

Conclusion:
The solver does not find a perfect optimum when getting the solution since one needs all data of available space to do this.
It does find the shortest route from the space that it has found "walkable".
