import sys
import numpy as np

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi('app.ui', self)
        self.ui.pushButton_calcular.clicked.connect(self.onClick)
    
    @pyqtSlot()
    def onClick(self):
        # Obtener informacion
        try:
            nf = int(self.ui.lineEdit_nf.text())
        except ValueError:
            nf = 0

        try:
            ng = int(self.lineEdit_ng.text())
        except ValueError:
            ng = 0
        
        try:
            imagenF = self.convertirAListaNums(self.ui.lineEdit_imagenF.text())
            dominioF = np.arange(nf, len(imagenF) + nf, 1)
            imagenG = self.convertirAListaNums(self.lineEdit_imagenG.text())
            dominioG = np.arange(ng, len(imagenG) + ng, 1)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Los valores de las funciones no pueden contener letras.')
            return
        

        imagenConvolucion = np.convolve(imagenF,imagenG)
        anchoPulso = len(imagenF) + len(imagenG) - 1
        primerN = nf + ng
        dominioConvolucion = np.arange(primerN, anchoPulso + primerN, 1)

        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.stem(dominioF, imagenF, '.', label='f[n]', markerfmt='C0o')
        ax1.stem(dominioG, imagenG, '.', label='g[n]', markerfmt='C1o', linefmt='C1--')
        ax1.set_title('Grafica de f[n] y g[n]')
        ax1.set_xticks(dominioF[ : : 1])
        ax1.grid(color='#0066cc', ls='--', lw=0.1)
        ax1.ticklabel_format(style='plain', axis='y')
        ax1.legend()
        ax1.axhline(y=0, color='k')
        ax1.axvline(x=0, color='k')

        ax2.stem(dominioConvolucion, imagenConvolucion, '.', label='f*g[n]', markerfmt='ro', linefmt='r-')
        ax2.set_title('Convolucion entre las dos funciones')
        ax2.set_xticks(dominioConvolucion[ : : 1])
        ax2.grid(which='major', axis='both', color='#0066cc', ls='--', lw=0.1)
        ax2.ticklabel_format(style='plain', axis='y')
        ax2.legend()
        ax2.axhline(y=0, color='k')
        ax2.axvline(x=0, color='k')

        plt.tight_layout()
        
        # plot
        self.plotWidget = FigureCanvas(fig)

        # Borrando el plot anterior
        for i in reversed(range(self.ui.gridLayout_2.count())): 
            self.ui.gridLayout_2.itemAt(i).widget().setParent(None)

        # Agregando el nuevo grafico
        self.ui.gridLayout_2.addWidget(self.plotWidget)
            
    def convertirAListaNums(self, listaDeStrings):
        return np.float_(listaDeStrings.split())

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
