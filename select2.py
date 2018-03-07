from PyQt4 import QtGui, QtCore


class RubberbandEnhancedLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.selection = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        '''
            Mouse is pressed. If selection is visible either set dragging mode (if close to border) or hide selection.
            If selection is not visible make it visible and start at this point.
        '''

        if event.button() == QtCore.Qt.LeftButton:

            position = QtCore.QPoint(event.pos())
            if self.selection.isVisible():
                # visible selection
                if (self.upper_left - position).manhattanLength() < 20:
                    # close to upper left corner, drag it
                    self.mode = "drag_upper_left"
                elif (self.lower_right - position).manhattanLength() < 20:
                    # close to lower right corner, drag it
                    self.mode = "drag_lower_right"
                else:
                    # clicked somewhere else, hide selection
                    #self.selection.show()#hide()
                    pass
            else:
                # no visible selection, start new selection
                self.upper_left = position
                self.lower_right = position
                self.mode = "drag_lower_right"
                self.selection.show()

    def mouseMoveEvent(self, event):
        '''
            Mouse moved. If selection is visible, drag it according to drag mode.
        '''
        if self.selection.isVisible():
            # visible selection
            if self.mode is "drag_lower_right":
                self.lower_right = QtCore.QPoint(event.pos())
            elif self.mode is "drag_upper_left":
                self.upper_left = QtCore.QPoint(event.pos())
            # update geometry
            self.selection.setGeometry(QtCore.QRect(self.upper_left, self.lower_right).normalized())







class RubberbandEnhancedLabelMultiple(QtGui.QLabel):

    def __init__(self, parent=None):
        self.max_bboxes = 10
        QtGui.QLabel.__init__(self, parent)
        self.selections = [QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self) for i in range(self.max_bboxes)]
        self.active_bboxes = 0
        self.upper_left = [QtCore.QPoint() for i in range(self.max_bboxes)]
        self.lower_right = [QtCore.QPoint() for i in range(self.max_bboxes)]
        self.mode = [" " for i in range(self.max_bboxes)]

    def mousePressEvent(self, event):
        '''
            Mouse is pressed. If selection is visible either set dragging mode (if close to border) or hide selection.
            If selection is not visible make it visible and start at this point.
        '''
        if event.button() == QtCore.Qt.LeftButton:
            #self.mode = [" " for i in range(self.max_bboxes)]

            i = 0
            fl = 0
            min_i = 0
            min_sh = 10000
            string = "saaaas"
            position = QtCore.QPoint(event.pos())
            for i in range(self.active_bboxes):
                if self.selections[i].isVisible():
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
                    # else:
                    #     # clicked somewhere else, hide selection
                    #     #self.selection.hide()
                    #     self.selections[i].show()

                    #     pass
                    i += 1

          
            if min_sh < 50:
              
                self.mode[min_i] = string

            else:
                # no visible selection, start new selection
                self.upper_left[self.active_bboxes] = position
                self.lower_right[self.active_bboxes] = position
                self.mode[self.active_bboxes] = "drag_lower_right"
                self.selections[self.active_bboxes].show()

                #print (self.active_bboxes, self.selections[self.active_bboxes].isVisible())
                self.active_bboxes += 1


    def mouseMoveEvent(self, event):
        '''
            Mouse moved. If selection is visible, drag it according to drag mode.
        '''
        for i in range(self.active_bboxes):
            if self.selections[i].isVisible():
                # visible selection
                if self.mode[i] is "drag_lower_right":
                    self.lower_right[i] = QtCore.QPoint(event.pos())


                elif self.mode[i] is "drag_upper_left":
                    self.upper_left[i] = QtCore.QPoint(event.pos())
                # update geometry
                self.selections[i].setGeometry(QtCore.QRect(self.upper_left[i], self.lower_right[i]).normalized())


    def mouseReleaseEvent(self, event):
        self.mode = [" " for i in range(self.max_bboxes)]

    def reset_selected(self):
        for sel in self.selections:
            sel.hide()
        self.selections = [QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self) for i in range(self.max_bboxes)]
        self.active_bboxes = 0
        self.upper_left = [QtCore.QPoint() for i in range(self.max_bboxes)]
        self.lower_right = [QtCore.QPoint() for i in range(self.max_bboxes)]
        self.mode = [" " for i in range(self.max_bboxes)]


# app = QtGui.QApplication([])

# screen_pixmap = QtGui.QPixmap('data/1.jpg')#.grabWindow(app.desktop().winId())

# window = QtGui.QWidget()
# layout = QtGui.QVBoxLayout(window)
# label = RubberbandEnhancedLabelMultiple()
# label.setPixmap(screen_pixmap)
# layout.addWidget(label)
# geometry = app.desktop().availableGeometry()
# window.setFixedSize(500, 500)
# window.show()
# app.exec_()