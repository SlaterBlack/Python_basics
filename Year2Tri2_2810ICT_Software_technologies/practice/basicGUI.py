import TKinter

class myGui (wx.Frame):
    def __init__ (self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent=parent
        self.initialise()
    def initialise(self):
        pnl = wx.Panel(self)
        st = wx.Statictext(pnl,lable = "Helloo World")
        fnt = st.GetFont()
        fnt.PointSize +=10
        st.SetFont(fnt)
        fnt = fnt.Bold()
        self.show(True)

app = wx.App()
gui = wx.Frame(None,0, title= "hello World")
app.MainLoop ()
