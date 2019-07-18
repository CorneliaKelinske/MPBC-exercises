def copy (file, copy_file):
    with open (file) as f:
       with open (copy_file, "w") as f1:
           for line in f:
               f1.write(line)
copy("story.txt", "story_copy.txt")