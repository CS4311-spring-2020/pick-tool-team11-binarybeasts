from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication)


class actionReport(object):
    app = QApplication([])
    app.setStyle('Fusion')

    def generateUi(self, actionReportWindow):
        actionReportWindow.setObjectName("actionReportWindow")
        # row, column
        actionReportWindow.resize(2500, 950)
        actionReportWindow.setAutoFillBackground(False)

        self.windowBackground = QtWidgets.QWidget(actionReportWindow)
        self.windowBackground.setObjectName("windowBackground")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.windowBackground)
        self.verticalLayout.setObjectName("verticalLayout")
        # action report table properties
        self.reportTableTitle = QtWidgets.QGroupBox(self.windowBackground)
        self.reportTableTitle.setObjectName("reportTableTitle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.reportTableTitle)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.reportTable = QtWidgets.QTreeWidget(self.reportTableTitle)
        self.reportTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.reportTable.setDefaultDropAction(QtCore.Qt.ActionMask)
        # seperates the rows with grey coloring
        self.reportTable.setAlternatingRowColors(True)
        self.reportTable.setRootIsDecorated(True)
        self.reportTable.setHeaderHidden(False)
        self.reportTable.setObjectName("reportTable")
        
        # creating space to add data later
        for i in range(4):
            QtWidgets.QTreeWidgetItem(self.reportTable)
       

        # changes the header space in between (like log file from source path)
        self.reportTable.header().setDefaultSectionSize(350)
        self.reportTable.header().setHighlightSections(True)

        # gives action report table the vertical layout
        self.verticalLayout_3.addWidget(self.reportTable)
        self.verticalLayout.addWidget(self.reportTableTitle)

        # selected log file table properties (Error Description table)
        self.selectedLogFile = QtWidgets.QGroupBox(self.windowBackground)
        self.selectedLogFile.setObjectName("selectedLogFile")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.selectedLogFile)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.errorDescription = QtWidgets.QTreeWidget(self.selectedLogFile)
        self.errorDescription.setEnabled(True)
        # seperates the rows with grey coloring
        self.errorDescription.setAlternatingRowColors(True)
        self.errorDescription.setUniformRowHeights(False)
        # option to hide header or keep it 
        self.errorDescription.setHeaderHidden(False)
        # can expand table on double click
        self.errorDescription.setExpandsOnDoubleClick(False)
        # errorDescription is the name of the table object
        self.errorDescription.setObjectName("errorDescription")
        
        # creating space to add data later
        for i in range(5):
            QtWidgets.QTreeWidgetItem(self.errorDescription)
        
        # option to hide header or keep it 
        self.errorDescription.header().setVisible(True)
        # changes the table to move along with the cursor. (like the override button)
        self.errorDescription.header().setCascadingSectionResizes(True)
        
        # changes the header space in between (like log file from source path)
        self.errorDescription.header().setDefaultSectionSize(450)
        self.errorDescription.header().setHighlightSections(False)
        # gives the error description table the vertical layout
        self.verticalLayout_2.addWidget(self.errorDescription)
        self.verticalLayout.addWidget(self.selectedLogFile)

        # creating an override button at the bottom of the 2 tables
        self.overrideButton = QtWidgets.QPushButton(self.windowBackground)
        self.overrideButton.setObjectName("overrideButton")
        self.verticalLayout.addWidget(self.overrideButton)
        
        # creating an expand button at the bottom of the 2 tables
        self.expandButton = QtWidgets.QPushButton(self.windowBackground)
        self.expandButton.setObjectName("expandButton")
        self.verticalLayout.addWidget(self.expandButton)

        actionReportWindow.setCentralWidget(self.windowBackground)
        # this is creating the menu bar options
        self.menuBarButton = QtWidgets.QMenuBar(actionReportWindow)
        # setting the position of the menu button option
        self.menuBarButton.setGeometry(QtCore.QRect(0, 0, 683, 22))
        self.menuBarButton.setObjectName("menuBarButton")
        self.menuMenu = QtWidgets.QMenu(self.menuBarButton)
        self.menuMenu.setObjectName("menuMenu")
        actionReportWindow.setMenuBar(self.menuBarButton)

        self.statusbar = QtWidgets.QStatusBar(actionReportWindow)
        self.statusbar.setObjectName("statusbar")
        actionReportWindow.setStatusBar(self.statusbar)
        # adding the Event Configuration option
        self.menuEvent_Configuration = QtWidgets.QAction(actionReportWindow)
        self.menuEvent_Configuration.setObjectName("menuEvent_Configuration")
        # adding the Enforcement Action Report option
        self.menuEnforcement_Action_Report = QtWidgets.QAction(actionReportWindow)
        self.menuEnforcement_Action_Report.setObjectName("menuEnforcement_Action_Report")
        # adding the Search/Filter Log Entries option
        self.menuSearch_Filter_Log_Entries = QtWidgets.QAction(actionReportWindow)
        self.menuSearch_Filter_Log_Entries.setObjectName("menuSearch_Filter_Log_Entries")
        # adding the Manage Graph option
        self.menuManage_Graph = QtWidgets.QAction(actionReportWindow)
        self.menuManage_Graph.setObjectName("menuManage_Graph")

        # options to add Action to each of the buttons
        self.menuMenu.addAction(self.menuEvent_Configuration)
        self.menuMenu.addAction(self.menuEnforcement_Action_Report)
        self.menuMenu.addAction(self.menuSearch_Filter_Log_Entries)
        self.menuMenu.addAction(self.menuManage_Graph)
        self.menuBarButton.addAction(self.menuMenu.menuAction())
        # adds the data to the window
        self.addData(actionReportWindow)
        
        # whenever an item is pressed in the action report table, hide the error description table.
        #self.reportTable.itemPressed['QTreeWidgetItem*','int'].connect(self.errorDescription.expandAll)
        
        # whenever the override button is pressed, hide the error description table.
        self.overrideButton.pressed.connect(self.selectedLogFile.hide)

        # whenever an item is pressed in the action report table, hide the error description table.
        #self.reportTable.itemPressed['QTreeWidgetItem*','int'].connect(self.errorDescription.expandAll)
        
        # whenever the expand button is pressed, expand the error description table.
        self.expandButton.pressed.connect(self.selectedLogFile.show)

        QtCore.QMetaObject.connectSlotsByName(actionReportWindow)
        # sets the tab order for the user
        actionReportWindow.setTabOrder(self.reportTable, self.errorDescription)
        actionReportWindow.setTabOrder(self.errorDescription, self.overrideButton)

    def addData(self, actionReportWindow):
        insert = QtCore.QCoreApplication.translate
        actionReportWindow.setWindowTitle(insert("actionReportWindow", "Log Configuration"))
        # Filling in the action report headers
        self.reportTableTitle.setTitle(insert("actionReportWindow", "Enforcement Action Report"))
        self.reportTable.headerItem().setText(0, insert("actionReportWindow", "Log File"))
        self.reportTable.headerItem().setText(1, insert("actionReportWindow", "Source Path"))
        self.reportTable.headerItem().setText(2, insert("actionReportWindow", "Cleansing Status"))
        self.reportTable.headerItem().setText(3, insert("actionReportWindow", "Validation Status"))
        self.reportTable.headerItem().setText(4, insert("actionReportWindow", "Ingestion Status"))
        __sortingEnabled = self.reportTable.isSortingEnabled()
        self.reportTable.setSortingEnabled(False)
        # Filling in the table contents 
        self.reportTable.topLevelItem(0).setText(0, insert("actionReportWindow", "Log File 1"))
        self.reportTable.topLevelItem(0).setText(1, insert("actionReportWindow", "/path/observer_notes.osv"))
        self.reportTable.topLevelItem(0).setText(2, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(0).setText(3, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(0).setText(4, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(1).setText(0, insert("actionReportWindow", "Log File 2"))
        self.reportTable.topLevelItem(1).setText(1, insert("actionReportWindow", "/path/incident_report.pd"))
        self.reportTable.topLevelItem(1).setText(2, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(1).setText(3, insert("actionReportWindow", "-"))
        self.reportTable.topLevelItem(1).setText(4, insert("actionReportWindow", "-"))
        self.reportTable.topLevelItem(2).setText(0, insert("actionReportWindow", "Log File 3"))
        self.reportTable.topLevelItem(2).setText(1, insert("actionReportWindow", "/path/observer_notes.osv"))
        self.reportTable.topLevelItem(2).setText(2, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(2).setText(3, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(2).setText(4, insert("actionReportWindow", "+"))
        self.reportTable.topLevelItem(3).setText(0, insert("actionReportWindow", "Log File 4"))
        self.reportTable.topLevelItem(3).setText(1, insert("actionReportWindow", "/path/incident_report.pd"))
        self.reportTable.topLevelItem(3).setText(2, insert("actionReportWindow", "-"))
        self.reportTable.topLevelItem(3).setText(3, insert("actionReportWindow", "-"))
        self.reportTable.topLevelItem(3).setText(4, insert("actionReportWindow", "-"))
        self.reportTable.setSortingEnabled(__sortingEnabled)

        # hardcoding the error description title
        self.selectedLogFile.setTitle(insert("actionReportWindow", "Log File 2"))
        # naming the error description headers
        self.errorDescription.headerItem().setText(0, insert("actionReportWindow", "Line Number"))
        self.errorDescription.headerItem().setText(1, insert("actionReportWindow", "Error Description"))

        __sortingEnabled = self.errorDescription.isSortingEnabled()
        self.errorDescription.setSortingEnabled(False)
        # adding information to the error description table
        self.errorDescription.topLevelItem(0).setText(0, insert("actionReportWindow", "0-001"))
        self.errorDescription.topLevelItem(0).setText(1, insert("actionReportWindow", "Time is invalid format...."))
        self.errorDescription.topLevelItem(1).setText(0, insert("actionReportWindow", "0-009"))
        self.errorDescription.topLevelItem(1).setText(1, insert("actionReportWindow", "No date is found ...."))
        self.errorDescription.topLevelItem(2).setText(0, insert("actionReportWindow", "0-015"))
        self.errorDescription.topLevelItem(2).setText(1, insert("actionReportWindow", "Date is in invalid format...."))
        self.errorDescription.topLevelItem(3).setText(0, insert("actionReportWindow", "0-026"))
        self.errorDescription.topLevelItem(3).setText(1, insert("actionReportWindow", "Time is invalid format...."))
        self.errorDescription.topLevelItem(4).setText(0, insert("actionReportWindow", "0-099"))
        self.errorDescription.topLevelItem(4).setText(1, insert("actionReportWindow", "No date is found ...."))
        self.errorDescription.setSortingEnabled(__sortingEnabled)
        # adding data to the buttons. (Filling them in)
        self.overrideButton.setText(insert("actionReportWindow", "Override Errors"))
        self.expandButton.setText(insert("actionReportWindow", "Expand Selected Log File"))
        self.menuMenu.setTitle(insert("actionReportWindow", "Menu"))
        self.menuEvent_Configuration.setText(insert("actionReportWindow", "Event Configuration"))
        self.menuEnforcement_Action_Report.setText(insert("actionReportWindow", "Enforcement Action Report"))
        self.menuSearch_Filter_Log_Entries.setText(insert("actionReportWindow", "Search/Filter Log Entries"))
        self.menuManage_Graph.setText(insert("actionReportWindow", "Manage Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    actionReportWindow = QtWidgets.QMainWindow()
    ui = actionReport()
    ui.generateUi(actionReportWindow)
    actionReportWindow.show()
    sys.exit(app.exec_())
