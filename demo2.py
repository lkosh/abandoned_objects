# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

NUM_IMAGE = 1
import pandas as pd

from select2 import RubberbandEnhancedLabelMultiple

from pyqtgraph import *
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
        self.Dialog = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(2000, 800)
        self.logs = QtGui.QPlainTextEdit()

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

        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(1310, 260, 99, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(1310, 310, 99, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(1310, 370, 115, 40))
        self.pushButton_9.setObjectName(_fromUtf8("resize_plus"))

        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(1310, 420, 115,40))
        self.pushButton_10.setObjectName(_fromUtf8("resize_minus"))

        self.pushButton_11 = QtGui.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(1310, 50, 99, 27))
        self.pushButton_11.setObjectName(_fromUtf8("shift"))


        self.button_idplus_1 = QtGui.QPushButton(Dialog)
        self.button_idplus_1.setObjectName(_fromUtf8("plus_1"))
        self.button_idminus_1 = QtGui.QPushButton(Dialog)
        self.button_idplus_2 = QtGui.QPushButton(Dialog)
        self.button_idminus_2 = QtGui.QPushButton(Dialog)

        #self.button_idminus_1.setGeometry(QtCore.QRect(5, 5, 10, 10))
        self.button_idplus_1.setGeometry(QtCore.QRect(5, 25, 10, 10))

        """ Custom class """
        self.label = RubberbandEnhancedLabelMultiple(Dialog) #QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 561, 411))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setFrameShape(QtGui.QFrame.Panel)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setLineWidth(3)


        self.label_2 = RubberbandEnhancedLabelMultiple(Dialog) #QtGui.QLabel(Dialog)
        """  Regime - 0 == stayed, 1 == appeared, 2 == disappeared"""
        self.reg = 0
        self.dict = {"human":0, "object":1, "car":2, "ignore":3}

        self.label_2.setGeometry(QtCore.QRect(670, 70, 561, 411))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_2.setFrameShape(QtGui.QFrame.Panel)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setLineWidth(3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.id = 0
        #self.n_img = 1
        self.data = pd.DataFrame(columns = ['image_1','image_2','x1','y1','x2','y2','class', 'pic', 'id'])

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Next", None))
        self.pushButton_2.setText(_translate("Dialog", "Save", None))
        self.pushButton_3.setText(_translate("Dialog", "Prev", None))

        """ setting actions for buttons"""
        self.pushButton.clicked.connect(self.getfile)
        self.pushButton_2.clicked.connect(self.save_data)
        self.pushButton_3.clicked.connect(self.prev_image)


        self.pushButton_4.setText(_translate("Dialog", "Человек", None))
        self.pushButton_4.clicked.connect(self.human)

        self.pushButton_5.setText(_translate("Dialog", "Машина", None))
        self.pushButton_5.clicked.connect(self.car)

        self.pushButton_6.setText(_translate("Dialog", "Объект", None))
        self.pushButton_6.clicked.connect(self.object)

        self.pushButton_11.setText(_translate("Dialog", "Игнор", None))
        self.pushButton_11.clicked.connect(self.ignore)

        self.pushButton_7.setText(_translate("Dialog", "Удалить c 1", None))
        self.pushButton_7.clicked.connect(self.delete_1)

        self.pushButton_8.setText(_translate("Dialog", "Удалить c 2", None))
        self.pushButton_8.clicked.connect(self.delete_2)

        self.pushButton_9.setText(_translate("Dialog", "Увеличить", None))
        self.pushButton_9.clicked.connect(self.plus)

        self.pushButton_10.setText(_translate("Dialog", "Уменьшить", None))
        self.pushButton_10.clicked.connect(self.minus)

        self.button_idminus_1.setText(_translate("Dialog", "ID --", None))
        self.button_idminus_1.clicked.connect(self.idchange_0_m1)
        self.button_idminus_2.setText(_translate("Dialog", "ID --", None))
        self.button_idminus_2.clicked.connect(self.idchange_1_m1)


        self.button_idplus_1.setText(_translate("Dialog", "ID ++", None))
        self.button_idplus_1.clicked.connect(self.idchange_0_1)

        self.button_idplus_2.setText(_translate("Dialog", "ID ++", None))
        self.button_idplus_2.clicked.connect(self.idchange_1_1)




        self.label.setText(_translate("Dialog", "image_1", None))
        self.label_2.setText(_translate("Dialog", "image_2", None))

        #create pixmap from image

        #self.label.setGeometry(QtCore.QRect(50, 70, pixmap.width(), pixmap.height()))


        self.label.n_img = 0


        #self.label_2.setGeometry(QtCore.QRect(670, 70, pixmap_2.width(), pixmap_2.height()))
        self.label_2.n_img = 1

        #self.selector = RubberbandEnhancedLabelMultiple()

    # def next_image(self):
    #     """
    #     Load next image from path
    #     """
    #     self.label.n_img += 1
    #     self.label_2.n_img += 1
    #     pixmap = QtGui.QPixmap('data/' + str(self.label.n_img) + '.jpg')
    #
    #     self.label.setPixmap(pixmap)
    #     self.label._pixmap = pixmap
    #     self.label.setGeometry(QtCore.QRect(20, 70, pixmap.width(), pixmap.height()))
    #
    #     pixmap_2 = QtGui.QPixmap('data/' + str(self.label_2.n_img) + '.jpg')
    #
    #     self.label_2.setPixmap(pixmap_2)
    #     self.label_2._pixmap = pixmap_2
    #
    #     self.label.reset_selected()
    #     self.label_2.reset_selected()
    #     self.label_2.setGeometry(QtCore.QRect(670, 70, pixmap_2.width(), pixmap_2.height()))
    #
    #     return
    def idchange(self, i, num):
        if num == 0:
            self.label.id += i
        else:
            self.label_2.id += i
    def idchange_0_1(self):
        print("01")
        self.label.curr_id += 1
    def idchange_1_1(self):
        print ("11")
        self.label_2.curr_id += 1
    def idchange_0_m1(self):
        print ("0-1")
        self.label.curr_id -= 1
    def idchange_1_m1(self):
        print ("1-1")
        self.label_2.curr_id -= 1

    def prev_image(self):
        """
        Load previous image
        """
        self.label.n_img -= 1
        self.label_2.n_img -= 1
        pixmap = QtGui.QPixmap('data/' + str(self.label.n_img) + '.jpg')

        self.label.setPixmap(pixmap)
        self.label._pixmap = pixmap
        self.label.setGeometry(QtCore.QRect(50, 70, pixmap.width(), pixmap.height()))

        pixmap_2 = QtGui.QPixmap('data/' + str(self.label_2.n_img) + '.jpg')

        self.label_2.setPixmap(pixmap)
        self.label_2._pixmap = pixmap_2

        self.label.reset_selected()
        self.label_2.reset_selected()
        self.label_2.setGeometry(QtCore.QRect(670, 70, pixmap_2.width(), pixmap_2.height()))

        print ('previous...')
        pass

    def save_data(self):
        """
        Write data to file
        """

        tmp = []
        #pd.DataFrame()

        for i in range(self.label.active_bboxes):
           # if self.label.selections[i].isVisible():
                x1,y1,x2,y2 = self.label.upper_left[i].x(),self.label.upper_left[i].y(), self.label.lower_right[i].x(),self.label.lower_right[i].y()
                x1, x2, y1, y2 = x1* self.scale, x2*self.scale, y1*self.scale, y2*self.scale
                #tmp.append(pd.DataFrame({'image':self.n_img,'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, index = [i]))
                tmp.append([self.label.name, self.label_2.name,  x1, y1, x2, y2, self.label.category[i], 0, self.label.id[i]])

        for i in range(self.label_2.active_bboxes):
            x1, y1, x2, y2 = self.label_2.upper_left[i].x(), self.label_2.upper_left[i].y(), \
                             self.label_2.lower_right[i].x(), self.label_2.lower_right[i].y()
            x1, x2, y1, y2 = x1 * self.scale, x2 * self.scale, y1 * self.scale, y2 * self.scale

            # tmp.append(pd.DataFrame({'image':self.n_img,'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, index = [i]))
            tmp.append([self.label.name, self.label_2.name, x1, y1, x2, y2, self.label_2.category[i], 1, self.label_2.id[i]])
            print (i)
        print (len(tmp))
        tmp = pd.DataFrame(tmp, columns=['image_1','image_2','x1','y1','x2','y2','class','pic','id'])
        print (tmp.shape)
            #f.write("%s %s %s %s %s\n"%(self.n_img, x1,y1,x2,y2))
        mask = (self.data.image_1 == self.label.n_img) & (self.data.image_2 == self.label_2)
        mask = ~mask

        self.data = self.data[mask]#self.data[self.data.image != self.n_img]
        #self.data.append(tmp)
        self.data = pd.concat([self.data, tmp])
        print (self.data.shape)
        self.data.sort_values(by=['image_1', 'image_2'], inplace=True)
        self.data.to_csv('logs.csv')

        print ('saving...')
        pass
    def car(self):
        self.label.change_color(self.dict['car'])
        self.label_2.change_color(self.dict['car'])

        #self.reg = self.dict['stayed']

    def object(self):
        self.label.change_color(self.dict['object'])
        self.label_2.change_color(self.dict['object'])

        #self.reg = self.dict['appeared']

    def human(self):
        self.label.change_color(self.dict['human'])
        self.label_2.change_color(self.dict['human'])

    def ignore(self):
        self.label.change_color(self.dict['ignore'])
        self.label_2.change_color(self.dict['ignore'])

        #self.reg = self.dict['disappeared']

    def delete_1(self):
        if self.label.active_bboxes > 0:

            self.label.active_bboxes -= 1

            self.label.selections[-1].hide()
            self.label.selections = self.label.selections[:-1]
            self.label.upper_left = self.label.upper_left[:-1]
            self.label.lower_right = self.label.lower_right[:-1]
            self.label.mode = self.label.mode[:-1]
        print ('ctrl z ',len(self.label.selections) )

    def delete_2(self):
        if self.label_2.active_bboxes > 0:
            self.label_2.active_bboxes -= 1

            self.label_2.selections[-1].hide()
            self.label_2.selections = self.label_2.selections[:-1]
            self.label_2.upper_left = self.label_2.upper_left[:-1]
            self.label_2.lower_right = self.label_2.lower_right[:-1]
            self.label_2.mode = self.label_2.mode[:-1]

        print ('ctrl z ', len(self.label_2.selections))

    def plus(self):
        h = self.label.height()
        w = self.label.width()
        self.label.setGeometry((QtCore.QRect(50, 70, w + 10, h + 10)))
        self.label_2.setGeometry(QtCore.QRect(670, 70, w + 10, h + 10))

    def minus(self):
        h = self.label.height()
        w = self.label.width()
        self.label.setGeometry((QtCore.QRect(50, 70, w - 10, h - 10)))
        self.label_2.setGeometry(QtCore.QRect(670, 70, w - 10, h - 10))

    def keyPressEvent(self):

        #   if type(event) == QtGui.QKeyEvent:
            print ("dsd")

    def getfile(self):
        scale = 840
        fname = QFileDialog.getOpenFileName(self.Dialog, 'Open file for 1st frame',
                                            'c:\\', "Image files (*.jpg *.gif)",options=QtGui.QFileDialog.DontUseNativeDialog)
        pixmap = QPixmap(fname)
        self.scale = pixmap.width()/scale

        pixmap = pixmap.scaledToWidth(scale)
        self.label.setGeometry(QtCore.QRect(20, 20, pixmap.width(), pixmap.height()))
        self.label._pixmap = pixmap
        self.label.setPixmap(pixmap)
        self.label.name = fname
        fname = QFileDialog.getOpenFileName(self.Dialog, 'Open file for 2nd frame',
                                            'c:\\', "Image files (*.jpg *.gif)", options=QtGui.QFileDialog.DontUseNativeDialog)
        pixmap_2 = QPixmap(fname)
        pixmap_2 = pixmap_2.scaledToWidth(scale)
        self.label_2._pixmap = pixmap_2
        self.label_2.setGeometry(QtCore.QRect(40 + pixmap.width(), 20,  pixmap_2.width(), pixmap_2.height()))
        self.label_2.setPixmap(pixmap_2)
        self.label_2.name = fname
        #shifting buttons

        #row 1
        self.pushButton.setGeometry(QtCore.QRect(20 + pixmap.width(), 40 + pixmap_2.height(), 131, 51))
        self.pushButton_2.setGeometry(QtCore.QRect(20 + pixmap.width() - 131 - 5, 40 + pixmap_2.height(), 131, 51))
        self.pushButton_3.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 10, 40 + pixmap_2.height(), 131, 51))
        #row 2
        self.pushButton_7.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50, 40 + pixmap_2.height() + 51 + 10, 115, 40))
        self.pushButton_8.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115, 40 + pixmap_2.height() + 51 + 10, 115, 40))
        self.pushButton_9.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115*2, 40 + pixmap_2.height() + 51 + 10, 115, 40))
        self.pushButton_10.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115*3, 40 + pixmap_2.height() + 51 + 10, 115, 40))

        #row 3
        self.pushButton_4.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50, 40 + pixmap_2.height() + 91 + 20, 115, 40))
        self.pushButton_5.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115, 40 + pixmap_2.height() + 91 + 20, 115, 40))
        self.pushButton_6.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115*2, 40 + pixmap_2.height() + 91 + 20, 115, 40))
        self.pushButton_11.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 115*3, 40 + pixmap_2.height() + 91 + 20, 115, 40))

        #self.button_idminus_1.setGeometry(QtCore.QRect(5, 5, 10, 10))
        self.button_idplus_1.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50, 40 + pixmap_2.height() + 91 + 20 + 60, 40, 40))
        self.button_idminus_1.setGeometry(QtCore.QRect(20 + pixmap.width() - 131*2 - 50 + 60, 40 + pixmap_2.height() + 91 + 20 + 60, 40, 40))
        # self.button_idminus_1.setGeometry(QtCore.QRect(5, 5, 10, 10))
        self.button_idplus_2.setGeometry(
            QtCore.QRect(20 + pixmap.width() - 131 * 2 - 50 + 100 + 120, 40 + pixmap_2.height() + 91 + 20 + 60, 40, 40))
        self.button_idminus_2.setGeometry(
            QtCore.QRect(20 + pixmap.width() - 131 * 2 - 50 + 100 + 180, 40 + pixmap_2.height() + 91 + 20 + 60, 40, 40))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


    def PaintEvent(self, event):
        self.PaintEvent(event)


if __name__ == "__main__":
   import sys
   app = QtGui.QApplication(sys.argv)
   Dialog = QtGui.QDialog()
   ui = Ui_Dialog()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())