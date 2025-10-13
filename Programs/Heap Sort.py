import time
import os
import sys

def heap_sort(data):
    def heapify(data, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            heapify(data, n, largest)

    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

def main():
    print("=== Heap Sort ===")

    filename = input("Enter file name: ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        sys.exit(1)

    data_type = input("Numbers or words? (n/w): ").strip().lower()

    try:
        with open(filename, "r") as f:
            items = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading: {e}")
        sys.exit(1)

    if data_type.startswith("w"):
        arr = [len(word) for word in items]
        sort_type = "words (lengths)"
    elif data_type.startswith("n"):
        try:
            arr = [int(x) for x in items]
            sort_type = "numbers"
        except ValueError:
            print("Error: Non-numeric values.")
            sys.exit(1)
    else:
        print("Invalid type.")
        sys.exit(1)

    start_time = time.time()
    heap_sort(arr)
    elapsed = round(time.time() - start_time, 5)

    print(f"Sorting finished in {elapsed} seconds!")

    save_sorted = input("Save sorted list? (y/n): ").strip().lower() == "y"
    if save_sorted:
        out_file = input("Output file name: ").strip()
        with open(out_file, "w") as f:
            for item in arr:
                f.write(str(item) + "\n")
        print(f"Sorted list saved to {out_file}")

    log_file = "sort_log.txt"
    with open(log_file, "a") as log:
        log.write(f"{filename} sorted ({sort_type}) in {elapsed} seconds using Heap Sort.\n")
    print(f"Log updated: {log_file}")

if __name__ == "__main__":
    main()
