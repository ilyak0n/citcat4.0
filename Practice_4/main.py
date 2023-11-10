def read_file(path):
    file_mn = set()
    file = open(path, encoding="utf8").read()
    file_list = file.lower().split()
    for i in range(len(file_list)):
        if "." or "," or "!" or "?" in file_list[i]:
            file_list[i] = file_list[i].replace(".","").replace(",","").replace("!","").replace("?","")
            file_mn.add(file_list[i])
        else:
            file_mn.add(file_list[i])
    file_words = list(file_mn)
    return file_words

def save_file(path, words):
    with open(path, "w", encoding='utf8') as file:
        file.write(f"Всего уникальных слов: {len(words)}\n\n")
        for i in range(len(words)):
            file.write(str(sorted(words)[i])+"\n")

words = read_file('data.txt')
save_file('count.txt', words)