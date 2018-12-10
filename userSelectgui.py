from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
# import run_prog
import motogui2

pathSignal = QtCore.pyqtSignal(str)

class Ui_SelectUser(QtWidgets.QMainWindow):
    def setup_Ui(self, SelectUser):
        SelectUser.setObjectName("SelectUser")
        SelectUser.resize(414, 325)
        self.userCreateButton = QtWidgets.QPushButton(SelectUser)
        self.userCreateButton.setGeometry(QtCore.QRect(60, 270, 100, 32))
        self.userCreateButton.setText('Create User')
        self.userCreateButton.setObjectName('userCreateButton')

        self.userSelectButtonBox = QtWidgets.QDialogButtonBox(SelectUser)
        self.userSelectButtonBox.setGeometry(QtCore.QRect(170, 270, 171, 32))
        self.userSelectButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.userSelectButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.userSelectButtonBox.setObjectName("userSelectButtonBox")
        self.userDisplayList = QtWidgets.QListWidget(SelectUser)
        self.userDisplayList.setGeometry(QtCore.QRect(80, 60, 251, 131))
        self.userDisplayList.setAlternatingRowColors(True)
        self.userDisplayList.setObjectName("userDisplayList")
        self.userSelectLabel = QtWidgets.QLabel(SelectUser)
        self.userSelectLabel.setGeometry(QtCore.QRect(70, 20, 291, 31))
        self.userSelectLabel.setObjectName("userSelectLabel")
        self.newUserLabel = QtWidgets.QLabel(SelectUser)
        self.newUserLabel.setGeometry(QtCore.QRect(70, 220, 71, 21))
        self.newUserLabel.setObjectName("newUserLabel")
        self.newUserName = QtWidgets.QLineEdit(SelectUser)
        self.newUserName.setGeometry(QtCore.QRect(150, 220, 181, 25))
        self.newUserName.setPlaceholderText("")
        self.newUserName.setObjectName("newUserName")
        SelectUser.setWindowTitle('User Selection')

        self.userSelectButtonBox.accepted.connect(self.readUsers)
        self.userCreateButton.clicked.connect(self.createUser)

        # self.setDirectory()
        # preload list of users
        cwd = os.getcwd()  # get current working directory
        usersLoc = '{0}\\users'.format(cwd)  # format it with /users
        if not os.path.exists(usersLoc):  # check if users directory exists. Make it if it doesn't
            os.makedirs(usersLoc)
        os.chdir(usersLoc)  # at this point, the directory should exist so change to
        self.userDisplayList.addItems(os.listdir())

        # if self.userSelectButtonBox.accepted:
        #     self.close()

        self.retranslateUi(SelectUser)


        # self.userSelectButtonBox.accepted.connect(self.showLogger)
        # self.userSelectButtonBox.rejected.connect(SelectUser.reject)
        # QtCore.QMetaObject.connectSlotsByName(SelectUser)

    def setDirectory(self):
        ourDir = ""
        with open('sys-vars.txt') as f:
            for line in f:
                ourDir = line.rstrip()
        os.chdir(ourDir)


    def readUsers(self):
        # self.setDirectory()
        cwd = os.getcwd()  # get current working directory
        usersLoc = '{0}\\users'.format(cwd)  # format it with /users
        print('read user directory: ' + cwd)
        # if not os.path.exists(usersLoc):  # check if users directory exists. Make it if it doesn't
        #     os.makedirs(usersLoc)
        os.chdir(usersLoc)  # at this point, the directory should exist so change to user folder
        cwd = os.getcwd()
        indivUserPath = '{0}\\{1}'.format(cwd, self.userDisplayList.currentItem().text())
        if os.path.exists(indivUserPath):
            os.chdir(indivUserPath)  # at this point, we're inside of the correct users files
        else:
            self.info = QtWidgets.QMessageBox()
            self.info.setIcon(QtWidgets.QMessageBox.Critical)
            self.info.setText('Failed to find user path!')
            self.info.setWindowTitle('Critical Error')
            self.info.show()

        # self.setVisible(False)

        # self.close()

    def createUser(self):
        if self.newUserName.text() != "":
            self.userDisplayList.clear()
            # AT THIS POINT WE SHOULD BE INSIDE OF THE USER FOLDER!!!!!
            # check if user file exists
            cwd = os.getcwd()  # get current working directory
            user = self.newUserName.text()
            userFolderLoc = '{0}\\users\\{1}'.format(cwd, user)  # format it with 'u
            # if not, create user folder
            if not os.path.exists(userFolderLoc):  # check if username exists. Make folder if it doesn't
                os.makedirs(userFolderLoc)
                # change directory into newly created user folder
                os.chdir(userFolderLoc)
                filenames = ['issue-list.txt', 'my-garage.txt', 'suggested-times.txt', 'work-log.txt', 'ride-log.txt']
                # then, create all necessary text files inside of the folder
                for file in filenames:
                    newFile = open(os.path.join(os.getcwd(), file), 'w+')  # create each file if it doesn't exist already
                    newFile.close()
            else:
                self.info = QtWidgets.QMessageBox()
                self.info.setIcon(QtWidgets.QMessageBox.Warning)
                self.info.setText('This username is already taken!')
                self.info.setWindowTitle('Error creating user')
                self.info.show()

            self.setVisible(False)
            # self.initInfo()
            # call self.init Info to initialize user info. Should be blank tho since its a new user
        else:
            self.info = QtWidgets.QMessageBox()
            self.info.setIcon(QtWidgets.QMessageBox.Warning)
            self.info.setText('Must enter a username!')
            self.info.setWindowTitle('Username Error')
            self.info.show()

    def retranslateUi(self, SelectUser):
        _translate = QtCore.QCoreApplication.translate
        # SelectUser.setWindowTitle(_translate("SelectUser", "Dialog"))
        self.userDisplayList.setToolTip(_translate("SelectUser", "Select your username."))
        __sortingEnabled = self.userDisplayList.isSortingEnabled()
        self.userDisplayList.setSortingEnabled(False)
        self.userDisplayList.setSortingEnabled(__sortingEnabled)
        self.userSelectLabel.setText(_translate("SelectUser", "Select user from list or Create new user"))
        self.newUserLabel.setText(_translate("SelectUser", "New User"))
