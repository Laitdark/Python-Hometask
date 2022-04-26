from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_add_contact(object):
    def setupUi(self, form_add_contact):
        form_add_contact.setObjectName("form_add_contact")
        form_add_contact.resize(286, 124)
        self.widget_form = QtWidgets.QWidget(form_add_contact)
        self.widget_form.setGeometry(QtCore.QRect(9, 9, 265, 101))
        self.widget_form.setObjectName("widget_form")
        self.formLayout = QtWidgets.QFormLayout(self.widget_form)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_add_contact = QtWidgets.QLabel(self.widget_form)
        self.label_add_contact.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_contact.setObjectName("label_add_contact")
        self.verticalLayout.addWidget(self.label_add_contact)
        self.select_user = QtWidgets.QComboBox(self.widget_form)
        self.select_user.setObjectName("select_user")
        self.verticalLayout.addWidget(self.select_user)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add = QtWidgets.QPushButton(self.widget_form)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_3.addWidget(self.btn_add)
        self.btn_cancel = QtWidgets.QPushButton(self.widget_form)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)

        self.retranslateUi(form_add_contact)
        QtCore.QMetaObject.connectSlotsByName(form_add_contact)

    def retranslateUi(self, form_add_contact):
        _translate = QtCore.QCoreApplication.translate
        form_add_contact.setWindowTitle(_translate("form_add_contact", "Add contact"))
        self.label_add_contact.setText(_translate("form_add_contact", "Choose a user to add to contact list"))
        self.btn_add.setText(_translate("form_add_contact", "Add"))
        self.btn_cancel.setText(_translate("form_add_contact", "Cancel"))