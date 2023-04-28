# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ISAT_to_VOC_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(600, 173)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_save_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_save_root.setEnabled(True)
        self.lineEdit_save_root.setReadOnly(True)
        self.lineEdit_save_root.setObjectName("lineEdit_save_root")
        self.gridLayout.addWidget(self.lineEdit_save_root, 3, 0, 1, 1)
        self.pushButton_save_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_save_root.setObjectName("pushButton_save_root")
        self.gridLayout.addWidget(self.pushButton_save_root, 3, 1, 1, 1)
        self.checkBox_is_instance = QtWidgets.QCheckBox(self.widget)
        self.checkBox_is_instance.setToolTip("")
        self.checkBox_is_instance.setAccessibleName("")
        self.checkBox_is_instance.setAccessibleDescription("")
        self.checkBox_is_instance.setObjectName("checkBox_is_instance")
        self.gridLayout.addWidget(self.checkBox_is_instance, 4, 1, 1, 1)
        self.lineEdit_label_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_label_root.setEnabled(True)
        self.lineEdit_label_root.setReadOnly(True)
        self.lineEdit_label_root.setObjectName("lineEdit_label_root")
        self.gridLayout.addWidget(self.lineEdit_label_root, 2, 0, 1, 1)
        self.pushButton_label_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_label_root.setObjectName("pushButton_label_root")
        self.gridLayout.addWidget(self.pushButton_label_root, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_process = QtWidgets.QWidget(Dialog)
        self.widget_process.setObjectName("widget_process")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_process)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.widget_process)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.current_num = QtWidgets.QLabel(self.widget_process)
        self.current_num.setText("")
        self.current_num.setObjectName("current_num")
        self.horizontalLayout_2.addWidget(self.current_num)
        self.label_3 = QtWidgets.QLabel(self.widget_process)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.all_num = QtWidgets.QLabel(self.widget_process)
        self.all_num.setText("")
        self.all_num.setObjectName("all_num")
        self.horizontalLayout_2.addWidget(self.all_num)
        self.verticalLayout.addWidget(self.widget_process)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cache = QtWidgets.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/关闭_close-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cache.setIcon(icon)
        self.pushButton_cache.setObjectName("pushButton_cache")
        self.horizontalLayout.addWidget(self.pushButton_cache)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/校验_check-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apply.setIcon(icon1)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ISAT to VOC png"))
        self.lineEdit_save_root.setPlaceholderText(_translate("Dialog", "png save root"))
        self.pushButton_save_root.setText(_translate("Dialog", "Save root"))
        self.checkBox_is_instance.setText(_translate("Dialog", "Is Instance"))
        self.lineEdit_label_root.setPlaceholderText(_translate("Dialog", "ISAT annotations root"))
        self.pushButton_label_root.setText(_translate("Dialog", "Label root"))
        self.label_3.setAccessibleName(_translate("Dialog", "aaa"))
        self.label_3.setText(_translate("Dialog", "/"))
        self.label.setText(_translate("Dialog", "Convert ISAT annotations to VOC png."))
        self.pushButton_cache.setText(_translate("Dialog", "cache"))
        self.pushButton_apply.setText(_translate("Dialog", "convert"))
import icons_rc
