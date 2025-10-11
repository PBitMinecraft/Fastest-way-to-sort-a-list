import random
import requests
import sys

def get_random_words(count):
    words = []
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number={count}")
        if response.status_code == 200:
            words = response.json()
        else:
            print("Could not fetch words.")
            sys.exit(1)
    except Exception as e:
        print(f"Error fetching words: {e}")
        sys.exit(1)
    return words

def main():
    print("=== Random List Writer ===")
    
    filename = input("Enter file name to save: ").strip()
    data_type = input("Words or numbers? (w/n): ").strip().lower()
    
    try:
        count = int(input("Values: "))
    except ValueError:
        print("Enter a valid number.")
        sys.exit(1)
    
    items = []
    if data_type in ["w", "word", "words"]:
        items = get_random_words(count)
    elif data_type in ["n", "num", "number", "numbers"]:
        items = [str(random.randint(0, 10000)) for _ in range(count)]
    else:
        print("Invalid option.")
        sys.exit(1)
    
    try:
        with open(filename, "w") as f:
            f.write("\n".join(items))
        print(f"Success, wrote {count} random {'words' if data_type.startswith('w') else 'numbers'} to '{filename}'")
    except Exception as e:
        print(f"Error writing to: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
