import csv

class Cabina :

    def __init__ (self, cod_cabina, posti_letto, ponte, costo_per_notte) :
        self._cod_cabina = cod_cabina
        self._posti_letto = posti_letto
        self._ponte = ponte
        self._costo_per_notte = costo_per_notte

    @property
    def cod_cabina (self) :
        return self._cod_cabina

    @property
    def posti_letto (self) :
        return self._posti_letto

    @property
    def ponte (self) :
        return self._ponte

    @property
    def costo_per_notte (self) :
        return self._costo_per_notte

    # Leggo dal file e prendo solamente le righe il cui primo elemento inizia per "C" ovvero la prima lettera del codice
    # delle cabine
    @classmethod
    def crea_cabina (cls, file_path) :
        from cabinaDeluxe import CabinaDeluxe
        cabine = []
        with open (file_path, "r", encoding = "utf-8") as infile :
            reader = csv.reader (infile)
            for riga in reader :
                for elemento in riga :
                    if elemento [0] == "C" :
                        if len (riga) == 4 :
                            cabina = cls (riga [0], riga [1], riga [2], float (riga [3]))
                            cabine.append (cabina)
                        elif len (riga) == 5 :
                            cabina = CabinaDeluxe (riga [0], riga [1], riga [2], riga [3], riga [4])
                            cabine.append (cabina)
        return cabine

    def __str__ (self) :
        return (f"Cabina: {self.cod_cabina}, "
                f"Posti letto: {self.posti_letto}, "
                f"Ponte: {self.ponte}, "
                f"Costo per notte: {self.costo_per_notte}.")

if __name__ == '__main__' :
    cabine = Cabina.crea_cabina ("dati_crociera.csv")
    for cabina in cabine :
        print (cabina)