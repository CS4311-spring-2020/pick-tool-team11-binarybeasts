from PyQt5 import QtCore, QtGui, QtWidgets

import Common


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(1121, 873)

        # -----------------------------layout for main window----------------------------------------------------------------------------------------#
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # -----------------------------holds all the widgets for vector selection--------------------------------------------------------------------#
        self.groupBoxVectorSelection = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxVectorSelection.sizePolicy().hasHeightForWidth())
        self.groupBoxVectorSelection.setSizePolicy(sizePolicy)
        self.groupBoxVectorSelection.setObjectName("groupBoxVectorSelection")
        self.formLayoutVector = QtWidgets.QHBoxLayout(self.groupBoxVectorSelection)
        self.formLayoutVector.setObjectName("formLayoutVector")
        self.labelVector = QtWidgets.QLabel(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVector.sizePolicy().hasHeightForWidth())
        self.labelVector.setSizePolicy(sizePolicy)
        self.labelVector.setObjectName("labelVector")
        self.formLayoutVector.addWidget(self.labelVector)
        self.comboBoxVector = QtWidgets.QComboBox(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxVector.sizePolicy().hasHeightForWidth())
        self.comboBoxVector.setSizePolicy(sizePolicy)
        self.comboBoxVector.setMinimumSize(QtCore.QSize(116, 0))
        self.comboBoxVector.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboBoxVector.setObjectName("comboBoxVector")
        self.comboBoxVector.addItem("")
        self.comboBoxVector.addItem("")
        self.comboBoxVector.addItem("")
        self.comboBoxVector.addItem("")
        self.formLayoutVector.addWidget(self.comboBoxVector)
        self.labelVectorDesc = QtWidgets.QLabel(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVectorDesc.sizePolicy().hasHeightForWidth())
        self.labelVectorDesc.setSizePolicy(sizePolicy)
        self.labelVectorDesc.setObjectName("labelVectorDesc")
        self.formLayoutVector.addWidget(self.labelVectorDesc)
        self.lineEditVectorDesc = QtWidgets.QLineEdit(self.groupBoxVectorSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVectorDesc.sizePolicy().hasHeightForWidth())
        self.lineEditVectorDesc.setSizePolicy(sizePolicy)
        self.lineEditVectorDesc.setObjectName("lineEditVectorDesc")
        self.formLayoutVector.addWidget(self.lineEditVectorDesc)
        self.verticalLayout.addWidget(self.groupBoxVectorSelection)

        # -----------------------------holds all the widgets for graphical view----------------------------------------------------------------------#
        self.groupBoxGraphView = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxGraphView.sizePolicy().hasHeightForWidth())
        self.groupBoxGraphView.setSizePolicy(sizePolicy)
        self.groupBoxGraphView.setObjectName("groupBoxGraphView")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxGraphView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxGraphBuilder = QtWidgets.QGroupBox(self.groupBoxGraphView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxGraphBuilder.sizePolicy().hasHeightForWidth())
        self.groupBoxGraphBuilder.setSizePolicy(sizePolicy)
        self.groupBoxGraphBuilder.setObjectName("groupBoxGraphBuilder")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxGraphBuilder)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonZoomIn = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonZoomIn.setObjectName("pushButtonZoomIn")
        self.gridLayout_2.addWidget(self.pushButtonZoomIn, 6, 0, 1, 1)
        self.pushButtonExport = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.gridLayout_2.addWidget(self.pushButtonExport, 0, 1, 1, 1)
        self.comboBoxFormat = QtWidgets.QComboBox(self.groupBoxGraphBuilder)
        self.comboBoxFormat.setObjectName("comboBoxFormat")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxFormat, 0, 0, 1, 1)
        self.pushButtonZoomOut = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonZoomOut.setObjectName("pushButtonZoomOut")
        self.gridLayout_2.addWidget(self.pushButtonZoomOut, 6, 1, 1, 1)
        self.pushButtonAddNode = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonAddNode.setObjectName("pushButtonAddNode")
        self.gridLayout_2.addWidget(self.pushButtonAddNode, 1, 0, 1, 1)
        self.labelTimelineOrientation = QtWidgets.QLabel(self.groupBoxGraphBuilder)
        self.labelTimelineOrientation.setObjectName("labelTimelineOrientation")
        self.gridLayout_2.addWidget(self.labelTimelineOrientation, 7, 0, 1, 1)
        self.comboBoxIntervalUnits = QtWidgets.QComboBox(self.groupBoxGraphBuilder)
        self.comboBoxIntervalUnits.setObjectName("comboBoxIntervalUnits")
        self.comboBoxIntervalUnits.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxIntervalUnits, 8, 1, 1, 1)
        self.labelInterval = QtWidgets.QLabel(self.groupBoxGraphBuilder)
        self.labelInterval.setObjectName("labelInterval")
        self.gridLayout_2.addWidget(self.labelInterval, 8, 0, 1, 1)
        self.comboBoxOrientation = QtWidgets.QComboBox(self.groupBoxGraphBuilder)
        self.comboBoxOrientation.setObjectName("comboBoxOrientation")
        self.comboBoxOrientation.addItem("")
        self.comboBoxOrientation.addItem("")
        self.comboBoxOrientation.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxOrientation, 7, 1, 1, 1)
        self.pushButtonDeleteNode = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonDeleteNode.setObjectName("pushButtonDeleteNode")
        self.gridLayout_2.addWidget(self.pushButtonDeleteNode, 2, 0, 1, 1)
        self.pushButtonEditNode = QtWidgets.QPushButton(self.groupBoxGraphBuilder)
        self.pushButtonEditNode.setObjectName("pushButtonEditNode")
        self.gridLayout_2.addWidget(self.pushButtonEditNode, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBoxGraphBuilder)
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBoxGraphView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addWidget(self.groupBoxGraphView)

        # -----------------------------holds all the widgets for tabular view------------------------------------------------------------------------#
        self.groupBoxTabularView = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTabularView.setObjectName("groupBoxTabularView")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxTabularView)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBoxNode = QtWidgets.QGroupBox(self.groupBoxTabularView)
        self.groupBoxNode.setObjectName("groupBoxNode")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxNode)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidgetNodes = QtWidgets.QTableWidget(self.groupBoxNode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetNodes.sizePolicy().hasHeightForWidth())
        self.tableWidgetNodes.setSizePolicy(sizePolicy)
        self.tableWidgetNodes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidgetNodes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidgetNodes.setAlternatingRowColors(True)
        self.tableWidgetNodes.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidgetNodes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidgetNodes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetNodes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetNodes.setShowGrid(False)
        self.tableWidgetNodes.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetNodes.setCornerButtonEnabled(False)
        self.tableWidgetNodes.setObjectName("tableWidgetNodes")
        self.tableWidgetNodes.setColumnCount(9)
        self.tableWidgetNodes.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidgetNodes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidgetNodes.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(1, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(2, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(3, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(4, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetNodes.setItem(5, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNodes.setItem(8, 0, item)
        self.tableWidgetNodes.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetNodes.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidgetNodes.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetNodes.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetNodes.verticalHeader().setVisible(True)
        self.tableWidgetNodes.verticalHeader().setMinimumSectionSize(30)
        self.tableWidgetNodes.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetNodes.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_4.addWidget(self.tableWidgetNodes)
        self.horizontalLayout_2.addWidget(self.groupBoxNode)
        self.verticalLayout.addWidget(self.groupBoxTabularView)

        # -----------------------------docakable relationship window---------------------------------------------------------------------------------#
        self.dockWidgetRelationship = QtWidgets.QDockWidget(GraphWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetRelationship.sizePolicy().hasHeightForWidth())
        self.dockWidgetRelationship.setSizePolicy(sizePolicy)
        self.dockWidgetRelationship.setFloating(True)
        self.dockWidgetRelationship.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidgetRelationship.setObjectName("dockWidgetRelationship")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # -----------------------------holds all the widgets for the relationships configuration-----------------------------------------------------#
        self.groupBoxRelationships = QtWidgets.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRelationships.sizePolicy().hasHeightForWidth())
        self.groupBoxRelationships.setSizePolicy(sizePolicy)
        self.groupBoxRelationships.setObjectName("groupBoxRelationships")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxRelationships)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidgetRelationships = QtWidgets.QTableWidget(self.groupBoxRelationships)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetRelationships.sizePolicy().hasHeightForWidth())
        self.tableWidgetRelationships.setSizePolicy(sizePolicy)
        self.tableWidgetRelationships.setAlternatingRowColors(True)
        self.tableWidgetRelationships.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetRelationships.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetRelationships.setShowGrid(False)
        self.tableWidgetRelationships.setObjectName("tableWidgetRelationships")
        self.tableWidgetRelationships.setColumnCount(5)
        self.tableWidgetRelationships.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRelationships.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidgetRelationships.setItem(9, 0, item)
        self.tableWidgetRelationships.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidgetRelationships)
        self.frameRelationshipButtons = QtWidgets.QFrame(self.groupBoxRelationships)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameRelationshipButtons.sizePolicy().hasHeightForWidth())
        self.frameRelationshipButtons.setSizePolicy(sizePolicy)
        self.frameRelationshipButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRelationshipButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameRelationshipButtons.setLineWidth(0)
        self.frameRelationshipButtons.setObjectName("frameRelationshipButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameRelationshipButtons)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonDeleteRelationship = QtWidgets.QPushButton(self.frameRelationshipButtons)
        self.pushButtonDeleteRelationship.setObjectName("pushButtonDeleteRelationship")
        self.horizontalLayout_3.addWidget(self.pushButtonDeleteRelationship)
        self.pushButtonEditRelationship = QtWidgets.QPushButton(self.frameRelationshipButtons)
        self.pushButtonEditRelationship.setObjectName("pushButtonEditRelationship")
        self.horizontalLayout_3.addWidget(self.pushButtonEditRelationship)
        self.pushButtonAddRelationship = QtWidgets.QPushButton(self.frameRelationshipButtons)
        self.pushButtonAddRelationship.setObjectName("pushButtonAddRelationship")
        self.horizontalLayout_3.addWidget(self.pushButtonAddRelationship)
        self.verticalLayout_3.addWidget(self.frameRelationshipButtons)
        self.verticalLayout_2.addWidget(self.groupBoxRelationships)
        self.dockWidgetRelationship.setWidget(self.dockWidgetContents)
        GraphWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetRelationship)

        GraphWindow.setCentralWidget(self.centralwidget)

        self.menubar = Common.PickMenuBar(GraphWindow, omit=Common.GRAPH)
        GraphWindow.setMenuBar(self.menubar)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

        # -----------------------------fill in data--------------------------------------------------------------------------------------------------#

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Graph/Table View"))
        self.groupBoxVectorSelection.setTitle(_translate("GraphWindow", "Vector Selection"))
        self.labelVector.setText(_translate("GraphWindow", "Vector:"))
        self.comboBoxVector.setItemText(0, _translate("GraphWindow", "Selec A Vector"))
        self.comboBoxVector.setItemText(1, _translate("GraphWindow", "Vector A"))
        self.comboBoxVector.setItemText(2, _translate("GraphWindow", "Vector B"))
        self.comboBoxVector.setItemText(3, _translate("GraphWindow", "Vector C"))
        self.labelVectorDesc.setText(_translate("GraphWindow", "Vector Description"))
        self.groupBoxGraphView.setTitle(_translate("GraphWindow", "Graphical View"))
        self.groupBoxGraphBuilder.setTitle(_translate("GraphWindow", "Graph Builder"))
        self.pushButtonZoomIn.setText(_translate("GraphWindow", "Zoom In"))
        self.pushButtonExport.setText(_translate("GraphWindow", "Export"))
        self.comboBoxFormat.setItemText(0, _translate("GraphWindow", "Export As"))
        self.comboBoxFormat.setItemText(1, _translate("GraphWindow", "JPEG"))
        self.comboBoxFormat.setItemText(2, _translate("GraphWindow", "PNG"))
        self.pushButtonZoomOut.setText(_translate("GraphWindow", "Zoom Out"))
        self.pushButtonAddNode.setText(_translate("GraphWindow", "Add Node"))
        self.labelTimelineOrientation.setText(_translate("GraphWindow", "Timeline Orientation:"))
        self.comboBoxIntervalUnits.setItemText(0, _translate("GraphWindow", "Interval Units"))
        self.labelInterval.setText(_translate("GraphWindow", "Interval:"))
        self.comboBoxOrientation.setItemText(0, _translate("GraphWindow", "Select Orientation"))
        self.comboBoxOrientation.setItemText(1, _translate("GraphWindow", "Vertical"))
        self.comboBoxOrientation.setItemText(2, _translate("GraphWindow", "Horizontal"))
        self.pushButtonDeleteNode.setText(_translate("GraphWindow", "Delete Node"))
        self.pushButtonEditNode.setText(_translate("GraphWindow", "Edit Node"))
        self.groupBoxTabularView.setTitle(_translate("GraphWindow", "Tabular View"))
        self.groupBoxNode.setTitle(_translate("GraphWindow", "Tabular View"))
        self.tableWidgetNodes.setSortingEnabled(True)
        item = self.tableWidgetNodes.verticalHeaderItem(0)
        item.setText(_translate("GraphWindow", "Node Property Visibility"))
        item = self.tableWidgetNodes.horizontalHeaderItem(0)
        item.setText(_translate("GraphWindow", "Node Id"))
        item = self.tableWidgetNodes.horizontalHeaderItem(1)
        item.setText(_translate("GraphWindow", "Node Name"))
        item = self.tableWidgetNodes.horizontalHeaderItem(2)
        item.setText(_translate("GraphWindow", "Node Timestamp"))
        item = self.tableWidgetNodes.horizontalHeaderItem(3)
        item.setText(_translate("GraphWindow", "Node Description"))
        item = self.tableWidgetNodes.horizontalHeaderItem(4)
        item.setText(_translate("GraphWindow", "Log Entry Reference"))
        item = self.tableWidgetNodes.horizontalHeaderItem(5)
        item.setText(_translate("GraphWindow", "Log Creator"))
        item = self.tableWidgetNodes.horizontalHeaderItem(6)
        item.setText(_translate("GraphWindow", "Icon Type"))
        item = self.tableWidgetNodes.horizontalHeaderItem(7)
        item.setText(_translate("GraphWindow", "Source"))
        item = self.tableWidgetNodes.horizontalHeaderItem(8)
        item.setText(_translate("GraphWindow", "Node Visibility"))
        __sortingEnabled = self.tableWidgetNodes.isSortingEnabled()
        self.tableWidgetNodes.setSortingEnabled(False)
        item = self.tableWidgetNodes.item(1, 0)
        item.setText(_translate("GraphWindow", "0-001"))
        item = self.tableWidgetNodes.item(2, 0)
        item.setText(_translate("GraphWindow", "0-002"))
        item = self.tableWidgetNodes.item(3, 0)
        item.setText(_translate("GraphWindow", "0-003"))
        item = self.tableWidgetNodes.item(4, 0)
        item.setText(_translate("GraphWindow", "0-004"))
        item = self.tableWidgetNodes.item(5, 0)
        item.setText(_translate("GraphWindow", "0-005"))
        item = self.tableWidgetNodes.item(6, 0)
        item.setText(_translate("GraphWindow", "0-006"))
        item = self.tableWidgetNodes.item(7, 0)
        item.setText(_translate("GraphWindow", "0-007"))
        item = self.tableWidgetNodes.item(8, 0)
        item.setText(_translate("GraphWindow", "0-008"))
        self.tableWidgetNodes.setSortingEnabled(__sortingEnabled)

        self.dockWidgetRelationship.setWindowTitle(_translate("GraphWindow", "Relationship Table"))
        self.groupBoxRelationships.setTitle(_translate("GraphWindow", "Relationship Configuration"))
        self.tableWidgetRelationships.setSortingEnabled(True)
        item = self.tableWidgetRelationships.horizontalHeaderItem(1)
        item.setText(_translate("GraphWindow", "Relationship ID"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(2)
        item.setText(_translate("GraphWindow", "Parent"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(3)
        item.setText(_translate("GraphWindow", "Child"))
        item = self.tableWidgetRelationships.horizontalHeaderItem(4)
        item.setText(_translate("GraphWindow", "Label"))
        __sortingEnabled = self.tableWidgetRelationships.isSortingEnabled()
        self.tableWidgetRelationships.setSortingEnabled(False)
        self.tableWidgetRelationships.setSortingEnabled(__sortingEnabled)
        self.pushButtonDeleteRelationship.setText(_translate("GraphWindow", "Delete Relationship"))
        self.pushButtonEditRelationship.setText(_translate("GraphWindow", "Edit Relationship"))
        self.pushButtonAddRelationship.setText(_translate("GraphWindow", "Add Relationship"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())
