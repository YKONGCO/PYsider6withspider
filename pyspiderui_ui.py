# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyspiderui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import pyiconqrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(342, 261)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(342, 311))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        iconThemeName = u"applications-office"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"pyicon/9348027.png", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1, 0, 341, 241))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cookielab = QLabel(self.widget)
        self.cookielab.setObjectName(u"cookielab")

        self.horizontalLayout.addWidget(self.cookielab)

        self.cookielabinput = QLineEdit(self.widget)
        self.cookielabinput.setObjectName(u"cookielabinput")

        self.horizontalLayout.addWidget(self.cookielabinput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.savepathlab = QLabel(self.widget)
        self.savepathlab.setObjectName(u"savepathlab")

        self.horizontalLayout_3.addWidget(self.savepathlab)

        self.savepathline = QLineEdit(self.widget)
        self.savepathline.setObjectName(u"savepathline")

        self.horizontalLayout_3.addWidget(self.savepathline, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ismysqllab = QLabel(self.widget)
        self.ismysqllab.setObjectName(u"ismysqllab")

        self.horizontalLayout_2.addWidget(self.ismysqllab)

        self.ismysql = QComboBox(self.widget)
        self.ismysql.addItem("")
        self.ismysql.addItem("")
        self.ismysql.setObjectName(u"ismysql")

        self.horizontalLayout_2.addWidget(self.ismysql, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.providebtn = QPushButton(self.widget)
        self.providebtn.setObjectName(u"providebtn")

        self.verticalLayout_2.addWidget(self.providebtn)

        self.state = QLabel(self.widget)
        self.state.setObjectName(u"state")

        self.verticalLayout_2.addWidget(self.state)

        self.startbtn = QPushButton(self.widget)
        self.startbtn.setObjectName(u"startbtn")

        self.verticalLayout_2.addWidget(self.startbtn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.outputtext = QTextBrowser(self.widget)
        self.outputtext.setObjectName(u"outputtext")

        self.verticalLayout_3.addWidget(self.outputtext)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyspider", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"\u770b\u4ec0\u4e48\u770b", None))
#endif // QT_CONFIG(tooltip)
        self.cookielab.setText(QCoreApplication.translate("MainWindow", u"cookie", None))
        self.cookielabinput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4e34\u65f6cookie", None))
        self.savepathlab.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.savepathline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u8def\u5f84", None))
        self.ismysqllab.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528mysql\u6570\u636e\u5e93", None))
        self.ismysql.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.ismysql.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))

        self.providebtn.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u53c2\u6570", None))
        self.state.setText(QCoreApplication.translate("MainWindow", u"\u672a\u63d0\u4ea4\u53c2\u6570", None))
        self.startbtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u722c\u866b", None))
        self.outputtext.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u672a\u8fd0\u884c", None))
    # retranslateUi

