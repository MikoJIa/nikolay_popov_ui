def extract_numbers_text(text):
    res = []
    current_num = ''
    for char in text.text:
        if char.isdigit():
            current_num += char
        elif current_num:
            res.append(current_num)
            current_num = ''
    return res