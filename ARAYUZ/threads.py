from EBA.eba import EBA
from PyQt5.QtCore import pyqtSignal, QObject
from ARAYUZ.parsers.cevap_parser import Parcala

class EbaThread(QObject):

    sonuc = pyqtSignal(object)
    text_edit_signal = pyqtSignal(object)


    def __init__(self, chromedriver_path, browser, TC, password, okul, sinif, ders, cevaplar):
        super().__init__()
        self.cdpath = chromedriver_path
        self.browser = browser
        self.TC = TC
        self.password = password
        self.okul = okul
        self.sinif = sinif
        self.ders = ders
        self.cevaplar = cevaplar 

    def run(self):
        EBA(
            self.sonuc,
            self.text_edit_signal,
            self.cdpath,
            self.browser,
            self.TC,
            self.password,
            self.okul,
            self.sinif,
            self.ders,
            Parcala(self.cevaplar).cevaplari_al(
                self.okul,
                self.sinif,
                self.ders
            ),
        ) 
