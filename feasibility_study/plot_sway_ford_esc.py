import pandas as pd
import matplotlib.pyplot as plt

filepath = r'C:\Users\natha\Documents\Elecbrakes\datasets\data_logger\sway\5_11_2024\log_4.csv'

data = pd.read_csv(filepath)[int(4.335e+05):int(9.500e+05)]

t = data['timestamp_ms'] / 993
bpf_out = data['bpf_out']
sway_mg = data['sway_mg']
output_voltage = data['output_voltage']

fig, axs = plt.subplots(1, 1, figsize=(12, 5), sharex=True)

axs.plot(t, bpf_out)
axs.plot(t, sway_mg, color='green')
# axs[0].twinx().plot(t, output_voltage, color='red')

# axs[1].plot(t, data['kp'])
# axs[1].twinx().plot(t, data['ki_p'])

plt.tight_layout()
plt.show()