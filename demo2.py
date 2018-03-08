# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

NUM_IMAGE = 1
import pandas as pd

from select2 import RubberbandEnhancedLabelMultiple
#rom dataloader import DataLoader
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

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
        """ Custom class """
        self.label = RubberbandEnhancedLabelMultiple(Dialog) #QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 561, 411))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = RubberbandEnhancedLabelMultiple(Dialog) #QtGui.QLabel(Dialog)
        """  Regime - 0 == stayed, 1 == appeared, 2 == disappeared"""
        self.reg = 0
        self.dict = {"stayed":0, "appeared":1, "disappeared":2}

        self.label_2.setGeometry(QtCore.QRect(670, 70, 561, 411))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.n_img = 1
        self.data = pd.DataFrame(columns = ['image','x1','y1','x2','y2','class'])

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
        self.pushButton_4.clicked.connect(self.stayed)

        self.pushButton_5.setText(_translate("Dialog", "Появился", None))
        self.pushButton_5.clicked.connect(self.appeared)

        self.pushButton_6.setText(_translate("Dialog", "Пропал", None))
        self.pushButton_6.clicked.connect(self.disappeared)

        self.label.setText(_translate("Dialog", "image_1", None))
        self.label_2.setText(_translate("Dialog", "image_2", None))

        #create pixmap from image
        pixmap = QtGui.QPixmap('data/1.jpg')
   

        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)
        #self.selector = RubberbandEnhancedLabelMultiple()

    def next_image(self):
        """
        Load next image from path
        """
        self.n_img += 1

        pixmap = QtGui.QPixmap('data/' + str(self.n_img) + '.jpg')

        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)
        self.label.reset_selected()
        self.label_2.reset_selected()
        return 

    def prev_image(self):
        """
        Load previous image
        """
        self.n_img -= 1

        pixmap = QtGui.QPixmap('data/' + str(self.n_img) + '.jpg')

        self.label.setPixmap(pixmap)

        self.label_2.setPixmap(pixmap)
        self.label.reset_selected()
        self.label_2.reset_selected()
        print ('previous...')
        pass

    def save_data(self):
        """
        Write data to file
        """

        tmp = []#pd.DataFrame()

        for i in range(self.label.active_bboxes):
            x1,y1,x2,y2 = self.label.upper_left[i].x(),self.label.upper_left[i].y(), self.label.lower_right[i].x(),self.label.lower_right[i].y()
            #tmp.append(pd.DataFrame({'image':self.n_img,'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, index = [i]))
            tmp.append([self.n_img, x1, y1, x2, y2, self.label.category[i]])
            print (i)
        print (len(tmp))
        tmp = pd.DataFrame(tmp, columns=['image','x1','y1','x2','y2','class'])
        print (tmp.shape)
            #f.write("%s %s %s %s %s\n"%(self.n_img, x1,y1,x2,y2))
        self.data = self.data[self.data.image != self.n_img]
        #self.data.append(tmp)
        self.data = pd.concat([self.data, tmp])
        print (self.data.shape)
        self.data.sort_values(by=['image'], inplace=True)
        self.data.to_csv('logs.csv')

        print ('saving...')
        pass
    def stayed(self):
        self.label.change_color(self.dict['stayed'])
        #self.reg = self.dict['stayed']

    def appeared(self):
        self.label.change_color(self.dict['appeared'])
        #self.reg = self.dict['appeared']

    def disappeared(self):
        self.label.change_color(self.dict['disappeared'])
        #self.reg = self.dict['disappeared']
if __name__ == "__main__":
   import sys
   app = QtGui.QApplication(sys.argv)
   Dialog = QtGui.QDialog()
   ui = Ui_Dialog()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())