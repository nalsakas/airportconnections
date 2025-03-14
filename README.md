# Airport Connections
Determine minimum number of missing connections

## Problem Statement:
Returns minimum number of routes that should be added for a given start airport in to the routes table,
such that all other airpots can be reached if a passenger wants to travel from starting airport.
There are no constraint on number of connections that a passenger can take.

Input: "LGA"
Output: 3

## Solution:
A dfs algorithm will determine all reachable airports including connections for a  given start airport.
Then this set will be checked aganist for all sets of all airports individually. Missing connections will be added based on
a sort algirithms. The airport with max difference sorted first. THis way number of connections needs to be added would be minimized.
If we add at least 3 more routes to the starting airport "LGA", in to the routes table, then all other airports will be
reachable from "LBA".