def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i in range(len(string)):
        if string_lower.count(string_lower[i]) == 1 and string_lower[i] != ' ':
            return string[i]
    return ''
