import time
import psutil
import csv
import cv2 as cv
import numpy as np
from threshold_white import threshold_white

# ---------- Nastavenia ----------
ITERATIONS = 1000  # počet iterácií testu
IMAGE_PATH = r"C:\Users\plibo\Desktop\Skola\BP\bp_try\OK\snimok_20250507_132816.jpg"  # jedna testovacia snímka
CSV_PATH = "resource_log.csv"
# --------------------------------

def imread_unicode(path):
    data = np.fromfile(path, dtype=np.uint8)
    return cv.imdecode(data, cv.IMREAD_COLOR)

def run_test():
    print(f"Spúšťam záťažový test ({ITERATIONS} iterácií)...")
    img = imread_unicode(IMAGE_PATH)
    if img is None:
        print("❌ Nepodarilo sa načítať obrázok.")
        return

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["iterácia", "čas_s", "CPU_%", "RAM_%"])

        for i in range(1, ITERATIONS + 1):
            start = time.perf_counter()
            threshold_white(img)
            elapsed = time.perf_counter() - start

            cpu = psutil.cpu_percent(interval=None)
            ram = psutil.virtual_memory().percent

            writer.writerow([i, f"{elapsed:.4f}", f"{cpu:.1f}", f"{ram:.1f}"])
            print(f"{i}/{ITERATIONS} | čas: {elapsed:.4f}s | CPU: {cpu:.1f}% | RAM: {ram:.1f}%")

    print(f"\n✅ Test dokončený. Dáta uložené do: {CSV_PATH}")

if __name__ == "__main__":
    run_test()
