from PyQt5.QtWidgets import *

def openWindow():
    window = QDialog()

    currencyLbl = QLabel("СНВ:")
    currencyEdit = QLineEdit()

    dateLbl = QLabel("Дата:")
    dateEdit = QLineEdit()

    mainLine = QVBoxLayout()
    extraLine1 = QHBoxLayout()
    extraLine2 = QHBoxLayout()

    extraLine1.addWidget(currencyLbl)
    extraLine1.addWidget(currencyEdit)
    mainLine.addLayout(extraLine1)


    extraLine2.addWidget(dateLbl)
    extraLine2.addWidget(dateEdit)
    mainLine.addLayout(extraLine2)