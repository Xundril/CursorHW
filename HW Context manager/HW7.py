# Task 1
# 1 Словник елементами якого буде пара ключ:значення: де ключ - мітка часу, значення - репліка в даний момент часу
with open("task1.txt", "r") as file:
    dict = {}
    content = file.readlines()
    for i in range(0, len(content), 2):
        content[i] = content[i].replace("\n", "")
        content[i + 1] = content[i + 1].replace("\n", "")
        dict.update({content[i]: content[i + 1]})
    print(dict)