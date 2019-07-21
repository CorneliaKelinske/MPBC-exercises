def find_and_replace (file, word, replacement):
    with open(file) as f1:
        text = f1.read()
        new = text.replace(word, replacement)
    with open(file, "w") as f2:
        f2.write(new)
               

find_and_replace("story.txt", "morning", "evening")

