import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stress_threads.csv")

plt.figure(figsize=(7,5))
plt.plot(df["threads"], df["avg_ms"], marker="o", label="Priemerný čas spracovania [ms]")
plt.title("Stress test – závislosť výkonu od počtu vlákien")
plt.xlabel("Počet vlákien")
plt.ylabel("Priemerný čas spracovania [ms]")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("stress_threads_time.png", dpi=300)
plt.show()

# druhý graf: CPU a RAM
plt.figure(figsize=(7,5))
plt.plot(df["threads"], df["cpu"], marker="s", label="Priemerné CPU (%)")
plt.plot(df["threads"], df["ram"], marker="^", label="Priemerná RAM (%)")
plt.title("Stress test – využitie CPU/RAM pri rôznych počtoch vlákien")
plt.xlabel("Počet vlákien")
plt.ylabel("Využitie prostriedkov [%]")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("stress_threads_resources.png", dpi=300)
plt.show()
