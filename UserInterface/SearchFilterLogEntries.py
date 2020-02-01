from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_SearchFilterWindow(object):
    def generateUi(self, SearchFilterWindow):
        SearchFilterWindow.setObjectName("SearchFilterWindow")
        SearchFilterWindow.resize(627, 659)

        # Create the layout objects that live in this window
        self.mainHorizontalView = QtWidgets.QWidget(SearchFilterWindow)
        self.mainHorizontalView.setObjectName("mainHorizontalView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainHorizontalView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchResultsLayout = QtWidgets.QGroupBox(self.mainHorizontalView)
        self.searchResultsLayout.setObjectName("searchResultsLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.searchResultsLayout)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchEditLayout = QtWidgets.QFormLayout()
        self.searchEditLayout.setObjectName("searchEditLayout")

        # Set up search fields with labels in the form layout
        self.searchBoxLabel = QtWidgets.QLabel(self.searchResultsLayout)
        self.searchBoxLabel.setObjectName("searchBoxLabel")
        self.searchEditLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.searchBoxLabel)
        self.searchBox = QtWidgets.QLineEdit(self.searchResultsLayout)
        self.searchBox.setObjectName("searchBox")

        self.searchEditLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchBox)
        self.searchStartDateLabel = QtWidgets.QLabel(self.searchResultsLayout)
        self.searchStartDateLabel.setObjectName("searchStartDateLabel")
        self.searchEditLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.searchStartDateLabel)

        # Set initial properties for start time/date picker
        self.searchStartDateTime = QtWidgets.QDateTimeEdit(self.searchResultsLayout)
        self.searchStartDateTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.searchStartDateTime.setProperty("showGroupSeparator", False)
        self.searchStartDateTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.searchStartDateTime.setDate(QtCore.QDate(2020, 1, 1))
        self.searchStartDateTime.setCalendarPopup(True)
        self.searchStartDateTime.setCurrentSectionIndex(0)
        self.searchStartDateTime.setObjectName("searchStartDateTime")

        self.searchEditLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.searchStartDateTime)
        self.searchEndDateLabel = QtWidgets.QLabel(self.searchResultsLayout)
        self.searchEndDateLabel.setObjectName("searchEndDateLabel")
        self.searchEditLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.searchEndDateLabel)

        # Set initial properties for end time/date picker
        self.searchEndDateTime = QtWidgets.QDateTimeEdit(self.searchResultsLayout)
        self.searchEndDateTime.setDate(QtCore.QDate(2020, 1, 1))
        self.searchEndDateTime.setCalendarPopup(True)
        self.searchEndDateTime.setCurrentSectionIndex(0)
        self.searchEndDateTime.setObjectName("searchEndDateTime")

        # Create check boxes for team selection in search
        self.searchEditLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.searchEndDateTime)
        self.searchRed = QtWidgets.QCheckBox(self.searchResultsLayout)
        self.searchRed.setObjectName("searchRed")
        self.searchEditLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.searchRed)
        self.searchWhite = QtWidgets.QCheckBox(self.searchResultsLayout)
        self.searchWhite.setObjectName("searchWhite")
        self.searchEditLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.searchWhite)
        self.searchBlue = QtWidgets.QCheckBox(self.searchResultsLayout)
        self.searchBlue.setObjectName("searchBlue")
        self.searchEditLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.searchBlue)

        # Add the Search Clear button
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchClear = QtWidgets.QPushButton(self.searchResultsLayout)
        self.searchClear.setObjectName("searchClear")
        self.horizontalLayout_4.addWidget(self.searchClear)

        # Add the Search Apply button
        self.searchApply = QtWidgets.QPushButton(self.searchResultsLayout)
        self.searchApply.setAutoExclusive(False)
        self.searchApply.setObjectName("searchApply")
        self.horizontalLayout_4.addWidget(self.searchApply)

        self.searchEditLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(self.searchResultsLayout)
        self.label.setObjectName("label")
        self.searchEditLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3.addLayout(self.searchEditLayout)

        # Set up the tree view that displays search results
        self.searchResultsView = QtWidgets.QTreeWidget(self.searchResultsLayout)
        self.searchResultsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.searchResultsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.searchResultsView.setAlternatingRowColors(True)
        self.searchResultsView.setHeaderHidden(False)
        self.searchResultsView.setObjectName("searchResultsView")

        # Create empty spaces to add data
        for i in range(5):
            QtWidgets.QTreeWidgetItem(self.searchResultsView)

        self.horizontalLayout_3.addWidget(self.searchResultsView)
        self.verticalLayout.addWidget(self.searchResultsLayout)

        self.vectorViewLayout = QtWidgets.QGroupBox(self.mainHorizontalView)
        self.vectorViewLayout.setObjectName("vectorViewLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.vectorViewLayout)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.vectorSelect = QtWidgets.QComboBox(self.vectorViewLayout)
        self.vectorSelect.setObjectName("vectorSelect")
        self.vectorSelect.addItem("")
        self.vectorSelect.addItem("")
        self.vectorSelect.addItem("")
        self.vectorSelect.addItem("")
        self.vectorSelect.addItem("")

        self.horizontalLayout.addWidget(self.vectorSelect)

        self.vectorSelectConfirm = QtWidgets.QPushButton(self.vectorViewLayout)
        self.vectorSelectConfirm.setCheckable(False)
        self.vectorSelectConfirm.setObjectName("vectorSelectConfirm")

        self.horizontalLayout.addWidget(self.vectorSelectConfirm)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.vectorView = QtWidgets.QTreeWidget(self.vectorViewLayout)
        self.vectorView.setAlternatingRowColors(True)
        self.vectorView.setObjectName("vectorView")

        # Create empty spaces to add data
        for i in range(10):
            QtWidgets.QTreeWidgetItem(self.vectorView)

        self.verticalLayout_4.addWidget(self.vectorView)
        self.verticalLayout.addWidget(self.vectorViewLayout)

        SearchFilterWindow.setCentralWidget(self.mainHorizontalView)

        # Create the menu bar to jump between windows
        self.menubar = QtWidgets.QMenuBar(SearchFilterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")

        self.menuJump_to = QtWidgets.QMenu(self.menubar)
        self.menuJump_to.setObjectName("menuJump_to")

        SearchFilterWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(SearchFilterWindow)
        self.statusbar.setObjectName("statusbar")

        SearchFilterWindow.setStatusBar(self.statusbar)

        self.actionEvent_Configuration = QtWidgets.QAction(SearchFilterWindow)
        self.actionEvent_Configuration.setObjectName("actionEvent_Configuration")

        self.actionEnforcement_Action_Report = QtWidgets.QAction(SearchFilterWindow)
        self.actionEnforcement_Action_Report.setObjectName("actionEnforcement_Action_Report")

        self.actionSearch_Filter_Log_Entries = QtWidgets.QAction(SearchFilterWindow)
        self.actionSearch_Filter_Log_Entries.setObjectName("actionSearch_Filter_Log_Entries")

        self.actionManage_Graph = QtWidgets.QAction(SearchFilterWindow)
        self.actionManage_Graph.setObjectName("actionManage_Graph")

        self.menuJump_to.addAction(self.actionEvent_Configuration)
        self.menuJump_to.addAction(self.actionEnforcement_Action_Report)
        self.menuJump_to.addAction(self.actionSearch_Filter_Log_Entries)
        self.menuJump_to.addAction(self.actionManage_Graph)

        self.menubar.addAction(self.menuJump_to.menuAction())

        self.addData(SearchFilterWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchFilterWindow)

    def addData(self, SearchFilterWindow):
        insert = QtCore.QCoreApplication.translate
        SearchFilterWindow.setWindowTitle(insert("SearchFilterWindow", "Search/Filter Log Entries"))

        # Insert text into search field buttons and labels
        self.searchResultsLayout.setTitle(insert("SearchFilterWindow", "Search Results"))
        self.searchBoxLabel.setText(insert("SearchFilterWindow", "Search"))
        self.searchStartDateLabel.setText(insert("SearchFilterWindow", "Start Date"))
        self.searchEndDateLabel.setText(insert("SearchFilterWindow", "End Date"))
        self.searchRed.setText(insert("SearchFilterWindow", "Red"))
        self.searchWhite.setText(insert("SearchFilterWindow", "White"))
        self.searchBlue.setText(insert("SearchFilterWindow", "Blue"))
        self.searchClear.setText(insert("SearchFilterWindow", "Clear Filters"))
        self.searchApply.setText(insert("SearchFilterWindow", "Apply Filters"))
        self.label.setText(insert("SearchFilterWindow", "Team"))

        # Set header columns on search results
        self.searchResultsView.headerItem().setText(0, insert("SearchFilterWindow", "Log ID"))
        self.searchResultsView.headerItem().setText(1, insert("SearchFilterWindow", "Time of Occurance"))
        self.searchResultsView.headerItem().setText(2, insert("SearchFilterWindow", "Description"))
        self.searchResultsView.headerItem().setText(3, insert("SearchFilterWindow", "Log Entry Reference"))
        self.searchResultsView.headerItem().setText(4, insert("SearchFilterWindow", "Log Creator"))
        self.searchResultsView.headerItem().setText(5, insert("SearchFilterWindow", "Action Type"))
        self.searchResultsView.headerItem().setText(6, insert("SearchFilterWindow", "Artifact"))

        __sortingEnabled = self.searchResultsView.isSortingEnabled()
        self.searchResultsView.setSortingEnabled(False)

        # Insert sample data into
        self.searchResultsView.topLevelItem(0).setText(0, insert("SearchFilterWindow", "0-002"))
        self.searchResultsView.topLevelItem(0).setText(1, insert("SearchFilterWindow", "10/23/2019 16:00"))
        self.searchResultsView.topLevelItem(0).setText(2, insert("SearchFilterWindow", "Red Team captured credentials using wireshark"))
        self.searchResultsView.topLevelItem(0).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.searchResultsView.topLevelItem(0).setText(4, insert("SearchFilterWindow", "Red"))
        self.searchResultsView.topLevelItem(0).setText(5, insert("SearchFilterWindow", "Red"))
        self.searchResultsView.topLevelItem(0).setText(6, insert("SearchFilterWindow", "/path/incident_repo"))
        self.searchResultsView.topLevelItem(1).setText(0, insert("SearchFilterWindow", "0-004"))
        self.searchResultsView.topLevelItem(1).setText(1, insert("SearchFilterWindow", "10/23/2019 16:18"))
        self.searchResultsView.topLevelItem(1).setText(2, insert("SearchFilterWindow", "Red Team login with captured credentials using Wireshark"))
        self.searchResultsView.topLevelItem(1).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.searchResultsView.topLevelItem(1).setText(4, insert("SearchFilterWindow", "Red"))
        self.searchResultsView.topLevelItem(1).setText(5, insert("SearchFilterWindow", "Red"))
        self.searchResultsView.topLevelItem(1).setText(6, insert("SearchFilterWindow", "/path/observer_notes"))
        self.searchResultsView.topLevelItem(2).setText(0, insert("SearchFilterWindow", "0-006"))
        self.searchResultsView.topLevelItem(2).setText(1, insert("SearchFilterWindow", "10/23/2019 16:27"))
        self.searchResultsView.topLevelItem(2).setText(2, insert("SearchFilterWindow", "Defenders disabled the account"))
        self.searchResultsView.topLevelItem(2).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.searchResultsView.topLevelItem(2).setText(4, insert("SearchFilterWindow", "Blue"))
        self.searchResultsView.topLevelItem(2).setText(5, insert("SearchFilterWindow", "Blue"))
        self.searchResultsView.topLevelItem(2).setText(6, insert("SearchFilterWindow", "/path/incident_repo"))
        self.searchResultsView.topLevelItem(3).setText(0, insert("SearchFilterWindow", "0-009"))
        self.searchResultsView.topLevelItem(3).setText(1, insert("SearchFilterWindow", "10/23/2019 16:27"))
        self.searchResultsView.topLevelItem(3).setText(2, insert("SearchFilterWindow", "Red team login was detected by Wireshark"))
        self.searchResultsView.topLevelItem(3).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.searchResultsView.topLevelItem(3).setText(4, insert("SearchFilterWindow", "Blue"))
        self.searchResultsView.topLevelItem(3).setText(5, insert("SearchFilterWindow", "Blue"))
        self.searchResultsView.topLevelItem(3).setText(6, insert("SearchFilterWindow", "/path/incident_repo"))
        self.searchResultsView.topLevelItem(4).setText(0, insert("SearchFilterWindow", "0-010"))
        self.searchResultsView.topLevelItem(4).setText(1, insert("SearchFilterWindow", "10/23/2019 16:27"))
        self.searchResultsView.topLevelItem(4).setText(2, insert("SearchFilterWindow", "Defenders disabled the account"))
        self.searchResultsView.topLevelItem(4).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.searchResultsView.topLevelItem(4).setText(4, insert("SearchFilterWindow", "White"))
        self.searchResultsView.topLevelItem(4).setText(5, insert("SearchFilterWindow", "Blue"))
        self.searchResultsView.topLevelItem(4).setText(6, insert("SearchFilterWindow", "/path/incident_repo"))
        self.searchResultsView.setSortingEnabled(__sortingEnabled)

        # Add sample vector options to vector selector
        self.vectorViewLayout.setTitle(insert("SearchFilterWindow", "Vector View"))
        self.vectorSelect.setItemText(0, insert("SearchFilterWindow", "Vector A"))
        self.vectorSelect.setItemText(1, insert("SearchFilterWindow", "Vector B"))
        self.vectorSelect.setItemText(2, insert("SearchFilterWindow", "Vector C"))
        self.vectorSelect.setItemText(3, insert("SearchFilterWindow", "Vector D"))
        self.vectorSelect.setItemText(4, insert("SearchFilterWindow", "Vector E"))
        self.vectorSelectConfirm.setText(insert("SearchFilterWindow", "Select Vector"))

        # Add headers to vector view table
        self.vectorView.headerItem().setText(0, insert("SearchFilterWindow", "Log ID"))
        self.vectorView.headerItem().setText(1, insert("SearchFilterWindow", "Time of Occurance"))
        self.vectorView.headerItem().setText(2, insert("SearchFilterWindow", "Description"))
        self.vectorView.headerItem().setText(3, insert("SearchFilterWindow", "Log Entry Reference"))
        self.vectorView.headerItem().setText(4, insert("SearchFilterWindow", "Log Creator"))
        self.vectorView.headerItem().setText(5, insert("SearchFilterWindow", "Action Type"))
        self.vectorView.headerItem().setText(6, insert("SearchFilterWindow", "Artifact"))
        __sortingEnabled = self.vectorView.isSortingEnabled()
        self.vectorView.setSortingEnabled(False)

        # Add sample vector data to vector view table
        self.vectorView.topLevelItem(0).setText(0, insert("SearchFilterWindow", "0-001"))
        self.vectorView.topLevelItem(0).setText(1, insert("SearchFilterWindow", "10/23/2019 15:51"))
        self.vectorView.topLevelItem(0).setText(3, insert("SearchFilterWindow", "usr/logs/blue/..."))
        self.vectorView.topLevelItem(0).setText(4, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(0).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(0).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        self.vectorView.topLevelItem(1).setText(0, insert("SearchFilterWindow", "0-002"))
        self.vectorView.topLevelItem(1).setText(1, insert("SearchFilterWindow", "10/23/2019 16:00"))
        self.vectorView.topLevelItem(1).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(1).setText(4, insert("SearchFilterWindow", "Red"))
        self.vectorView.topLevelItem(1).setText(5, insert("SearchFilterWindow", "Red"))
        self.vectorView.topLevelItem(1).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        self.vectorView.topLevelItem(2).setText(0, insert("SearchFilterWindow", "0-003"))
        self.vectorView.topLevelItem(2).setText(1, insert("SearchFilterWindow", "10/23/2019 16:09"))
        self.vectorView.topLevelItem(2).setText(3, insert("SearchFilterWindow", "usr/logs/blue/..."))
        self.vectorView.topLevelItem(2).setText(4, insert("SearchFilterWindow", "White"))
        self.vectorView.topLevelItem(2).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(2).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        self.vectorView.topLevelItem(3).setText(0, insert("SearchFilterWindow", "0-004"))
        self.vectorView.topLevelItem(3).setText(1, insert("SearchFilterWindow", "10/23/2019 16:18"))
        self.vectorView.topLevelItem(3).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(3).setText(4, insert("SearchFilterWindow", "Red,White"))
        self.vectorView.topLevelItem(3).setText(5, insert("SearchFilterWindow", "Red"))
        self.vectorView.topLevelItem(3).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        self.vectorView.topLevelItem(4).setText(0, insert("SearchFilterWindow", "0-005"))
        self.vectorView.topLevelItem(4).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(4).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(4).setText(4, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(4).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(4).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        self.vectorView.topLevelItem(5).setText(0, insert("SearchFilterWindow", "0-006"))
        self.vectorView.topLevelItem(5).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(5).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(5).setText(4, insert("SearchFilterWindow", "Red"))
        self.vectorView.topLevelItem(5).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(5).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        self.vectorView.topLevelItem(6).setText(0, insert("SearchFilterWindow", "0-007"))
        self.vectorView.topLevelItem(6).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(6).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(6).setText(4, insert("SearchFilterWindow", "White"))
        self.vectorView.topLevelItem(6).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(6).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        self.vectorView.topLevelItem(7).setText(0, insert("SearchFilterWindow", "0-008"))
        self.vectorView.topLevelItem(7).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(7).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(7).setText(4, insert("SearchFilterWindow", "Red, White"))
        self.vectorView.topLevelItem(7).setText(5, insert("SearchFilterWindow", "Red"))
        self.vectorView.topLevelItem(7).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        self.vectorView.topLevelItem(8).setText(0, insert("SearchFilterWindow", "0-009"))
        self.vectorView.topLevelItem(8).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(8).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(8).setText(4, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(8).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(8).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        self.vectorView.topLevelItem(9).setText(0, insert("SearchFilterWindow", "0-0010"))
        self.vectorView.topLevelItem(9).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        self.vectorView.topLevelItem(9).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        self.vectorView.topLevelItem(9).setText(4, insert("SearchFilterWindow", "White"))
        self.vectorView.topLevelItem(9).setText(5, insert("SearchFilterWindow", "Blue"))
        self.vectorView.topLevelItem(9).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        self.vectorView.setSortingEnabled(__sortingEnabled)

        self.menuJump_to.setTitle(insert("SearchFilterWindow", "Jump to..."))
        self.actionEvent_Configuration.setText(insert("SearchFilterWindow", "Event Configuration"))
        self.actionEnforcement_Action_Report.setText(insert("SearchFilterWindow", "Enforcement Action Report"))
        self.actionSearch_Filter_Log_Entries.setText(insert("SearchFilterWindow", "Search/Filter Log Entries"))
        self.actionManage_Graph.setText(insert("SearchFilterWindow", "Manage Graph"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SearchFilterWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchFilterWindow()
    ui.generateUi(SearchFilterWindow)
    SearchFilterWindow.show()
    sys.exit(app.exec_())
