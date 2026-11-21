# Gambler's-ruin

The Gambler's ruin problem goes as follow : consider that a gambler at each play has a probability p to win 1 unit and 
probability q = 1 - p to lose 1, each play's outcome being independent of each other. The player has a fixed amount of 
units "start" at the start of the game. Depending on how the first gamble plays out, his fortune can either reach a 
fixed goal amount "N", or it can goes to 0, and the gambler would be then "ruined". 
What my code does : 
It plays a fixed "trials" amount of games (here 10 000) for each starting amount from 1 to N - 1 (here N = 20). It then 
calculate the probability of loss (how much the gambler lost over the amount of trials). It then calculates the 
probability of loss for each of those values from a theoretical formula ( in "theory.py" file ). Finally, It puts all 
the values in 2 lists and compares every probabilities for each values. With the graph, we can see that both curves (of 
the simulation and theory) have almost the same shape, as expected.


