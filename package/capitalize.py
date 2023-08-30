def capitalize(text):
    if text == '':
        return ''
    if type(text) != str:
        return 'Введите текст'
    first_letter = text[0].upper()
    remaining_letters = text[1:]
    return f'{first_letter}{remaining_letters}'
