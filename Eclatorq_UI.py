# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 580, 600, 110))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setAccessibleDescription("")
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, 0, 120, 110))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.y_Button = QtWidgets.QPushButton(self.groupBox_2)
        self.y_Button.setGeometry(QtCore.QRect(10, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.y_Button.setFont(font)
        self.y_Button.setCheckable(False)
        self.y_Button.setChecked(False)
        self.y_Button.setAutoDefault(False)
        self.y_Button.setDefault(False)
        self.y_Button.setObjectName("y_Button")
        self.yd_Button = QtWidgets.QPushButton(self.groupBox)
        self.yd_Button.setGeometry(QtCore.QRect(130, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.yd_Button.setFont(font)
        self.yd_Button.setObjectName("yd_Button")
        self.save_button = QtWidgets.QPushButton(self.groupBox)
        self.save_button.setGeometry(QtCore.QRect(370, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.save_button.setFont(font)
        self.save_button.setCheckable(False)
        self.save_button.setObjectName("save_button")
        self.camera_id = QtWidgets.QLineEdit(self.groupBox)
        self.camera_id.setGeometry(QtCore.QRect(240, 30, 50, 60))
        self.camera_id.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_id.setObjectName("camera_id")
        self.modereset = QtWidgets.QPushButton(self.groupBox)
        self.modereset.setGeometry(QtCore.QRect(480, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.modereset.setFont(font)
        self.modereset.setCheckable(False)
        self.modereset.setObjectName("modereset")
        self.QRcheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.QRcheckBox.setGeometry(QtCore.QRect(300, 70, 51, 20))
        self.QRcheckBox.setText("")
        self.QRcheckBox.setObjectName("QRcheckBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(300, 30, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pic_g = QtWidgets.QGroupBox(self.centralwidget)
        self.pic_g.setGeometry(QtCore.QRect(20, 20, 760, 560))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pic_g.setFont(font)
        self.pic_g.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pic_g.setAutoFillBackground(True)
        self.pic_g.setTitle("")
        self.pic_g.setFlat(False)
        self.pic_g.setCheckable(False)
        self.pic_g.setObjectName("pic_g")
        self.graphicsView = QtWidgets.QGraphicsView(self.pic_g)
        self.graphicsView.setGeometry(QtCore.QRect(50, 50, 660, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.last_button = QtWidgets.QPushButton(self.pic_g)
        self.last_button.setGeometry(QtCore.QRect(0, 220, 30, 140))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.last_button.setFont(font)
        self.last_button.setObjectName("last_button")
        self.next_button = QtWidgets.QPushButton(self.pic_g)
        self.next_button.setGeometry(QtCore.QRect(730, 220, 30, 140))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.label_2 = QtWidgets.QLabel(self.pic_g)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 470, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.type_comboBox = QtWidgets.QComboBox(self.pic_g)
        self.type_comboBox.setGeometry(QtCore.QRect(610, 20, 80, 22))
        self.type_comboBox.setObjectName("type_comboBox")
        self.label_5 = QtWidgets.QLabel(self.pic_g)
        self.label_5.setGeometry(QtCore.QRect(540, 20, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(870, 20, 340, 580))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.show_text = QtWidgets.QTextBrowser(self.groupBox_3)
        self.show_text.setEnabled(True)
        self.show_text.setGeometry(QtCore.QRect(30, 70, 280, 390))
        self.show_text.setObjectName("show_text")
        self.aug_num_text = QtWidgets.QLineEdit(self.groupBox_3)
        self.aug_num_text.setGeometry(QtCore.QRect(30, 30, 71, 31))
        self.aug_num_text.setAlignment(QtCore.Qt.AlignCenter)
        self.aug_num_text.setObjectName("aug_num_text")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.trainm_Button = QtWidgets.QPushButton(self.groupBox_3)
        self.trainm_Button.setGeometry(QtCore.QRect(140, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.trainm_Button.setFont(font)
        self.trainm_Button.setCheckable(False)
        self.trainm_Button.setObjectName("trainm_Button")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 470, 341, 110))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAcceptDrops(False)
        self.groupBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.train_Button = QtWidgets.QPushButton(self.groupBox_4)
        self.train_Button.setGeometry(QtCore.QRect(120, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.train_Button.setFont(font)
        self.train_Button.setCheckable(False)
        self.train_Button.setObjectName("train_Button")
        self.trainy_Button = QtWidgets.QPushButton(self.groupBox_4)
        self.trainy_Button.setGeometry(QtCore.QRect(230, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.trainy_Button.setFont(font)
        self.trainy_Button.setCheckable(False)
        self.trainy_Button.setObjectName("trainy_Button")
        self.add_Button = QtWidgets.QPushButton(self.groupBox_4)
        self.add_Button.setGeometry(QtCore.QRect(10, 30, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.add_Button.setFont(font)
        self.add_Button.setCheckable(False)
        self.add_Button.setObjectName("add_Button")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(630, 610, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.close_button.setFont(font)
        self.close_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_button.setObjectName("close_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 610, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 610, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.typemodel = QtWidgets.QLineEdit(self.centralwidget)
        self.typemodel.setGeometry(QtCore.QRect(890, 640, 70, 20))
        self.typemodel.setObjectName("typemodel")
        self.yolomodel = QtWidgets.QLineEdit(self.centralwidget)
        self.yolomodel.setGeometry(QtCore.QRect(1010, 640, 70, 20))
        self.yolomodel.setObjectName("yolomodel")
        self.open_dir_Button = QtWidgets.QPushButton(self.centralwidget)
        self.open_dir_Button.setGeometry(QtCore.QRect(1110, 610, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setUnderline(False)
        self.open_dir_Button.setFont(font)
        self.open_dir_Button.setCheckable(False)
        self.open_dir_Button.setChecked(False)
        self.open_dir_Button.setDefault(False)
        self.open_dir_Button.setFlat(False)
        self.open_dir_Button.setObjectName("open_dir_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEngineerMode = QtWidgets.QAction(MainWindow)
        self.actionEngineerMode.setCheckable(True)
        self.actionEngineerMode.setShortcutVisibleInContextMenu(True)
        self.actionEngineerMode.setObjectName("actionEngineerMode")
        self.menuSetting.addAction(self.actionEngineerMode)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Control Pannl"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Open Camera"))
        self.y_Button.setText(_translate("MainWindow", "Lock Classify"))
        self.y_Button.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.yd_Button.setText(_translate("MainWindow", "Check Reset"))
        self.yd_Button.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.save_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.camera_id.setText(_translate("MainWindow", "0"))
        self.modereset.setText(_translate("MainWindow", "Mode Reset"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Use QR <br/>Code </span></p></body></html>"))
        self.last_button.setText(_translate("MainWindow", "<"))
        self.last_button.setShortcut(_translate("MainWindow", "Left"))
        self.next_button.setText(_translate("MainWindow", ">"))
        self.next_button.setShortcut(_translate("MainWindow", "Right"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Type :</p><p><br/></p></body></html>"))
        self.aug_num_text.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "aug_num"))
        self.trainm_Button.setText(_translate("MainWindow", "Optimization Algorithmain"))
        self.trainm_Button.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Class Model Train"))
        self.train_Button.setText(_translate("MainWindow", "Train"))
        self.train_Button.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.trainy_Button.setText(_translate("MainWindow", "Retrain YOLO"))
        self.trainy_Button.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.add_Button.setText(_translate("MainWindow", "Add Type"))
        self.add_Button.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.close_button.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Type Model</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>YOLO Model</p></body></html>"))
        self.typemodel.setText(_translate("MainWindow", "keras"))
        self.yolomodel.setText(_translate("MainWindow", "best"))
        self.open_dir_Button.setText(_translate("MainWindow", "OpenPath"))
        self.open_dir_Button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionEngineerMode.setText(_translate("MainWindow", "Engineer Mode\n"
""))
        self.actionEngineerMode.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
