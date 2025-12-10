def get_num_words(text):
    words = text.split()
    return(f"Found {len(words)} total words")

def character_count(text):
    char_dict = {}

    words = text.lower().split()

    for word in words:
        for char in word:
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_count(items):
    return items["num"]

def sort_list(character_dict):
    list_of_dicts = []
    for key in character_dict:
        if key.isalpha():
            list_of_dicts.append({"char": key, "num": character_dict[key]})
    
    list_of_dicts.sort(reverse=True, key=sort_count)

    for stat in list_of_dicts:
        print(f"{stat['char']}: {stat['num']}")    
    