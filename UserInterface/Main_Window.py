import sys
import ActionReport, Configurations, Filter, GraphWindow
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PICK Tool"
        self.top = 600
        self.left = 300
        self.width = 680
        self.height = 580


        # Button Changes window to the Event Configuration window
        self.eventConfigButton = QtWidgets.QPushButton("Event Configuration", self)
        self.eventConfigButton.move(360, 150)
        self.eventConfigButton.resize(250, 40)
        self.eventConfigButton.setToolTip("<h5></h5>")

        self.eventConfigButton.clicked.connect(self.eventConfigButtonClicked)

        # Button 2 Changes window to the Enforcement Action Report window
        self.actionReportButton = QtWidgets.QPushButton("Enforcement Action Report", self)
        self.actionReportButton.move(80, 150)
        self.actionReportButton.resize(250, 40)
        self.actionReportButton.setToolTip("<h5></h5>")

        self.actionReportButton.clicked.connect(self.actionReportButtonClicked)

        # Button 3 Changes window to the Search/Filter window
        self.searchFilterButton = QtWidgets.QPushButton("Search/Filter", self)
        self.searchFilterButton.move(360, 200)
        self.searchFilterButton.resize(250, 40)
        self.searchFilterButton.setToolTip("<h5></h5>")

        self.searchFilterButton.clicked.connect(self.searchFilterButtonClicked)

        # Button 4 Changes window to the Manage Graph
        self.manageGraphButton = QtWidgets.QPushButton("Manage Graph", self)
        self.manageGraphButton.move(80, 200)
        self.manageGraphButton.resize(250, 40)
        self.manageGraphButton.setToolTip("<h5></h5>")

        self.manageGraphButton.clicked.connect(self.manageGraphButtonClicked)

        self.main_window()

    def main_window(self):

        self.label = QtWidgets.QLabel("<h3>PICK Tool</h3>", self)
        self.label.move(300, 80)
        self.label = QtWidgets.QLabel(self)

        pixmap = QtGui.QPixmap("pick0.png")
        lbl = QtWidgets.QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.move(400, 10)
        lbl.resize(128, 128)

        pixmap = QtGui.QPixmap("pick0.png")
        lbl = QtWidgets.QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.move(170, 10)
        lbl.resize(128, 128)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def searchFilterButtonClicked(self):
        self.filterWindow = QtWidgets.QMainWindow()
        Filter.FilterUi().setupUi(self.filterWindow)
        self.filterWindow.show()

    def manageGraphButtonClicked(self):
        self.graphWindow = QtWidgets.QMainWindow()
        GraphWindow.Ui_GrapWindow().setupUi(self.graphWindow)
        self.graphWindow.show()

    def eventConfigButtonClicked(self):
        self.eventConfigWindow = QtWidgets.QMainWindow()
        Configurations.ConfigurationsUi().generateUi(self.eventConfigWindow)
        self.eventConfigWindow.show()

    def actionReportButtonClicked(self):
        self.actionReportWindow = QtWidgets.QMainWindow()
        ActionReport.actionReport().generateUi(self.actionReportWindow)
        self.actionReportWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())
