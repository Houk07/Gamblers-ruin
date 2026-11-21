def ruin_theory(start, N, p):
    if p == 0.5 :
        return 1 - start/N

    q = 1 - p
    return ( (q/p)**N - (q/p)**start )/((q/p)**N - 1)
    
