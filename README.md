DNA and Population Growth Analysis

Overview
This project contains basic Python functions to analyze DNA sequences, simulate population growth, and compute string similarity. It is designed for beginners, using only fundamental Python constructs without external libraries.

Features
1. DNA to Protein Translation**: Converts a DNA sequence into its corresponding protein sequence.
2. Logistic Growth Simulation**: Models population growth using a logistic function.
3. Generate Growth Curves**: Creates multiple population growth curves with varied initial conditions.
4. Time to 80% Maximum Growth**: Determines the time required for a population to reach 80% of its carrying capacity.
5. Hamming Distance Calculation**: Computes the difference between two strings (e.g., usernames) by counting character mismatches.

Usage

1. DNA to Protein Translation
```python
protein = translate_dna("ATGCGTACGTTAG")
print("Protein:", protein)
```

2. Logistic Growth Simulation
```python
population = logistic_growth(10, 1000, 10, 0.1)
print("Population size at time 10:", population)
```

3. Generate Growth Curves
```python
growth_data = generate_growth_curves(5, 10)  # 5 curves over 10 time steps
print("Sample Growth Data:", growth_data[:2])
```

4. Time to Reach 80% of Maximum Growth
```python
time_needed = time_to_80_percent(1000, 10, 0.1)
print("Time to 80% carrying capacity:", time_needed)
```

5. Hamming Distance Calculation
```python
distance = hamming_distance("SlackUser", "TwitterHandle")
print("Hamming Distance:", distance)
```

Notes
- The DNA translation function stops at a stop codon (`TAA`, `TAG`, `TGA`).
- The logistic growth model assumes an exponential approach to the carrying capacity.
- The Hamming distance function pads shorter strings with spaces.

Author
This project is a beginner-friendly implementation of biological and computational concepts using Python.

