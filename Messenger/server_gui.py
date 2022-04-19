# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServerWindow(object):
    def setupUi(self, ServerWindow):
        ServerWindow.setObjectName("ServerWindow")
        ServerWindow.resize(868, 671)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServerWindow.sizePolicy().hasHeightForWidth())
        ServerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ServerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_active_clients = QtWidgets.QLabel(self.centralwidget)
        self.label_active_clients.setAlignment(QtCore.Qt.AlignCenter)
        self.label_active_clients.setObjectName("label_active_clients")
        self.verticalLayout.addWidget(self.label_active_clients)
        self.table_active_clients = QtWidgets.QTableWidget(self.centralwidget)
        self.table_active_clients.setObjectName("table_active_clients")
        self.table_active_clients.setColumnCount(4)
        self.table_active_clients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_clients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_clients.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_clients.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_clients.setHorizontalHeaderItem(3, item)
        self.table_active_clients.horizontalHeader().setVisible(True)
        self.table_active_clients.horizontalHeader().setCascadingSectionResizes(True)
        self.table_active_clients.horizontalHeader().setStretchLastSection(True)
        self.table_active_clients.verticalHeader().setCascadingSectionResizes(False)
        self.table_active_clients.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.table_active_clients)
        self.label_server_status = QtWidgets.QLabel(self.centralwidget)
        self.label_server_status.setObjectName("label_server_status")
        self.verticalLayout.addWidget(self.label_server_status)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        ServerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 26))
        self.menubar.setObjectName("menubar")
        self.menuClients_history = QtWidgets.QMenu(self.menubar)
        self.menuClients_history.setObjectName("menuClients_history")
        self.menuServer_settings = QtWidgets.QMenu(self.menubar)
        self.menuServer_settings.setObjectName("menuServer_settings")
        ServerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ServerWindow)
        self.statusbar.setObjectName("statusbar")
        ServerWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuClients_history.menuAction())
        self.menubar.addAction(self.menuServer_settings.menuAction())

        self.retranslateUi(ServerWindow)
        QtCore.QMetaObject.connectSlotsByName(ServerWindow)

    def retranslateUi(self, ServerWindow):
        _translate = QtCore.QCoreApplication.translate
        ServerWindow.setWindowTitle(_translate("ServerWindow", "Server"))
        self.label_active_clients.setText(_translate("ServerWindow", "Active clients"))
        item = self.table_active_clients.horizontalHeaderItem(0)
        item.setText(_translate("ServerWindow", "Username"))
        item = self.table_active_clients.horizontalHeaderItem(1)
        item.setText(_translate("ServerWindow", "IP"))
        item = self.table_active_clients.horizontalHeaderItem(2)
        item.setText(_translate("ServerWindow", "Port"))
        item = self.table_active_clients.horizontalHeaderItem(3)
        item.setText(_translate("ServerWindow", "Login time"))
        self.label_server_status.setText(_translate("ServerWindow", "Server is working"))
        self.menuClients_history.setTitle(_translate("ServerWindow", "Clients"))
        self.menuServer_settings.setTitle(_translate("ServerWindow", "Server"))