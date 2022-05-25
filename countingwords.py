introString =input("enter your introduction")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount+=1

print(characterCount)
print(wordCount)