import random
from theory import ruin_theory
import matplotlib.pyplot as plt

p = float(input("Probability of win ?: "))

while p >= 1 or p <= 0 :
    p = float(input("Probability of win (between 0 and 1) ?: "))


def play(start, N, p):
    
    while start < N and start > 0 :
        if random.random() < p :
            start += 1
        else :
            start -= 1

    return start == 0
    
def estimate_ruin(start, N, trials, p):
    
    count = 0
    for i in range(trials):
        if play(start, N, p) :
            count += 1
    return count/trials

list_1 = []
list_2 = []
for i in range(1, 20):
    list_1.append(estimate_ruin(i, 20, 10000, p))
    list_2.append(ruin_theory(i, 20, p))
 

starts = range(1, 20)
simulated = list_1
theory = list_2

plt.plot(starts, simulated, "o", label="Simulation")
plt.plot(starts, theory, label="Theory")
plt.xlabel("Starting fortune")
plt.ylabel("Probability of ruin")
plt.title(f"Gambler's ruin (p = {p}): simulation vs theory (N = 20, 10,000 trials)")
plt.xticks(range(0, 21, 5))
plt.legend()
plt.savefig(f"ruin_p{p}.png", dpi=150)
plt.show()