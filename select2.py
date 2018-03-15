from PyQt4 import QtGui, QtCore
#
#
# class RubberbandEnhancedLabel(QtGui.QLabel):
#
#     def __init__(self, parent=None):
#         QtGui.QLabel.__init__(self, parent)
#         self.selection = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
#
#     def mousePressEvent(self, event):
#         '''
#             Mouse is pressed. If selection is visible either set dragging mode (if close to border) or hide selection.
#             If selection is not visible make it visible and start at this point.
#         '''
#
#         if event.button() == QtCore.Qt.LeftButton:
#
#             position = QtCore.QPoint(event.pos())
#             if self.selection.isVisible():
#                 # visible selection
#                 if (self.upper_left - position).manhattanLength() < 20:
#                     # close to upper left corner, drag it
#                     self.mode = "drag_upper_left"
#                 elif (self.lower_right - position).manhattanLength() < 20:
#                     # close to lower right corner, drag it
#                     self.mode = "drag_lower_right"
#                 else:
#                     # clicked somewhere else, hide selection
#                     #self.selection.show()#hide()
#                     pass
#             else:
#                 # no visible selection, start new selection
#                 self.upper_left = position
#                 self.lower_right = position
#                 self.mode = "drag_lower_right"
#                 self.selection.show()
#
#     def mouseMoveEvent(self, event):
#         '''
#             Mouse moved. If selection is visible, drag it according to drag mode.
#         '''
#         if self.selection.isVisible():
#             # visible selection
#             if self.mode is "drag_lower_right":
#                 self.lower_right = QtCore.QPoint(event.pos())
#             elif self.mode is "drag_upper_left":
#                 self.upper_left = QtCore.QPoint(event.pos())
#             # update geometry
#             self.selection.setGeometry(QtCore.QRect(self.upper_left, self.lower_right).normalized())
#
#
#

from pyqtgraph import *
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class RubberbandEnhancedLabelMultiple(QtGui.QLabel):

    def __init__(self, parent=None):
        self.max_bboxes = 10
        QtGui.QLabel.__init__(self, parent)
        self.selections = []#[QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self) for i in range(self.max_bboxes)]
        self.active_bboxes = 0
        # for s in self.selections:
        #     s.hide()
        self.upper_left = []#[QtCore.QPoint() for i in range(self.max_bboxes)]
        self.lower_right = []#[QtCore.QPoint() for i in range(self.max_bboxes)]
        self.mode = []#[" " for i in range(self.max_bboxes)]
        self.category = []#[0]*self.max_bboxes
        self.reg = 0
        self.color = QtGui.QColor('red')#QtGui.QPalette(QtGui.QColor('red'))
        #self.color.setBrush(QtGui.QPalette.Foreground, QtGui.QBrush(QtGui.QColor('red')))
        #self.color.setBrush(QtGui.QPalette.Base, QtGui.QBrush(QtGui.QColor('red')))
        self.curr_id = 0
        self.id = []
        self._pixmap = QPixmap(self.width(), self.height())

 
    def change_color(self, i):
        d = {0:QtGui.QColor('red'), 1:QtGui.QColor('blue'), 2:QtGui.QColor('green'), 3:QtGui.QColor('black')}
        self.color = QtGui.QColor(d[i])

        self.reg = i


    def mousePressEvent(self, event):
        '''
            Mouse is pressed. If selection is visible either set dragging mode (if close to border) or hide selection.
            If selection is not visible make it visible and start at this point.
        '''
        # self.setPixmap(self._pixmap)
        # self.update()
        if event.button() == QtCore.Qt.LeftButton:
            #self.mode = [" " for i in range(self.max_bboxes)]
            print ("press")
            i = 0
            fl = 0
            min_i = 0
            min_sh = 10000
            string = "saaaas"
            position = QtCore.QPoint(event.pos())
            for sel in self.selections:
                if sel.isVisible():
                    # visible selection
                    if (self.upper_left[i] - position).manhattanLength() < min_sh:
                        # close to upper left corner, drag it
                        fl = 1
                        #self.mode[i] = "drag_upper_left"
                        min_sh = (self.upper_left[i] - position).manhattanLength()
                        min_i = i
                        string = "drag_upper_left"
                    if (self.lower_right[i] - position).manhattanLength() < min_sh:
                        # close to lower right corner, drag it
                        #self.mode[i] = "drag_lower_right"
                        min_sh = (self.lower_right[i] - position).manhattanLength()
                        min_i = i
                        string =  "drag_lower_right"
                        fl = 1
                i += 1
                    # else:
                    #     # clicked somewhere else, hide selection
                    #     #self.selection.hide()
                    #     self.selections[i].show()

                    #     pass
                print ('loop 1')
          
            if min_sh < 50:
              
                self.mode[min_i] = string

            else:
                # no visible selection, start new selection
                print (len(self.selections))

                self.selections.append(QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self))
                self.category.append(self.reg)
                self.upper_left.append(position)
                self.lower_right.append(position)
                self.mode.append("drag_lower_right")
                self.selections[-1].setGeometry(QtCore.QRect(self.upper_left[-1], self.lower_right[-1]).normalized())
                #self.color.setBrush(QtGui.QColor(255,0,0))
                # self.selections[-1].setPalette(self.color)

                #self.selections[-1].setStyle(QtGui.QStyleFactory.create('windowsvista'))
                self.selections[-1].show()
                self.id.append(self.curr_id)
                if self.reg != 3:
                    self.curr_id += 1
                # self.upper_left[self.active_bboxes] = position
                # self.lower_right[self.active_bboxes] = position
                # self.mode[self.active_bboxes] = "drag_lower_right"
                # self.selections[self.active_bboxes].show()

                #print (self.active_bboxes, self.selections[self.active_bboxes].isVisible())
                self.active_bboxes += 1
                print ("new", self.active_bboxes)


    def mouseMoveEvent(self, event):
        '''
            Mouse moved. If selection is visible, drag it according to drag mode.
        '''
        #print ("MouseMove")
        for i in range(self.active_bboxes):
            if self.selections[i].isVisible():
                # visible selection
                if self.mode[i] == "drag_lower_right":
                    self.lower_right[i] = QtCore.QPoint(event.pos())


                elif self.mode[i] == "drag_upper_left":
                    self.upper_left[i] = QtCore.QPoint(event.pos())
                # update geometry
                self.selections[i].setGeometry(QtCore.QRect(self.upper_left[i], self.lower_right[i]).normalized())

                # painter = QtGui.QPainter()
                # painter.begin(self)
                # pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.DashDotDotLine)
                # painter.setPen(pen)                # painter.drawRect(self.upper_left[i].x(), self.upper_left[i].y(), self.selections[i].height(), self.selections[i].width())

    def mouseReleaseEvent(self, event):
        print ("ReleaseMouse")
       # pass
        self.mode = [" " for i in range(len(self.mode))]
        i = 0
        for s in self.selections:
            print
            if self.upper_left[i].x() == self.lower_right[i].x() or self.upper_left[i].y() == self.lower_right[i].y():
                print ('remove')
                s.hide()
                self.selections.remove(s)
                self.active_bboxes -= 1

            i += 1
        # if self.selections[self.active_bboxes-1].width() == 0 and self.selections[self.active_bboxes-1].width() == 0 :
        #     self.selections[self.active_bboxes-1].hide()
        #     self.active_bboxes -= 1

    def paintEvent(self, event):
        super(RubberbandEnhancedLabelMultiple, self).paintEvent(event)
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setOpacity(0.1)
        d = {0:QtGui.QColor('red'), 1:QtGui.QColor('blue'), 2:QtGui.QColor('green'), 3:QtGui.QColor('black')}

        for i in range(len(self.selections)):
            brush = QtGui.QBrush(QtCore.Qt.SolidPattern)

            brush.setColor(d[self.category[i]])
            qp.setBrush(brush)

            qp.drawRect(self.upper_left[i].x(), self.upper_left[i].y(), self.selections[i].width(),
                    self.selections[i].height())

        self.update()
        qp.end()

    def reset_selected(self):
        for sel in self.selections:
            sel.hide()

        self.selections = [] #[QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self) for i in range(self.max_bboxes)]
        self.active_bboxes = 0
        self.upper_left = []#[QtCore.QPoint() for i in range(self.max_bboxes)]
        self.lower_right = []#[QtCore.QPoint() for i in range(self.max_bboxes)]
        self.mode = []#[" " for i in range(self.max_bboxes)]

    def keyPressEvent(self, event):
        print ("key")
        if event.key()==(QtCore.Qt.Key_Backspace):
            print ('ctrl z')
            self.selections[self.active_bboxes].hide()
            self.active_bboxes -= 1
    #
    # def resizeEvent(self, event):
    #     self.setPixmap(self._pixmap.scaled(
    #         self.width(), self.height(),
    #         QtCore.Qt.KeepAspectRatio))
# app = QtGui.QApplication([])
#
# screen_pixmap = QtGui.QPixmap('data/1.jpg')#.grabWindow(app.desktop().winId())
#
# window = QtGui.QWidget()
# layout = QtGui.QVBoxLayout(window)
# label = RubberbandEnhancedLabel()
# label.setPixmap(screen_pixmap)
# layout.addWidget(label)
# geometry = app.desktop().availableGeometry()
# window.setFixedSize(500, 500)
# window.show()
# app.exec_()