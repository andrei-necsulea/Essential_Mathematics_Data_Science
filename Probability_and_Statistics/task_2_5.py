'''
Flipping a coin is a commonly used example of a simple probability experiment.
Let's assume that you have a fair,
two-sided coin, the possible outcomes are heads (H) and tails (T), as shown below:

Each of two possible outcomes of an experiment has an equal likelihood of occuring, ie. P(H)=P(T)=1/2.

Perform a trial by flipping a virtual coin n times, where n∈{10,100,1000,1000000},
and count how many times we get heads.
See, if the expected number of heads is equal to the number you get in each trial.
Which results are the closest to the ideal number?

Additionally, you can generate barplots with results for each trial. Use f-strings to adjust plot titles.
'''

import random
import matplotlib.pyplot as plt

def  coin_flipping(flippings):
    times_h = []
    for n in flippings:
        no_times_h = 0
        for _ in range(n):
            flip = random.choice(['H' , 'T'])
            if flip == 'H':
                no_times_h += 1
        expected_times_h = n/2
        times_h.append(no_times_h)
        print(f"For {n} flips: Got {no_times_h} heads (Expected: {expected_times_h}).")

    plt.figure(figsize=(10, 6))
    heights = [5000, 25000, 50000, 100000]
    plt.bar(x = [str(n) for n in flippings] , height=heights)
    plt.yticks(ticks=heights, labels=times_h)
    plt.axhline(y=0, color='black')
    plt.title("Number of Heads for Different Number of Flips")
    plt.xlabel("Number of Flips")
    plt.ylabel("Heads Count")
    plt.tight_layout()
    plt.show()

n_flippings = [10, 100, 1000, 1000000]
coin_flipping(n_flippings)