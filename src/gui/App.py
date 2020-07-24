import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.main_ui import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow_ui = Ui_MainWindow()
    mainWindow_ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
