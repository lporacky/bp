import os
import time
import psutil
import cv2 as cv
import random
import csv
from threshold_white import threshold_white


def load_images(folder):
    images = []
    for f in os.listdir(folder):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            img = cv.imread(os.path.join(folder, f))
            images.append(img)
    return images


def process_batch(images):
    start = time.time()
    cpu_before = psutil.cpu_percent(interval=None)
    ram_before = psutil.virtual_memory().percent

    for img in images:
        threshold_white(img)

    duration = time.time() - start
    fps = len(images) / duration

    cpu_after = psutil.cpu_percent(interval=None)
    ram_after = psutil.virtual_memory().percent

    return fps, cpu_after, ram_after


def run_load_test(folder):
    samples = load_images(folder)
    batch_sizes = [10,20,30,40,50,60,70,80,90,100]

    with open("load_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["batch_size", "fps", "cpu_percent", "ram_percent"])

        for size in batch_sizes:
            print(f"--- Testing batch size {size} ---")
            batch = [random.choice(samples) for _ in range(size)]

            fps, cpu, ram = process_batch(batch)
            writer.writerow([size, fps, cpu, ram])

    print("\nVýsledky uložené v load_results.csv")


if __name__ == "__main__":
    run_load_test(r"C:\Users\plibo\Desktop\Skola\BP\vzorky\kamera\all")
