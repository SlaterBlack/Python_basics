import wx
import wx.grid as grid

class myGui (wx.Frame):
    def __init__ (self,parent,id,title):
        super(myGui, self).__init__(parent,id,title)
        self.parent = parent
       
        self.initialise()

    def initialise(self):
        #   frame customising
        self.Center()                                                   #   Place frame in centre of screen
        self.panel1 = wx.Panel(self)
        self.panel1.SetSize(300, 100)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 255))

         #   Adding text 
        self.st = wx.StaticText(self.panel1,label = "Hello World")      #   Insert static text
        fnt = self.st.GetFont()                                         #   Obtain font of text stored in "st" and store it in order to change it
        fnt.PointSize +=10                                              #   Change font size
        fnt = fnt.Bold()                                                #   Make font bold
        self.st.SetFont(fnt)                                            #   Set font setting (activate previous changes)
        self.st.SetLabel("Some new text")

        #   Adding a button
        btn = wx.Button(self.panel1,pos=(25,100),label="Don't press this button")
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

        #   create grid
        mygrid = grid.Grid(self)
        mygrid.CreateGrid(5,3)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid,1,wx.EXPAND)
        self.SetSizer(sizer)

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
    frame = myGui(None,-1, title= "Lets Practice a Bit")
    app.MainLoop () 