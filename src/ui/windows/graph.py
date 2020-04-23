from ui.windows import search_filter, configurations_window, action_report, graph
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
import sys
import os
sys.path.insert(1,os.path.dirname(__file__)+"/..")

from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot


class GraphWindow(object):
    def setupUi(self, graphWindow):
        graphWindow.setObjectName("graphWindow")
        graphWindow.resize(1155, 895)
        graphWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(graphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        #*-----------------------vector selection objects------------------------------------------------*#

        self.groupBoxVectorSelection = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxVectorSelection.sizePolicy().hasHeightForWidth())
        self.groupBoxVectorSelection.setSizePolicy(sizePolicy)
        self.groupBoxVectorSelection.setObjectName("groupBoxVectorSelection")
        self.gridLayout.addWidget(self.groupBoxVectorSelection, 0, 0, 1, 1)
        self.formLayoutVector = QtWidgets.QHBoxLayout(self.groupBoxVectorSelection)
        self.formLayoutVector.setObjectName("formLayoutVector")
        
        #vector label
        self.labelVector = QtWidgets.QLabel(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVector.sizePolicy().hasHeightForWidth())
        self.labelVector.setSizePolicy(sizePolicy)
        self.labelVector.setObjectName("labelVector")
        self.formLayoutVector.addWidget(self.labelVector) 

        #vector combo box
        self.comboBoxVector = QtWidgets.QComboBox(self.groupBoxVectorSelection)
        self.comboBoxVector.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxVector.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboBoxVector.setObjectName("comboBoxVector")
        vectors = 3
        for vector in range(vectors):
            self.comboBoxVector.addItem("")
        self.formLayoutVector.addWidget(self.comboBoxVector)

        #vector description label
        self.labelVectorDesc = QtWidgets.QLabel(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVectorDesc.sizePolicy().hasHeightForWidth())
        self.labelVectorDesc.setSizePolicy(sizePolicy)
        self.labelVectorDesc.setObjectName("labelVectorDesc")
        self.formLayoutVector.addWidget(self.labelVectorDesc)

        #vector description line edit
        self.lineEditVectorDesc = QtWidgets.QLineEdit(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVectorDesc.sizePolicy().hasHeightForWidth())
        self.lineEditVectorDesc.setSizePolicy(sizePolicy)
        self.lineEditVectorDesc.setObjectName("lineEditVectorDesc")
        self.formLayoutVector.addWidget(self.lineEditVectorDesc)

        #*----------------------multi-document-area---------------------------------------------------------------*#
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mdiArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mdiArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.mdiArea.setActivationOrder(QtWidgets.QMdiArea.ActivationHistoryOrder)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mdiArea.setTabPosition(QtWidgets.QTabWidget.North)
        self.mdiArea.setObjectName("mdiArea")


    #*-------------------------Graph Subwindow------------------------------------------------------------------*#

        self.subwindow_Graph = QtWidgets.QWidget()
        self.subwindow_Graph.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.subwindow_Graph.setObjectName("subwindow_Graph")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.subwindow_Graph)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        # Interval Label and combo box
        self.IntervalLabel = QtWidgets.QLabel(self.subwindow_Graph)
        self.IntervalLabel.setObjectName("IntervalLabel")
        self.gridLayout_3.addWidget(self.IntervalLabel, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.Interval = QtWidgets.QComboBox(self.subwindow_Graph)
        self.Interval.setObjectName("Interval")
        self.Interval.addItem("") # Select Interval
        self.Interval.addItem("") # Seconds
        self.Interval.addItem("") # Minutes 
        self.Interval.addItem("") # Hours
        self.gridLayout_3.addWidget(self.Interval, 2, 2, 1, 1)

        #Timeline orientation label and combo box
        self.TimelineOrientationLabel = QtWidgets.QLabel(self.subwindow_Graph)
        self.TimelineOrientationLabel.setObjectName("TimelineOrientationLabel")
        self.gridLayout_3.addWidget(self.TimelineOrientationLabel, 2, 3, 1, 1, QtCore.Qt.AlignRight)
        self.TimelineOrientation = QtWidgets.QComboBox(self.subwindow_Graph)
        self.TimelineOrientation.setObjectName("TimelineOrientation")
        self.TimelineOrientation.addItem("") # Selection Orientation
        self.TimelineOrientation.addItem("") # Horizontal
        self.TimelineOrientation.addItem("") # Vertical
        self.gridLayout_3.addWidget(self.TimelineOrientation, 2, 4, 1, 1)

        
        # Events
        def node_selected(node):
            if(qgv.manipulation_mode==QGraphVizManipulationMode.Node_remove_Mode):
                print("Node {} removed".format(node))
            else:
                print("Node selected {}".format(node))

        def edge_selected(edge):
            if(qgv.manipulation_mode==QGraphVizManipulationMode.Edge_remove_Mode):
                print("Edge {} removed".format(edge))
            else:
                print("Edge selected {}".format(edge))

        def node_invoked(node):
            print("Node double clicked")
        def edge_invoked(node):
            print("Edge double clicked")
        def node_removed(node):
            print("Node removed")
        def edge_removed(node):
            print("Edge removed")

        # Create QGraphViz graph widget
        show_subgraphs=True
        qgv = QGraphViz(
            show_subgraphs=show_subgraphs,
            
            node_selected_callback=node_selected,
            edge_selected_callback=edge_selected,
            node_invoked_callback=node_invoked,
            edge_invoked_callback=edge_invoked,
            node_removed_callback=node_removed,
            edge_removed_callback=edge_removed,

            hilight_Nodes=True,
            hilight_Edges=True
            )
        qgv.setStyleSheet("background-color:white;")

        # Create A new Graph using Dot layout engine
        qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))


        # Build the graph (the layout engine organizes where the nodes and connections are)
        qgv.build()
        # Save it to a file to be loaded by Graphviz if needed
        qgv.save("test.gv")
        

        # Create a widget to handle the QGraphViz object
        graphWidget=QWidget()
        graphWidget.setLayout(QVBoxLayout())
        self.gridLayout_3.addWidget(graphWidget, 3, 0, 1, 6)
        # Add the QGraphViz object to the layout
        graphWidget.layout().addWidget(qgv)


        #Buttons Functionality
        def manipulate():
            qgv.manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode

        def save():
            fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.csv")
            if(fname[0]!=""):
                qgv.save(fname[0])

            #fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
            #if(fname[0]!=""):
            #    qgv.saveAsJson(fname[0])  

            #fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.gv")
            #if(fname[0]!=""):
            #    qgv.save(fname[0])
            
        def new():
            qgv.engine.graph = Graph("MainGraph")
            qgv.build()
            qgv.repaint()

        def load():
            fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.csv")
            if(fname[0]!=""):
                qgv.load_file(fname[0])

            #fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
            #if(fname[0]!=""):
            #    qgv.loadAJson(fname[0])

            #fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.gv")
            #if(fname[0]!=""):
            #    qgv.load_file(fname[0])

        def add_node():

            #add node dialog
            addNodeDialog = QDialog()
            addNodeDialog.ok=False
            addNodeDialog.node_name=""
            addNodeDialog.node_label=""
            addNodeDialog.node_type="None"

            # Layouts
            main_layout = QVBoxLayout()
            addNodeLayout = QFormLayout()
            buttons_layout = QHBoxLayout()

            main_layout.addLayout(addNodeLayout)
            main_layout.addLayout(buttons_layout)
            addNodeDialog.setLayout(main_layout)

            #line edits
            leNodeName = QLineEdit()
            leNodeLabel = QLineEdit()
            cbxNodeType = QComboBox()
            leImagePath = QLineEdit()

            #buttons
            pbOK = QPushButton()
            pbCancel = QPushButton()

            cbxNodeType.addItems(["None","circle","box"])
            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            addNodeLayout.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
            addNodeLayout.setWidget(0, QFormLayout.FieldRole, leNodeName)
            addNodeLayout.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
            addNodeLayout.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
            addNodeLayout.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
            addNodeLayout.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
            addNodeLayout.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
            addNodeLayout.setWidget(3, QFormLayout.FieldRole, leImagePath)

            #ok button handler
            def ok():
                addNodeDialog.OK=True
                addNodeDialog.node_name = leNodeName.text()
                addNodeDialog.node_label = leNodeLabel.text()
                if(leImagePath.text()): 
                    addNodeDialog.node_type = "ui/windows/" + leImagePath.text() 
                else: 
                    addNodeDialog.node_type = cbxNodeType.currentText()
                addNodeDialog.close()

            #cancel button handler
            def cancel():
                addNodeDialog.OK=False
                addNodeDialog.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            addNodeDialog.exec_()

            #node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
            if addNodeDialog.OK and addNodeDialog.node_name != '':
                    qgv.addNode(qgv.engine.graph, addNodeDialog.node_name, label=addNodeDialog.node_label, shape=addNodeDialog.node_type)
                    qgv.build()

        def rem_node():
            qgv.manipulation_mode=QGraphVizManipulationMode.Node_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemNode.setChecked(True)


        def rem_edge():
            qgv.manipulation_mode=QGraphVizManipulationMode.Edge_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemEdge.setChecked(True)

        def add_edge():
            qgv.manipulation_mode=QGraphVizManipulationMode.Edges_Connect_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnAddEdge.setChecked(True)

        # Add two horizontal layouts (pannels to hold buttons)
        hpanelTop=QHBoxLayout()
        graphWidget.layout().addLayout(hpanelTop)

        hpanelBottom=QHBoxLayout()
        graphWidget.layout().addLayout(hpanelBottom)

        # Add buttons 
        btnNew = QPushButton("New")    
        btnNew.clicked.connect(new)
        hpanelTop.addWidget(btnNew) 

        btnOpen = QPushButton("Open")    
        btnOpen.clicked.connect(load)
        hpanelTop.addWidget(btnOpen)

        btnSave = QPushButton("Export")    
        btnSave.clicked.connect(save)
        hpanelTop.addWidget(btnSave)

        
        buttons_list=[]
        btnManip = QPushButton("Manipulate")    
        btnManip.setCheckable(True)
        btnManip.setChecked(True)
        btnManip.clicked.connect(manipulate)
        hpanelTop.addWidget(btnManip)
        buttons_list.append(btnManip)

        btnAddNode = QPushButton("Add Node")    
        btnAddNode.clicked.connect(add_node)
        hpanelBottom.addWidget(btnAddNode)
        buttons_list.append(btnManip)

        btnRemNode = QPushButton("Rem Node")    
        btnRemNode.setCheckable(True)
        btnRemNode.clicked.connect(rem_node)
        hpanelBottom.addWidget(btnRemNode)
        buttons_list.append(btnRemNode)

        btnAddEdge = QPushButton("Add Relationship")    
        btnAddEdge.setCheckable(True)
        btnAddEdge.clicked.connect(add_edge)
        hpanelBottom.addWidget(btnAddEdge)
        buttons_list.append(btnAddEdge)

        btnRemEdge = QPushButton("Rem Relationship")    
        btnRemEdge.setCheckable(True)
        btnRemEdge.clicked.connect(rem_edge)
        hpanelBottom.addWidget(btnRemEdge)
        buttons_list.append(btnRemEdge)
       

    #*-------------------------Tabular View Subwindow------------------------------------------------------------------*#

        self.subwindow_Table = QtWidgets.QWidget()
        self.subwindow_Table.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.subwindow_Table.setObjectName("subwindow_Table")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.subwindow_Table)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #table widget
        self.tableWidgetNodes = QtWidgets.QTableWidget(self.subwindow_Table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetNodes.sizePolicy().hasHeightForWidth())
        self.tableWidgetNodes.setSizePolicy(sizePolicy)
        self.tableWidgetNodes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetNodes.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidgetNodes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidgetNodes.setAlternatingRowColors(True)
        self.tableWidgetNodes.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidgetNodes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidgetNodes.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidgetNodes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetNodes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetNodes.setShowGrid(False)
        self.tableWidgetNodes.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetNodes.setCornerButtonEnabled(False)
        nodes = 3
        node_properties = 9
        self.tableWidgetNodes.setObjectName("tableWidgetNodes")
        self.tableWidgetNodes.setColumnCount(node_properties)
        self.tableWidgetNodes.setRowCount(nodes)
        #node table row header
        for node in range(nodes):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetNodes.setVerticalHeaderItem(node, item)

        #node table column header
        for property in range(node_properties):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetNodes.setHorizontalHeaderItem(property, item)

        #creates the first column in the first row without a check box
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidgetNodes.setItem(0, 0, item)

        #creates the rest of the columns in the first row with checkboxes
        for property in range(node_properties):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)
            self.tableWidgetNodes.setItem(0, property+1, item)

        #creates temporary nodes
        for node in range(nodes):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidgetNodes.setItem(node + 1, 0, item)
            for property in range(node_properties):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetNodes.setItem(node + 1, property + 1, item)

        #table properties
        self.tableWidgetNodes.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetNodes.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidgetNodes.horizontalHeader().setHighlightSections(True)
        self.tableWidgetNodes.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetNodes.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetNodes.verticalHeader().setVisible(True)
        self.tableWidgetNodes.verticalHeader().setMinimumSectionSize(30)
        self.tableWidgetNodes.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetNodes.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidgetNodes)

    #*-------------------------Relationship Table Subwindow------------------------------------------------------------------*#

        #subwindow and layout properties
        self.subwindow_Relationship = QtWidgets.QWidget()
        self.subwindow_Relationship.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.subwindow_Relationship.setObjectName("subwindow_Relationship")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.subwindow_Relationship)
        self.verticalLayout.setContentsMargins(-1, -1, 17, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        #add relationship frame
        self.frameRelationship = QtWidgets.QFrame(self.subwindow_Relationship)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameRelationship.sizePolicy().hasHeightForWidth())
        self.frameRelationship.setSizePolicy(sizePolicy)
        self.frameRelationship.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frameRelationship.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRelationship.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRelationship.setObjectName("frameRelationship")
        self.verticalLayout.addWidget(self.frameRelationship)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameRelationship)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #relationship label & line edit
        self.labelRelationship = QtWidgets.QLabel(self.frameRelationship)
        self.labelRelationship.setObjectName("labelRelationship")
        self.gridLayout_2.addWidget(self.labelRelationship, 0, 2, 1, 1)
        self.lineEditRelationship = QtWidgets.QLineEdit(self.frameRelationship)
        self.lineEditRelationship.setObjectName("lineEditRelationship")
        self.gridLayout_2.addWidget(self.lineEditRelationship, 0, 1, 1, 1)

        #parent node label & line edit
        self.labelParent = QtWidgets.QLabel(self.frameRelationship)
        self.labelParent.setObjectName("labelParent")
        self.gridLayout_2.addWidget(self.labelParent, 1, 2, 1, 1)
        self.lineEditParent = QtWidgets.QLineEdit(self.frameRelationship)
        self.lineEditParent.setObjectName("lineEditParent")
        self.gridLayout_2.addWidget(self.lineEditParent, 1, 1, 1, 1)

        #child node label & line edit
        self.labelChild = QtWidgets.QLabel(self.frameRelationship)
        self.labelChild.setObjectName("labelChild")
        self.gridLayout_2.addWidget(self.labelChild, 2, 2, 1, 1)
        self.lineEditChild = QtWidgets.QLineEdit(self.frameRelationship)
        self.lineEditChild.setObjectName("lineEditChild")
        self.gridLayout_2.addWidget(self.lineEditChild, 2, 1, 1, 1)

        #add relationship button
        self.pushButtonAddRelationship = QtWidgets.QPushButton(self.frameRelationship)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddRelationship.sizePolicy().hasHeightForWidth())
        self.pushButtonAddRelationship.setSizePolicy(sizePolicy)
        self.pushButtonAddRelationship.setObjectName("pushButtonAddRelationship")
        self.gridLayout_2.addWidget(self.pushButtonAddRelationship, 3, 1, 1, 1)

    

        #relationships table
        self.tableWidgetRelationships = QtWidgets.QTableWidget(self.subwindow_Relationship)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetRelationships.sizePolicy().hasHeightForWidth())
        self.tableWidgetRelationships.setSizePolicy(sizePolicy)
        self.tableWidgetRelationships.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetRelationships.setAlternatingRowColors(True)
        self.tableWidgetRelationships.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetRelationships.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetRelationships.setShowGrid(False)
        self.tableWidgetRelationships.setObjectName("tableWidgetRelationships")
        self.tableWidgetRelationships.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # a relationship is the length of a single relationship
        relationship = 4
        # relationships is the length of a set of relationships
        relationships = 4
        # setting the relationship table dimensions
        self.tableWidgetRelationships.setColumnCount(relationship)
        self.tableWidgetRelationships.setRowCount(relationships)
        # creating the row header for relationships
        for relation in range(relationships):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetRelationships.setVerticalHeaderItem(relation, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
            self.tableWidgetRelationships.setHorizontalHeaderItem(relation, item)
            

        # creates the table
        for relation in range(relationships):
            # creates a checkbox in the column
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidgetRelationships.setItem(relation, 0, item)
            for label in range(relationship):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetRelationships.setItem(relation, label+1, item)

        self.tableWidgetRelationships.horizontalHeader().setVisible(True)
        self.tableWidgetRelationships.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidgetRelationships.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetRelationships.verticalHeader().setVisible(True)
        self.tableWidgetRelationships.verticalHeader().setDefaultSectionSize(30)
        self.tableWidgetRelationships.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetRelationships)
        self.pushButtonDeleteRelationship = QtWidgets.QPushButton(self.subwindow_Relationship)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteRelationship.sizePolicy().hasHeightForWidth())

        #delete relationship button
        self.pushButtonDeleteRelationship.setSizePolicy(sizePolicy)
        self.pushButtonDeleteRelationship.setObjectName("pushButtonDeleteRelationship")
        self.verticalLayout.addWidget(self.pushButtonDeleteRelationship)

        
        self.mdiArea.addSubWindow(self.subwindow_Relationship)
        self.mdiArea.addSubWindow(self.subwindow_Table)
        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 1)
        self.mdiArea.addSubWindow(self.subwindow_Graph)

    #*------------------------------Menu Bar---------------------------------------------------*#
        graphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(graphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_Window = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_Window.setObjectName("menuOpen_Window")
        self.menuSubwindow_Layout_2 = QtWidgets.QMenu(self.menuFile)
        self.menuSubwindow_Layout_2.setObjectName("menuSubwindow_Layout_2")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        graphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(graphWindow)
        self.statusbar.setObjectName("statusbar")
        graphWindow.setStatusBar(self.statusbar)
        self.actionEvent_Configuration = QtWidgets.QAction(graphWindow)
        self.actionEvent_Configuration.setObjectName("actionEvent_Configuration")
        self.actionEnforcement_Action_Report = QtWidgets.QAction(graphWindow)
        self.actionEnforcement_Action_Report.setObjectName("actionEnforcement_Action_Report")
        self.actionManage_Graph = QtWidgets.QAction(graphWindow)
        self.actionManage_Graph.setObjectName("actionManage_Graph")
        self.actionFilter_Logs = QtWidgets.QAction(graphWindow)
        self.actionFilter_Logs.setObjectName("actionFilter_Logs")
        self.actionGraphical_View = QtWidgets.QAction(graphWindow)
        self.actionGraphical_View.setObjectName("actionGraphical_View")
        self.actionTabular_View = QtWidgets.QAction(graphWindow)
        self.actionTabular_View.setObjectName("actionTabular_View")
        self.actionRelationship_Table = QtWidgets.QAction(graphWindow)
        self.actionRelationship_Table.setObjectName("actionRelationship_Table")


        self.actionTile = QtWidgets.QAction(graphWindow)
        self.actionTile.setObjectName("actionTile")


        self.actionCascade = QtWidgets.QAction(graphWindow)
        self.actionCascade.setObjectName("actionCascade")


        self.menuOpen_Window.addAction(self.actionGraphical_View)
        self.menuOpen_Window.addAction(self.actionTabular_View)
        self.menuOpen_Window.addAction(self.actionRelationship_Table)
        self.menuSubwindow_Layout_2.addAction(self.actionTile)
        self.menuSubwindow_Layout_2.addAction(self.actionCascade)
        self.menuFile.addAction(self.menuOpen_Window.menuAction())
        self.menuFile.addAction(self.menuSubwindow_Layout_2.menuAction())
        self.menuMenu.addAction(self.actionEvent_Configuration)
        self.menuMenu.addAction(self.actionEnforcement_Action_Report)
        self.menuMenu.addAction(self.actionManage_Graph)
        self.menuMenu.addAction(self.actionFilter_Logs)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.mdiArea.tileSubWindows()

        self.retranslateUi(graphWindow)
        self.actionTile.triggered.connect(self.mdiArea.tileSubWindows)
        self.actionCascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        QtCore.QMetaObject.connectSlotsByName(graphWindow)

    def retranslateUi(self, graphWindow):
        insert = QtCore.QCoreApplication.translate
        graphWindow.setWindowTitle(insert("graphWindow", "MainWindow"))

        #*-------------------------Menu Options------------------------------------------------------------------*#

        self.menuFile.setTitle(insert("graphWindow", "Window"))
        self.menuOpen_Window.setTitle(insert("graphWindow", "Open Window"))
        self.menuSubwindow_Layout_2.setTitle(insert("graphWindow", "Subwindow Layout"))
        self.menuMenu.setTitle(insert("graphWindow", "Menu"))
        self.actionEvent_Configuration.setText(insert("graphWindow", "Event  Configuration"))
        self.actionEnforcement_Action_Report.setText(insert("graphWindow", "Enforcement Action Report"))
        self.actionManage_Graph.setText(insert("graphWindow", "Manage Graph"))
        self.actionTile.setText(insert("graphWindow", "Tile"))
        self.actionCascade.setText(insert("graphWindow", "Cascade"))

        #*-------------------------Vector selection Options------------------------------------------------------------------*#

        self.groupBoxVectorSelection.setTitle(insert("graphWindow", "Vector Selection"))
        self.labelVector.setText(insert("graphWindow", "Vector:"))
        self.comboBoxVector.setItemText(0, insert("graphWindow", "Selec A Vector"))
        self.comboBoxVector.setItemText(1, insert("graphWindow", "Vector A"))
        self.comboBoxVector.setItemText(2, insert("graphWindow", "Vector B"))
        self.comboBoxVector.setItemText(3, insert("graphWindow", "Vector C"))
        self.labelVectorDesc.setText(insert("graphWindow", "Vector Description"))

        #*-------------------------Graph Subwindow------------------------------------------------------------------*#
        self.actionGraphical_View.setText(insert("graphWindow", "Graphical View"))

        #Interval data
        self.IntervalLabel.setText(insert("MainWindow", "Interval:"))
        self.Interval.setItemText(0, insert("MainWindow", "Select an Interval"))
        self.Interval.setItemText(1, insert("MainWindow", "Seconds"))
        self.Interval.setItemText(2, insert("MainWindow", "Minutes"))
        self.Interval.setItemText(3, insert("MainWindow", "Hours"))

        #Timeline orientation data
        self.TimelineOrientationLabel.setText(insert("MainWindow", "Timeline Orientation:"))
        self.TimelineOrientation.setItemText(0, insert("MainWindow", "Select Orienatation"))
        self.TimelineOrientation.setItemText(1, insert("MainWindow", "Horizontal"))
        self.TimelineOrientation.setItemText(2, insert("MainWindow", "Vertical"))

        #*-------------------------Tabular View Subwindow------------------------------------------------------------------*#
        
        self.actionTabular_View.setText(insert("graphWindow", "Tabular View"))
        self.subwindow_Table.setWindowTitle(insert("graphWindow", "Tabular View"))

        #table headers
        self.tableWidgetNodes.setSortingEnabled(True)
        item = self.tableWidgetNodes.verticalHeaderItem(0)
        item.setText(insert("graphWindow", "Property Visibility"))
        item = self.tableWidgetNodes.horizontalHeaderItem(0)
        item.setText(insert("graphWindow", "Node Visibility"))
        item = self.tableWidgetNodes.horizontalHeaderItem(1)
        item.setText(insert("graphWindow", "Node Id"))
        item = self.tableWidgetNodes.horizontalHeaderItem(2)
        item.setText(insert("graphWindow", "Node Name"))
        item = self.tableWidgetNodes.horizontalHeaderItem(3)
        item.setText(insert("graphWindow", "Node Timestamp"))
        item = self.tableWidgetNodes.horizontalHeaderItem(4)
        item.setText(insert("graphWindow", "Node Description"))
        item = self.tableWidgetNodes.horizontalHeaderItem(5)
        item.setText(insert("graphWindow", "Log Entry Reference"))
        item = self.tableWidgetNodes.horizontalHeaderItem(6)
        item.setText(insert("graphWindow", "Log Creator"))
        item = self.tableWidgetNodes.horizontalHeaderItem(7)
        item.setText(insert("graphWindow", "Icon Type"))
        item = self.tableWidgetNodes.horizontalHeaderItem(8)
        item.setText(insert("graphWindow", "Source"))
        __sortingEnabled = self.tableWidgetNodes.isSortingEnabled()
        self.tableWidgetNodes.setSortingEnabled(False)

        #items in table
        item = self.tableWidgetNodes.item(1, 1)
        item.setText(insert("graphWindow", "0-001"))
        item = self.tableWidgetNodes.item(1, 2)
        item.setText(insert("graphWindow", "Packet Sniffing"))
        item = self.tableWidgetNodes.item(1, 3)
        item.setText(insert("graphWindow", "09:32:45"))
        item = self.tableWidgetNodes.item(1, 4)
        item.setText(insert("graphWindow", "Blue team starts their reconnaissance by inte rcepting packets"))
        item = self.tableWidgetNodes.item(1, 5)
        item.setText(insert("graphWindow", "00-00003"))
        item = self.tableWidgetNodes.item(1, 6)
        item.setText(insert("graphWindow", "Blue"))
        item = self.tableWidgetNodes.item(1, 7)
        item.setText(insert("graphWindow", "Sword"))
        item = self.tableWidgetNodes.item(1, 8)
        item.setText(insert("graphWindow", "C:\\Users\\User\\PycharmProjects\\untitled"))
        item = self.tableWidgetNodes.item(2, 1)
        item.setText(insert("graphWindow", "0-002"))
        item = self.tableWidgetNodes.item(2, 6)
        item.setText(insert("graphWindow", "Red"))
        item = self.tableWidgetNodes.item(2, 7)
        item.setText(insert("graphWindow", "Shield"))
        item = self.tableWidgetNodes.item(2, 8)
        item.setText(insert("graphWindow", "C:\\Users\\User\\PycharmProjects\\untitled"))
        
        self.tableWidgetNodes.setSortingEnabled(__sortingEnabled)
        self.subwindow_Graph.setWindowTitle(insert("graphWindow", "Graphical View"))

        #*-------------------------Relationship Table Subwindow------------------------------------------------------------------*#

        self.actionRelationship_Table.setText(insert("graphWindow", "Relationship Table"))

        #add relationship labels
        self.subwindow_Relationship.setWindowTitle(insert("graphWindow", "Relationship Table"))

        self.pushButtonAddRelationship.setText(insert("graphWindow", "Add Relationship"))
        self.pushButtonAddRelationship.clicked.connect(lambda: self.addTableData(self.tableWidgetRelationships, self.lineEditRelationship.text(), self.lineEditParent.text(), self.lineEditChild.text()))
        self.pushButtonAddRelationship.clicked.connect(lambda: self.clearData(self.tableWidgetRelationships, self.lineEditRelationship, self.lineEditParent, self.lineEditChild))

        self.pushButtonDeleteRelationship.setText(insert("graphWindow", "Delete Relationship"))
        self.pushButtonDeleteRelationship.clicked.connect(lambda: self.removeTableData(self.tableWidgetRelationships))

        self.labelRelationship.setText(insert("graphWindow", "Relationship Label:"))
        self.labelParent.setText(insert("graphWindow", "Parent Node:"))
        self.labelChild.setText(insert("graphWindow", "Child Node:"))

        self.tableWidgetRelationships.setSortingEnabled(True)
        item = self.tableWidgetRelationships.verticalHeaderItem(0)
        item.setText(insert("graphWindow", "1"))
        item = self.tableWidgetRelationships.verticalHeaderItem(1)
        item.setText(insert("graphWindow", "2"))
        item = self.tableWidgetRelationships.verticalHeaderItem(2)
        item.setText(insert("graphWindow", "3"))
        item = self.tableWidgetRelationships.verticalHeaderItem(3)
        item.setText(insert("graphWindow", "4"))
        
        item = self.tableWidgetRelationships.horizontalHeaderItem(0)
        item.setText(insert("graphWindow", "Relationship ID"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(1)
        item.setText(insert("graphWindow", "Label"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(2)
        item.setText(insert("graphWindow", "Parent"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(3)
        item.setText(insert("graphWindow", "Child"))
        __sortingEnabled = self.tableWidgetRelationships.isSortingEnabled()
        self.tableWidgetRelationships.setSortingEnabled(False)

        #test data
        item = self.tableWidgetRelationships.item(0, 0)
        item.setText(insert("graphWindow", "00-00001"))
        item = self.tableWidgetRelationships.item(0, 1)
        item.setText(insert("graphWindow", "intercepting"))
        item = self.tableWidgetRelationships.item(0, 2)
        item.setText(insert("graphWindow", "00-00000"))
        item = self.tableWidgetRelationships.item(0, 3)
        item.setText(insert("graphWindow", "00-00002"))
        item = self.tableWidgetRelationships.item(1, 0)
        item.setText(insert("graphWindow", "00-00002"))
        item = self.tableWidgetRelationships.item(1, 1)
        item.setText(insert("graphWindow", "scanning"))
        item = self.tableWidgetRelationships.item(1, 2)
        item.setText(insert("graphWindow", "00-00001"))
        item = self.tableWidgetRelationships.item(1, 3)
        item.setText(insert("graphWindow", "00-00005"))
        item = self.tableWidgetRelationships.item(2, 0)
        item.setText(insert("graphWindow", "00-00003"))
        item = self.tableWidgetRelationships.item(2, 1)
        item.setText(insert("graphWindow", "ping"))
        item = self.tableWidgetRelationships.item(2, 2)
        item.setText(insert("graphWindow", "00-00001"))
        item = self.tableWidgetRelationships.item(2, 3)
        item.setText(insert("graphWindow", "00-00004"))
        item = self.tableWidgetRelationships.item(3, 0)
        item.setText(insert("graphWindow", "00-00004"))
        item = self.tableWidgetRelationships.item(3, 1)
        item.setText(insert("graphWindow", "broadcasting"))
        item = self.tableWidgetRelationships.item(3, 2)
        item.setText(insert("graphWindow", "00-00003"))
        item = self.tableWidgetRelationships.item(3, 3)
        item.setText(insert("graphWindow", "00-00008"))
        self.tableWidgetRelationships.setSortingEnabled(__sortingEnabled)

        

    #adds data to given tree widget with two columns
    def addTableData(self, table, col1, col2, col3):
        
        table.insertRow(0)

        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        table.setItem(0, 0, item)
        
        table.setItem(0, 1, QtWidgets.QTableWidgetItem(col1))
        table.setItem(0, 2, QtWidgets.QTableWidgetItem(col2))
        table.setItem(0, 3, QtWidgets.QTableWidgetItem(col3))

    #clears data from line/text edits after adding to tree widget
    def clearData(self, table, col1, col2, col3):
            col1.clear()
            col2.clear()
            col3.clear()
    
    #removes selected items from given tree widget
    def removeTableData(self, table):
        selectedItems = table.selectionModel().selectedRows() 
        for item in sorted(selectedItems):
                table.removeRow(item.row())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphWindow = QtWidgets.QMainWindow()
    ui = GraphWindow()
    ui.setupUi(graphWindow)
    graphWindow.show()
    sys.exit(app.exec_())
