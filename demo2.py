# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

NUM_IMAGE = 1



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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1451, 638)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 540, 131, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 540, 131, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 540, 121, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(1310, 100, 99, 27))
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(1310, 160, 99, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(1310, 210, 99, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 561, 411))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(670, 70, 561, 411))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.n_img = 1

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Next", None))
        self.pushButton_2.setText(_translate("Dialog", "Save", None))
        self.pushButton_3.setText(_translate("Dialog", "Prev", None))

        """ setting actions for buttons"""
        self.pushButton.clicked.connect(self.next_image)
        self.pushButton_2.clicked.connect(self.save_data)
        self.pushButton_3.clicked.connect(self.prev_image)


        self.pushButton_4.setText(_translate("Dialog", "Остался", None))
        self.pushButton_5.setText(_translate("Dialog", "Появился", None))
        self.pushButton_6.setText(_translate("Dialog", "Пропал", None))
        self.label.setText(_translate("Dialog", "image_1", None))
        self.label_2.setText(_translate("Dialog", "image_2", None))
        pixmap = QtGui.QPixmap('data/1.jpg')
        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)

    def next_image(self):
        """
        Load next image from path
        """
        self.n_img += 1

        pixmap = QtGui.QPixmap('data/' + str(self.n_img) + '.jpg')

        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)
        return 

    def prev_image(self):
        """
        Load previous image
        """
        self.n_img -= 1

        pixmap = QtGui.QPixmap('data/' + str(self.n_img) + '.jpg')

        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)

        print ('previous...')
        pass

    def save_data(self):
        """
        Write data to file
        """
        with open('logs.txt','a') as f:
            f.write(str(self.n_img) + ' 0 0 0')
        print ('saving...')
        pass

if __name__ == "__main__":
   import sys
   app = QtGui.QApplication(sys.argv)
   Dialog = QtGui.QDialog()
   ui = Ui_Dialog()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())