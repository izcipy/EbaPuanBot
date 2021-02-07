from PyQt5.QtWidgets import QApplication
from ARAYUZ.ana_arayuz import App


if __name__ == "__main__":
    uygulama = QApplication([])
    App = App(); App.start_()
    uygulama.exec_() 
