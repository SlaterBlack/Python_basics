import wx

class myGui (wx.Frame):
    def __init__ (self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        #   Adding text 
        self.s1 = wx.StaticText(pnl,label = "Hello World")      #   insert static text
        self.s2 = wx.StaticText(pnl,label = "Hello World")      #   insert static text
        self.s3 = wx.StaticText(pnl,label = "Hello World")      #   insert static text
        self.s4 = wx.StaticText(pnl,label = "Hello World")      #   insert static text
        self.s5 = wx.StaticText(pnl,label = "Hello World")      #   insert static text
        self.s6 = wx.StaticText(pnl,label = "Hello World")      #   insert static text

        self.s1.SetPosition((10, 10))
        self.s2.SetPosition((10, 30))
        self.s3.SetPosition((10, 50))
        self.s4.SetPosition((10, 70))
        self.s5.SetPosition((10, 90))
        self.s6.SetPosition((10, 110))


        fnt = self.s1.GetFont()                                 #   Obtain font of text stored in "st" and store it in order to change it
        fnt.PointSize +=10                                      #   Change font size
        fnt = fnt.Bold()                                        #   Make font bold
        self.s1.SetFont(fnt)                                    #   Set font setting (activate previous changes)
        self.s1.SetLabel("Some new text")

        #   frame customising
        self.Center()                                           #   Place frame in centre of screen
        pnl.SetBackgroundColour(wx.Colour(151,97,184))          #   Change frame background colour
        

        
        #   Adding a button
        btn = wx.Button(pnl,pos=(25,200),label="Don't press this button")
        self.Bind(wx.EVT_BUTTON,self.onButton,btn)

        #   Adding a menu
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.onExit, exitItem)
        
        self.Show(True)

    def onButton(self,event):
        wx.MessageBox("I said not to press the button")
        self.updateText("Sad World")

    def onExit(self,event):
        self.Close(True)
        pass

    def updateText(self,newText):
        self.st.SetLabel('You bitch')


if __name__ == "__main__": 
    app = wx.App()
    frame = myGui(None,-1, title= "Hello World")
    app.MainLoop () 