def up_string(string):
    """Возвращение строки в верхнем регистре"""
    return string.upper()
def upping_first_letters(text):
    """Функция для заглавных букв"""
    return ' '.join(word.capitalize() for word in text.split())



