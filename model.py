STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is not None:
            self.crke = crke
        else:
            self.crke = []

    def napacne_crke(self): #napacne so use crke ki niso u nasem geslu
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz

        #''.join([(crka if crka in self.crke else '_'] for crka in self.geslo))

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke()) #s presledki bi radi združli

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open('besede.txt', encoding='utf8') as d:
    bazen_besed = d.read().split('\n')

# bazen_besed = []
# with open('besede.txt', encoding='utf8') as d:
#     for beseda in d: #ko se s for zanko sprehajš čez datoteko dobiš vrstico za vrstico
#         bazen_besed.append(beseda.strip())

#za nakljucne stvari je knjiznica random
import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo) #crke smo privzeli na zacetku da se zacne iz nule(neobvezn argument) zto nerabmo pist kukr argument