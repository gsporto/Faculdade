import os
import wx
import wx.html2 

class MyApp(wx.App):
    def __init__(self, path_abs):
        super().__init__()
        self.InitBrowser(path_abs)

    def InitBrowser(self, path_abs):
        webBrowser=WebFrame(None, path_abs, "My Web App", pos=(100,100), size=(800, 600))
        webBrowser.Show()

########################################################################################################################

class WebFrame(wx.Frame):
    def __init__(self, parent, path_abs, title, pos, size):
        super().__init__(parent, title=title, pos=pos, size=size)
        self.browser=wx.html2.WebView.New(self)
        self.browser.LoadURL(path_abs)
        self.navBar=NavBar(self, self.browser)

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.navBar, 0, wx.EXPAND)
        sizer.Add(self.browser, 1, wx.EXPAND)
        self.SetSizer(sizer)

########################################################################################################################

class NavBar(wx.Panel):
    def __init__(self, parent, browser):
        super().__init__(parent)
        self.browser=browser
        self.url=wx.TextCtrl(parent=self, style=wx.TE_PROCESS_ENTER)
        self.url.SetHint("Enter URL Address")
        bt_back=wx.Button(self, style=wx.BU_EXACTFIT)
        bt_back.Bitmap=wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_TOOLBAR)
        bt_fore = wx.Button(self, style=wx.BU_EXACTFIT)
        bt_fore.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(bt_back, 0, wx.ALL, 5)
        sizer.Add(bt_fore, 0, wx.ALL, 5)
        sizer.Add(self.url, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def onEnter(self, event):
        self.browser.LoadURL(self.url.Value)

    def goBack(self, event):
        event.Enable(self.browser.CanGoBack())
        self.browser.GoBack()

    def goForward(self, event):
        event.Enable(self.browser.CanGoForward)
        self.browser.GoForward()

########################################################################################################################

if __name__ == "__main__":
    path_sys = os.getcwd().replace("\\", "/")
    path_abs = "file:/%s/%s" % (path_sys, "Html_Video/Pagina1.html")
    print("path_abs=%s\n" % path_abs)
    url="www.google.com"

    app=MyApp(path_abs)
    app.MainLoop()
