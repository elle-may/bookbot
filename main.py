def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    create_report(file_contents)

def count_words(text):
    # removes all line breaks
    removed_line_breaks = text.replace("\n", " ")
    split_text = removed_line_breaks.split(" ")
    # removes all instances of empty text
    split_text_clean = [i for i in split_text if i != ""]
    count_of_word = len(split_text_clean)
    return count_of_word

def count_characters(text):
    lowercase = text.lower()
    count_of_char = {}
    for i in lowercase:
        if i in count_of_char:
            count_of_char[i] += 1
        else:
            count_of_char[i] = 1
    return count_of_char

def create_report(text):
    count_of_char = count_characters(text)
    count_of_alphabet_char = {}
    for key, value in count_of_char.items():
        if key.isalpha():
            count_of_alphabet_char[key] = value
    # sort dictionary by value from highest to lowest
    count_of_alphabet_char_desc = dict(sorted(count_of_alphabet_char.items(), key=lambda item: item[1], reverse=True))
    
    # create report
    begin_report = f"--- Begin report of books/frankenstein.txt ---\n"
    word_count_report = f"{count_words(text)} words found in the document\n\n"
    
    character_count_list = []
    for key, value in count_of_alphabet_char_desc.items():
        character_count_list.append(f"The '{key}' character was found {value} times")

    print(begin_report + word_count_report + "\n".join(character_count_list))

main()