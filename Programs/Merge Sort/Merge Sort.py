import time
import os
import sys

def merge_sort(data):
    def merge_sort_rec(data, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_rec(data, left, mid)
            merge_sort_rec(data, mid + 1, right)
            merge(data, left, mid, right)

    def merge(data, left, mid, right):
        left_copy = data[left:mid + 1]
        right_copy = data[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_copy) and j < len(right_copy):
            if left_copy[i] <= right_copy[j]:
                data[k] = left_copy[i]
                i += 1
            else:
                data[k] = right_copy[j]
                j += 1
            k += 1
        while i < len(left_copy):
            data[k] = left_copy[i]
            i += 1
            k += 1
        while j < len(right_copy):
            data[k] = right_copy[j]
            j += 1
            k += 1

    merge_sort_rec(data, 0, len(data) - 1)

def main():
    print("=== Merge Sort ===")

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
    merge_sort(arr)
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
        log.write(f"{filename} sorted ({sort_type}) in {elapsed} seconds using Merge Sort.\n")
    print(f"Log updated: {log_file}")

if __name__ == "__main__":
    main()
