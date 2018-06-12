path='/home/lt/download/words.txt'
with open(path) as words:
    x = words.read()
word = x.split(' ')
newWord = list(set(word))
newWord.sort(key=word.index)
# print(newWord)

with open("Q1.txt", "w") as f:
    for key, value in enumerate(newWord):
        y = str(value)+' '+str(key)+' '+str(word.count(value))+'\n'
        f.write(y)
