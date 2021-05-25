from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

def convertirAListaNums(listaDeStrings):
    return np.float_(list(listaDeStrings.split(" ")))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_convolucionador = QtWidgets.QLabel(self.centralwidget)
        self.label_convolucionador.setGeometry(QtCore.QRect(500, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_convolucionador.setFont(font)
        self.label_convolucionador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_convolucionador.setObjectName("label_convolucionador")

        self.groupBox_parametros = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_parametros.setGeometry(QtCore.QRect(40, 80, 1161, 163))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_parametros.setFont(font)
        self.groupBox_parametros.setObjectName("groupBox_parametros")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_parametros)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.label_valoresF = QtWidgets.QLabel(self.groupBox_parametros)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_valoresF.setFont(font)
        self.label_valoresF.setObjectName("label_valoresF")
        self.gridLayout.addWidget(self.label_valoresF, 0, 2, 1, 1)

        self.label_valoresG = QtWidgets.QLabel(self.groupBox_parametros)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_valoresG.setFont(font)
        self.label_valoresG.setObjectName("label_valoresG")
        self.gridLayout.addWidget(self.label_valoresG, 1, 2, 1, 1)

        self.lineEdit_imagenG = QtWidgets.QLineEdit(self.groupBox_parametros)
        self.lineEdit_imagenG.setObjectName("lineEdit_imagenG")
        self.gridLayout.addWidget(self.lineEdit_imagenG, 1, 3, 1, 1)

        self.lineEdit_nf = QtWidgets.QLineEdit(self.groupBox_parametros)
        self.lineEdit_nf.setObjectName("lineEdit_nf")
        self.gridLayout.addWidget(self.lineEdit_nf, 0, 1, 1, 1)

        self.lineEdit_imagenF = QtWidgets.QLineEdit(self.groupBox_parametros)
        self.lineEdit_imagenF.setObjectName("lineEdit_imagenF")
        self.gridLayout.addWidget(self.lineEdit_imagenF, 0, 3, 1, 1)

        self.lineEdit_ng = QtWidgets.QLineEdit(self.groupBox_parametros)
        self.lineEdit_ng.setObjectName("lineEdit_ng")
        self.gridLayout.addWidget(self.lineEdit_ng, 1, 1, 1, 1)

        self.label_nNoNuloG = QtWidgets.QLabel(self.groupBox_parametros)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nNoNuloG.setFont(font)
        self.label_nNoNuloG.setObjectName("label_nNoNuloG")
        self.gridLayout.addWidget(self.label_nNoNuloG, 1, 0, 1, 1)

        self.label_nNoNuloF = QtWidgets.QLabel(self.groupBox_parametros)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nNoNuloF.setFont(font)
        self.label_nNoNuloF.setObjectName("label_nNoNuloF")
        self.gridLayout.addWidget(self.label_nNoNuloF, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_calcular = QtWidgets.QPushButton(self.groupBox_parametros, clicked = lambda: self.onPress())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_calcular.sizePolicy().hasHeightForWidth())
        self.pushButton_calcular.setSizePolicy(sizePolicy)
        self.pushButton_calcular.setObjectName("pushButton_calcular")
        self.verticalLayout.addWidget(self.pushButton_calcular)

        self.widget_pestaniaPloteo = QtWidgets.QWidget(self.centralwidget)
        self.widget_pestaniaPloteo.setGeometry(QtCore.QRect(40, 260, 1161, 541))
        self.widget_pestaniaPloteo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_pestaniaPloteo.setObjectName("widget_pestaniaPloteo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.lineEdit_nf, self.lineEdit_imagenF)
        MainWindow.setTabOrder(self.lineEdit_imagenF, self.lineEdit_ng)
        MainWindow.setTabOrder(self.lineEdit_ng, self.lineEdit_imagenG)
        MainWindow.setTabOrder(self.lineEdit_imagenG, self.pushButton_calcular)

    def onPress(self):
        nf = int(self.lineEdit_nf.text())
        imagenF = convertirAListaNums(self.lineEdit_imagenF.text())
        dominioF = np.arange(nf, len(imagenF) + nf, 1)

        ng = int(self.lineEdit_ng.text())
        imagenG = convertirAListaNums(self.lineEdit_imagenG.text())
        dominioG = np.arange(ng, len(imagenG) + ng, 1)

        imagenConvolucion = np.convolve(imagenF, imagenG)
        anchoPulso = len(imagenF) + len(imagenG) - 1
        primerN = nf + ng
        dominioConvolucion = np.arange(primerN, anchoPulso + primerN, 1)

        for i in imagenConvolucion:
            print(i)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convolucionador"))
        self.label_convolucionador.setText(_translate("MainWindow", "Convolucionador"))
        self.groupBox_parametros.setTitle(_translate("MainWindow", "Parámetros"))
        self.label_valoresF.setText(_translate("MainWindow", "Valores f[n]"))
        self.label_valoresG.setText(_translate("MainWindow", "Valores g[n]"))
        self.label_nNoNuloG.setText(_translate("MainWindow", "Primer n no nulo de g[n]"))
        self.label_nNoNuloF.setText(_translate("MainWindow", "Primer n no nulo de f[n]"))
        self.pushButton_calcular.setText(_translate("MainWindow", "Calcular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
