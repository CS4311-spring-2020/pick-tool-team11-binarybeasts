from PyQt5 import QtCore, QtGui, QtWidgets
from ui.common import menu_bar


class ConfigurationsWindow(object):
    def generateUi(self, configurationsWindow):
        configurationsWindow.setObjectName("configurationsWindow")
        configurationsWindow.resize(800, 650)


        self.windowBackground = QtWidgets.QWidget(configurationsWindow)
        self.windowBackground.setObjectName("windowBackground")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.windowBackground)
        self.gridLayout_5.setObjectName("gridLayout_5")


#*-------------------------Menu bar creation & properties----------------------------------------------------*#
        self.menubar = menu_bar.PickMenuBar(configurationsWindow, omit=menu_bar.CONFIGURATIONS)
        configurationsWindow.setMenuBar(self.menubar)
#*-------------------------Configuration Tabs properties----------------------------------------------------*#
        self.ConfigurationTabs = QtWidgets.QTabWidget(self.windowBackground)
        self.ConfigurationTabs.setEnabled(True)
        self.ConfigurationTabs.setObjectName("ConfigurationTabs")
        self.gridLayout_5.addWidget(self.ConfigurationTabs, 0, 0, 1, 1)
        configurationsWindow.setCentralWidget(self.windowBackground)
#*-------------------------Team Configuration Tab----------------------------------------------------*#
        self.TeamConfigurationTab = QtWidgets.QWidget()
        self.TeamConfigurationTab.setObjectName("TeamConfigurationTab")
        self.ConfigurationTabs.addTab(self.TeamConfigurationTab, "")
        #sets tab to a grid layout
        self.gridLayout = QtWidgets.QGridLayout(self.TeamConfigurationTab)
        self.gridLayout.setObjectName("gridLayout")

        #lead checkbox
        self.leadCheckbox = QtWidgets.QCheckBox(self.TeamConfigurationTab)
        self.leadCheckbox.setObjectName("leadCheckbox")
        self.gridLayout.addWidget(self.leadCheckbox, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)

        #lead IP address
        self.leadIPAddrLabel = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.leadIPAddrLabel.setObjectName("leadIPAddrLabel")
        self.gridLayout.addWidget(self.leadIPAddrLabel, 1, 0, 1, 1)
        self.leadIPAddr = QtWidgets.QLineEdit(self.TeamConfigurationTab)
        self.leadIPAddr.setObjectName("leadIPAddr")
        self.gridLayout.addWidget(self.leadIPAddr, 1, 1, 1, 1)

        #number of connections to the lead's IP address 
        self.numOfConnectionsLabel = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.numOfConnectionsLabel.setObjectName("numOfConnectionsLabel")
        self.gridLayout.addWidget(self.numOfConnectionsLabel, 2, 0, 1, 1)
        self.numOfConnections = QtWidgets.QLineEdit(self.TeamConfigurationTab)
        self.numOfConnections.setEnabled(False)
        self.numOfConnections.setObjectName("numOfConnections")
        self.gridLayout.addWidget(self.numOfConnections, 2, 1, 1, 1)

        #adds a label to use as a spacer to keep desired layout & properties
        self.spacer2 = QtWidgets.QLabel(self.TeamConfigurationTab)
        self.spacer2.setText("")
        self.spacer2.setObjectName("spacer2")
        self.gridLayout.addWidget(self.spacer2, 4, 0, 1, 1)

        #connect button 
        self.connectBttn = QtWidgets.QPushButton(self.TeamConfigurationTab)
        self.connectBttn.setObjectName("connectBttn")
        self.gridLayout.addWidget(self.connectBttn, 3, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Event Configuration Tab----------------------------------------------------*#
        self.EventConfigurationTab = QtWidgets.QWidget()
        self.EventConfigurationTab.setObjectName("EventConfigurationTab")
        self.ConfigurationTabs.addTab(self.EventConfigurationTab, "")

        #sets tab to a grid layout
        self.gridLayout_2 = QtWidgets.QGridLayout(self.EventConfigurationTab)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #event name 
        self.eventNameLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventNameLabel.setObjectName("eventNameLabel")
        self.gridLayout_2.addWidget(self.eventNameLabel, 0, 0, 1, 1)
        self.eventName = QtWidgets.QLineEdit(self.EventConfigurationTab)
        self.eventName.setObjectName("eventName")
        self.gridLayout_2.addWidget(self.eventName, 0, 1, 1, 1)

        #event description
        self.eventDescLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventDescLabel.setObjectName("eventDescLabel")
        self.gridLayout_2.addWidget(self.eventDescLabel, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.eventDesc = QtWidgets.QTextEdit(self.EventConfigurationTab)
        self.eventDesc.setObjectName("eventDesc")
        self.gridLayout_2.addWidget(self.eventDesc, 1, 1, 1, 1)

        #event start
        self.eventStartLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventStartLabel.setObjectName("eventStartLabel")
        self.gridLayout_2.addWidget(self.eventStartLabel, 4, 0, 1, 1)
        self.eventStart = QtWidgets.QDateTimeEdit(self.EventConfigurationTab)
        self.eventStart.setDate(QtCore.QDate(2020, 1, 1))
        self.eventStart.setCalendarPopup(True)
        self.eventStart.setObjectName("eventStart")
        self.gridLayout_2.addWidget(self.eventStart, 4, 1, 1, 1)

        #event end
        self.eventEndLabel = QtWidgets.QLabel(self.EventConfigurationTab)
        self.eventEndLabel.setObjectName("eventEndLabel")
        self.gridLayout_2.addWidget(self.eventEndLabel, 6, 0, 1, 1)
        self.eventEnd = QtWidgets.QDateTimeEdit(self.EventConfigurationTab)
        self.eventEnd.setDate(QtCore.QDate(2020, 1, 1))
        self.eventEnd.setCalendarPopup(True)
        self.eventEnd.setObjectName("eventEnd")
        self.gridLayout_2.addWidget(self.eventEnd, 6, 1, 1, 1)

        #save event button
        self.saveEventBttn = QtWidgets.QPushButton(self.EventConfigurationTab)
        self.saveEventBttn.setObjectName("saveEventBttn")
        self.gridLayout_2.addWidget(self.saveEventBttn, 7, 1, 1, 1, QtCore.Qt.AlignRight)
#*-------------------------Directory Configuration Tab----------------------------------------------------*#
        self.DirectoryConfigurationTab = QtWidgets.QWidget()
        self.DirectoryConfigurationTab.setObjectName("DirectoryConfigurationTab")

        #sets tab to a grid layout
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DirectoryConfigurationTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ConfigurationTabs.addTab(self.DirectoryConfigurationTab, "")

        #root directory
        self.rootDirectoryLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.rootDirectoryLabel.setObjectName("rootDirectoryLabel")
        self.gridLayout_3.addWidget(self.rootDirectoryLabel, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.rootDirectory = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.rootDirectory.setObjectName("rootDirectory")
        self.gridLayout_3.addWidget(self.rootDirectory, 0, 1, 1, 1)

        self.searchDirectoryBttn = QtWidgets.QPushButton(self.DirectoryConfigurationTab)
        self.searchDirectoryBttn.setObjectName("searchDirectoryBttn")
        self.gridLayout_3.addWidget(self.searchDirectoryBttn, 0, 2, 1, 1)

        #red team folder
        self.redTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.redTeamLabel.setObjectName("redTeamLabel")
        self.gridLayout_3.addWidget(self.redTeamLabel, 1, 0, 1, 1)
        self.redTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.redTeamFolder.setObjectName("redTeamFolder")
        self.gridLayout_3.addWidget(self.redTeamFolder, 1, 1, 1, 1)

        self.searchRTFbttn = QtWidgets.QPushButton(self.DirectoryConfigurationTab)
        self.searchRTFbttn.setObjectName("searchRTFbttn")
        self.gridLayout_3.addWidget(self.searchRTFbttn, 1, 2, 1, 1)

        #blue team folder
        self.blueTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.blueTeamLabel.setObjectName("blueTeamLabel")
        self.gridLayout_3.addWidget(self.blueTeamLabel, 2, 0, 1, 1)
        self.blueTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.blueTeamFolder.setObjectName("blueTeamFolder")
        self.gridLayout_3.addWidget(self.blueTeamFolder, 2, 1, 1, 1)

        self.searchBTFbttn = QtWidgets.QPushButton(self.DirectoryConfigurationTab)
        self.searchBTFbttn.setObjectName("searchBTFbttn")
        self.gridLayout_3.addWidget(self.searchBTFbttn, 2, 2, 1, 1)

        #white team folder
        self.whiteTeamLabel = QtWidgets.QLabel(self.DirectoryConfigurationTab)
        self.whiteTeamLabel.setObjectName("whiteTeamLabel")
        self.gridLayout_3.addWidget(self.whiteTeamLabel, 3, 0, 1, 1)
        self.whiteTeamFolder = QtWidgets.QLineEdit(self.DirectoryConfigurationTab)
        self.whiteTeamFolder.setObjectName("whiteTeamFolder")
        self.gridLayout_3.addWidget(self.whiteTeamFolder, 3, 1, 1, 1)

        self.searchWTFbttn = QtWidgets.QPushButton(self.DirectoryConfigurationTab)
        self.searchWTFbttn.setObjectName("searchWTFbttn")
        self.gridLayout_3.addWidget(self.searchWTFbttn, 3, 2, 1, 1)

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

        #vector name
        self.vectorNameLabel = QtWidgets.QLabel(self.VectorConfigurationTab)
        self.vectorNameLabel.setObjectName("vectorNameLabel")
        self.gridLayout_4.addWidget(self.vectorNameLabel, 0, 0, 1, 1)
        self.vectorName = QtWidgets.QLineEdit(self.VectorConfigurationTab)
        print(self.vectorName)
        self.vectorName.setObjectName("vectorName")
        self.gridLayout_4.addWidget(self.vectorName, 0, 1, 1, 1)

        #vector description
        self.vectorDescLabel = QtWidgets.QLabel(self.VectorConfigurationTab)
        self.vectorDescLabel.setObjectName("vectorDescLabel")
        self.gridLayout_4.addWidget(self.vectorDescLabel, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.vectorDesc = QtWidgets.QTextEdit(self.VectorConfigurationTab)
        self.vectorDesc.setObjectName("vectorDesc")
        self.gridLayout_4.addWidget(self.vectorDesc, 1, 1, 1, 1)

        #add vector button 
        self.addVectorBttn = QtWidgets.QPushButton(self.VectorConfigurationTab)
        self.addVectorBttn.setObjectName("addVectorBttn")
        self.gridLayout_4.addWidget(self.addVectorBttn, 2, 1, 1, 1, QtCore.Qt.AlignRight)

        #vector table tree widget & properties
        self.vectorTable = QtWidgets.QTreeWidget(self.VectorConfigurationTab)
        self.vectorTable.setAlternatingRowColors(True)
        self.vectorTable.setAllColumnsShowFocus(False)
        self.vectorTable.setObjectName("vectorTable")
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

#*-------------------------Icon Configuration Tab----------------------------------------------------*#
        self.ConfigurationTabs.addTab(self.VectorConfigurationTab, "")
        self.IconConfigurationTab = QtWidgets.QWidget()
        self.IconConfigurationTab.setObjectName("IconConfigurationTab")
        self.ConfigurationTabs.addTab(self.IconConfigurationTab, "")
        self.gridLayout_5.addWidget(self.ConfigurationTabs, 1, 0, 1, 1)
        #set tab to a grid layout
        self.gridLayout_6 = QtWidgets.QGridLayout(self.IconConfigurationTab)
        self.gridLayout_6.setObjectName("gridLayout_6")      

        #Icon Name
        self.iconNameLabel = QtWidgets.QLabel(self.IconConfigurationTab)
        self.iconNameLabel.setObjectName("iconNameLabel")
        self.gridLayout_6.addWidget(self.iconNameLabel, 1, 0, 1, 1)
        self.iconName = QtWidgets.QLineEdit(self.IconConfigurationTab)
        self.iconName.setObjectName("iconName")
        self.gridLayout_6.addWidget(self.iconName, 1, 1, 1, 1)

        #icon source
        self.iconSourceLabel = QtWidgets.QLabel(self.IconConfigurationTab)
        self.iconSourceLabel.setObjectName("iconSourceLabel")
        self.gridLayout_6.addWidget(self.iconSourceLabel, 2, 0, 1, 1)
        self.iconSource = QtWidgets.QLineEdit(self.IconConfigurationTab)
        self.iconSource.setObjectName("iconSource")
        self.gridLayout_6.addWidget(self.iconSource, 2, 1, 1, 1)

        self.searchIconBttn = QtWidgets.QPushButton(self.IconConfigurationTab)
        self.searchIconBttn.setObjectName("searchIconBttn")
        self.gridLayout_6.addWidget(self.searchIconBttn, 2, 3, 1, 1)

        #Add Icon Button
        self.addIconBttn = QtWidgets.QPushButton(self.IconConfigurationTab)
        self.addIconBttn.setObjectName("addIconBttn")
        self.gridLayout_6.addWidget(self.addIconBttn, 3, 1, 1, 1, QtCore.Qt.AlignRight)

        #Icon Table Tree Widget
        self.iconTable = QtWidgets.QTreeWidget(self.IconConfigurationTab)
        self.iconTable.setAlternatingRowColors(True)
        self.iconTable.setAllColumnsShowFocus(False)
        self.iconTable.setObjectName("iconTable")
        self.iconTable.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.iconTable.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.iconTable.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.iconTable.header().setDefaultSectionSize(250)
        self.iconTable.header().setSortIndicatorShown(True)
        self.gridLayout_6.addWidget(self.iconTable, 4, 0, 1, 4)

        #creating space withing vector table to add data later
        for i in range(3):
            QtWidgets.QTreeWidgetItem(self.iconTable)


        #Delete Icon Button
        self.deleteIconBttn = QtWidgets.QPushButton(self.IconConfigurationTab)
        self.deleteIconBttn.setObjectName("deleteIconBttn")
        self.gridLayout_6.addWidget(self.deleteIconBttn, 7, 3, 1, 1, QtCore.Qt.AlignRight)
        


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
        #set checkbox, labels, buttons and text fields
        self.leadCheckbox.setText(insert("configurationsWindow", "Lead"))
        self.leadIPAddrLabel.setText(insert("configurationsWindow", "Lead IP Address:"))
        self.numOfConnectionsLabel.setText(insert("configurationsWindow", "No. of estrablished connections:"))
        self.connectBttn.setText(insert("configurationsWindow", "Connect"))
        self.numOfConnections.setText(insert("configurationsWindow", "5"))  
#*--------------------------Event Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.EventConfigurationTab), insert("configurationsWindow", "Event Configuration"))
        #Set labels & buttons
        self.eventNameLabel.setText(insert("configurationsWindow", "Event Name:"))
        self.eventDescLabel.setText(insert("configurationsWindow", "Event Description:"))
        self.eventStartLabel.setText(insert("configurationsWindow", "Event Start Timestamp:"))
        self.eventEndLabel.setText(insert("configurationsWindow", "Event End Timestamp:"))
        self.saveEventBttn.setText(insert("configurationsWindow", "Save Event"))
#*--------------------------Directory Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.DirectoryConfigurationTab), insert("configurationsWindow", "Directory Configuration"))
        #Set Labels & buttons
        self.rootDirectoryLabel.setText(insert("configurationsWindow", "Root Directory:"))
        self.redTeamLabel.setText(insert("configurationsWindow", "Red Team Folder:"))
        self.blueTeamLabel.setText(insert("configurationsWindow", "Blue Team Folder:"))
        self.whiteTeamLabel.setText(insert("configurationsWindow", "White Team Folder:"))
        self.startDataIngestionBttn.setText(insert("configurationsWindow", "Start Data Ingestion"))

        
        self.searchDirectoryBttn.setIcon(QtGui.QIcon("folderBrowser.png"))
        self.searchDirectoryBttn.clicked.connect(lambda: self.open_directory_dialog_box(self.rootDirectory))
        self.searchRTFbttn.setIcon(QtGui.QIcon("folderBrowser.png"))
        self.searchRTFbttn.clicked.connect(lambda: self.open_directory_dialog_box(self.redTeamFolder))
        self.searchBTFbttn.setIcon(QtGui.QIcon("folderBrowser.png"))
        self.searchBTFbttn.clicked.connect(lambda: self.open_directory_dialog_box(self.blueTeamFolder))
        self.searchWTFbttn.setIcon(QtGui.QIcon("folderBrowser.png"))
        self.searchWTFbttn.clicked.connect(lambda: self.open_directory_dialog_box(self.whiteTeamFolder))
        
#*--------------------------Vector Configuration Tab--------------------------------------------------*#
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.VectorConfigurationTab), insert("configurationsWindow", "Vector Configuration"))
        #Set labels, buttons & headers
        self.vectorNameLabel.setText(insert("configurationsWindow", "Vector Name:"))
        self.vectorDescLabel.setText(insert("configurationsWindow", "Vector Description:"))
        self.addVectorBttn.setText(insert("configurationsWindow", "Add Vector"))
        self.deleteVectorBttn.setText(insert("configurationsWindow", "Delete Vector"))
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

#*--------------------------Icon Configuration Tab--------------------------------------------------*#
        self.deleteIconBttn.setText(insert("configurationsWindow", "Delete Icon"))
        self.addIconBttn.setText(insert("configurationsWindow", "Add Icon"))
        self.iconNameLabel.setText(insert("configurationsWindow", "Icon Name: "))

        self.searchIconBttn.setIcon(QtGui.QIcon("folderBrowser.png"))
        self.searchIconBttn.clicked.connect(lambda: self.open_file_dialog_box(self.iconSource))

        self.iconTable.setSortingEnabled(True)
        self.iconTable.headerItem().setText(0, insert("configurationsWindow", "Icon Name"))
        self.iconTable.headerItem().setText(1, insert("configurationsWindow", "Icon Source"))
        self.iconTable.headerItem().setText(2, insert("configurationsWindow", "Image Preview"))
        __sortingEnabled = self.iconTable.isSortingEnabled()
        self.iconTable.setSortingEnabled(False)
        self.iconTable.topLevelItem(0).setText(0, insert("configurationsWindow", "Icon 3"))
        self.iconTable.topLevelItem(1).setText(0, insert("configurationsWindow", "Icon 2"))
        self.iconTable.topLevelItem(2).setText(0, insert("configurationsWindow", "Icon 1"))
        self.iconTable.setSortingEnabled(__sortingEnabled)
        self.iconSourceLabel.setText(insert("configurationsWindow", "Icon Source: "))
        self.ConfigurationTabs.setTabText(self.ConfigurationTabs.indexOf(self.IconConfigurationTab), insert("configurationsWindow", "Icon Configuration"))

       
    def open_file_dialog_box(self, lineEdit):
        filename = QtWidgets.QFileDialog.getOpenFileNames()
        if len(filename[0])==0:
            return
        else:
            path = filename[0][0]
        
        insert = QtCore.QCoreApplication.translate
        lineEdit.setText(insert("configurationsWindow", path))   

    def open_directory_dialog_box(self, lineEdit):
        directoryName = QtWidgets.QFileDialog.getExistingDirectory()
        print("directory ======" + str(directoryName))
        if directoryName == "":
            return
        else:
            path = directoryName
        
        insert = QtCore.QCoreApplication.translate
        lineEdit.setText(insert("configurationsWindow", path))


        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    configurationsWindow = QtWidgets.QMainWindow()
    ui = ConfigurationsWindow()
    ui.generateUi(configurationsWindow)
    configurationsWindow.show()
    sys.exit(app.exec_())
