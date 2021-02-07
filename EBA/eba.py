from locators.locators import AllLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class EBA(object):
    
    def __init__(self, sonuc, text_edit_signal, chromedriver_path, browser, TC, password, okul, sinif, ders, cevaplar):
        super(EBA, self).__init__()
        self.sonuc = sonuc
        self.text_edit_signal = text_edit_signal
        self.cdpath = chromedriver_path
        self.TC = TC
        self.password = password
        self.okul = okul
        self.sinif = sinif
        self.ders = ders
        self.cevaplar = cevaplar
        try:
            self.text_edit_signal.emit("Tarayıcı Açılıyor...")
            self._br = browser(self.cdpath)
            self._br.get()
            self.text_edit_signal.emit("Giriş Yapılıyor...")
            self.yap()
        except OSError:
            self.sonuc.emit("driver hata")
        


    def login(self, TC, password):

        tc_input = self._br.element(
            AllLocators.tc_input,
            wait_=True,
            while_=True
        )
        tc_input.send_keys(TC)
        self.text_edit_signal.emit("TC girildi")

        password_input = self._br.element(
            AllLocators.password_input,
            wait_=True,
            while_=True
        )
        password_input.send_keys(password)  
        self.text_edit_signal.emit("Şifre girildi")

        password_input.send_keys(Keys.ENTER)
        self.text_edit_signal.emit('<font color="blue">TC ve Şifre Doğrulanıyor...</font>')

        try:
            alert = self._br.element(
                AllLocators.alert,
                wait_=True,
                wait_second=5
            )
            if alert:
                return True

        except TimeoutException:
            return False


    def tarama_testleri_click(self):

        tarama_testleri = self._br.element(
            AllLocators.tarama_testleri,
            wait_=True,
            while_=True,
            click_=True
        )
        self.text_edit_signal.emit('<font color="blue">Tarama testleri bölümüne girildi</font>')


    def okul_sinif_ders(self, okul_, sinif_, ders_): 
        
        okul_sec = self._br.element(
            AllLocators.okul_list,
            wait_=True,
            while_=True,
            click_=True
        )

        okullar = self._br.element(
            AllLocators.okul_list_box,
            wait_=True,
            while_=True
        )
        okullar = okullar.find_elements_by_tag_name("span")
        for okul in okullar:
            if okul.text == okul_:
                okul.click()
                self.text_edit_signal.emit(f'<font color="green">Okul Seçildi : {okul_}</font>')
                break
            
            else: pass

        sinif_sec = self._br.element(
            AllLocators.sinif_list,
            wait_=True,
            while_=True,
            click_=True
        )
        siniflar = self._br.element(
            AllLocators.sinif_list_box,
            wait_=True,
            while_=True
        )

        siniflar = siniflar.find_elements_by_tag_name("span")
        for sinif in siniflar:
            if sinif.text == sinif_:
                sinif.click()
                self.text_edit_signal.emit(f'<font color="green">Sınıf Seçildi : {sinif_}</font>')
                break

            else: pass

        ders_sec = self._br.element(
            AllLocators.ders_list,
            wait_=True,
            while_=True,
            click_=True
        )
        
        dersler = self._br.element(
            AllLocators.ders_list_box,
            wait_=True,
            while_=True
        )

        dersler = dersler.find_elements_by_tag_name("span")
        for ders in dersler:
            if ders.text == ders_:
                ders.click()
                self.text_edit_signal.emit(f'<font color="green">Ders Seçildi : {ders_}</font>')
                break

            else: pass

    def cevap_cevir(self, cevap):
        if cevap == "A":
            return "1"
        
        elif cevap == "B":
            return "2"
        
        elif cevap == "C":
            return "3"
        
        elif cevap == "D":
            return "4"
        
        elif cevap == "E":
            return "5"

        else:
            return "1"

    def test_sayisi(self):
        testler = self._br.element(
            AllLocators.testler_full,
            wait_=True,
            while_=True
        )

        testler_ = testler.find_elements_by_tag_name("div")

        test_sayisi_ = int(len(testler_))

        return test_sayisi_

    def teste_basla(self):
        time.sleep(0.5)
        basla = self._br.element(
            AllLocators.basla,
            wait_=True,
            while_=True
        )
        
        time.sleep(1.5)
        basla_div = basla.find_elements_by_tag_name("div")
        for div in basla_div[-3:]:
            
            if "YENİDEN BAŞLA" in div.text:
                basla_div[-2].click()
                break

            elif "Soru Sayısı" in div.text:
                basla_div[-1].click()
                break 

            elif "CEVAPLARIM" in div.text:
                basla_div[-3].click()
                break
            
            elif "YAZDIR" in div.text:
                basla_div[-1].click()
                break

    def cevaplari_isaretle(self, cevaplar):

        for soru_numarasi, soru_cevabi in cevaplar.items():
            soru_numarasi = soru_numarasi[4:]

            if soru_numarasi == "1":
                self._br.element(
                    (
                        AllLocators.sorular[0],
                        AllLocators.sorular[1].format(
                            soru_numarasi
                        )
                    ),
                    wait_=True
                )

                cevap = self.cevap_cevir(soru_cevabi)

                self._br.element(
                    (
                        AllLocators.cevaplar[0],
                        AllLocators.cevaplar[1].format(
                            soru_numarasi, 
                            cevap
                        ),
                    ),
                    wait_=True,
                    while_=True,
                    click_=True  
                )

                self.text_edit_signal.emit(f'<font color="green">{soru_numarasi}-) {soru_cevabi}</font>')
                

            else:
                self._br.element(
                    (
                        AllLocators.sorular[0],
                        AllLocators.sorular[1].format(
                            soru_numarasi
                        )
                    ),
                    wait_=True
                )
                
                cevap = self.cevap_cevir(soru_cevabi)
                self._br.element(
                    (
                        AllLocators.cevaplar[0],
                        AllLocators.cevaplar[1].format(
                            soru_numarasi, 
                            cevap
                        )
                    ),
                    wait_=True,
                    while_=True,
                    click_=True
                )

                self._br.element(
                    (
                        AllLocators.cevaplar[0],
                        AllLocators.cevaplar[1].format(
                            soru_numarasi, 
                            cevap
                        )
                    ),
                    wait_=True,
                    while_=True,
                    click_=True
                )

                self.text_edit_signal.emit(f'<font color="green">{soru_numarasi}-) {soru_cevabi}</font>')


    def testi_bitir(self):
        
        self._br.element(
            AllLocators.bitir_kapat,
            wait_=True,
            while_=True,
            click_=True
        )

        self._br.element(
            AllLocators.bitir_1,
            wait_=True,
            while_=True,
            click_=True
        )

        self._br.element(
            AllLocators.bitir_kapat,
            wait_=True,
            while_=True,
            click_=True
        )

        self._br.element(
            AllLocators.geri,
            wait_=True,
            while_=True,
            click_=True
        )
        
        self.text_edit_signal.emit(f'<font color="green">Testten Çıkıldı</font>')



    def testleri_yap(self, cevaplar):

        for unite_baslik, testler_bilgi in cevaplar.items():

            uniteler = self._br.element(
                AllLocators.unite_list,
                wait_=True,
                while_=True,
                click_=True
            )

            uniteler = self._br.element(
                AllLocators.unite_list,
                wait_=True
            )

            uniteler = uniteler.find_elements_by_tag_name("option")
            unite_sayisi = len(uniteler)

            for i in range(1, unite_sayisi + 1):
                unite_basliklari = self._br.element(
                    AllLocators.unite_option.format(i),
                    multiple=True
                )

                if unite_basliklari[0].text == unite_baslik:
                    unite_basliklari[0].click()
                    self.text_edit_signal.emit(f'<font color="green">Üniteye Girildi : {unite_baslik}</font>')
                    break

            test_sayisi = self.test_sayisi()

            for test_isim, numara_cevap in testler_bilgi.items():
                for test in range(2, test_sayisi - 1):
                    test_text = self._br.element(
                        (
                            AllLocators.testler_isim[0],
                            AllLocators.testler_isim[1].format(
                                test
                            )
                        ),
                        wait_=True,
                        while_=True
                    )

                    if test_text.text == test_isim:
                        test_text.click()
                        self.text_edit_signal.emit(f'<font color="green">Teste Girildi : {test_isim}</font>')
                        
                        self.text_edit_signal.emit(f'<font color="blue">Teste Başlanıyor...</font>')
                        self.teste_basla()

                        self.text_edit_signal.emit(f'<font color="blue">Cevaplar İşaretleniyor...</font>')
                        self._br.switch_to_frame(
                            AllLocators.frame
                        )
                        
                        self.cevaplari_isaretle(numara_cevap)

                        self.text_edit_signal.emit(f'<font color="green">Tüm Cevaplar İşaretlendi</font>')
                        self.text_edit_signal.emit(f'<font color="blue">Testten Çıkılıyor...</font>')
                        self.testi_bitir()
                        self.text_edit_signal.emit(f'<font color="red">{10*"<b>- - </b>"}</font>')

                        break


    def yap(self):
        try:
            if self.login(self.TC, self.password) == False:
                self.text_edit_signal.emit('<font color="green">Başarıyla giriş yapıldı</font>')
                self._br.br.get("https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.775/index.html#/main/testCenter/")
                self.tarama_testleri_click()
                self.okul_sinif_ders(self.okul, self.sinif, self.ders)
                self.testleri_yap(self.cevaplar) 
                self._br.br.quit()
                self.sonuc.emit("bitti")

            else:
                self.sonuc.emit("giriş başarısız")
                self.text_edit_signal.emit('<font color="red">Giriş Yapılamadı</font>')
                self._br.br.quit() 

        except TimeoutException:
            self.sonuc.emit("zaman aşımı")
            self.text_edit_signal.emit('<font color="red">Uygulama Zaman Aşımına Uğradı</font')
            self._br.br.quit()


