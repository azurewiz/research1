Exploring Emergent Phenomena in a Modified Cellular Automaton
Abstract:
This project investigates how such minor modifications to the classical rules of Conway’s Game of Life can lead to unexpected emergent behaviours and patterns. By introducing a probabilistic element into the standard model, this study compares the dynamics of the modified automaton with the traditional version, revealing insights into population stability, chaotic patterns, and system resilience and stability.
Introduction:
Cellular automata have long served as a model for understanding complex systems. The classic Conway’s Game of Life demonstrates how simple rules can generate intricate patterns. In this study, we modify the birth rule by introducing a small, random chance for dead cells to become alive. This change is designed to simulate external stochastic influences and observe how it impacts the system’s dynamics.
Methodology:
•	Model Setup:
A grid of size nxn where n = 50 is initialized with a randomized distribution of alive (1) and dead (0) cells, with a 20% probability for the cell to start as alive.
•	Simulation Parameters:
The two simulations are conducted over 100 iterations:
1.	Standard Model: Utilizes the original rules of Conway’s Game of Life.
2.	Modified Model: In addition to the standard rules, dead cells have a 10% chance to be alive at each step.
•	Data Collection:
The evolution of the grid is recorded for each iteration. Key observations include the final state of the grid, overall population trends, and the emergence of patterns.
•	Visualization:
Final states of both simulations are visualized using Matplotlib. These images provide a visual comparison between the standard and modified models.
Results:
•	Standard Model:
The grid evolution under standard rules yielded predictable oscillatory and stable configurations typical of Conway’s Game of Life.
•	Modified Model:
The introduction of a probabilistic element resulted in more dynamic behaviour, including sporadic bursts of activity and prolonged periods of apparent chaos, highlighting the sensitivity of cellular automata to rule modifications.
•	Github repo:  https://github.com/azurewiz/research1
Conclusion:
This study confirms that incorporating randomness into deterministic systems like cellular automata can result in complex emergent behaviour. The observed differences between the standard and modified models provide a basis for future research into the interplay between determinism and stochasticity in complex systems. Further work could extend this analysis to larger grids, varied probabilities, or other rule modifications.
Future Work:
•	Experiment with different grid sizes and longer simulation durations.
•	Explore the impact of varying the spontaneous birth probability.
•	Investigate other modifications (e.g., probabilistic death) and their effects on emergent behaviour.
References:
•	Conway’s Game of Life – Wikipedia
