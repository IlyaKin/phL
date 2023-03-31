# Задание2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("file2.txt", "r") as file2:
    content=file2.readlines()
    print(len(content))
    for i in range(len(content)):
        words=content[i].split()
        print(f"Кол-во слов {i+1} строки = {len(words)}")

