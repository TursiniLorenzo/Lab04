from passeggero import Passeggero
from cabina import Cabina
from cabinaDeluxe import CabinaDeluxe
import operator

class Crociera:

    def __init__(self, nome):
        self._nome = nome
        self._elenco_passeggeri = []
        self._elenco_cabine = []
        self._passeggero_per_cabina = []

    @property
    def nome (self) :
        return self._nome

    @nome.setter
    def nome (self, nuovo_nome) :
        self._nome = nuovo_nome
        return

    @property
    def elenco_passeggeri (self) :
        return self._elenco_passeggeri

    @property
    def elenco_cabine (self) :
        return self._elenco_cabine

    @property
    def passeggero_per_cabina (self) :
        return self._passeggero_per_cabina

    # Inserisco i dati relativi alle cabine e ai passeggeri attraverso i metodi definiti nelle classi Cabina e
    # Passeggeri
    def carica_file_dati(self, file_path):
        self._elenco_cabine = Cabina.crea_cabina (file_path)
        self._elenco_passeggeri = Passeggero.crea_passeggero(file_path)
        return self.elenco_cabine, self.elenco_passeggeri

    def __str__(self) :
        passeggeri_str = "\n".join (str(p) for p in self.elenco_passeggeri)
        cabine_str = "\n".join (str(c) for c in self.elenco_cabine)
        return (f"Elenco passeggeri:\n{passeggeri_str if passeggeri_str else 'Nessun passeggero'}, "
                f"\nElenco cabine:\n{cabine_str if cabine_str else 'Nessuna cabina'}")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        if not hasattr (self, "_passeggero_per_cabina") :
            self._passeggero_per_cabina = []

        for assegnazione in self._passeggero_per_cabina :
            if assegnazione [0] == codice_cabina :
                return False # Verifico che la cabina non sia già stata assegnata

        self._passeggero_per_cabina.append ([codice_cabina, codice_passeggero])
        return True

    def cabine_ordinate_per_prezzo(self):
        cabine_ordinate = sorted (self.elenco_cabine, key = operator.attrgetter ("costo_per_notte"))
        return cabine_ordinate

    def elenca_passeggeri(self):
        return self.elenco_passeggeri

    def applica_sovrapprezzo (self) :
        for cabine in self._elenco_cabine :
            if isinstance (cabine, CabinaDeluxe) :
                cabine.sovrapprezzo() # Se le cabine sono delle cabine deluxe, allora applico il sovrapprezzo
