import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("endurance_test2.csv")

# 1️⃣ Graf – čas spracovania
plt.figure(figsize=(8,5))
plt.plot(df["minute"], df["avg_ms"], marker="o", label="Priemerný čas spracovania [ms]")
plt.title("Endurance test – vývoj spracovania v čase")
plt.xlabel("Čas testu [minúty]")
plt.ylabel("Priemerný čas spracovania [ms]")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.ylim(20, 50)
plt.tight_layout()
plt.savefig("endurance_time.png", dpi=300)
plt.show()

# 2️⃣ Graf – CPU a RAM v čase
plt.figure(figsize=(8,5))
plt.plot(df["minute"], df["cpu"], label="CPU [%]")
plt.plot(df["minute"], df["ram"], label="RAM [%]")
plt.title("Endurance test – využitie CPU a RAM počas testu")
plt.xlabel("Čas testu [minúty]")
plt.ylabel("Využitie prostriedkov [%]")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.ylim(0, 70)
plt.tight_layout()
plt.savefig("endurance_resources.png", dpi=300)
plt.show()



# # Ak máš stĺpec 'avg_ms' = priemerný čas spracovania jednej snímky
# plt.figure(figsize=(8,5))
# plt.plot(df["minute"], df["avg_ms"], marker="o", color="tab:blue", label="Priemerný čas spracovania [ms]")
#
# plt.title("Endurance test – vývoj rýchlosti spracovania snímok v čase")
# plt.xlabel("Čas testu [minúty]")
# plt.ylabel("Priemerný čas spracovania [ms]")
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.legend()
# plt.tight_layout()
# plt.savefig("endurance_speed.png", dpi=300)
# plt.show()
plt.figure(figsize=(8,5))
plt.plot(df["minute"], df["avg_ms"], marker="o", color="tab:blue", label="Priemerný čas spracovania [ms]")

plt.title("Endurance test – vývoj rýchlosti spracovania snímok v čase")
plt.xlabel("Čas testu [minúty]")
plt.ylabel("Priemerný čas spracovania [ms]")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# 🔹 nastavenie rozsahu Y osi
plt.ylim(20, 50)  # tu zadaj svoj rozsah, napr. podľa typických hodnôt

plt.tight_layout()
plt.savefig("endurance_speed_zoomed.png", dpi=300)
plt.show()
