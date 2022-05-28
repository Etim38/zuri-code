#Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    str1=input("word:")
    str2=input("anagram:")
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
