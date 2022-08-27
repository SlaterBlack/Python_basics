import wx

class myGui (wx.Frame):
    def __init__ (self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        
        self.initialise()

    def initialise(self):
        self.panel1 = wx.Panel(self)
        self.panel1.SetSize(300, 100)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 255))

        self.Show(True)
    
    def updateText(self,newText):
        pass

if __name__ == "__main__":
    app = wx.App()
    frame = myGui(None,-1, title= "Hello World")
    app.MainLoop () 