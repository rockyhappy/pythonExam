import pandas as pd


# with open('python/text.txt', 'r+', encoding='utf-16') as file:
#     for each in file:
#         s=each.split()
#         size=s.__len__()
#         for i in range(size):
#             print(s[i]+",")
#     file.close()

# with open('python/text.txt', 'r+', encoding='utf-16') as file:
#     while file.readlines()!=[]:
#         s=file.readline().split()
#         size=s.__len__()
#         for i in range(size):
#             print(s[i]+",")
#     file.close()

# with open('python/text.txt', 'a+', encoding='utf-16') as file:
#     lines=["I am a lucky person\n","second line\n","third line\n"]
#     file.writelines(lines)
#     file.close()

# with open('python/textsomee.txt', 'a+', encoding='utf-8') as file:
#     file.write("I am a lucky person\n")
#     file.write("second line\n")
#     file.write("third line\n")
#     print(file.read())
#     file.close()
with open('python/textsomee.txt', 'r', encoding='utf-8') as file:
    file.readline()
    print(file.read())
    file.close()


