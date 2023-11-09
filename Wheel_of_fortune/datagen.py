
def get_words(path = 'words.txt'):
    with open('words.txt', encoding = "utf8") as text:
        text_list = text.read().upper().splitlines()
        return text_list


def get_records(record, path = 'rec.txt'):
    with open("rec.txt", mode = "r+") as record_file:
        cur_record = record_file.readline()
        cur_record = max(int(cur_record), record)
        record_file.seek(0)
        record_file.write(str(cur_record))
        return cur_record


if __name__ == "__main__":
    print(get_words())
    print(get_records(0))

