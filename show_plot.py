import pandas as pd
import matplotlib.pyplot as plt

# Načítanie CSV
df = pd.read_csv("perf_results.csv")

# ---------------------------
# 1. Histogram celkového času
# ---------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["t_total_ms"], bins=30, edgecolor="black")
plt.title("Rozdelenie času spracovania snímok")
plt.xlabel("Celkový čas spracovania (ms)")
plt.ylabel("Počet snímok")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# ---------------------------
# 2. Vývoj CPU a RAM v čase
# ---------------------------
plt.figure(figsize=(9, 5))
plt.plot(df.index, df["cpu_pct"], label="CPU [%]", linewidth=1.5)
plt.plot(df.index, df["mem_pct"], label="RAM [%]", linewidth=1.5)
plt.title("Využitie CPU a RAM počas testu")
plt.xlabel("Poradie snímky")
plt.ylabel("Zaťaženie (%)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# ---------------------------
# 3. Scatter – závislosť CPU od času
# ---------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["cpu_pct"], df["t_total_ms"], alpha=0.6)
plt.title("Závislosť času spracovania od CPU")
plt.xlabel("CPU [%]")
plt.ylabel("Celkový čas (ms)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
