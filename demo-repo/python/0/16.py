word1=input("Please enter the first word: ")
word2=input("Please enter the second word: ")

if word1 != word2:
    if len(word1)==len(word2):
        print("bu sozlerin ancaq uzunluqlari beraberdir")
    elif len(word1) != len(word2):
        print("uzunluqlar bele beraber deyil")
else:
    print("sozler beraberdir") 
           