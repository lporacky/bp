import time
import cv2 as cv
import psutil
import csv
import os
import concurrent.futures

from threshold_white import threshold_white


def load_images(folder):
    images = []
    for f in os.listdir(folder):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            img = cv.imread(os.path.join(folder, f))
            images.append(img)
    return images


def process_batch(images, threads):
    start_time = time.time()

    cpu_before = psutil.cpu_percent(interval=None)
    ram_before = psutil.virtual_memory().percent

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        list(executor.map(threshold_white, images))

    duration = time.time() - start_time
    fps = len(images) / duration

    cpu_after = psutil.cpu_percent(interval=None)
    ram_after = psutil.virtual_memory().percent

    return fps, cpu_after, ram_after


def run_test(folder):
    images = load_images(folder)
    tests = [1, 2, 4, 6, 8, 10, 12, 14, 16]

    with open("threads_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["threads", "fps", "cpu_percent", "ram_percent"])

        for t in tests:
            print(f"--- Testing threads={t} ---")
            fps, cpu, ram = process_batch(images, t)
            writer.writerow([t, fps, cpu, ram])

    print("\nVýsledky uložené v threads_results.csv")


if __name__ == "__main__":
    run_test(r"C:\Users\plibo\Desktop\Skola\BP\vzorky\kamera\all")
