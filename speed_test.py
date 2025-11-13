import os, time, csv, statistics as stats
import cv2 as cv
import psutil
from threshold_white import threshold_white

RESULT_CSV = "perf_results.csv"

def try_directory(folder_path):
    times = []
    load_times, proc_times = [], []
    cpu_points, mem_points = [], []

    with open(RESULT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["filename","t_load_ms","t_proc_ms","t_total_ms","cpu_pct","mem_pct"])

        for filename in os.listdir(folder_path):
            if not filename.lower().endswith((".jpg",".png",".jpeg",".bmp",".tif")):
                continue

            file_path = os.path.join(folder_path, filename)

            t0 = time.perf_counter()
            img = cv.imread(file_path)
            t1 = time.perf_counter()

            threshold_white(img)
            t2 = time.perf_counter()

            t_load = (t1 - t0) * 1000
            t_proc = (t2 - t1) * 1000
            t_total = (t2 - t0) * 1000

            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory().percent

            w.writerow([filename, f"{t_load:.2f}", f"{t_proc:.2f}", f"{t_total:.2f}", f"{cpu:.1f}", f"{mem:.1f}"])

            load_times.append(t_load); proc_times.append(t_proc); times.append(t_total)
            cpu_points.append(cpu); mem_points.append(mem)

            print(f"{filename}: load {t_load:.1f} ms | proc {t_proc:.1f} ms | total {t_total:.1f} ms")

    if times:
        p50 = stats.median(times)
        p90 = stats.quantiles(times, n=10)[8]   # približne P90
        p99 = stats.quantiles(times, n=100)[98] # približne P99
        avg = stats.mean(times); sd = stats.pstdev(times)
        fps = 1000.0 / avg

        print("\n--- Výsledky testu ---")
        print(f"Počet snímok: {len(times)}")
        print(f"Priemer: {avg:.2f} ms | SD: {sd:.2f} ms")
        print(f"P50: {p50:.2f} ms | P90: {p90:.2f} ms | P99: {p99:.2f} ms")
        print(f"Min: {min(times):.2f} ms | Max: {max(times):.2f} ms | Odhad FPS: {fps:.2f}")
        print(f"Priemerné CPU: {stats.mean(cpu_points):.1f}% | Priemerná RAM: {stats.mean(mem_points):.1f}%")

try_directory(r"C:\Users\plibo\Desktop\Skola\BP\vzorky\mobil\all")
