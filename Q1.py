with open('words.txt') as words:
    x = words.read()
word = x.split(' ')

with open("Q1.txt", "w") as f:
    for key, value in enumerate(word):
        y = str(value)+' '+str(key)+' '+str(word.count(value))+'\n'
        f.write(y)