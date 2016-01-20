from PyQt4 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("mainwindow.ui") # type: <class 'PyQt4.QtGui.QWidget'>

window.show()
sys.exit(app.exec_())