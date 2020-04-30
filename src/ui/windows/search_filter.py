import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.common import menu_bar
from configuration.configurations import Configuration
from threading import Thread
from ingestion.splunk import Splunk


class FilterUi(object):

    def setupUi(self, SearchFilterWindow):
        SearchFilterWindow.setObjectName("SearchFilterWindow")
        SearchFilterWindow.resize(870, 690)

        # Create layouts in this window
        self.mainVerticalView = QtWidgets.QWidget(SearchFilterWindow)
        self.mainVerticalView.setObjectName("mainVerticalView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainVerticalView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterConfigurationLayout = QtWidgets.QGroupBox(self.mainVerticalView)
        self.filterConfigurationLayout.setObjectName("filterConfigurationLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.filterConfigurationLayout)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filterFormLayout = QtWidgets.QFormLayout()
        self.filterFormLayout.setObjectName("filterFormLayout")

        # Add widgets to the filter Form Layout
        self.keywordSearchLabel = QtWidgets.QLabel(self.filterConfigurationLayout)
        self.keywordSearchLabel.setObjectName("keywordSearchLabel")
        self.filterFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.keywordSearchLabel)
        self.keywordSearchBox = QtWidgets.QLineEdit(self.filterConfigurationLayout)
        self.keywordSearchBox.setObjectName("keywordSearchBox")
        self.filterFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.keywordSearchBox)
        self.creatorLabel = QtWidgets.QLabel(self.filterConfigurationLayout)
        self.creatorLabel.setObjectName("creatorLabel")
        self.filterFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.creatorLabel)
        self.creatorWhiteCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.creatorWhiteCheck.setObjectName("creatorWhiteCheck")
        self.filterFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.creatorWhiteCheck)
        self.creatorRedCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.creatorRedCheck.setObjectName("creatorRedCheck")
        self.filterFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.creatorRedCheck)
        self.creatorBlueCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.creatorBlueCheck.setObjectName("creatorBlueCheck")
        self.filterFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.creatorBlueCheck)
        self.eventTypeLabel = QtWidgets.QLabel(self.filterConfigurationLayout)
        self.eventTypeLabel.setObjectName("eventTypeLabel")
        self.filterFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.eventTypeLabel)
        self.eventTypeRedCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.eventTypeRedCheck.setObjectName("eventTypeRedCheck")
        self.filterFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.eventTypeRedCheck)
        self.eventTypeWhiteCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.eventTypeWhiteCheck.setObjectName("eventTypeWhiteCheck")
        self.filterFormLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.eventTypeWhiteCheck)
        self.eventTypeBlueCheck = QtWidgets.QCheckBox(self.filterConfigurationLayout)
        self.eventTypeBlueCheck.setObjectName("eventTypeBlueCheck")
        self.filterFormLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.eventTypeBlueCheck)
        self.startTimestampLabel = QtWidgets.QLabel(self.filterConfigurationLayout)
        self.startTimestampLabel.setObjectName("startTimestampLabel")
        self.filterFormLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.startTimestampLabel)
        self.startTimestampEdit = QtWidgets.QDateTimeEdit(self.filterConfigurationLayout)
        self.startTimestampEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.startTimestampEdit.setProperty("showGroupSeparator", False)
        self.startTimestampEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startTimestampEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.startTimestampEdit.setCalendarPopup(True)
        self.startTimestampEdit.setCurrentSectionIndex(0)
        self.startTimestampEdit.setObjectName("startTimestampEdit")
        self.filterFormLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.startTimestampEdit)
        self.endTimestampLabel = QtWidgets.QLabel(self.filterConfigurationLayout)
        self.endTimestampLabel.setObjectName("endTimestampLabel")
        self.filterFormLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.endTimestampLabel)
        self.endTimestampEdit = QtWidgets.QDateTimeEdit(self.filterConfigurationLayout)
        self.endTimestampEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.endTimestampEdit.setCalendarPopup(True)
        self.endTimestampEdit.setCurrentSectionIndex(0)
        self.endTimestampEdit.setObjectName("endTimestampEdit")
        self.filterFormLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.endTimestampEdit)
        self.applyFilterButton = QtWidgets.QPushButton(self.filterConfigurationLayout)
        self.applyFilterButton.setObjectName("applyFilterButton")
        self.filterFormLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.applyFilterButton)
        self.horizontalLayout_3.addLayout(self.filterFormLayout)

        self.filterView = QtWidgets.QTreeWidget(self.filterConfigurationLayout)
        self.filterView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.filterView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.filterView.setAlternatingRowColors(True)
        self.filterView.setHeaderHidden(False)
        self.filterView.setObjectName("searchResultsView")
        self.filterView.setSortingEnabled(True)
        self.filterView.header().setSortIndicatorShown(True)



        # Add vector select combo box and select button
        self.horizontalLayout_3.addWidget(self.filterView)
        self.verticalLayout.addWidget(self.filterConfigurationLayout)
        self.vectorViewLayout = QtWidgets.QGroupBox(self.mainVerticalView)
        self.vectorViewLayout.setObjectName("vectorViewLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.vectorViewLayout)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vectorSelectButtonLayout = QtWidgets.QHBoxLayout()
        self.vectorSelectButtonLayout.setObjectName("vectorSelectButtonLayout")
        self.vectorSelectCombo = QtWidgets.QComboBox(self.vectorViewLayout)
        self.vectorSelectCombo.setObjectName("vectorSelectCombo")
        self.vectorSelectCombo.addItem("")
        self.vectorSelectCombo.addItem("")
        self.vectorSelectCombo.addItem("")
        self.vectorSelectCombo.addItem("")
        self.vectorSelectCombo.addItem("")
        self.vectorSelectButtonLayout.addWidget(self.vectorSelectCombo)
        self.vectorSelectConfirmButton = QtWidgets.QPushButton(self.vectorViewLayout)
        self.vectorSelectConfirmButton.setCheckable(False)
        self.vectorSelectConfirmButton.setObjectName("vectorSelectConfirmButton")
        self.vectorSelectButtonLayout.addWidget(self.vectorSelectConfirmButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vectorSelectButtonLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.vectorSelectButtonLayout)

        # Add the Tree widget to display selected vector
        self.vectorView = QtWidgets.QTreeWidget(self.vectorViewLayout)
        self.vectorView.setAlternatingRowColors(True)
        self.vectorView.setWordWrap(False)
        self.vectorView.setObjectName("vectorView")



        self.vectorView.header().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.vectorView)
        self.verticalLayout.addWidget(self.vectorViewLayout)
        SearchFilterWindow.setCentralWidget(self.mainVerticalView)

        self.menubar = menu_bar.PickMenuBar(SearchFilterWindow, omit=menu_bar.FILTER)
        SearchFilterWindow.setMenuBar(self.menubar)

        self.addData(SearchFilterWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchFilterWindow)

    def addData(self, SearchFilterWindow):
        configuration = Configuration.get_instance()

        insert = QtCore.QCoreApplication.translate
        SearchFilterWindow.setWindowTitle(insert("SearchFilterWindow", "Search/Filter Log Entries"))

        # Add labels to UI elements
        self.filterConfigurationLayout.setTitle(insert("SearchFilterWindow", "Filter Configuration"))
        self.keywordSearchLabel.setText(insert("SearchFilterWindow", "Keyword search"))
        self.creatorLabel.setText(insert("SearchFilterWindow", "Creator"))
        self.creatorWhiteCheck.setText(insert("SearchFilterWindow", "White"))
        self.creatorRedCheck.setText(insert("SearchFilterWindow", "Red"))
        self.creatorBlueCheck.setText(insert("SearchFilterWindow", "Blue"))
        self.eventTypeLabel.setText(insert("SearchFilterWindow", "Event Type"))
        self.eventTypeRedCheck.setText(insert("SearchFilterWindow", "Red"))
        self.eventTypeWhiteCheck.setText(insert("SearchFilterWindow", "White"))
        self.eventTypeBlueCheck.setText(insert("SearchFilterWindow", "Blue"))
        self.startTimestampLabel.setText(insert("SearchFilterWindow", "Start Timestamp"))
        self.endTimestampLabel.setText(insert("SearchFilterWindow", "End Timestamp"))
        self.applyFilterButton.setText(insert("SearchFilterWindow", "Apply Filter"))

        # Add labels to filter view
        self.filterView.setSortingEnabled(True)
        self.filterView.headerItem().setText(0, insert("SearchFilterWindow", "Log ID"))
        self.filterView.headerItem().setText(1, insert("SearchFilterWindow", "Time of Occurance"))
        self.filterView.headerItem().setText(2, insert("SearchFilterWindow", "Description"))
        self.filterView.headerItem().setText(3, insert("SearchFilterWindow", "Log Entry Reference"))
        self.filterView.headerItem().setText(4, insert("SearchFilterWindow", "Log Creator"))
        self.filterView.headerItem().setText(5, insert("SearchFilterWindow", "Action Type"))
        self.filterView.headerItem().setText(6, insert("SearchFilterWindow", "Artifact"))
        __sortingEnabled = self.filterView.isSortingEnabled()
        self.filterView.setSortingEnabled(False)


        # Add sample data to filter view
        messsage = QMessageBox()
        messsage.setWindowTitle("Please wait...")
        messsage.setText("Retrieving log entries from splunk. Log entries might take a sec to load.\n\nClick OK")
        messsage.setIcon(QMessageBox.Information)
        messsage.exec_()
        Thread(target=self.get_log_entries_thread, args=(configuration, )).start()

        self.filterView.setSortingEnabled(__sortingEnabled)
        self.vectorViewLayout.setTitle(insert("SearchFilterWindow", "Vector View"))

        # Add sample options to vector select combo box
        self.vectorSelectCombo.setItemText(0, insert("SearchFilterWindow", "Vector A"))
        self.vectorSelectCombo.setItemText(1, insert("SearchFilterWindow", "Vector B"))
        self.vectorSelectCombo.setItemText(2, insert("SearchFilterWindow", "Vector C"))
        self.vectorSelectCombo.setItemText(3, insert("SearchFilterWindow", "Vector D"))
        self.vectorSelectCombo.setItemText(4, insert("SearchFilterWindow", "Vector E"))
        self.vectorSelectConfirmButton.setText(insert("SearchFilterWindow", "Select Vector"))

        # Add labels to vector view
        self.vectorView.setSortingEnabled(True)
        self.vectorView.headerItem().setText(0, insert("SearchFilterWindow", "Log ID"))
        self.vectorView.headerItem().setText(1, insert("SearchFilterWindow", "Time of Occurance"))
        self.vectorView.headerItem().setText(2, insert("SearchFilterWindow", "Description"))
        self.vectorView.headerItem().setText(3, insert("SearchFilterWindow", "Log Entry Reference"))
        self.vectorView.headerItem().setText(4, insert("SearchFilterWindow", "Log Creator"))
        self.vectorView.headerItem().setText(5, insert("SearchFilterWindow", "Action Type"))
        self.vectorView.headerItem().setText(6, insert("SearchFilterWindow", "Artifact"))
        __sortingEnabled = self.vectorView.isSortingEnabled()
        self.vectorView.setSortingEnabled(False)

        # Add sample data to vector view
        # self.vectorView.topLevelItem(0).setText(0, insert("SearchFilterWindow", "0-001"))
        # self.vectorView.topLevelItem(0).setText(1, insert("SearchFilterWindow", "10/23/2019 15:51"))
        # self.vectorView.topLevelItem(0).setText(3, insert("SearchFilterWindow", "usr/logs/blue/..."))
        # self.vectorView.topLevelItem(0).setText(4, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(0).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(0).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        # self.vectorView.topLevelItem(1).setText(0, insert("SearchFilterWindow", "0-002"))
        # self.vectorView.topLevelItem(1).setText(1, insert("SearchFilterWindow", "10/23/2019 16:00"))
        # self.vectorView.topLevelItem(1).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(1).setText(4, insert("SearchFilterWindow", "Red"))
        # self.vectorView.topLevelItem(1).setText(5, insert("SearchFilterWindow", "Red"))
        # self.vectorView.topLevelItem(1).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        # self.vectorView.topLevelItem(2).setText(0, insert("SearchFilterWindow", "0-003"))
        # self.vectorView.topLevelItem(2).setText(1, insert("SearchFilterWindow", "10/23/2019 16:09"))
        # self.vectorView.topLevelItem(2).setText(3, insert("SearchFilterWindow", "usr/logs/blue/..."))
        # self.vectorView.topLevelItem(2).setText(4, insert("SearchFilterWindow", "White"))
        # self.vectorView.topLevelItem(2).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(2).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        # self.vectorView.topLevelItem(3).setText(0, insert("SearchFilterWindow", "0-004"))
        # self.vectorView.topLevelItem(3).setText(1, insert("SearchFilterWindow", "10/23/2019 16:18"))
        # self.vectorView.topLevelItem(3).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(3).setText(4, insert("SearchFilterWindow", "Red,White"))
        # self.vectorView.topLevelItem(3).setText(5, insert("SearchFilterWindow", "Red"))
        # self.vectorView.topLevelItem(3).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        # self.vectorView.topLevelItem(4).setText(0, insert("SearchFilterWindow", "0-005"))
        # self.vectorView.topLevelItem(4).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(4).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(4).setText(4, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(4).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(4).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        # self.vectorView.topLevelItem(5).setText(0, insert("SearchFilterWindow", "0-006"))
        # self.vectorView.topLevelItem(5).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(5).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(5).setText(4, insert("SearchFilterWindow", "Red"))
        # self.vectorView.topLevelItem(5).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(5).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        # self.vectorView.topLevelItem(6).setText(0, insert("SearchFilterWindow", "0-007"))
        # self.vectorView.topLevelItem(6).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(6).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(6).setText(4, insert("SearchFilterWindow", "White"))
        # self.vectorView.topLevelItem(6).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(6).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        # self.vectorView.topLevelItem(7).setText(0, insert("SearchFilterWindow", "0-008"))
        # self.vectorView.topLevelItem(7).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(7).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(7).setText(4, insert("SearchFilterWindow", "Red, White"))
        # self.vectorView.topLevelItem(7).setText(5, insert("SearchFilterWindow", "Red"))
        # self.vectorView.topLevelItem(7).setText(6, insert("SearchFilterWindow", "/path/observer_notes.osv"))
        # self.vectorView.topLevelItem(8).setText(0, insert("SearchFilterWindow", "0-009"))
        # self.vectorView.topLevelItem(8).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(8).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(8).setText(4, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(8).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(8).setText(6, insert("SearchFilterWindow", "/path/incident/report.pd"))
        # self.vectorView.topLevelItem(9).setText(0, insert("SearchFilterWindow", "0-0010"))
        # self.vectorView.topLevelItem(9).setText(1, insert("SearchFilterWindow", "10/24/2019 16:27"))
        # self.vectorView.topLevelItem(9).setText(3, insert("SearchFilterWindow", "usr/logs/red/..."))
        # self.vectorView.topLevelItem(9).setText(4, insert("SearchFilterWindow", "White"))
        # self.vectorView.topLevelItem(9).setText(5, insert("SearchFilterWindow", "Blue"))
        # self.vectorView.topLevelItem(9).setText(6, insert("SearchFilterWindow", "/path/incident/report2.pd"))
        self.vectorView.setSortingEnabled(__sortingEnabled)

    def get_log_entries_thread(self, configuration):
        if configuration.splunk:
            all_log_entries = configuration.splunk.get_log_entries()
            self.insert_log_entry_search_data(all_log_entries)

    def insert_log_entry_search_data(self, log_entries):
        insert = QtCore.QCoreApplication.translate
        # Add empty spaces to Search Results view to enter sample data
        for i in range(len(log_entries)):
            QtWidgets.QTreeWidgetItem(self.filterView)

        # add actual data
        for i in range(len(log_entries)):
            self.filterView.topLevelItem(i).setText(0, insert("SearchFilterWindow", log_entries[i].id))
            self.filterView.topLevelItem(i).setText(1, insert("SearchFilterWindow", log_entries[i].time))
            self.filterView.topLevelItem(i).setText(2, insert("SearchFilterWindow", log_entries[i].data))
            self.filterView.topLevelItem(i).setText(3, insert("SearchFilterWindow", log_entries[i].source_file))
            self.filterView.topLevelItem(i).setText(4, insert("SearchFilterWindow", "-"))
            self.filterView.topLevelItem(i).setText(5, insert("SearchFilterWindow", "-"))
            self.filterView.topLevelItem(i).setText(6, insert("SearchFilterWindow", "-"))

    def insert_log_entry_vector_view(self, vector):
        # Add spaced for sample data in the vector tree widget
        for i in range(10):
            QtWidgets.QTreeWidgetItem(self.vectorView)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SearchFilterWindow = QtWidgets.QMainWindow()
    ui = FilterUi()
    ui.setupUi(SearchFilterWindow)
    SearchFilterWindow.show()
    sys.exit(app.exec_())
