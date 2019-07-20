def statistics(file):
    
    
    with open(file) as f:
        text = f.read()
        num_lines = len(text.split("\n"))
        num_char = len(text)
        num_words = len([word for word in text.split()]) 
      

  
    figures = {"lines" : num_lines, "words" : num_words, "characters" : num_char}
    
    return figures

print(statistics("story.txt"))