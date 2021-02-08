from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, 
                             QTextEdit, QPushButton)
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap


class App_1(QWidget):

    def __init__(self, arayuz):
        super().__init__()
        self.arayuz = arayuz
        self.setUi()
        self.resize(704, 594)
        self.setMinimumSize(QSize(704, 594))
        self.setMaximumSize(QSize(704, 594))


    def setUi(self):

        self.setObjectName("centralwidget")

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(False)
        self.text_edit.setGeometry(QRect(11, 70, 679, 511))
        self.text_edit.setObjectName("textEdit")
        
        """self.pushButton2 = QPushButton(self)
        self.pushButton2.setGeometry(QRect(10, 551, 679, 36))
        self.pushButton2.setText("Sonlandır")
        self.pushButton2.setObjectName("pushButton2")"""
        
        
        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 10, 679, 60))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("<b>EBA PUAN KASMA BOT</b>")
        self.label.setObjectName("label")
        
        self.pushButton3 = QPushButton(self)
        self.pushButton3.setDisabled(True)
        self.pushButton3.setGeometry(QRect(20, 13, 60, 50))
        self.pushButton3.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/back.png"), QIcon.Normal, QIcon.Off)
        self.pushButton3.setIcon(icon)
        self.pushButton3.setIconSize(QSize(30, 30))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.clicked.connect(self.arayuz)



