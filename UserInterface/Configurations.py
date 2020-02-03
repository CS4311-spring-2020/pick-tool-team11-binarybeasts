from PyQt5 import QtCore, QtGui, QtWidgets


class ConfigurationsUi(object):
    def generateUi(self, configurationsWindow):
        configurationsWindow.setObjectName("configurationsWindow")
        configurationsWindow.resize(800, 650)


        self.windowBackground = QtWidgets.QWidget(configurationsWindow)
        self.windowBackground.setObjectName("windowBackground")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.windowBackground)
        self.gridLayout_5.setObjectName("gridLayout_5")


#*-------------------------Menu bar creation & properties----------------------------------------------------*#      
        #Menu bar creation & properties
        self.menubar = QtWidgets.QMenuBar(configurationsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        configurationsWindow.setMenuBar(self.menubar)
        #configurations menu option
        self.actionConfigurations = QtWidgets.QAction(configurationsWindow)
        self.actionConfigurations.setObjectName("actionConfigurations")
        #enforcement action report meny option
        self.actionEnforcement_Action_Report = QtWidgets.QAction(configurationsWindow)
        self.actionEnforcement_Action_Report.setObjectName("actionEnforcement_Action_Report")
        #search/filter log entries menu option
        self.actionSearch_Filter_Log_Entries = QtWidgets.QAction(configurationsWindow)
        self.actionSearch_Filter_Log_Entries.setObjectName("actionSearch_Filter_Log_Entries")
        #manage graph menu option
        self.actionManage_Graph = QtWidgets.QAction(configurationsWindow)
        self.actionManage_Graph.setObjectName("actionManage_Graph")
        #actions for each menu option
        self.menuOptions.addAction(self.actionConfigurations)
        self.menuOptions.addAction(self.actionEnforcement_Action_Report)
        self.menuOptions.addAction(self.actionSearch_Filter_Log_Entries)
        self.menuOptions.addAction(self.actionManage_Graph)
        self.menubar.addAction(self.menuOptions.menuAction())
#*-------------------------Configuration Tabs properties----------------------------------------------------*#
        self.ConfigurationTabs = QtWidgets.QTabWidget(self.windowBackground)
        self.ConfigurationTabs.setEnabled(True)
        self.ConfigurationTabs.setObjectName("ConfigurationTabs")
        self.gridLayout_5.addWidget(self.ConfigurationTabs, 0, 0, 1, 1)
        configurationsWindow.setCentralWidget(self.windowBackground)
#*-------------------------Team Configuration Tab----------------------------------------------------*#
        self.TeamConfigurationTab = QtWidgets.QWidget()
        self.TeamConfigurationTab.setObjectName("TeamConfigurationTab")
        #adds the tab to the window
        self.ConfigurationTabs.addTab(self.TeamConfigurationTab, "")
        #sets tab to a grid layout
        self.gridLayout = QtWidgets.QGridLayout(self.TeamConfigurationTab)
        self.gridLayout.setObjectName("gridLayout")
        #lead checkbox & properties
        self.leadCheckbox = QtWidgets.QCheckBox(self.TeamConfigurationTab)
        self.leadCheckbox.setObjectName("leadCheckbox")
        self.gridLayout.addWidget(self.leadCheckbox, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        #lead IP address label & properties
        self.leadIPAddrLabel = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.leadIPAddrLabel.setObjectName("leadIPAddrLabel")
        self.gridLayout.addWidget(self.leadIPAddrLabel, 1, 0, 1, 1)
        #lead IP address text field & properties
        self.leadIPAddr = QtWidgets.QLineEdit(self.TeamConfigurationTab)
        self.leadIPAddr.setObjectName("leadIPAddr")
        self.gridLayout.addWidget(self.leadIPAddr, 1, 1, 1, 1)
        #number of connections to the lead's IP address label & properties
        self.numOfConnectionsLabel = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.numOfConnectionsLabel.setObjectName("numOfConnectionsLabel")
        self.gridLayout.addWidget(self.numOfConnectionsLabel, 2, 0, 1, 1)
        #number of connections disabled text field & properties
        self.numOfConnections = QtWidgets.QLineEdit(self.TeamConfigurationTab)
        self.numOfConnections.setEnabled(False)
        self.numOfConnections.setObjectName("numOfConnections")
        self.gridLayout.addWidget(self.numOfConnections, 2, 1, 1, 1)
        #adds a label to use as a spacer to keep desired layout & properties
        self.spacer2 = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.spacer2.setText("")
        self.spacer2.setObjectName("spacer2")
        self.gridLayout.addWidget(self.spacer2, 4, 0, 1, 1)
        #connect button & properties
        self.connectBttn = QtWidgets.QPushButton(self.TeamConfigurationTab)
        self.connectBttn.setObjectName("connectBttn")
        self.gridLayout.addWidget(self.connectBttn, 3, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Event Configuration Tab----------------------------------------------------*#
        self.EventConfigurationTab = QtWidgets.QWidget()
        self.EventConfigurationTab.setObjectName("EventConfigurationTab")
        #add event configuration tab
        self.ConfigurationTabs.addTab(self.EventConfigurationTab, "")
        #sets tab to a grid layout
        self.gridLayout_2 = QtWidgets.QGridLayout(self.EventConfigurationTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #event name label & properties
        self.eventNameLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventNameLabel.setObjectName("eventNameLabel")
        self.gridLayout_2.addWidget(self.eventNameLabel, 0, 0, 1, 1)
        #event name text field &  properties
        self.eventName = QtWidgets.QLineEdit(self.EventConfigurationTab)
        self.eventName.setObjectName("eventName")
        self.gridLayout_2.addWidget(self.eventName, 0, 1, 1, 1)
        #event description label & properties
        self.eventDescLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventDescLabel.setObjectName("eventDescLabel")
        self.gridLayout_2.addWidget(self.eventDescLabel, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        #event description text field & properties
        self.eventDesc = QtWidgets.QTextEdit(self.EventConfigurationTab)
        self.eventDesc.setObjectName("eventDesc")
        self.gridLayout_2.addWidget(self.eventDesc, 1, 1, 1, 1)
        #event start label & properties
        self.eventStartLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventStartLabel.setObjectName("eventStartLabel")
        self.gridLayout_2.addWidget(self.eventStartLabel, 4, 0, 1, 1)
        #event start timestamp & properties
        self.eventStart = QtWidgets.QDateTimeEdit(self.EventConfigurationTab)
        self.eventStart.setDate(QtCore.QDate(2020, 1, 1))
        self.eventStart.setCalendarPopup(True)
        self.eventStart.setObjectName("eventStart")
        self.gridLayout_2.addWidget(self.eventStart, 4, 1, 1, 1)
        #event end label & properties
        self.eventEndLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventEndLabel.setObjectName("eventEndLabel")
        self.gridLayout_2.addWidget(self.eventEndLabel, 6, 0, 1, 1)
        #event end timestamp & properties
        self.eventEnd = QtWidgets.QDateTimeEdit(self.EventConfigurationTab)
        self.eventEnd.setDate(QtCore.QDate(2020, 1, 1))
        self.eventEnd.setCalendarPopup(True)
        self.eventEnd.setObjectName("eventEnd")
        self.gridLayout_2.addWidget(self.eventEnd, 6, 1, 1, 1)
        #save event button & properties
        self.saveEventBttn = QtWidgets.QPushButton(self.EventConfigurationTab)
        self.saveEventBttn.setObjectName("saveEventBttn")
        self.gridLayout_2.addWidget(self.saveEventBttn, 7, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Directory Configuration Tab----------------------------------------------------*#
        self.DirectoryConfigurationTab = QtWidgets.QWidget()
        self.DirectoryConfigurationTab.setObjectName("DirectoryConfigurationTab")
        #sets tab to a grid layout
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DirectoryConfigurationTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #add directory configuration tab
        self.ConfigurationTabs.addTab(self.DirectoryConfigurationTab, "")
        #root directory label & properties
        self.rootDirectoryLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.rootDirectoryLabel.setObjectName("rootDirectoryLabel")
        self.gridLayout_3.addWidget(self.rootDirectoryLabel, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        #root directory text field & properties
        self.rootDirectory = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.rootDirectory.setObjectName("rootDirectory")
        self.gridLayout_3.addWidget(self.rootDirectory, 0, 1, 1, 1)
        #red team folder label & properties
        self.redTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.redTeamLabel.setObjectName("redTeamLabel")
        self.gridLayout_3.addWidget(self.redTeamLabel, 1, 0, 1, 1)
        #red team folder text field & properties
        self.redTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.redTeamFolder.setObjectName("redTeamFolder")
        self.gridLayout_3.addWidget(self.redTeamFolder, 1, 1, 1, 1)
        #blue team folder label & properties
        self.blueTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.blueTeamLabel.setObjectName("blueTeamLabel")
        self.gridLayout_3.addWidget(self.blueTeamLabel, 2, 0, 1, 1)
        #blue team folder text field and properties
        self.blueTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.blueTeamFolder.setObjectName("blueTeamFolder")
        self.gridLayout_3.addWidget(self.blueTeamFolder, 2, 1, 1, 1)
        #white team folder label & properties
        self.whiteTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.whiteTeamLabel.setObjectName("whiteTeamLabel")
        self.gridLayout_3.addWidget(self.whiteTeamLabel, 3, 0, 1, 1)
        #white team folder text field & properties
        self.whiteTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.whiteTeamFolder.setObjectName("whiteTeamFolder")
        self.gridLayout_3.addWidget(self.whiteTeamFolder, 3, 1, 1, 1)
        #adds a label to use as a spacer to keep desired layout & properties
        self.spacer1 = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.spacer1.setText("")
        self.spacer1.setObjectName("spacer1")
        self.gridLayout_3.addWidget(self.spacer1, 5, 0, 1, 1)
        #start ingestion button & properties
        self.startDataIngestionBttn = QtWidgets.QPushButton(self.DirectoryConfigurationTab)
        self.startDataIngestionBttn.setObjectName("startDataIngestionBttn")
        self.gridLayout_3.addWidget(self.startDataIngestionBttn, 4, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Vector Configuration Tab----------------------------------------------------*#
        self.VectorConfigurationTab = QtWidgets.QWidget()
        self.VectorConfigurationTab.setObjectName("VectorConfigurationTab")
        #sets tab to a grid layout
        self.gridLayout_4 = QtWidgets.QGridLayout(self.VectorConfigurationTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        #add vector configuration tab
        self.ConfigurationTabs.addTab(self.VectorConfigurationTab, "")
        #vector name label & properties
        self.vectorNameLabel = QtWidgets.QLabel(self.VectorConfigurationTab)
        self.vectorNameLabel.setObjectName("vectorNameLabel")
        self.gridLayout_4.addWidget(self.vectorNameLabel, 0, 0, 1, 1)
        #vector name text field & properties
        self.vectorName = QtWidgets.QLineEdit(self.VectorConfigurationTab)
        self.vectorName.setObjectName("vectorName")
        self.gridLayout_4.addWidget(self.vectorName, 0, 1, 1, 1)
        #vector description label & properties
        self.vectorDescLabel = QtWidgets.QLabel(self.VectorConfigurationTab)
        self.vectorDescLabel.setObjectName("vectorDescLabel")
        self.gridLayout_4.addWidget(self.vectorDescLabel, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        #vector description text field & properties
        self.vectorDesc = QtWidgets.QTextEdit(self.VectorConfigurationTab)
        self.vectorDesc.setObjectName("vectorDesc")
        self.gridLayout_4.addWidget(self.vectorDesc, 1, 1, 1, 1)
        #add vector button & properties
        self.addVectorBttn = QtWidgets.QPushButton(self.VectorConfigurationTab)
        self.addVectorBttn.setObjectName("addVectorBttn")
        self.gridLayout_4.addWidget(self.addVectorBttn, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        #vector table tree widget & properties
        self.vectorTable = QtWidgets.QTreeWidget(self.VectorConfigurationTab)
        self.vectorTable.setAlternatingRowColors(True)
        self.vectorTable.setAllColumnsShowFocus(False)
        self.vectorTable.setObjectName("vectorTable")
        #vector table header properties
        self.vectorTable.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.vectorTable.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.vectorTable.header().setDefaultSectionSize(230)
        self.vectorTable.header().setSortIndicatorShown(True)
        self.gridLayout_4.addWidget(self.vectorTable, 4, 0, 1, 2)
        #creating space withing vector table to add data later
        for i in range(3):
            QtWidgets.QTreeWidgetItem(self.vectorTable)
        #Delete vector button
        self.deleteVectorBttn = QtWidgets.QPushButton(self.VectorConfigurationTab)
        self.deleteVectorBttn.setObjectName("deleteVectorBttn")
        self.gridLayout_4.addWidget(self.deleteVectorBttn, 5, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Add Data----------------------------------------------------*#
        #adds all data to window
        self.addData(configurationsWindow)
        self.ConfigurationTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(configurationsWindow)

    def addData(self, configurationsWindow):
        insert = QtCore.QCoreApplication.translate
        configurationsWindow.setWindowTitle(insert("configurationsWindow", "Configurations"))
#*-------------------------Team Configuration Tab-------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.TeamConfigurationTab), insert("configurationsWindow", "Team Configuration"))
        #set checkbox
        self.leadCheckbox.setText(insert("configurationsWindow", "Lead"))
        #Set Labels
        self.leadIPAddrLabel.setText(insert("configurationsWindow", "Lead IP Address:"))
        self.numOfConnectionsLabel.setText(insert("configurationsWindow", "No. of estrablished connections:"))
        #Set Button
        self.connectBttn.setText(insert("configurationsWindow", "Connect"))
        #Set text fields
        self.numOfConnections.setText(insert("configurationsWindow", "5"))  
#*--------------------------Event Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.EventConfigurationTab), insert("configurationsWindow", "Event Configuration"))
        #Set labels
        self.eventNameLabel.setText(insert("configurationsWindow", "Event Name:"))
        self.eventDescLabel.setText(insert("configurationsWindow", "Event Description:"))
        self.eventStartLabel.setText(insert("configurationsWindow", "Event Start Timestamp:"))
        self.eventEndLabel.setText(insert("configurationsWindow", "Event End Timestamp:"))
        #Set buttons
        self.saveEventBttn.setText(insert("configurationsWindow", "Save Event"))
#*--------------------------Directory Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.DirectoryConfigurationTab), insert("configurationsWindow", "Directory Configuration"))
        #Set Labels
        self.rootDirectoryLabel.setText(insert("configurationsWindow", "Root Directory:"))
        self.redTeamLabel.setText(insert("configurationsWindow", "Red Team Folder:"))
        self.blueTeamLabel.setText(insert("configurationsWindow", "Blue Team Folder:"))
        self.whiteTeamLabel.setText(insert("configurationsWindow", "White Team Folder:"))
        #Set buttons
        self.startDataIngestionBttn.setText(insert("configurationsWindow", "Start Data Ingestion"))
#*--------------------------Vector Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.VectorConfigurationTab), insert("configurationsWindow", "Vector Configuration"))
        #Set labels
        self.vectorNameLabel.setText(insert("configurationsWindow", "Vector Name:"))
        self.vectorDescLabel.setText(insert("configurationsWindow", "Vector Description:"))
        #Set buttons
        self.addVectorBttn.setText(insert("configurationsWindow", "Add Vector"))
        self.deleteVectorBttn.setText(insert("configurationsWindow", "Delete Vector"))
        #Set Vector table headers
        self.vectorTable.setSortingEnabled(True)
        self.vectorTable.headerItem().setText(0, insert("configurationsWindow", "Vector Name"))
        self.vectorTable.headerItem().setText(1, insert("configurationsWindow", "Vector Description"))
        __sortingEnabled = self.vectorTable.isSortingEnabled()
        self.vectorTable.setSortingEnabled(False)
        #set vector table data
        self.vectorTable.topLevelItem(0).setText(0, insert("configurationsWindow", "Vector C"))
        self.vectorTable.topLevelItem(0).setText(1, insert("configurationsWindow", "Testing Vector A"))
        self.vectorTable.topLevelItem(1).setText(0, insert("configurationsWindow", "Vector B"))
        self.vectorTable.topLevelItem(1).setText(1, insert("configurationsWindow", "Testing Vector B"))
        self.vectorTable.topLevelItem(2).setText(0, insert("configurationsWindow", "Vector A"))
        self.vectorTable.topLevelItem(2).setText(1, insert("configurationsWindow", "Testing Vector C"))
        self.vectorTable.setSortingEnabled(__sortingEnabled)
#*--------------------------Menu Options--------------------------------------------------*#
        #set menu options
        self.menuOptions.setTitle(insert("configurationsWindow", "Menu"))
        self.actionConfigurations.setText(insert("configurationsWindow", "Configurations"))
        self.actionEnforcement_Action_Report.setText(insert("configurationsWindow", "Enforcement Action Report"))
        self.actionSearch_Filter_Log_Entries.setText(insert("configurationsWindow", "Search/Filter Log Entries"))
        self.actionManage_Graph.setText(insert("configurationsWindow", "Manage Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    configurationsWindow = QtWidgets.QMainWindow()
    ui = ConfigurationsUi()
    ui.generateUi(configurationsWindow)
    configurationsWindow.show()
    sys.exit(app.exec_())
