import numpy as np
import csv
import os
import matplotlib.pyplot as plt

# The file must exist at this path
file_path = os.path.join(r"\\192.168.15.45\TapeDrive", "TapeDownramp.tsv")

# Change these numbers to make the tape drive voltage curve

# User variables to set
initial_reduction_ratio = 0.85
# asymptote_voltage = -0.450
asymptote_reduction_ratio = 0.0
decay_rate = 0.25
num_steps = 80
# End user variables set

steps = np.arange(num_steps//2)
red_ratio = asymptote_reduction_ratio + (initial_reduction_ratio - asymptote_reduction_ratio) * np.exp(-steps * decay_rate)
red_ratio_reversed = red_ratio[::-1]

red_ratio = np.concatenate([red_ratio, red_ratio_reversed])
steps = np.arange(red_ratio.shape[0])

with open(file_path, "w") as fout:
    tsv_writer = csv.writer(fout, delimiter='\t')
    tsv_writer.writerow(red_ratio)

plt.plot(steps, red_ratio, marker='o')
plt.xlabel("Steps")
plt.ylabel("Reduction Ratio")
plt.show()