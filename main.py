def count_words(input_str):
    return len(input_str.split())

def count_letters(input_str):
    lower_input_str = input_str.lower()
    count_dict = {}
    for char in lower_input_str:
        if not char in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def count_dictionary_to_sorted_list(count_dict):
    count_list = []
    for char in count_dict:
        if char.isalpha():
            count_list.append({ "char": char, "count": count_dict[char]})

    sorted_list = sorted(count_list, reverse=True, key=lambda dict: dict["count"])
    return sorted_list


def print_report(input_str):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(input_str)} words found in the document")
    print("\n")
    sorted_list = count_dictionary_to_sorted_list(count_letters(input_str))

    for entry in sorted_list:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")

if __name__ == '__main__':
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    print_report(file_contents)
