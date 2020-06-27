import os
import wx
import wx.html2

class MyBrowser(wx.Dialog):
  def __init__(self, *args, **kwds):
    wx.Dialog.__init__(self, *args, **kwds)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.browser = wx.html2.WebView.New(self)
    sizer.Add(self.browser, 1, wx.EXPAND, 10)
    self.SetSizer(sizer)
    self.SetSize((700, 700))
    self.Bind(wx.EVT_CLOSE, self.on_close)

  def on_close(self, event):
    if self.__exit__:
        print("Sair...")
        self.Destroy()

if __name__ == '__main__':
  path_sys=os.getcwd().replace("\\","/")
  path_abs = "file:/%s/%s" % (path_sys, "Html_Report/Nota_Fiscal.html")
  print("path_abs=%s\n" % path_abs)

  app = wx.App()
  dialog = MyBrowser(None, -1)
  dialog.browser.LoadURL(path_abs)
  dialog.Show()
  ## app.SetExitOnFrameDelete(True)
  app.MainLoop()
