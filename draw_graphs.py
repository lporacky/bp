import matplotlib.pyplot as plt
import csv

sizes = []
fps = []
cpu = []
ram = []

with open("load_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["batch_size"]))
        fps.append(float(row["fps"]))
        cpu.append(float(row["cpu_percent"]))
        ram.append(float(row["ram_percent"]))

plt.figure(figsize=(10,5))
plt.plot(sizes, fps, marker="o")
plt.title("Výkon podľa privalu obrázkov")
plt.xlabel("Veľkosť dávky")
plt.ylabel("FPS")
plt.grid()
plt.savefig("load_fps.png")

plt.figure(figsize=(10,5))
plt.plot(sizes, cpu, marker="o", label="CPU %")
plt.plot(sizes, ram, marker="o", label="RAM %")
plt.legend()
plt.title("CPU/RAM podľa privalu obrázkov")
plt.xlabel("Veľkosť dávky")
plt.ylabel("Využitie (%)")
plt.grid()
plt.savefig("load_cpu_ram.png")

print("Grafy uložené: load_fps.png, load_cpu_ram.png")

threads = []
fps = []
cpu = []
ram = []

with open("threads_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        threads.append(int(row["threads"]))
        fps.append(float(row["fps"]))
        cpu.append(float(row["cpu_percent"]))
        ram.append(float(row["ram_percent"]))

plt.figure(figsize=(10,5))
plt.plot(threads, fps, marker="o")
plt.title("Výkon podľa počtu vlákien")
plt.xlabel("Počet vlákien")
plt.ylabel("FPS")
plt.grid()
plt.savefig("threads_fps.png")

plt.figure(figsize=(10,5))
plt.plot(threads, cpu, marker="o", label="CPU %")
plt.plot(threads, ram, marker="o", label="RAM %")
plt.legend()
plt.title("CPU/RAM podľa počtu vlákien")
plt.xlabel("Počet vlákien")
plt.ylabel("Využitie (%)")
plt.grid()
plt.savefig("threads_cpu_ram.png")

print("Grafy uložené: threads_fps.png, threads_cpu_ram.png")
