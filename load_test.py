import cv2 as cv
import os, time, csv, psutil, statistics as stats
from threshold_white import threshold_white

images_dir = r"C:\Users\plibo\Desktop\Skola\BP\vzorky\kamera\all"
image_files = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.lower().endswith((".jpg",".png"))]

# rôzne úrovne záťaže (simulované FPS)
fps_levels = [5, 15, 30, 60]  # snímky/s

with open("load_test.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["fps","image","load_ms","proc_ms","total_ms","cpu","ram"])

    for fps in fps_levels:
        print(f"\n--- Test pre {fps} FPS ---")
        delay = 1.0 / fps  # oneskorenie medzi snímkami
        times = []

        for i, file_path in enumerate(image_files[:200]):  # napr. 200 snímok
            start = time.perf_counter()
            img = cv.imread(file_path)
            load_t = (time.perf_counter() - start) * 1000

            start_proc = time.perf_counter()
            threshold_white(img)
            total_t = (time.perf_counter() - start_proc) * 1000

            times.append(total_t)
            cpu = psutil.cpu_percent(interval=0)
            ram = psutil.virtual_memory().percent
            w.writerow([fps, os.path.basename(file_path), load_t, total_t, total_t + load_t, cpu, ram])

            # simulácia rýchlosti kamery
            time.sleep(delay)

        print(f"Priemer pre {fps} FPS: {stats.mean(times):.2f} ms | SD: {stats.pstdev(times):.2f} | Max: {max(times):.2f}")
