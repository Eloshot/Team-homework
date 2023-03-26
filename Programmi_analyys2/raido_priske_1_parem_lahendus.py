#Pakutud lahenduse versioon Team-homework 
#Koodi täiendas Taiger Kala

#https://leetcode.com/problems/reverse-string/description/

#Võtan kasutajalt sisendi
word = input("Sisesta sõna, mida ümber põõrata\n")

wordArray = []
finalArray = []

#Teen sisendist array
for taht in word:
    wordArray.append(taht)


for i in range(0, len(wordArray)):
    finalArray.append(wordArray[len(wordArray) - (i + 1)])

print(finalArray)
