def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            # print(file_contents)
    except FileNotFoundError:
        print("No such file or directory")

    print(f"--- Begin report of {f.name} ---")
    print(f"{word_counter(file_contents)} words found in the document")
    print(f"{letter_counter(file_contents)}")
    print("--- End report ---")


def word_counter(file_contents):
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter


def letter_counter(file_contents):
    letters = file_contents.lower()
    total = {}
    for char in set(letters):
        if char.isalpha() == 1:
            total[char] = file_contents.count(char)
    return total


def sort_on(total):
    return total["num"]



    
main()