import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# --- Load data ---
df = pd.read_excel("hyster4.xlsx", sheet_name="Sheet1")
df.columns = df.columns.str.lower()
df = df.rename(columns={'voltage': 'V', 'displacement': 'x'})


# --- Positive and negative voltage sections ---
pos = df[df['V'] > 0]
neg = df[df['V'] < 0]

# --- n1: from start to max displacement in +V ---
n1_min_idx = pos['x'].idxmin()
n1 = df.loc[:n1_min_idx]

# --- p1: from min displacement in +V to V ≈ 0 ---
try:
    p1_max_idx = pos['x'].idxmax()  #Find the row index in the pos DataFrame where the displacement x is at its minimum
    p1_end_idx = df[(df.index > p1_max_idx) & (df['V'] < 0.1)].index[0]
    p1 = df.loc[p1_max_idx:p1_end_idx]
except IndexError:
    p1 = pd.DataFrame()
    print("⚠️ Could not find full n1 region.")

# --- p2: from 0 V to max displacement in -V ---
try:
    p2_start_idx = neg[neg['V'] < -0.1].index[0]
    p2_min_idx = neg['x'].idxmin()
    p2 = df.loc[p2_start_idx:p2_min_idx]
except IndexError:
    p2 = pd.DataFrame()
    print("⚠️ Could not find n2 region.")

# --- n2: from min displacement in -V to end ---
try:
    n2_max_idx = neg['x'].idxmax()
    n2 = df.loc[n2_max_idx:]
except IndexError:
    n2 = pd.DataFrame()
    print("⚠️ Could not find p2 region.")

# --- Linear fit function ---
def calc_d33(region, label):
    if region.empty:
        print(f"{label} region is empty. Skipping.")
        return None, region
    slope, _, _, _, _ = linregress(region['V'], region['x'])
    d33 = slope * 1e3  # nm/V to pm/V
    print(f"{label} d33: {d33:.2f} pm/V")
    return slope, region

# --- Calculate all d33 values ---
s_p1, p1 = calc_d33(p1, "p1")
s_n1, n1 = calc_d33(n1, "n1")
s_n2, n2 = calc_d33(n2, "n2")
s_p2, p2 = calc_d33(p2, "p2")

print(f"average positive d33: {((s_p1+s_p2)*1000/2):.2f}")
print(f"average negative d33: {((s_n1+s_n2)*1000/2):.2f}")

# --- Plot the results ---
plt.figure(figsize=(10, 6))
plt.plot(df['V'], df['x'], color='lightgray', label='Full loop')

if not p1.empty: plt.plot(p1['V'], p1['x'], 'b.', label='p1')
if not n1.empty: plt.plot(n1['V'], n1['x'], 'r.', label='n1')
if not n2.empty: plt.plot(n2['V'], n2['x'], 'g.', label='n2')
if not p2.empty: plt.plot(p2['V'], p2['x'], 'm.', label='p2')

plt.xlabel("Voltage (V)")
plt.ylabel("Displacement (nm)")
plt.title("Butterfly Loop with p1, n1, n2, p2 Regions")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()