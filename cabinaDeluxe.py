from cabina import Cabina

class CabinaDeluxe (Cabina) :

    def __init__ (self, cod_cabina, posti_letto, ponte, costo_per_notte, tipo_cabina) :
        super().__init__(cod_cabina, posti_letto, ponte, costo_per_notte)
        self._tipo_cabina = tipo_cabina

    @property
    def tipo_cabina (self) :
        return self._tipo_cabina

    def __str__(self):
        return super().__str__() + f", Tipo cabina: {self.tipo_cabina}"

    def sovrapprezzo (self) :
        costo = float (self.costo_per_notte)
        tipo = self.tipo_cabina
        if isinstance (tipo, int) or (isinstance (tipo, str) and tipo.isdigit()) :
            numero = int (tipo)
            costo *= (1 + 0.10 * numero)
        else :
            costo *= 1.20

        self._costo_per_notte = costo
        return self._costo_per_notte

if __name__ == "__main__" :
    cabine = Cabina.crea_cabina ("dati_crociera.csv")
    for cabina in cabine :
        print (cabina)
