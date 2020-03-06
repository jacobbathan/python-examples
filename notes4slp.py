from swampy.Gui import *

g = Gui()
g.title('Gui')
g.mainloop()

button = g.bu(text='Press me.')
label = g.la(text='Press the button')

def make_label():
    g.la(text='Thank you')

button2 = g.bu(text='No, press me!', command=make_label)

# canvas widgets
canvas = g.ca(width=500, height=500)
# width and height are dimensions in pixels
canvas.config(bg='white')
# value of bg is a string that names a color
# shapes on canvas are called items
item = canvas.circle([0,0], 100, fill='red')
# first arg is a coordinate pair, that specifices the center of the circle
# 2nd arg is radius
item.config(fill='yellow', outline='orange', width=10)
# coordinate sequences
canvas.rectangle([0,0], [200, 200], fill='blue', outline='orange', width=10)
# oval takes a bounding box and draws an oval within rectangle
canvas.oval([[0, 0], [200, 100]], outline='orange', width=10)
canvas.line([[0, 100], [100, 200], [200, 100]], width=10)
# polygon takes same args, but draws the last leg of polygon and fills
canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='red', outline='orange', width=10)
# widgets
# en creates new entry
entry = g.en(text='default text')
# te grecreates text widget
text = g.te(width=100, height=5)
text.insert(END, 'A line of text')
text.insert(1.1, 'nother')

# packing widgets
class SimpleTurtleWorld(TurtleWorld):
    def setup(self):
        """create the GUI"""

        self.row()

        self.canvas = self.ca(width=400, height=400, bg='white')

        # right frame
        self.col()

        # buttons
        self.gr(cols=2)
        self.bu(text='Print canvas', command=self.canvas.dump)
        self.bu(text='Quit', command=self.quit)
        self.bu(text='Make Turtle', command=self.make_turtle)
        self.bu(text='Clear', command=self.clear)
        self.endgr()


        # run file
        self.row([0,1], pady=30)
        self.bu(text='Run file', command=self.run_file)
        self.en_file = self.en(text='snowflake.py', width=5)
        self.endrow()

        # run this code
        self.te_code = self.te(width=25, height=10)
        self.te_code.insert(END, 'world.clear()\n')
        self.te_code.insert(END, 'bob = Turtle(world)\n')

        self.bu(text='Run code', command=self.run_text)

        # leave the column open to accomodate Turtle control panels
        #self.endcol()


if __name__ == '__main__':
    world = SimpleTurtleWorld()
    world.inter = Interpreter(world, globals())
    world.mainloop()

# arranging widgets in a GUI is called packing

# menu and callables
g = Gui()
g.title('')
g.la('Select a color:')
colors = ['red', 'green', 'blue']
mb = g.mb(text=colors[0])

def set_color(color):
    print color
    mb.config(text=color)

for color in colors:
    g.mi(mb, text=color, command=Callable(set_color, color))

g.mainloop()

#binding
class Draggable(Item):
    """A Canvas Item with bindings for dragging and dropping.

    Given an item, Draggable(item) creates bindings and returns
    a Draggable object with the same canvas and tag as the original.
    """
    def __init__(self, item):
        self.canvas = item.canvas
        self.tag = item.tag
        self.bind('<ButtonPress-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.drop)

    # the following event handlers take an event object as a parameter

    def select(self, event):
        """Selects this item for dragging."""
        self.dragx = event.x
        self.dragy = event.y

        self.fill = self.cget('fill')
        self.config(fill='orange')
        
    def drag(self, event):
        """Move this item using the pixel coordinates in the event object."""
        # see how far we have moved
        dx = event.x - self.dragx
        dy = event.y - self.dragy

        # save the current drag coordinates
        self.dragx = event.x
        self.dragy = event.y

        # move the item 
        self.move(dx, dy)

    def drop(self, event):
        """Drops this item."""
        self.config(fill=self.fill)


# create the Gui and the Canvas
g = Gui()
ca = g.ca(width=500, height=500, bg='white')

def make_circle(event):
    """Makes a circle item at the location of a button press."""
    pos = ca.canvas_coords([event.x, event.y])
    item = ca.circle(pos, 5, fill='red')
    item = Draggable(item)

ca.bind('<ButtonPress-3>', make_circle)

def make_text(event=None):
    """Pressing Return in the Entry makes a text item."""
    text = en.get()
    item = ca.text([0,0], text)
    item = Draggable(item)


g.row([0,1])
bu = g.bu('Make text item:', make_text)
en = g.en()
en.bind('<Return>', make_text)

g.mainloop()
