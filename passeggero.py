import csv

class Passeggero :

    def __init__ (self, cod_passeggero, nome, cognome) :
        self._cod_passeggero = cod_passeggero
        self._nome = nome
        self._cognome = cognome

    @property
    def cod_passeggero (self) :
        return self._cod_passeggero

    @property
    def nome (self) :
        return self._nome

    @property
    def cognome (self) :
        return self._cognome

    # Leggo dal file e prendo solamente le righe il cui primo elemento inizia per "P" ovvero la prima lettera del codice
    # dei passeggeri
    @classmethod
    def crea_passeggero (cls, file_path) :
        passeggeri = []
        with open (file_path, "r", encoding = "utf-8") as infile :
            reader = csv.reader (infile)
            for riga in reader :
                for elemento in riga :
                    if elemento [0] == "P" :
                        passeggero = cls (riga [0], riga [1], riga [2])
                        passeggeri.append (passeggero)
        return passeggeri

    def __str__ (self) :
        return (f"Passeggero: {self.cod_passeggero}, "
                f"Nome: {self.nome}, "
                f"Cognome: {self.cognome}.")

if __name__ == '__main__' :
    passeggeri = Passeggero.crea_passeggero("dati_crociera.csv")
    for passeggero in passeggeri :
        print(passeggero)