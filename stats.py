def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def no_of_words(path_to_file):
    counts = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents_lower = file_contents.lower()
    for char in file_contents_lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def char_count(path_to_file):
    report_list = []
    char_dict = no_of_words(path_to_file)
    for char, count in char_dict.items():
        if not char.isalpha():
            continue
            
        report_list.append({
            "char": char, 
            "num": count
        })
    report_list.sort(reverse=True, key=sort_on)
    return report_list

