import time
import os
import sys

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def main():
    print("=== Selection Sort ===")

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
    selection_sort(arr)
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
        log.write(f"{filename} sorted ({sort_type}) in {elapsed} seconds using Selection Sort.\n")
    print(f"Log updated: {log_file}")

if __name__ == "__main__":
    main()
