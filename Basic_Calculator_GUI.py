import wx

class GameGUI (wx.Frame):
	def __init__(self, parent, title ):
		wx.Frame.__init__(self,parent,title=title,size=(540,280))
		self.initialise()

	def initialise(self):
		self.number = 4
		print(self.number)
		pnl = wx.Panel(self)
		rows = wx.BoxSizer(wx.VERTICAL)
		head = wx.StaticText(pnl, label="Calculator")
		font = head.GetFont() #get the standard font
		font.PointSize += 10 #increases the size
		font = font.Bold() #makes it bold
		head.SetFont(font) #resets the font
		rows.Add(head, 1, wx.ALIGN_CENTER|wx.BOTTOM, border=2)
		pnl.SetBackgroundColour(wx.Colour(70, 171, 159))
		self.ansText = wx.StaticText(pnl, label=" ", style=wx.ALIGN_CENTRE_HORIZONTAL)
		self.ansText.SetBackgroundColour(wx.Colour(255,255,255,255))
		self.ansText.SetMinSize((200,50))
		font.PointSize+=5
		self.ansText.SetFont(font)
		rows.Add(self.ansText,1,wx.ALIGN_CENTER|wx.BOTTOM, border=2)
		
		numSize = wx.BoxSizer(wx.HORIZONTAL)
		self.num1 = wx.TextCtrl(pnl)
		self.num2 = wx.TextCtrl(pnl)
		numSize.Add(self.num1,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		numSize.Add(self.num2,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		rows.Add(numSize, 2, wx.ALIGN_CENTER)
		
		butSize = wx.BoxSizer(wx.HORIZONTAL)
		addButton = wx.Button(pnl, label="+")
		subButton = wx.Button(pnl, label="-")
		mulButton = wx.Button(pnl, label="*")
		divButton = wx.Button(pnl, label="/")
		clrButton = wx.Button(pnl, label="Clear")
		butSize.Add(addButton,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		butSize.Add(subButton,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		butSize.Add(mulButton ,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		butSize.Add(divButton,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		butSize.Add(clrButton,1,wx.ALIGN_CENTER|wx.RIGHT, border = 10)
		rows.Add(butSize, 1, wx.ALIGN_CENTER)
		
		self.Bind(wx.EVT_BUTTON,self.onAdd, addButton)
		self.Bind(wx.EVT_BUTTON,self.onSub, subButton)
		self.Bind(wx.EVT_BUTTON,self.onMul, mulButton)
		self.Bind(wx.EVT_BUTTON,self.onDiv, divButton)
		self.Bind(wx.EVT_BUTTON,self.onClear, clrButton)
		
		pnl.SetSizerAndFit(rows)
		self.Show(True)
		
	def onClear(self, event):
		self.num1.Value = ""
		self.num2.Value = ""
		self.ansText.Label = ""
		
	def onAdd(self, event):
		try: 
			i1 = int(self.num1.Value)
			i2 = int(self.num2.Value)
			a = i1+i2
			self.ansText.Label = str(a)
			self.num1.Value = ""
			self.num2.Value = ""

		except ValueError:
			wx.MessageBox("Please enter 2 integer values")
			self.num1.Value = ""
			self.num2.Value = ""
			self.ansText.Label = ""
			
	def onSub(self, event):
		try: 
			i1 = int(self.num1.Value)
			i2 = int(self.num2.Value)
			a = i1-i2
			self.ansText.Label = str(a)
			self.num1.Value = ""
			self.num2.Value = ""

		except ValueError:
			wx.MessageBox("Please enter 2 integer values")
			self.num1.Value = ""
			self.num2.Value = ""
			self.ansText.Label = ""
			
	def onMul(self, event):
		try: 
			i1 = int(self.num1.Value)
			i2 = int(self.num2.Value)
			a = i1*i2
			self.ansText.Label = str(a)
			self.num1.Value = ""
			self.num2.Value = ""

		except ValueError:
			wx.MessageBox("Please enter 2 integer values")
			self.num1.Value = ""
			self.num2.Value = ""
			self.ansText.Label = ""
			
	def onDiv(self, event):
		try: 
			i1 = int(self.num1.Value)
			i2 = int(self.num2.Value)
			a = i1//i2
			self.ansText.Label = str(a)
			self.num1.Value = ""
			self.num2.Value = ""

		except ValueError:
			wx.MessageBox("Please enter 2 integer values")
			self.num1.Value = ""
			self.num2.Value = ""
			self.ansText.Label = ""
		except ZeroDivisionError:
			wx.MessageBox("Cannot divide by 0")
			self.num1.Value = ""
			self.num2.Value = ""
			self.ansText.Label = ""
			
app = wx.App()
frame = GameGUI(None, "Calculator")
app.MainLoop()