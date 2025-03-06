import re #libreria Regular Expretions

class Dictionary:
    def __init__(self,dizionario = {}):
        self.dizionario = dizionario #Dizionario interno


    def addWord(self,parola_aliena,parola_italiana):
        self.dizionario[parola_aliena] =parola_italiana
        return self.dizionario
    '''
    def addWords(self,parola_aliena,parole_italiane):
        self.dizionario[parola_aliena] = parole_italiane
        return self.dizionario
    '''
    def translate(self, aliena):
        return self.dizionario[aliena]

    def translateWordWildCard(self,parola_con_wildCard):
        #sostituisce il carattere ? con il . per cercare un'espressione regolare
        pattern = parola_con_wildCard.replace("?",".")
        #adesso cerchiamo una parola nel dizionario che corrisponda a pattern
        for aliena, traduzione in self.dizionario.items(): #items restituisce una lista di tuple(aliena, trad) in ordine d'inserimento
            if re.fullmatch(pattern,aliena): # Il suo scopo è verificare se l'intera stringa parola_aliena corrisponde esattamente al pattern specificato.
                return traduzione
        return"Nessuno traduzione trovata"
