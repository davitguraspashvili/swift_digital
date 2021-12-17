s = "bcdef\nabcdefg\nbcde\nbcdef\n"
word = ""
d = {}
 
for i in s:   
    if i != "\n":
        word += i
    elif i == "\n":
        if word in d:
            d.update({word:d.get(word) + 1}) 
        else:
            d.update({word:1})
        word = ""
            
print(len(d))

appearences = ""
for i in d.values(): 
    appearences += str(i) + " "
print(appearences)