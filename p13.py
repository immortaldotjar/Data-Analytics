import numpy as np

n = int(input("Enter number of categories: "))

observed = []
expected = []

for i in range(n):
    o = float(input(f"Enter Observed Frequency {i+1}: "))
    e = float(input(f"Enter Expected Frequency {i+1}: "))

    print("\n")
    observed.append(o)
    expected.append(e)

observed = np.array(observed)
expected = np.array(expected)

chi_square = np.sum(((observed - expected) ** 2) / expected)

print(f"Observed Frequencies : {observed}")
print(f"Expected Frequencies : {expected}")
print(f"\nChi-Square Value = {chi_square:.4f}")