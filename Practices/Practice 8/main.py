import pymorphy2
from translate import Translator

def pymorphy2_311_hotfix():
    from inspect import getfullargspec
    from pymorphy2.units.base import BaseAnalyzerUnit

    def _get_param_names_311(klass):
        if klass.__init__ is object.__init__:
            return []
        args = getfullargspec(klass.__init__).args
        return sorted(args[1:])

    setattr(BaseAnalyzerUnit, '_get_param_names', _get_param_names_311)

def pymorphy2_example():
    pymorphy2_311_hotfix()
    morph = pymorphy2.MorphAnalyzer()
    primary_form_words = []
    with open("input_messages.txt", encoding="utf-8") as file:
        words = file.read().split()
        for word in words:
            if word.isalpha():
                parse_result = morph.parse(word)
                primary_form_words.append(parse_result[0].normal_form)
    return primary_form_words

def list_to_tuple(listik):
    book = {}
    for word in listik:
        book[word] = book.get(word, 0) + 1
    sorted_book = sorted(book.items(), key= lambda x: x[1], reverse=True)
    return sorted_book

def translating_words(listok):
    translator = Translator(from_lang="ru", to_lang="en")
    translated_book = []
    for word in range(len(listok)):
        translation = translator.translate(str(listok[word][0]))
        translated_book.append([listok[word][0], translation, listok[word][1]])
    return translated_book

list = pymorphy2_example()
print(list)
listik = list_to_tuple(list)
print(listik)
dictick = translating_words(listik)
print(dictick)

file = open('words.txt', 'w', encoding="utf8")
for i in range(len(dictick)):
    file.write(f"{dictick[i][0]}|{dictick[i][1]}|{dictick[i][2]}\n")
