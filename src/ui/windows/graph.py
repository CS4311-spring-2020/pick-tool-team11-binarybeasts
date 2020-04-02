from PyQt5 import QtCore, QtGui, QtWidgets
from ui.common import menu_bar

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
        graphWindow.resize(998, 600)

        self.centralwidget = QtWidgets.QWidget(graphWindow)
        self.centralwidget.setObjectName("centralwidget")

        # sets this to vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        graphWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(graphWindow)


        #*-------------------------Menu bar creation & properties----------------------------------------------------*#
        self.menubar = menu_bar.PickMenuBar(graphWindow, omit=menu_bar.GRAPH)
        graphWindow.setMenuBar(self.menubar)

        #*-------------------------Manage Graph Tab------------------------------------------------------------------*#

        # Manage Graph Tab
        self.ManageGraphTab = QtWidgets.QWidget()
        self.ManageGraphTab.setObjectName("ManageGraphTab")
        self.gridLayout = QtWidgets.QGridLayout(self.ManageGraphTab)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget.addTab(self.ManageGraphTab, "")

        #horizontal layout for vector selection and description
        self.VectorSelectionHorizontalLayout = QtWidgets.QHBoxLayout()
        self.VectorSelectionHorizontalLayout.setObjectName("VectorSelectionHorizontalLayout")
        self.gridLayout.addLayout(self.VectorSelectionHorizontalLayout, 0,0,1,1)

        #Vector label and combo box
        self.VectorLabel = QtWidgets.QLabel(self.ManageGraphTab)
        self.VectorLabel.setObjectName("VectorLabel")
        self.VectorSelectionHorizontalLayout.addWidget(self.VectorLabel)
        self.Vector = QtWidgets.QComboBox(self.ManageGraphTab)
        self.Vector.setObjectName("Vector")
        self.Vector.addItem("") # Select Vector
        self.Vector.addItem("") # Vector A
        self.Vector.addItem("") # Vector B
        self.Vector.addItem("") # Vector C
        self.VectorSelectionHorizontalLayout.addWidget(self.Vector)

        #Vector Description label and line edit
        self.vectorDescLabel = QtWidgets.QLabel(self.ManageGraphTab)
        self.vectorDescLabel.setObjectName("vectorDescLabel")
        self.VectorSelectionHorizontalLayout.addWidget(self.vectorDescLabel)
        self.vectorDesc = QtWidgets.QLineEdit(self.ManageGraphTab)
        self.vectorDesc.setObjectName("vectorDesc")
        self.VectorSelectionHorizontalLayout.addWidget(self.vectorDesc)

        #graph view groupbox
        self.graphViewGroupBox2 = QtWidgets.QGroupBox(self.ManageGraphTab)
        self.graphViewGroupBox2.setObjectName("graphViewGroupBox2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graphViewGroupBox2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.graphViewGroupBox2, 1, 0, 1, 1)


        # Interval Label and combo box
        self.IntervalLabel = QtWidgets.QLabel(self.graphViewGroupBox2)
        self.IntervalLabel.setObjectName("IntervalLabel")
        self.gridLayout_3.addWidget(self.IntervalLabel, 2, 4, 1, 1, QtCore.Qt.AlignRight)
        self.Interval = QtWidgets.QComboBox(self.graphViewGroupBox2)
        self.Interval.setObjectName("Interval")
        self.Interval.addItem("") # Select Interval
        self.Interval.addItem("") # Seconds
        self.Interval.addItem("") # Minutes 
        self.Interval.addItem("") # Hours
        self.gridLayout_3.addWidget(self.Interval, 2, 5, 1, 1)

        #Timeline orientation label and combo box
        self.TimelineOrientationLabel = QtWidgets.QLabel(self.graphViewGroupBox2)
        self.TimelineOrientationLabel.setObjectName("TimelineOrientationLabel")
        self.gridLayout_3.addWidget(self.TimelineOrientationLabel, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.TimelineOrientation = QtWidgets.QComboBox(self.graphViewGroupBox2)
        self.TimelineOrientation.setObjectName("TimelineOrientation")
        self.TimelineOrientation.addItem("") # Selection Orientation
        self.TimelineOrientation.addItem("") # Horizontal
        self.TimelineOrientation.addItem("") # Vertical
        self.gridLayout_3.addWidget(self.TimelineOrientation, 2, 3, 1, 1)


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

        # Define sone graph
        n1 = qgv.addNode(qgv.engine.graph, "Node1", label="N1")
        n2 = qgv.addNode(qgv.engine.graph, "Node2", label="N2")
        n3 = qgv.addNode(qgv.engine.graph, "Node3", label="N3")
        n4 = qgv.addNode(qgv.engine.graph, "Node4", label="N4")
        n5 = qgv.addNode(qgv.engine.graph, "Node5", label="N5")
        n6 = qgv.addNode(qgv.engine.graph, "Node6", label="N6")

        sub = qgv.addSubgraph(qgv.engine.graph, "sub graph", qgv.engine.graph.graph_type, label="Subgraph")
        n7 = qgv.addNode(sub, "Node7", label="N7")
        n8 = qgv.addNode(sub, "Node8", label="N8")

        # Adding nodes with an image as its shape
        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\icon\dbicon.png"
        n9 = qgv.addNode(qgv.engine.graph, "Node9", label="N9", shape=icon_path)

        qgv.addEdge(n1, n2, {})
        qgv.addEdge(n3, n2, {})
        qgv.addEdge(n2, n4, {"width":2})
        qgv.addEdge(n4, n5, {"width":4})
        qgv.addEdge(n4, n6, {"width":5,"color":"red"})
        qgv.addEdge(n3, n6, {"width":2})
        qgv.addEdge(n6, n9, {"width":5,"color":"red"})


        # Build the graph (the layout engine organizes where the nodes and connections are)
        qgv.build()
        # Save it to a file to be loaded by Graphviz if needed
        qgv.save("test.gv")
        

        # Create a widget to handle the QGraphViz object
        wi=QWidget()
        wi.setLayout(QVBoxLayout())
        self.gridLayout_3.addWidget(wi, 3, 0, 1, 8)
        # Add the QGraphViz object to the layout
        wi.layout().addWidget(qgv)

        # Add a horizontal layout (a pannel to select what to do)
        hpanel=QHBoxLayout()
        wi.layout().addLayout(hpanel)


        # Add few buttons to the panel
        def manipulate():
            qgv.manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode

        def save():
            fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
            if(fname[0]!=""):
                qgv.saveAsJson(fname[0])

            #fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.gv")
            #if(fname[0]!=""):
            #    qgv.save(fname[0])
            
        def new():
            qgv.engine.graph = Graph("MainGraph")
            qgv.build()
        qgv.repaint()

        def load():
            fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
            if(fname[0]!=""):
                qgv.loadAJson(fname[0])

            #fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.gv")
            #if(fname[0]!=""):
            #    qgv.load_file(fname[0])

        def add_node():
            dlg = QDialog()
            dlg.ok=False
            dlg.node_name=""
            dlg.node_label=""
            dlg.node_type="None"
            # Layouts
            main_layout = QVBoxLayout()
            l = QFormLayout()
            buttons_layout = QHBoxLayout()

            main_layout.addLayout(l)
            main_layout.addLayout(buttons_layout)
            dlg.setLayout(main_layout)

            leNodeName = QLineEdit()
            leNodeLabel = QLineEdit()
            cbxNodeType = QComboBox()
            leImagePath = QLineEdit()

            pbOK = QPushButton()
            pbCancel = QPushButton()

            cbxNodeType.addItems(["None","circle","box"])
            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
            l.setWidget(0, QFormLayout.FieldRole, leNodeName)
            l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
            l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
            l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
            l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
            l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
            l.setWidget(3, QFormLayout.FieldRole, leImagePath)

            def ok():
                dlg.OK=True
                dlg.node_name = leNodeName.text()
                dlg.node_label = leNodeLabel.text()
                if(leImagePath.text()): 
                    dlg.node_type = leImagePath.text()
                else: 
                    dlg.node_type = cbxNodeType.currentText()
                dlg.close()

            def cancel():
                dlg.OK=False
                dlg.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            dlg.exec_()

            #node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
            if dlg.OK and dlg.node_name != '':
                    qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
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

        def add_subgraph():
            dlg = QDialog()
            dlg.ok=False
            dlg.subgraph_name=""
            dlg.subgraph_label=""
            dlg.subgraph_type="None"
            # Layouts
            main_layout = QVBoxLayout()
            l = QFormLayout()
            buttons_layout = QHBoxLayout()

            main_layout.addLayout(l)
            main_layout.addLayout(buttons_layout)
            dlg.setLayout(main_layout)

            leSubgraphName = QLineEdit()
            leSubgraphLabel = QLineEdit()

            pbOK = QPushButton()
            pbCancel = QPushButton()

            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            l.setWidget(0, QFormLayout.LabelRole, QLabel("Subgraph Name"))
            l.setWidget(0, QFormLayout.FieldRole, leSubgraphName)
            l.setWidget(1, QFormLayout.LabelRole, QLabel("Subgraph Label"))
            l.setWidget(1, QFormLayout.FieldRole, leSubgraphLabel)
    
            def ok():
                dlg.OK=True
                dlg.subgraph_name = leSubgraphName.text()
                dlg.subgraph_label = leSubgraphLabel.text()
                dlg.close()
        
            def cancel():
                dlg.OK=False
                dlg.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            dlg.exec_()

            if dlg.OK and dlg.subgraph_name != '':
                    qgv.addSubgraph(qgv.engine.graph, dlg.subgraph_name, subgraph_type= GraphType.SimpleGraph, label=dlg.subgraph_label)
                    qgv.build()

        def rem_subgraph():
            qgv.manipulation_mode=QGraphVizManipulationMode.Subgraph_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemSubGraph.setChecked(True)

        # Add buttons                
        btnNew = QPushButton("New")    
        btnNew.clicked.connect(new)
        btnOpen = QPushButton("Open")    
        btnOpen.clicked.connect(load)

        btnSave = QPushButton("Save")    
        btnSave.clicked.connect(save)

        hpanel.addWidget(btnNew)    
        hpanel.addWidget(btnOpen)
        hpanel.addWidget(btnSave)

        buttons_list=[]
        btnManip = QPushButton("Manipulate")    
        btnManip.setCheckable(True)
        btnManip.setChecked(True)
        btnManip.clicked.connect(manipulate)
        hpanel.addWidget(btnManip)
        buttons_list.append(btnManip)

        btnAddNode = QPushButton("Add Node")    
        btnAddNode.clicked.connect(add_node)
        hpanel.addWidget(btnAddNode)
        buttons_list.append(btnManip)

        btnRemNode = QPushButton("Rem Node")    
        btnRemNode.setCheckable(True)
        btnRemNode.clicked.connect(rem_node)
        hpanel.addWidget(btnRemNode)
        buttons_list.append(btnRemNode)

        btnAddEdge = QPushButton("Add Relationship")    
        btnAddEdge.setCheckable(True)
        btnAddEdge.clicked.connect(add_edge)
        hpanel.addWidget(btnAddEdge)
        buttons_list.append(btnAddEdge)

        btnRemEdge = QPushButton("Rem Relationship")    
        btnRemEdge.setCheckable(True)
        btnRemEdge.clicked.connect(rem_edge)
        hpanel.addWidget(btnRemEdge)
        buttons_list.append(btnRemEdge)

        btnAddSubGraph = QPushButton("Add Subgraph")    
        btnAddSubGraph.clicked.connect(add_subgraph)
        hpanel.addWidget(btnAddSubGraph)

        btnRemSubGraph = QPushButton("Rem Subgraph")    
        btnRemSubGraph.setCheckable(True)
        btnRemSubGraph.clicked.connect(rem_subgraph)
        hpanel.addWidget(btnRemSubGraph)
        buttons_list.append(btnRemSubGraph)

        #*-------------------------Table View Tab--------------------------------------------------------------------*#

        # Table View tab
        self.TableViewTab = QtWidgets.QWidget()
        self.TableViewTab.setObjectName("TableViewTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.TableViewTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget.addTab(self.TableViewTab, "")

        #Node Table Widget and all its properties
        self.nodeTableWidget = QtWidgets.QTableWidget(self.TableViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeTableWidget.sizePolicy().hasHeightForWidth())
        self.nodeTableWidget.setSizePolicy(sizePolicy)
        self.nodeTableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nodeTableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nodeTableWidget.setAlternatingRowColors(True)
        self.nodeTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.nodeTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.nodeTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.nodeTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.nodeTableWidget.setShowGrid(False)
        self.nodeTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.nodeTableWidget.setCornerButtonEnabled(False)
        self.nodeTableWidget.setObjectName("nodeTableWidget")

        self.nodeTableWidget.setColumnCount(9)
        self.nodeTableWidget.setRowCount(2)

        #vertical header items
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setVerticalHeaderItem(1, item)
        #horizontal header items
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(8, item)

        #visibility property checkbox for each column
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.nodeTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.nodeTableWidget.setItem(0, 8, item)

        #item 1
        item = QtWidgets.QTableWidgetItem()
        self.nodeTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.nodeTableWidget.setItem(1, 8, item)
        
        
        #horizontal header properties
        self.nodeTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.nodeTableWidget.horizontalHeader().setDefaultSectionSize(142)
        self.nodeTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.nodeTableWidget.horizontalHeader().setStretchLastSection(True)
        #vertical header properties
        self.nodeTableWidget.verticalHeader().setVisible(True)
        self.nodeTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.nodeTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.nodeTableWidget.verticalHeader().setStretchLastSection(False)
        
        self.gridLayout_6.addWidget(self.nodeTableWidget, 0, 0, 1, 1)

        #*-------------------------Relationship Configuration Tab----------------------------------------------------*#

        #Relationship configuration tab
        self.RelationshipConfigTab = QtWidgets.QWidget()
        self.RelationshipConfigTab.setObjectName("RelationshipConfigTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.RelationshipConfigTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget.addTab(self.RelationshipConfigTab, "")


        #relationship label and line edit
        self.RelationshipLabel = QtWidgets.QLabel(self.RelationshipConfigTab)
        self.RelationshipLabel.setObjectName("RelationshipLabel")
        self.gridLayout_4.addWidget(self.RelationshipLabel, 1, 0, 1, 1)
        self.Relationship = QtWidgets.QLineEdit(self.RelationshipConfigTab)
        self.Relationship.setObjectName("Relationship")
        self.gridLayout_4.addWidget(self.Relationship, 1, 1, 1, 5)

        #Parent node label and line edit
        self.ParentNodeLabel = QtWidgets.QLabel(self.RelationshipConfigTab)
        self.ParentNodeLabel.setObjectName("ParentNodeLabel")
        self.gridLayout_4.addWidget(self.ParentNodeLabel, 2, 0, 1, 1)
        self.ParentNode = QtWidgets.QLineEdit(self.RelationshipConfigTab)
        self.ParentNode.setObjectName("ParentNode")
        self.gridLayout_4.addWidget(self.ParentNode, 2, 1, 1, 5)

        #Child Node label and line edit
        self.ChildNodeLabel = QtWidgets.QLabel(self.RelationshipConfigTab)
        self.ChildNodeLabel.setObjectName("ChildNodeLabel")
        self.gridLayout_4.addWidget(self.ChildNodeLabel, 3, 0, 1, 1)
        self.ChildNode = QtWidgets.QLineEdit(self.RelationshipConfigTab)
        self.ChildNode.setObjectName("ChildNode")
        self.gridLayout_4.addWidget(self.ChildNode, 3, 1, 1, 5)

        #add relationship button
        self.AddRelationshipBttn_2 = QtWidgets.QPushButton(self.RelationshipConfigTab)
        self.AddRelationshipBttn_2.setObjectName("AddRelationshipBttn_2")
        self.gridLayout_4.addWidget(self.AddRelationshipBttn_2, 4, 5, 1, 1)

        #delete relationship button 
        self.DeleteRelationshipBttn = QtWidgets.QPushButton(self.RelationshipConfigTab)
        self.DeleteRelationshipBttn.setObjectName("DeleteRelationshipBttn")
        self.gridLayout_4.addWidget(self.DeleteRelationshipBttn, 6, 5, 1, 1)

        

        #Relationship Table widget & properties
        self.RelationshipTableWidget = QtWidgets.QTableWidget(self.RelationshipConfigTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RelationshipTableWidget.sizePolicy().hasHeightForWidth())
        self.RelationshipTableWidget.setSizePolicy(sizePolicy)
        self.RelationshipTableWidget.setAlternatingRowColors(True)
        self.RelationshipTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.RelationshipTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.RelationshipTableWidget.setShowGrid(False)
        self.RelationshipTableWidget.setObjectName("RelationshipTableWidget")
        self.RelationshipTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.RelationshipTableWidget.setColumnCount(5)
        self.RelationshipTableWidget.setRowCount(0)

        #vertical header items
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setVerticalHeaderItem(0, item)
        

        #horizontal header items
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RelationshipTableWidget.setHorizontalHeaderItem(4, item)

        
        self.RelationshipTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.RelationshipTableWidget, 5, 0, 1, 6)

        self.addData(graphWindow)

        # fills out tables and stuff with information
    def addData(self, graphWindow):
        insert = QtCore.QCoreApplication.translate
        graphWindow.setWindowTitle(insert("graphWindow", "graphWindow"))
        
        #*-------------------------Manage Graph Tab------------------------------------------------------------------*#

        #vector selection 
        self.VectorLabel.setText(insert("graphWindow", "Vector:"))
        self.Vector.setItemText(0, insert("graphWindow", "Select a vector"))
        self.Vector.setItemText(1, insert("graphWindow", "Vector A"))
        self.Vector.setItemText(2, insert("graphWindow", "Vector B"))
        self.Vector.setItemText(3, insert("graphWindow", "Vector C"))
        self.vectorDescLabel.setText(insert("graphWindow", "Vector Description:"))


        #Interval data
        self.IntervalLabel.setText(insert("graphWindow", "Interval:"))
        self.Interval.setItemText(0, insert("graphWindow", "Select an Interval"))
        self.Interval.setItemText(1, insert("graphWindow", "Seconds"))
        self.Interval.setItemText(2, insert("graphWindow", "Minutes"))
        self.Interval.setItemText(3, insert("graphWindow", "Hours"))

        #Timeline orientation data
        self.TimelineOrientationLabel.setText(insert("graphWindow", "Timeline Orientation:"))
        self.TimelineOrientation.setItemText(0, insert("graphWindow", "Select Orienatation"))
        self.TimelineOrientation.setItemText(1, insert("graphWindow", "Horizontal"))
        self.TimelineOrientation.setItemText(2, insert("graphWindow", "Vertical"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ManageGraphTab), insert("graphWindow", "Manage Graph"))


        #*-------------------------Table View Tab--------------------------------------------------------------------*#

        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TableViewTab), insert("graphWindow", "Table View"))


        self.nodeTableWidget.setSortingEnabled(True)

        #vertical headers
        item = self.nodeTableWidget.verticalHeaderItem(0)
        item.setText(insert("graphWindow", "Visibility"))

        #horizontal headers
        item = self.nodeTableWidget.horizontalHeaderItem(0)
        item.setText(insert("graphWindow", "Node Id"))
        item = self.nodeTableWidget.horizontalHeaderItem(1)
        item.setText(insert("graphWindow", "Node Name"))
        item = self.nodeTableWidget.horizontalHeaderItem(2)
        item.setText(insert("graphWindow", "Node Timestamp"))
        item = self.nodeTableWidget.horizontalHeaderItem(3)
        item.setText(insert("graphWindow", "Node Description"))
        item = self.nodeTableWidget.horizontalHeaderItem(4)
        item.setText(insert("graphWindow", "Log Entry Reference"))
        item = self.nodeTableWidget.horizontalHeaderItem(5)
        item.setText(insert("graphWindow", "Log Creator"))
        item = self.nodeTableWidget.horizontalHeaderItem(6)
        item.setText(insert("graphWindow", "Icon Type"))
        item = self.nodeTableWidget.horizontalHeaderItem(7)
        item.setText(insert("graphWindow", "Source"))
        item = self.nodeTableWidget.horizontalHeaderItem(8)
        item.setText(insert("graphWindow", "Node Visibility"))
        __sortingEnabled = self.nodeTableWidget.isSortingEnabled()
        self.nodeTableWidget.setSortingEnabled(False)

        #items
        item = self.nodeTableWidget.item(1, 0)
        item.setText(insert("graphWindow", "0-001"))
        
        self.nodeTableWidget.setSortingEnabled(__sortingEnabled)
        

        #*-------------------------Relationship Configuration Tab----------------------------------------------------*#


        #Relationship configuration
        self.AddRelationshipBttn_2.setText(insert("graphWindow", "Add Relationship"))
        self.AddRelationshipBttn_2.clicked.connect(lambda: self.addTableData(self.RelationshipTableWidget, self.Relationship.text(), self.ParentNode.text(), self.ChildNode.text()))
        self.AddRelationshipBttn_2.clicked.connect(lambda: self.clearData(self.RelationshipTableWidget, self.Relationship, self.ParentNode, self.ChildNode))

        self.ChildNodeLabel.setText(insert("graphWindow", "Child Node:"))
        self.ParentNodeLabel.setText(insert("graphWindow", "Parent Node:"))
        self.RelationshipLabel.setText(insert("graphWindow", "Raltionship Label:"))

        self.DeleteRelationshipBttn.setText(insert("graphWindow", "Delete Relationship"))
        self.DeleteRelationshipBttn.clicked.connect(lambda: self.removeTableData(self.RelationshipTableWidget))

        self.RelationshipTableWidget.setSortingEnabled(True)
        item = self.RelationshipTableWidget.horizontalHeaderItem(1)
        item.setText(insert("graphWindow", "Relationship ID"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(2)
        item.setText(insert("graphWindow", "Label"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(3)
        item.setText(insert("graphWindow", "Parent"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(4)
        item.setText(insert("graphWindow", "Child"))
        __sortingEnabled = self.RelationshipTableWidget.isSortingEnabled()
        self.RelationshipTableWidget.setSortingEnabled(False)
        self.RelationshipTableWidget.setSortingEnabled(__sortingEnabled)
        

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RelationshipConfigTab), insert("graphWindow", "Relationship Configuration"))

    #adds data to given tree widget with two columns
    def addTableData(self, table, col1, col2, col3):
        
        table.insertRow(0)

        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(0, 0, item)

        table.setItem(0, 1, QtWidgets.QTableWidgetItem("0-"))
        table.setItem(0, 2, QtWidgets.QTableWidgetItem(col1))
        table.setItem(0, 3, QtWidgets.QTableWidgetItem(col2))
        table.setItem(0, 4, QtWidgets.QTableWidgetItem(col3))

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
    ui = graphWindow()
    ui.setupUi(graphWindow)
    graphWindow.show()
    sys.exit(app.exec_())
