import wx

class myGui (wx.Frame):
    def __init__ (self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        #text 
        st = wx.StaticText(pnl,label = "Hello World")   #insert static text
        fnt = st.GetFont()                              # Obtain font of text stored in "st" and store it in order to change it
        fnt.PointSize +=10                              # Change font size
        fnt = fnt.Bold()                                # Make font bold
        st.SetFont(fnt)                                 # Set font setting (activate previous changes)
        
        #frame
        self.Center()                                   # Place frame in centre of screen
       
        
        btn = wx.Button(pnl, l
        
        
        
        
        
        able "Don't press this this button")

        self.Show(True)
    
    def updateText(self,newText):
        pass

if __name__ == "__main__":
    app = wx.App()
    frame = myGui(None,-1, title= "Hello World")
    app.MainLoop () 