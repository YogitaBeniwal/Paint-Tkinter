from tkinter import *
from tkinter import ttk,colorchooser
 
class main:
    bg= ""
    fg= ""
    def __init__(self,master):
        self.master = master
        #Color fg is the canvas brush colour
        self.color_fg = 'white'
        #Color bg is the background colour
        self.color_bg = 'white'
        #Starting positions of drawing set to none
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.eraser_mode = False
        self.drawWidgets()
        self.change_bg()

        #Drawing a line of the motion of mouse and stop on realising the mouse
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)

    #This function will be used to paint a line and value of self.old_x and y will change on releasing the mouse
    def paint(self,e):
        global bg,fg
        if self.old_x and self.old_y:
          #self.c.create_line(self.old_x, self.old_y, e.x,e.y, width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
          if not self.eraser_mode:
                self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg, capstyle=ROUND, smooth=True)

                fg = self.color_fg
          else:
                # If eraser mode is active, draw with transparent white to erase
                self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=bg, capstyle=ROUND, smooth=True)  #NEW
      
        self.old_x = e.x
        self.old_y = e.y

    #Set self.old_x and y to none
    def reset(self,e):    
        self.old_x = None
        self.old_y = None       

    #Setting width to position 'e'
    def changeW(self,e): 
        self.penwidth = e

    #Clear function to clear screen
    def clear(self):
        self.c.delete(ALL)

    #Erase function to erase drawing
    def eraser(self):
        self.eraser_mode = not self.eraser_mode

    def change_fg(self):  #changing the pen color
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]
  
    def change_bg(self):  #changing the background colour canvas
        global bg  
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        bg = self.color_bg 

    #Set all widgets to respective functions
    def drawWidgets(self):
        global bg
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Size',font=('arial 12')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 30,command=self.changeW,orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=10)
        self.controls.pack(side=LEFT)
        
        self.c = Canvas(self.master, width=500,height=500,bg=self.color_bg)
        self.c.pack(fill=BOTH,expand=True)

        #Add menu on top for choosing colour and resetting
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Choose Colours',menu=colormenu)
        
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)

        optionmenu1 = Menu(menu)
        menu.add_cascade(label='Erase',menu=optionmenu1)
        optionmenu1.add_command(label='Erase Pen',command=self.eraser)
        
        optionmenu = Menu(menu)
        menu.add_cascade(label='Reset and Exit',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy)

#Initializing the app     
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Paint')
    root.mainloop()
