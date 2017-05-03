# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Jun 22 18:08:17 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class UiMyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName(_fromUtf8("MyForm"))
        MyForm.resize(585, 676)
        self.imageList = QtGui.QListWidget(MyForm)
        self.imageList.setGeometry(QtCore.QRect(200, 20, 360, 192))
        self.imageList.setObjectName(_fromUtf8("imageList"))
        self.dimenSelector = QtGui.QComboBox(MyForm)
        self.dimenSelector.setGeometry(QtCore.QRect(20, 50, 141, 22))
        self.dimenSelector.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dimenSelector.setObjectName(_fromUtf8("dimenSelector"))
        self.dimenSelector.addItem(_fromUtf8(""))
        self.dimenSelector.addItem(_fromUtf8(""))
        self.dimenSelector.addItem(_fromUtf8(""))
        self.dimenSelector.addItem(_fromUtf8(""))
        self.prevLabel = QtGui.QLabel(MyForm)
        self.prevLabel.setGeometry(QtCore.QRect(20, 200, 46, 13))
        self.prevLabel.setObjectName(_fromUtf8("prevLabel"))
        self.image_preview_portrait = QtGui.QLabel(MyForm)
        self.image_preview_portrait.setGeometry(QtCore.QRect(190, 220, 261, 431))
        self.image_preview_portrait.setObjectName(_fromUtf8("image_preview_portrait"))
        self.image_preview_landscape = QtGui.QLabel(MyForm)
        self.image_preview_landscape.setGeometry(QtCore.QRect(80, 320, 431, 261))
        self.image_preview_landscape.setObjectName(_fromUtf8("image_preview_landscape"))
        self.saveBtn = QtGui.QPushButton(MyForm)
        self.saveBtn.setGeometry(QtCore.QRect(20, 20, 141, 23))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))

        self.retranslateUi(MyForm)
        QtCore.QObject.connect(self.saveBtn, QtCore.SIGNAL(_fromUtf8("released()")), MyForm.file_save)
        QtCore.QObject.connect(self.imageList, QtCore.SIGNAL("currentRowChanged(int)"), MyForm.change_image_preview)
        QtCore.QObject.connect(self.dimenSelector, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(const QString&)")), MyForm.switch_samples)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        MyForm.setWindowTitle(_translate("MyForm", "Dialog", None))
        self.dimenSelector.setItemText(0, _translate("MyForm", "Select a device...", None))
        self.dimenSelector.setItemText(1, _translate("MyForm", "Icon", None))
        self.dimenSelector.setItemText(2, _translate("MyForm", "Smartphone", None))
        self.dimenSelector.setItemText(3, _translate("MyForm", "Landscape", None))
        self.prevLabel.setText(_translate("MyForm", "Preview", None))
        self.saveBtn.setText(_translate("MyForm", "Save", None))

