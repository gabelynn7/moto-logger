# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from main_gui import Ui_MainWindow
#
# app = QApplication(sys.argv)
# window = QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(window)
#
# window.show()
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
# from main_gui import Ui_MainWindow
from motogui2 import Ui_MainWindow
from PyQt5 import QtWidgets
import random
import moto_facts


# class MotoGui(QMainWindow):
#     def __init__(self):
#         super(MotoGui, self).__init__()
#
#         # Set up the user interface from Designer.
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

        # Make some local modifications.
        #self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        # self.ui.okButton.clicked.connect(self.accept)
        # self.ui.cancelButton.clicked.connect(self.reject)


# from PyQt5.QtWidgets import QMainWindow


# class Logic(QMainWindow, Ui_MainWindow):
# class Logic(QMainWindow, Ui_MotoMaintenanceLogger):
#     def __init__(self, *args, **kwargs):
#         QMainWindow.__init__(self, *args, **kwargs)
#         # self.randFact()
#         QtWidgets.QMessageBox.about(self, "Random Motorcycle Fact!", random.choice(moto_facts.random_fact))
#         self.setupUi(self)
#         print('finished init')
#
#     def randFact(self):
#         print('I\'m in here')
#         QtWidgets.QMessageBox.about(self, "Random Motorcycle Fact!", random.choice(moto_facts.random_fact))

    # def closeEvent(self, event):
    #     print('I\'m in the close event!')
    #     answer = QtWidgets.QMessageBox.question(
    #         self,
    #         'Are you sure you want to quit ?',
    #         'Task is in progress !',
    #         QtWidgets.QMessageBox.Yes,
    #         QtWidgets.QMessageBox.No)
    #     if answer == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
