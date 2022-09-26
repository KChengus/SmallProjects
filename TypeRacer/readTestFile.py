file_name = "text1.txt"

with open(file_name, 'r', encoding="utf-8") as f:
    words = f.read().split()

if __name__ == "__main__":
    print(words)