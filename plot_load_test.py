import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

# --- 1. Načítanie dát ---
df = pd.read_csv("load_test.csv")

# Pre istotu vyčisti dáta
df = df.dropna(subset=["fps", "total_ms", "cpu", "ram"])

# --- 2. Spočítaj priemery pre každú záťaž (FPS) ---
summary = df.groupby("fps").agg({
    "total_ms": ["mean", "max", "std"],
    "cpu": "mean",
    "ram": "mean"
}).reset_index()

summary.columns = ["FPS", "Priemer_ms", "Max_ms", "SD_ms", "Priemer_CPU", "Priemer_RAM"]
print(summary)

# --- 3. Graf: FPS vs. priemerný čas spracovania ---
plt.figure(figsize=(7,5))
plt.plot(summary["FPS"], summary["Priemer_ms"], marker="o", label="Priemerný čas spracovania")
plt.errorbar(summary["FPS"], summary["Priemer_ms"], yerr=summary["SD_ms"], fmt='none', capsize=5, color='gray', alpha=0.6)
plt.title("Záťažový test – vzťah FPS a času spracovania")
plt.xlabel("Počet snímok za sekundu (FPS)")
plt.ylabel("Priemerný čas spracovania [ms]")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("loadtest_time.png", dpi=300)
plt.show()

# --- 4. Graf: FPS vs. CPU/RAM ---
plt.figure(figsize=(7,5))
plt.plot(summary["FPS"], summary["Priemer_CPU"], marker="s", label="Priemerné CPU (%)")
plt.plot(summary["FPS"], summary["Priemer_RAM"], marker="^", label="Priemerná RAM (%)")
plt.title("Záťažový test – využitie CPU a RAM pri rôznych FPS")
plt.xlabel("Počet snímok za sekundu (FPS)")
plt.ylabel("Využitie prostriedkov [%]")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("loadtest_resources.png", dpi=300)
plt.show()

# --- 5. (Voliteľne) Boxplot všetkých časov spracovania ---
plt.figure(figsize=(7,5))
df.boxplot(column="total_ms", by="fps", grid=False)
plt.title("Rozloženie časov spracovania podľa FPS")
plt.suptitle("")  # odstráni duplikovaný titulok
plt.xlabel("Počet snímok za sekundu (FPS)")
plt.ylabel("Celkový čas spracovania [ms]")
plt.tight_layout()
plt.savefig("loadtest_boxplot.png", dpi=300)
plt.show()
