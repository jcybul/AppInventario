
from PyQt5 import QtWidgets , uic 
import sys
from dbTools import get_database

class Login(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('login.ui', self) # Load the .ui file
        self.button = self.findChild(QtWidgets.QPushButton, 'login')
        self.passwordBar = self.findChild(QtWidgets.QLineEdit,'passwordField')
        self.button.clicked.connect(self.checkconnection)
        self.show()

    def checkconnection(self):
        text = self.passwordBar.text()
        if get_database(text) != "Error":
            self.accept()
        else:
            print("Wrong Password")


class Main(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent) # Call the inherited classes __init__ metho)
        uic.loadUi('main.ui', self)
        self.orderButton = self.findChild(QtWidgets.QPushButton, 'order')
        self.orderButton.clicked.connect(self.completeOrder)
        self.show()

    def completeOrder(self):
        print("Orden")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login() # Create an instance of our class
    
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Main()
        window.show()
        sys.exit(app.exec_())

