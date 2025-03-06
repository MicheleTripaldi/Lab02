import dictionary
import translator as tr
from dictionary import Dictionary


t = tr.Translator()
d = Dictionary()

with open("dictionary.txt","r",encoding="utf-8") as file:
    for line in file:
        coppia = line.strip().split(" ")
        if len(coppia) == 2:
            d.addWord(coppia[0], coppia[1])
        else:
            d.addWord(coppia[0], [coppia[1], coppia[2]])
#print(d) FUNZIONA
# print il menu
t.printMenu()
# adesso devo permettere di scegliere una delle 5 opzioni

scelta = input(f"Scegli l'opzione:")
match scelta:
    case "1":
        utente = input(f"Inserire la parola d'aggiungere con la traduzione/traduzioni:")
        coppia = utente.lower().split(" ")
        if len(coppia) == 2:
            d.addWord(coppia[0], coppia[1])
            print(d.dizionario) #FUNZIONA

        else:
            lista= [coppia[1], coppia[2]]
            d.addWord(coppia[0],lista)
            print(d.dizionario)
       # with open("dictionary.txt","r",encoding="utf-8") as file:
        #    file.write()

    case "2":# cerca una traduzione
        utente = input((f"Inserire la parola da tradurre:"))
        utente = utente.lower()
        if utente in d.dizionario:
            print(d.translate(utente))
        else:
            print("Parola non presente nel dizionario")
    case "3": # cercare con wildcard
        utente = input((f"Inserire la parola con WildCard:"))
        print(d.translateWordWildCard(utente))

    case "4": # stampa tutto il dizionario d
        print(d.dizionario)
    case "5":
        print("Spiacente sei uscito dal programma!")




'''
while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input() 

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input()
        pass
    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break

'''