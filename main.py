import argparse
import json
import random


def parser_data():
    parser = argparse.ArgumentParser(prog="Word filling game",
                                     description="A simple game",
                                     allow_abbrev=True)
    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-p", "--passage", help="指定文章")
    args = parser.parse_args()
    return args


def read_articles(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_inputs(hints):
    keys = []
    for hint in hints:
        print(f"请输入{hint}:")
        keys.append(input())
    return keys


def replace(article, keys):
    for i in range(len(keys)):
        c = str(i + 1)
        article = article.replace("{{" + c + "}}", keys[i])
    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    r = True
    for art in articles:
        if art["title"] == args.passage:
            r = False
            article = art
            break
    if r:
        n = random.randint(0, len(articles) - 1)
        article = articles[n]
    print(article["title"])
    print(article["article"])
    keys = get_inputs(article["hints"])
    print("这是替换后的结果：")
    print(replace(article["article"], keys))
