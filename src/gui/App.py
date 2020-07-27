import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from algorithm.DataHandler import DataHandler
from gui.main_ui import Ui_MainWindow

if __name__ == '__main__':
    # 算法层启动
    dataHandler = DataHandler('./input_data/origin_data.txt')
    BGM = []  # 记录每一类推荐的BGM类型
    for i in range(9):
        BGM.append(dataHandler.getMusicType(i))

    # 应用层启动
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow_ui = Ui_MainWindow()
    mainWindow_ui.setupUi(mainWindow, BGM)
    mainWindow.show()
    sys.exit(app.exec_())
