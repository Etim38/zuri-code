 # Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open("./story.txt" ,"r") as f:
      contents = f.read()
    print(contents)


def count_words():
    f=read_file_content("./story.txt")
    word_count = {}
    for line in f:
        line = strip_punctuations(line)
        words = line.split(" ")
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count
    print ("word_count:", count)
                
                
                
