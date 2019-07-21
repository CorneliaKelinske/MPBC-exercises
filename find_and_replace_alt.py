def find_and_replace (file, word, replacement):
    with open(file, "r+") as f1:
        text = f1.read()
        new = text.replace(word, replacement)
        f1.seek(0)
        f1.write(new)

find_and_replace("story.txt", "evening", "morning")