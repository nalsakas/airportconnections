# Airport Connections
Determine minimum number of missing connections that should be added tot the routing table of starting airport such that a passenger
can travel all other airports from starting airport. Number all connections is irrelevant. Number of connections corresponds depth of dfs.

## Problem Statement:
Returns minimum number of routes that should be added for a given start airport in to the routes table,
such that all other airports can be reached if a passenger wants to travel from starting airport.
There are no constraints on the number of connections that a passenger can take.

Input: "LGA"
Output: 3

## Solution:
A dfs algorithm will determine all reachable airports including connections for a  given start airport.
Then this set will be checked aganist for all sets of all airports individually. Missing connections will be added based on
a sort algirithm. The airport with max difference with respect to start set will be sorted first. This way number of connections needs to be added to the 
rout table will be minimized. If we add min. 3 more routes to the starting airport "LGA"'s routing table, then all other airports will be reachable from "LBA".
