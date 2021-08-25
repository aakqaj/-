import ijson
import random
from pypinyin import pinyin


def pinyin2hanzi(pinyin_list: list) -> list:
    if type(pinyin_list) is str:
        pinyin_list = [pinyin_list.split()]

    with open("./data/word.json", 'r', encoding='utf-8') as json_fp:
        word_json_data = list(ijson.items(json_fp, 'item'))
        results_list = []

        for pinyin_item in pinyin_list:
            results_list.append({"pinyin": pinyin_item[0], "words": []})

        for word_ in word_json_data:
            for i, pinyin_item in enumerate(pinyin_list):
                if word_['pinyin'] == pinyin_item[0]:
                    results_list[i]["words"].append(word_["word"])

        return results_list
    pass


def ningzaishuoshenmo(line_: str) -> str:
    sentence = ""
    line_pinyin = pinyin(line_)
    data_list = pinyin2hanzi(line_pinyin)

    for i, word in enumerate(data_list):
        if len(word["words"]) == 0:
            sentence += word['pinyin']
            continue

        print(word)

        while True:
            redress = random.choice(word["words"])
            if pinyin(redress)[0][0] == line_pinyin[i][0]:
                break
        sentence += redress

    return sentence
    pass


if __name__ == '__main__':
    while True:
        line = input('please input one sentence: ')
        # line = "你踏马的别说废话了"

        print(ningzaishuoshenmo(line))

        input('please enter any key to continue')
        print('======================================================================')

    pass
