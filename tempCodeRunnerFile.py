omee.txt', 'w+', encoding='utf-8') as file:
    file.write("I am a lucky person\n")
    file.write("second line\n")
    file.write("third line\n")
    print(file.read())
    file.close()