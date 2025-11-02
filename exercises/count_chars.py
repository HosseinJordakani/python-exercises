# count_chars.py
def count_chars(s: str) -> dict:
    """Return dictionary of char -> count for string s."""
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

if __name__ == "__main__":
    text = input("Enter text: ")
    result = count_chars(text)
    print("Character counts:")
    for k, v in sorted(result.items()):
        print(f"'{k}': {v}")
