import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import *

class Window5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enforcement Action Report")
        #Window Dimensions
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580
        self.setGeometry(self.top, self.left, self.width, self.height)

class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Event Configuration")
        #Window Dimensions
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580
        self.setGeometry(self.top, self.left, self.width, self.height)


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Graph")
        #Window Dimensions
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580
        self.setGeometry(self.top, self.left, self.width, self.height)


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search/Filter")

        #Window Dimensions
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580
        self.setGeometry(self.top, self.left, self.width, self.height)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PICK Tool"
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580


        # Button Changes window to the Event Configuration window
        self.pushButton = QPushButton("Event Configuration", self)
        self.pushButton.move(360, 150)
        self.pushButton.resize(250, 40)
        self.pushButton.setToolTip("<h5></h5>")

        self.pushButton.clicked.connect(self.window4)

        # Button 2 Changes window to the Enforcement Action Report window
        self.pushButton2 = QPushButton("Enforcement Action Report", self)
        self.pushButton2.move(80, 150)
        self.pushButton2.resize(250, 40)
        self.pushButton2.setToolTip("<h5></h5>")

        self.pushButton2.clicked.connect(self.window5)

        # Button 3 Changes window to the Search/Filter window
        self.pushButton3 = QPushButton("Search/Filter", self)
        self.pushButton3.move(360, 200)
        self.pushButton3.resize(250, 40)
        self.pushButton3.setToolTip("<h5></h5>")

        self.pushButton3.clicked.connect(self.window2)

        # Button 4 Changes window to the Manage Graph
        self.pushButton4 = QPushButton("Manage Graph", self)
        self.pushButton4.move(80, 200)
        self.pushButton4.resize(250, 40)
        self.pushButton4.setToolTip("<h5></h5>")

        self.pushButton4.clicked.connect(self.window3)

        self.main_window()

    def main_window(self):

        self.label = QLabel("<h3>PICK Tool</h3>", self)
        self.label.move(300, 80)
        self.label = QLabel(self)

        pixmap = QPixmap("pick0.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.move(400, 10)
        lbl.resize(128, 128)

        pixmap = QPixmap("pick0.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.move(170, 10)
        lbl.resize(128, 128)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()

    def window3(self):
        self.w = Window3()
        self.w.show()
        self.hide()

    def window4(self):
        self.w = Window4()
        self.w.show()
        self.hide()

    def window5(self):
        self.w = Window5()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())