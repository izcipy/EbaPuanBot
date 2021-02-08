from PyQt5.QtWidgets import (QMenu, QAction, QStatusBar, QWidget, 
                            QMainWindow, QHBoxLayout, QFrame, QComboBox, 
                            QPushButton, QLineEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import (QIcon, QCursor, QPixmap)
from PyQt5.QtCore import (QSize, QRect, QThread, Qt)
from ARAYUZ.cevaplar.cevaplar import cevaplar_json
from ARAYUZ.parsers.text_parser import parser
from ARAYUZ.parsers.cevap_parser import Parcala
from EBA.browser import Browser
from ARAYUZ.threads import EbaThread
from ARAYUZ.alt_arayuz import App_1
import os

class App(QMainWindow):

    bekleme_suresi = 1500 #ms

    def __init__(self):
        super().__init__()


    def start_(self):
        Parcala(cevaplar_json).parcala_()
        Parcala(cevaplar_json).duzenle()
        self.parcala_run = Parcala.okul_ders_sinif

        self.setWindowTitle("Eba Puan Kasma Bot")
        self.setObjectName("MainWindow")
        self.resize(704, 594)
        self.setMaximumSize(QSize(704, 594))
        self.setMinimumSize(QSize(704, 594))
        self.setWindowIcon(QIcon("icons/eba.png"))
        self.create_menu_bar()
        self.create_status_bar()
        self.tema = "ARAYUZ/themes/style_black.css"
        self.setUi()
        self.oto_chromedriver_sec()
        
        self.show()

    def create_menu_bar(self):

        self.menuBar_ = self.menuBar()

        ayarlar = self.menuBar_.addMenu("Ayarlar")
        ayarlar.setToolTip("Uygulama Ayarları") 

        tema_degistir = QMenu(self.menuBar_)
        tema_degistir.setTitle("Tema Değiştir")
        tema_degistir.setIcon(QIcon("icons/theme.png")) 

        karanlik_tema = QAction(self)
        karanlik_tema.setText("Karanlık Tema")

        kirmizi_tema = QAction(self)
        kirmizi_tema.setText("Kırmızı Tema")

        tema_degistir.addAction(karanlik_tema)
        tema_degistir.addAction(kirmizi_tema)

        ayarlar.addMenu(tema_degistir)
        ayarlar.triggered.connect(self.Menuler_islem)

        yardim = self.menuBar_.addMenu("Yardım")
        yardim.setToolTip("Yardım")

        hakkinda = QAction(self)
        hakkinda.setText("Eba Puan Bot Hakkında")
        hakkinda.setIcon(QIcon("icons/eba.png")) 

        yardim.addAction(hakkinda)
        yardim.triggered.connect(self.Menuler_islem)

    def create_status_bar(self):
        self.status_bar = QStatusBar(self)
        self.status_bar.setObjectName("statusbar")
        self.setStatusBar(self.status_bar)

    def create_layout(self):
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QRect(10, 140, 591, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

    def create_frame(self):
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(45, 90, 611, 451))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame1")

    def create_central_widget(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget") 


    def create_combobox(self):

        self.combobox_1 = QComboBox(self.horizontalLayoutWidget)
        self.combobox_1.setObjectName("comboBox")
        self.combobox_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.combobox_1)

        self.combobox_2 = QComboBox(self.horizontalLayoutWidget)
        self.combobox_2.setObjectName("comboBox")
        self.combobox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.combobox_2)

        self.combobox_3 = QComboBox(self.horizontalLayoutWidget)
        self.combobox_3.setObjectName("comboBox")
        self.combobox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.combobox_3)

        self.combobox_1.insertItem(0, QIcon(self.school_png), " Okul Seçiniz...")
        self.combobox_2.insertItem(0, QIcon(self.class_png), " Sınıf Seçiniz...")
        self.combobox_3.insertItem(0, QIcon(self.ders_png), " Ders Seçiniz...")

        self.combobox_1.addItems(self.okullar())
        self.combobox_2.setDisabled(True)
        self.combobox_3.setDisabled(True)

        self.combobox_1.activated["int"].connect(self.combobox_1_activated)
        self.combobox_2.activated["int"].connect(self.combobox_2_activated)
        self.combobox_3.activated["int"].connect(self.combobox_3_activated)


    def create_push_button(self):
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setText("Puan Kas")
        self.pushButton.setGeometry(QRect(30, 390, 551, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.tikla)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setText("Driver Seç")
        self.pushButton_2.setGeometry(QRect(64, 80, 481, 31))
        self.pushButton_2.setObjectName("pushButton1")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        
        self.ebalogo = QPushButton(self.centralwidget)
        self.ebalogo.setGeometry(QRect(300, 30, 100, 101))
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/eba.png"), QIcon.Normal, QIcon.Off)
        self.ebalogo.setIcon(icon)
        self.ebalogo.setIconSize(QSize(60, 60))
        self.ebalogo.setCheckable(False)
        self.ebalogo.setObjectName("ebalogo")

    def create_line_edit(self):
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setPlaceholderText("Kimlik No")
        self.lineEdit.setGeometry(QRect(40, 220, 531, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setPlaceholderText("Şifre")
        self.lineEdit_2.setGeometry(QRect(40, 280, 531, 51))
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True) 

    def create_file_dialog(self):
        self.file_dialog_1 = QFileDialog()

        self.pushButton_2.clicked.connect(self.chromedriver_sec)

    def setUi(self):

        self.setStyleSheet(open(self.tema, "r", encoding="utf8").read())

        self.ders_png = "icons/ders.png"
        self.class_png = "icons/class.png"
        self.school_png = "icons/school.png" 

        self.create_central_widget() 
        self.create_frame() 
        self.create_layout() 
        self.create_combobox()
        self.create_push_button()
        self.create_file_dialog()
        self.create_line_edit()
        self.setCentralWidget(self.centralwidget) 


    def Menuler_islem(self, action):
        action_text = action.text()

        if action_text == "Karanlık Tema":
            self.tema = "ARAYUZ/themes/style_black.css"
            self.setStyleSheet(open(self.tema, "r", encoding="utf8").read())

        elif action_text == "Kırmızı Tema":
            self.tema = "ARAYUZ/themes/style_red.css"
            self.setStyleSheet(open(self.tema, "r", encoding="utf8").read())

        elif action_text == "Eba Puan Bot Hakkında":
            QMessageBox.about(
                self,
                "deneme",
                parser("font", "hakkında")
            ) 

    def oto_chromedriver_sec(self):
        dosyalar = os.listdir()
        if "chromedriver.exe" in dosyalar:
            self.file_dialog_1.selectFile("chromedriver.exe")
            self.pushButton_2.setText("Driver Seçildi(chromedriver.exe)")

        else:
            pass

    def chromedriver_sec(self):
        options = self.file_dialog_1.Options()
        options |= self.file_dialog_1.DontUseNativeDialog
        filename, _ = self.file_dialog_1.getOpenFileName(
            self,
            "Dosya Aç",
            ".",
            "Tüm Dosyalar (*);;Exe Dosyaları (*.exe)",
            options=options
        ) 

        if filename:
            self.pushButton_2.setText(f"Driver Seçildi({filename})") 
            self.status_bar.showMessage(
                f"Driver Seçildi : {filename}",
                self.bekleme_suresi
            ) 


    def combobox_1_activated(self, selected_index):
        if selected_index == 0:
            self.status_bar.showMessage("Lütfen başka bir seçenek seçin", self.bekleme_suresi)
            self.combobox_1.showPopup() 
            self.combobox_2.clear()
            self.combobox_2.insertItem(0, QIcon(self.class_png), " Sınıf Seçiniz...")
            self.combobox_2.setDisabled(True)
            self.combobox_3.clear()
            self.combobox_3.insertItem(0, QIcon(self.ders_png), " Ders Seçiniz...")
            self.combobox_3.setDisabled(True)

        else:
            self.combobox_2.clear()
            okul_text = self.combobox_1.itemText(selected_index)
            self.status_bar.showMessage(f"Okul Seçildi : {okul_text}", self.bekleme_suresi)
            self.combobox_2.insertItem(0, QIcon(self.class_png), " Sınıf Seçiniz...")
            self.combobox_2.addItems(self.siniflar(okul_text))
            self.combobox_2.setDisabled(False)
            self.combobox_2.showPopup() 


    def combobox_2_activated(self, selected_index):
        if selected_index == 0:
            self.status_bar.showMessage("Lütfen başka bir seçenek seçin", self.bekleme_suresi)
            self.combobox_2.showPopup()
            self.combobox_3.clear()
            self.combobox_3.insertItem(0, QIcon(self.ders_png), " Ders Seçiniz...")
            self.combobox_3.setDisabled(True)

        else:
            self.combobox_3.clear()
            okul_text = self.combobox_1.currentText()
            sinif_text = self.combobox_2.itemText(selected_index)
            self.status_bar.showMessage(f"Sınıf Seçildi : {sinif_text}", self.bekleme_suresi) 
            self.combobox_3.insertItem(0, QIcon(self.ders_png), " Ders Seçiniz...")
            self.combobox_3.addItems(self.dersler(okul_text, sinif_text))
            self.combobox_3.setDisabled(False)
            self.combobox_3.showPopup() 

    def combobox_3_activated(self, selected_index):
        if selected_index == 0:
            self.status_bar.showMessage("Lütfen başka bir seçenek seçin", self.bekleme_suresi)
            self.combobox_3.showPopup()

        else:
            ders_text = self.combobox_3.itemText(selected_index)
            self.status_bar.showMessage(f"Ders Seçildi : {ders_text}", self.bekleme_suresi)
            
    def arayuz_degistir_1(self):
        self.widget.hide() 
        self.status_bar.show() 
        self.menuBar_.show() 
        self.setUi() 

    def arayuz_degistir_2(self):
        self.widget = App_1(self.arayuz_degistir_1)
        self.geri_button = self.widget.pushButton3
        self.status_bar.hide()
        self.menuBar_.hide()
        self.centralwidget.hide()
        self.update() 
        self.setCentralWidget(self.widget)
        #self.setStyleSheet(open("ARAYUZ/themes/style1.css", "r", encoding="utf8").read())


    def tikla(self):
        if self.combobox_1.currentIndex() == 0:
            self.status_bar.showMessage("Lütfen okul seçiniz", self.bekleme_suresi)
            self.combobox_1.showPopup()

        elif self.combobox_2.currentIndex() == 0:
            self.status_bar.showMessage("Lütfen sınıf seçiniz", self.bekleme_suresi)
            self.combobox_2.showPopup()

        elif self.combobox_3.currentIndex() == 0:
            self.status_bar.showMessage("Lütfen ders seçiniz", self.bekleme_suresi)
            self.combobox_3.showPopup()

        elif "(" not in self.pushButton_2.text():
            QMessageBox.about(
                self,
                "Driver Dosyası Seçilmedi",
                parser("font", "driver yok")
            )

        elif len(self.lineEdit.text()) == 0:
            QMessageBox.about(
                self,
                "Kimlik No Girilmedi",
                parser("font", "TC yok")
            ) 

        elif len(self.lineEdit_2.text()) == 0:
            QMessageBox.about(
                self,
                "Şifre Girilmedi",
                parser("font", "şifre yok")
            )

        else:
            #_ = QWidget(self)
            #self.setCentralWidget(_) 

            self.arayuz_degistir_2()

            
            okul = self.combobox_1.currentText() 
            sinif = self.combobox_2.currentText() 
            ders = self.combobox_3.currentText() 
            chromedriver_path = self.pushButton_2.text().split("(")[-1][:-1]
            TC = self.lineEdit.text()
            password = self.lineEdit_2.text()

            self._thread = QThread(self)
            self.eba_thread = EbaThread(
                chromedriver_path,
                Browser,
                TC,
                password,
                okul,
                sinif,
                ders,
                cevaplar_json
            ) 
            self.eba_thread.moveToThread(self._thread)
            self._thread.finished.connect(self.eba_thread.deleteLater)
            self._thread.started.connect(self.eba_thread.run)
            self.eba_thread.sonuc.connect(self.bitti)
            self.eba_thread.text_edit_signal.connect(self.text_edit_append)
            self._thread.start()

    def text_edit_append(self, text):
        self.widget.text_edit.append(text)

    def bitti(self, deger):

        if deger == "driver hata":
            self._thread.quit()
            self.arayuz_degistir_1()
            self.geri_button.setDisabled(False)
            QMessageBox.about(
                self,
                "Driver Çalıştırılamadı",
                parser("font", "driver hata")
            )

        elif deger == "giriş başarısız":
            self._thread.quit()
            self.geri_button.setDisabled(False)
            QMessageBox.about(
                self,
                "Giriş Başarısız",
                parser("font", "giriş yapılamadı")
            ) 

        elif deger == "zaman aşımı":
            self._thread.quit()
            self.geri_button.setDisabled(False)
            QMessageBox.about(
                self,
                "Zaman Aşımı",
                parser("font", "zaman aşımı")
            ) 
            
        elif deger == "bitti":
            self.geri_button.setDisabled(False)
            QMessageBox.about(
                self,
                "Program Sonlandı",
                parser("font", "bitti")
            )
            
    def okullar(self):
        okullar = []
        
        for okul in self.parcala_run.keys():
            okullar.append(okul) 

        return okullar

    def siniflar(self, okul):
        siniflar = []

        for sinif in self.parcala_run[okul].keys():
            siniflar.append(sinif)

        return siniflar

    def dersler(self, okul, sinif):
        return self.parcala_run[okul][sinif]


