def main(src = "books/frankenstein.txt"):
    text = file_reader(src)
    word_count = word_counter(text)
    dict = counter(text)
    dict = dict_sorter(dict)
    reporter(src, word_count, dict)


def file_reader(src):
    # reads the file and returns the text
    with open(src) as f:
        text = f.read()
        return text


def word_counter(text):
    # returns the number of words in the text
    words = text.split()
    return len(words)


def counter(text):
    # counts the number of times each letter appears in the text
    text = text.lower()
    dict = {}
    for letter in text:
        if letter.isalpha():
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict


def dict_sorter(dict):
    # sorts the dictionary by values in descending order
    letters = list(dict.keys())
    values = list(dict.values())
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[i] < values[j]:
                values[i], values[j] = values[j], values[i]
                letters[i], letters[j] = letters[j], letters[i]
    sorted_dict = {letters[i]: values[i] for i in range(len(letters))}
    return sorted_dict


def reporter(src, word_count, dict):
    # prints the report
    print(f"--- Begin report on {src} ---")
    print(f"{word_count} words found in the document\n")
    for k, v in dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    

if __name__ == "__main__":
    main()
