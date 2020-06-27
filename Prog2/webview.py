from PyQt5 import QtCore, QtGui, QtWidgets
#froPyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWebEngineWidgets import *



class MyTest(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super(MyTest, self).__init__(parent)

    # def createWindow(self,wintype):
        # self.webView = MyTest()
        # self.webView.show()

        # return super(MyTest, self).createWindow(wintype)


class Ui_Dialog19(object):
    def setupUi(self, Dialog19,var_user,var_pass):
        Dialog19.setObjectName("Dialog19")
        Dialog19.resize(800, 600)
        Dialog19.setWindowFlags(Dialog19.windowFlags() |
        QtCore.Qt.WindowMinimizeButtonHint |
        QtCore.Qt.WindowMaximizeButtonHint)
        self.var_user = var_user
        self.var_pass = var_pass
        self.centralwidget = QtWidgets.QWidget(Dialog19)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = MyTest(self)
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(Dialog19)
        self.statusbar.setObjectName("statusbar")
        self.setLayout(self.gridLayout)


        self.webView.installEventFilter(self)
        self.webView.setUrl(QtCore.QUrl("https://ww1.jeppesen.com/icharts/"))
        self.retranslateUi(Dialog19)
        QtCore.QMetaObject.connectSlotsByName(Dialog19)






        self.webView.loadFinished.connect(self._on_load_finished)


    def showEvent(self,event):
        # self.webView.setUrl(QtCore.QUrl("https://ww1.jeppesen.com/icharts/"))
        pass

    def _on_load_finished(self):
        self.webView.page().toHtml(self.Callable)

        # self.webView.page().settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)

    def Callable(self, html_str):
        self.html = html_str


        self.webView.page().runJavaScript("document.getElementsByName('login-username')[0].value='%s';"%(self.var_user))
        self.webView.page().runJavaScript("document.getElementsByName('login-password')[0].value='%s';"%(self.var_pass))
        self.webView.page().runJavaScript("document.getElementById('loginSubmit').click();")
        self.webView.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.HyperlinkAuditingEnabled, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
        self.webView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)




    def retranslateUi(self, Dialog19):
        _translate = QtCore.QCoreApplication.translate
        Dialog19.setWindowTitle(_translate("Dialog19", "Eva air insider"))