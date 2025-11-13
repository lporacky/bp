import cv2 as cv
import os, time, psutil, csv, statistics as stats
from threshold_white import threshold_white

# Cesty a nastavenia
images_dir = r"C:\Users\plibo\Desktop\Skola\BP\vzorky\kamera\all"
image_files = [os.path.join(images_dir, f) for f in os.listdir(images_dir)
               if f.lower().endswith((".jpg",".png"))]

TEST_DURATION_MIN = 360          # trvanie testu (minúty)
LOG_INTERVAL_SEC = 60           # logovanie každú minútu
results = []

start_time = time.time()
next_log = start_time + LOG_INTERVAL_SEC
end_time = start_time + TEST_DURATION_MIN * 60
cycle_count = 0

print(f"🕓 Spúšťam endurance test na {TEST_DURATION_MIN} minút...")
print("Zaznamenávam výkon každú minútu...")

while time.time() < end_time:
    times = []
    nok_count = 0

    # Spracuj všetky obrázky v jednom cykle
    for img_path in image_files:
        t0 = time.perf_counter()
        img = cv.imread(img_path)
        result = threshold_white(img)
        if result is None or img is None:
            nok_count += 1
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000)  # v ms

    cycle_count += 1

    # loguj každú minútu
    if time.time() >= next_log:
        avg_time = stats.mean(times)
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        timestamp = round((time.time() - start_time) / 60, 2)
        results.append((timestamp, avg_time, cpu, ram, nok_count))
        print(f"[{timestamp} min] avg={avg_time:.1f} ms | CPU={cpu:.1f}% | RAM={ram:.1f}% | NOK={nok_count}")
        next_log += LOG_INTERVAL_SEC

# uloženie výsledkov
with open("endurance_test2.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["minute","avg_ms","cpu","ram","nok"])
    w.writerows(results)

print("\n✅ Endurance test ukončený.")
