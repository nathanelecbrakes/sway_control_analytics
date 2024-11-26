import pandas as pd
import matplotlib.pyplot as plt

filepath = r'C:\Users\natha\Documents\Elecbrakes\datasets\data_logger\sway\5_11_2024\log_4.csv'

data = pd.read_csv(filepath)

t = data['timestamp_ms']
bpf_out = data['bpf_out']
sway_mg = data['sway_mg']
output_voltage = data['output_voltage']

fig, axs = plt.subplots(2, 1, figsize=(12, 5), sharex=True)

axs[0].plot(bpf_out)
axs[0].plot(sway_mg, color='green')
axs[0].twinx().plot(output_voltage, color='red')

axs[1].plot(data['kp'])
axs[1].twinx().plot(data['ki_p'])

plt.tight_layout()
plt.show()