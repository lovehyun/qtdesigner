# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# NOTE: pyuic5 -x hello2.ui -o hello2-auto.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(7, 16, 381, 191))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 361, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 240, 371, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.slot_1st)
        self.pushButton_2.clicked.connect(self.slot_2nd)
        self.pushButton_3.clicked.connect(self.slot_3rd)
        self.lineEdit.textChanged['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "여기에 출력됩니다"))
        self.pushButton.setText(_translate("Dialog", "첫번째 버튼"))
        self.pushButton_2.setText(_translate("Dialog", "두번째 버튼"))
        self.pushButton_3.setText(_translate("Dialog", "세번째 버튼"))

    def slot_1st(self):
        self.label.setText("첫번째 버튼")

    def slot_2nd(self):
        self.label.setText("두번째 버튼!")
	
    def slot_3rd(self):
        self.label.setText("세번째 버튼?")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
