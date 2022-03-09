from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, Rectangle
import random

grades = ["B+", "B+", "A-", "A", "A-", "A", "A-", "A-"]
count = 140

class GpaCircularProgressBar(ProgressBar):

    def _calculateavg():
        global avg
        global countA
        global countAminus
        global countBplus
        global countB
        global countBminus
        global countCplus
        global countC
        global countCminus
        global countDplus
        global countD
        global countDminus
        global countF
        
        countA = grades.count("A")
        countAminus = grades.count("A-")
        countBplus = grades.count("B+")
        countB = grades.count("B")
        countBminus = grades.count("B-")
        countCplus = grades.count("C+")
        countC = grades.count("C")
        countCminus = grades.count("C-")
        countDplus = grades.count("D+")
        countD = grades.count("D")
        countDminus = grades.count("D-")
        countF = grades.count("F")

        if countA > countAminus and countA > countBplus and countA > countB and countA > countBminus and countA > countCplus and countA > countC and countA > countCminus and countA > countDplus and countA > countD and countA > countDminus and countA > countF:
            avg = " A "        
        elif countAminus > countA and countAminus > countBplus and countAminus > countB and countAminus > countBminus and countAminus > countCplus and countAminus > countC and countAminus > countCminus and countAminus > countDplus and countAminus > countD and countAminus > countDminus and countAminus > countF:
            avg = " A- "
        elif countBplus > countA and countBplus > countAminus and countBplus > countB and countBplus > countBminus and countBplus > countCplus and countBplus > countC and countBplus > countCminus and countBplus > countDplus and countBplus > countD and countBplus > countDminus and countBplus > countF:
            avg = " B+ "
        elif countB > countA and countB > countAminus and countB > countBplus and countB > countBminus and countB > countCplus and countB > countC and countB > countCminus and countB > countDplus and countB > countD and countB > countDminus and countB > countF:
            avg = " B "
        elif countBminus > countA and countBminus > countAminus and countBminus > countBplus and countBminus > countB and countBminus > countCplus and countBminus > countC and countBminus > countCminus and countBminus > countDplus and countBminus > countD and countBminus > countDminus and countBminus > countF:
            avg = " B- "
        elif countCplus > countA and countCplus > countAminus and countCplus > countBplus and countCplus > countB and countCplus > countBminus and countCplus > countC and countCplus > countCminus and countCplus > countDplus and countCplus > countD and countCplus > countDminus and countCplus > countF:
            avg = " C+ "
        elif countC > countA and countC > countAminus and countC > countBplus and countC > countB and countC > countBminus and countC > countCplus and countC > countCminus and countC > countDplus and countC > countD and countC > countDminus and countC > countF:
            avg = " C "
        elif countCminus > countA and countCminus > countAminus and countCminus > countBplus and countCminus > countB and countCminus > countBminus and countCminus > countCplus and countCminus > countC and countCminus > countDplus and countCminus > countD and countCminus > countDminus and countCminus > countF:
            avg = " C- "
        elif countDplus > countA and countDplus > countAminus and countDplus > countBplus and countDplus > countB and countDplus > countBminus and countDplus > countCplus and countDplus > countC and countDplus > countCminus and countDplus > countD and countDplus > countDminus and countDplus > countF:
            avg = " D+ "
        elif countD > countA and countD > countAminus and countD > countBplus and countD > countB and countD > countBminus and countD > countCplus and countD > countC and countD > countCminus and countD > countDplus and countD > countDminus and countD > countF:
            avg = " D "
        elif countDminus > countA and countDminus > countAminus and countDminus > countBplus and countDminus > countB and countDminus > countBminus and countDminus > countCplus and countDminus > countC and countDminus > countCminus and countDminus > countDplus and countDminus > countD and countDminus > countF:
            avg = " D- "
        elif countF > countA and countF > countAminus and countF > countBplus and countF > countB and countF > countBminus and countF > countCplus and countF > countC and countF > countCminus and countF > countDplus and countF > countD and countF > countDminus:
            avg = " F "

    _calculateavg()

    def _calculategpa():
        global gpa
        gpa = ((countA*4)+(countAminus*4)+(countBplus*3)+(countB*3)+(countBminus*3)+(countCplus*2)+(countC*2)+(countCminus*2)+(countDplus*1)+(countD*1)+(countDminus*1)+(countF*0))/8
    _calculategpa()

    def __init__(self, **kwargs):
        super(GpaCircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text=f"{gpa}\nGPA", font_size=self.thickness, halign='center')

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:
            
            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(.16, .0941, .3412)
            Ellipse(pos=self.pos, size=self.size)

            if gpa < 2.0:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .15, .10)
            elif gpa >= 2.0 and gpa < 3.0:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .9961, 0)
            elif gpa >= 3.0 and gpa <= 4.0:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(.15, .85, .10)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))

            # Draw the inner circle (colour should be equal to the background)
            Color(.2157, .1686, .549)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))

            # Center and draw the progress text
            Color(1, 1, 1, 1)
            #added pos[0]and pos[1] for centralizing label text whenever pos_hint is set
            Rectangle(texture=self.label.texture, size=self.texture_size,
                  pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))


    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = f"{gpa}\nGPA"
        self.refresh_text()

        # Draw all the elements
        self.draw()


class CountCircularProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super(CountCircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text=f"{count}\nLeft", font_size=self.thickness, halign='center')

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:
            
            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(.16, .0941, .3412)
            Ellipse(pos=self.pos, size=self.size)

            if ((count/200)*100 )*100 <= 100/3:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .15, .10)
            elif (count/200)*100  >= 100/2.99999999 and (count/200)*100  <= 100/1.5:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .9961, 0)
            elif (count/200)*100  >= 100/1.49999999 and (count/200)*100  <= 100:
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(.15, .85, .10)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))

            # Draw the inner circle (colour should be equal to the background)
            Color(.2157, .1686, .549)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))

            # Center and draw the progress text
            Color(1, 1, 1, 1)
            #added pos[0]and pos[1] for centralizing label text whenever pos_hint is set
            Rectangle(texture=self.label.texture, size=self.texture_size,
                  pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))


    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = f"{count}\nLEFT"
        self.refresh_text()

        # Draw all the elements
        self.draw()


class AvgCircularProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super(AvgCircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text=f"{avg}\nAVG", font_size=self.thickness, halign='center')

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:
            
            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(.16, .0941, .3412)
            Ellipse(pos=self.pos, size=self.size)

            if avg == " F " or avg == " D- " or avg == " D " or avg == " D+ ":
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .15, .10)
            elif avg == " C- " or avg == " C " or avg == " C+ " or avg == " B- ":
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(1, .9961, 0)
            elif avg == " B " or avg == " B+ " or avg == " A- " or avg == " A ":
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
                Color(.15, .85, .10)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))

            # Draw the inner circle (colour should be equal to the background)
            Color(.2157, .1686, .549)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))

            # Center and draw the progress text
            Color(1, 1, 1, 1)
            #added pos[0]and pos[1] for centralizing label text whenever pos_hint is set
            Rectangle(texture=self.label.texture, size=self.texture_size,
                  pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))


    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = f"{avg}\nAVG"
        self.refresh_text()

        # Draw all the elements
        self.draw()

