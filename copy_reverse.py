def copy_and_reverse(file, reversed_file):
    
    with open(file) as f:
        text = f.read()
        reversed_text = text[::-1]
    
    with open(reversed_file, "w") as f1:
        f1.write(reversed_text)

copy_and_reverse("story.txt","reverse_story")