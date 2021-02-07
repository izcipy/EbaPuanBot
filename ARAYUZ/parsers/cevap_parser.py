
class Parcala(object):

    okullar = []
    dersler = []
    siniflar = []
    okul_ders_sinif = {}

    def __init__(self, cevaplar):
        self.cevaplar = cevaplar
    
    def parcala_(self):
        for bilgi, cevap in self.cevaplar.items():
            bilgi_split = bilgi.split("|")
            
            self.dersler.append(
                bilgi_split[0]
            )
            self.okullar.append(
                bilgi_split[1]
            )
            self.siniflar.append(
                bilgi_split[2]
            )


    def duzenle(self):
        for i in range(0, len(self.dersler)):
            if self.okullar[i] in self.okul_ders_sinif:
                if self.siniflar[i] in self.okul_ders_sinif[self.okullar[i]]:
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]].append(self.dersler[i])

                else:
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]] = []
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]].append(self.dersler[i])

            else:
                self.okul_ders_sinif[self.okullar[i]] = {}
                if self.siniflar[i] in self.okul_ders_sinif[self.okullar[i]]:
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]].append(self.dersler[i])
                    
                else:
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]] = []
                    self.okul_ders_sinif[self.okullar[i]][self.siniflar[i]].append(self.dersler[i])

    def cevaplari_al(self, okul, sinif, ders):
        text = f"{ders}|{okul}|{sinif}"
        for bilgi, cevaplar in self.cevaplar.items():
            if bilgi == text:
                return cevaplar
                break



