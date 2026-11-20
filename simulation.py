import random
from theory import ruin_theory
import matplotlib.pyplot as plt

def play(start, N):
    
    while start < N and start > 0 :
        s = random.randint(1,2)
        if s == 1 :
            start += 1
        elif s == 2 :
            start -= 1
    return start == 0
    
def estimate_ruin(start, N, trials):
    
    count = 0
    for i in range(trials):
        if play(start, N) :
            count += 1
    return count/trials

list_1 = []
list_2 = []
for i in range(1, 20):
    list_1.append(estimate_ruin(i, 20, 10000))
    list_2.append(ruin_theory(i, 20))
 

starts = range(1, 20)
simulated = list_1
theory = list_2

plt.plot(starts, simulated, "o", label="Simulation")
plt.plot(starts, theory, label="Theory")
plt.xlabel("Starting fortune")
plt.ylabel("Probability of ruin")
plt.title("Gambler's ruin: simulation vs theory (N = 20, 10,000 trials)")
plt.xticks(range(0, 21, 5))
plt.legend()
plt.savefig("ruin.png", dpi=150)
plt.show()