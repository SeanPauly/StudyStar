###################modules###################
from kivy.clock import Clock
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen
import time
from kivy.uix.popup import Popup
import pytesseract
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.properties import ObjectProperty
try:
    from PIL import Image
except ImportError:
    from PIL import Image
from kivymd.uix.button import MDFlatButton
from plyer import email
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import json
import webbrowser
from Extra_Widgets.circularprogressbar import gpa, avg, count
from kivy.uix.screenmanager import FadeTransition
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.lang.builder import Builder
import socketio
from kivy import Config
###################size###################
Window.size = (400, 700)
__version__ = "0.0.1"
Config.set('graphics', 'multisamples', '0')

###################MDLINKS###################
'''
## Links

- [Repo](https://github.com/SeanPauly/StudyStar "<project-name> Repo")

- [Live](<Homepage url> "Coming Soon...")

- [Bugs](https://github.com/SeanPauly/StudyStar/issues "Issues Page")
'''



#############################################
class SoSDialog(MDDialog):
    pass

class SoSDialog(MDDialog):
    pass


class CustomDialog(MDDialog):
    pass

class Content(BoxLayout):
    pass

class IMG(MDCard):
    pass

class CustomCancelButton(MDFlatButton):
    pass

class CustomSendButton(MDFlatButton):
    pass

#############################################

###################scripts###################
from WindowManager.WindowManager import *


###################SplashScreen###################
class SplashScreen(Screen):
    """This class will show the Splash screen of StudyStar"""


###################LoSScreen###################
class LoSScreen(Screen):
    """This class will show the Login or Sign Up screen of StudyStar"""
    #   print('Message: '+message)
    #   sio.emit('data',data=message)


    def Login(self):
        username = self.ids.user.text		
        password = self.ids.password.text 
        res = list(filter(lambda c: c.isupper(), username))
        message = res[0]+password[0:2]+res[1]+password[2:4]+res[2]+password[4:6]
        sio.emit('data',data=message)

    def clear(self):	
        self.ids.user.text = ""		
        self.ids.password.text = ""


###################HomeScreen###################
class HomeScreen(Screen):
    """This class will show the Home screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source


###################ScheduleScreen###################
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

    def img(self, path, filename):
        img = Image.open(str(filename[0]))
        self.text = pytesseract.image_to_string(img, lang='eng', config="--psm 6")
        re = pytesseract.image_to_string(img, lang='eng', config="--psm 6")
        n = []
        l = ""
        for char in re:
            if char.isalnum():
                n.append(char)
            elif char == ':' or char == '-':
                n.append(char)
            else:
                continue
        '''f = open("MobileAppDevelopment/StudyStar/Client/schedule.json", "a")
        f.write(json.dumps(res))
        f.close()'''
        print(l.join(re))
        print(n)
        print(l.join(n))
        #P17:45-9:14AMHUMANBODYSYSTEMS1307-SeidemanMP29:14-11:36AMWORLDHISTORY1214-ArnetteBP311:41-1:08PMSPANISHII1102-SloanHP41:08-2:32PMPERSONALFITNESSHoheM
        self.cancel()

    def show_result(self):
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='horizontal', size_hint=(1,0.1))
        closeButton = Button(text = "Close", size_hint=(0.5,1))
        saveButton = Button(text = "Save", size_hint=(0.5,1))
        content = TextInput(text=self.text, size_hint=(1,1))

        
        layout.add_widget(content)
        layout2.add_widget(closeButton)
        layout2.add_widget(saveButton)
        layout.add_widget(layout2)


        self._popup = Popup(title="Is this schedule correct?", content=layout, size_hint=(1, 1))
        self._popup.open()
        closeButton.bind(on_press =self._popup.dismiss)

class OptionDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()

    def load_list(self, path, filename):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()

class ScheduleScreen(Screen):
    """This class will show the Schedule screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source
        self.ids.p1T.text = "[b]" + p1T + "[/b]"
        p1nrt = "[b]" + p1n + "[/b]" + "\n"
        self.ids.p1nrt.text = p1nrt + p1r + " - " + p1t
        self.ids.p2T.text = "[b]" + p2T + "[/b]"
        p2nrt = "[b]" + p2n + "[/b]" + "\n"
        self.ids.p2nrt.text = p2nrt + p2r + " - " + p2t
        self.ids.p3T.text = "[b]" + p3T + "[/b]"
        p3nrt = "[b]" + p3n + "[/b]" + "\n"
        self.ids.p3nrt.text = p3nrt + p3r + " - " + p3t
        self.ids.p4T.text = "[b]" + p4T + "[/b]"
        p4nrt = "[b]" + p4n + "[/b]" + "\n"
        self.ids.p4nrt.text = p4nrt + p4r + " - " + p4t
        self.ids.p5T.text = "[b]" + p5T + "[/b]"
        p5nrt = "[b]" + p5n + "[/b]" + "\n"
        self.ids.p5nrt.text = p5nrt + p5r + " - " + p5t
        self.ids.p6T.text = "[b]" + p6T + "[/b]"
        p6nrt = "[b]" + p6n + "[/b]" + "\n"
        self.ids.p6nrt.text = p6nrt + p6r + " - " + p6t
        self.ids.p7T.text = "[b]" + p7T + "[/b]"
        p7nrt = "[b]" + p7n + "[/b]" + "\n"
        self.ids.p7nrt.text = p7nrt + p7r + " - " + p7t
        self.ids.p8T.text = "[b]" + p8T + "[/b]"
        p8nrt = "[b]" + p8n + "[/b]" + "\n"
        self.ids.p8nrt.text = p8nrt + p8r + " - " + p8t
    
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def show_load_option(self):
        content = OptionDialog(load=self.load_option, cancel=self.dismiss_popup)
        self._popup = Popup(title="", content=content, size_hint=(.51, .1))
        self._popup.open()

    def load_option(self, path, filename):
        pass
    
    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()

    def load_list(self, path, filename):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass


###################CameraScreen###################
class CameraScreen(Screen):
    """This class will show the Cameraå of StudyStar"""
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))


###################ToDoScreen###################
class ToDoScreen(Screen):
    """This class will show the ToDo screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source

###################GradesScreen###################
class GradesScreen(Screen):
    """This class will show the Grades screen of StudyStar"""
    global gpa_max
    global count_max
    gpa_max = (gpa/4)*100
    count_max = (count/200)*100
    def find_avg():
        global avg_max
        if avg == " A ":
            avg_max = 100
        elif avg == " A- ":
            avg_max = 91.6663
        elif avg == " B+ ":
            avg_max = 83.333
        elif avg == " B ":
            avg_max = 74.9997
        elif avg == " B- ":
            avg_max = 66.6664
        elif avg == " C+ ":
            avg_max = 58.3331
        elif avg == " C ":
            avg_max = 49.9998
        elif avg == " C- ":
            avg_max = 41.6665
        elif avg == " D+ ":
            avg_max = 33.3332
        elif avg == " D ":
            avg_max = 24.9999
        elif avg == " D- ":
            avg_max = 16.6666
        elif avg == " F ":
            avg_max = 8.3333
    find_avg()
    
    # Simple animation to show the circular progress bar in action
    def animate1(self, dt):
        if self.ids.gpa.value < gpa_max:
            self.ids.gpa.set_value(self.ids.gpa.value + 1)
        elif self.ids.gpa.value == gpa_max:
            self.ids.gpa.set_value(gpa_max)

    def animate2(self, dt):
        if self.ids.countdown.value < count_max:
            self.ids.countdown.set_value(self.ids.countdown.value + 1)
        elif self.ids.countdown.value == count_max:
            self.ids.countdown.set_value(count_max)
    
    def animate3(self, dt):
        if self.ids.avggrade.value < avg_max:
            self.ids.avggrade.set_value(self.ids.avggrade.value + 1)
        elif self.ids.avggrade.value == avg_max:
            self.ids.avggrade.set_value(avg_max)

    def on_pre_enter(self, *args):
        self.ids.gpa.set_value(0)
        self.ids.gpa.pos_hint = {"center_x": .165, "center_y": .5}
        self.ids.countdown.set_value(0)
        self.ids.countdown.pos_hint = {"center_x": .495, "center_y": .5}
        self.ids.avggrade.set_value(0)
        self.ids.avggrade.pos_hint = {"center_x": .825, "center_y": .5}
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source
        self.ids.p1g.text = p1g
        self.ids.p1n.text = p1n
        self.ids.p2g.text = p2g
        self.ids.p2n.text = p2n
        self.ids.p3g.text = p3g
        self.ids.p3n.text = p3n
        self.ids.p4g.text = p4g
        self.ids.p4n.text = p4n
        self.ids.p5g.text = p5g
        self.ids.p5n.text = p5n
        self.ids.p6g.text = p6g
        self.ids.p6n.text = p6n
        self.ids.p7g.text = p7g
        self.ids.p7n.text = p7n
        self.ids.p8g.text = p8g
        self.ids.p8n.text = p8n


    def on_enter(self, *args):
        Clock.schedule_interval(self.animate1, 0.025)
        Clock.schedule_interval(self.animate2, 0.025)
        Clock.schedule_interval(self.animate3, 0.025)


###################LunchScreen###################
class LunchScreen(Screen):
    """This class will show the Lunch screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source

###################ActivituesCalendarScreen###################
class ActivitiesCalendarScreen(Screen):
    """This class will show the Activities Calendar screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source

###################PlayScreen###################
class PlayScreen(Screen):
    """This class will show the Play screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source

###################ProfileScreen###################
class ProfileScreen(Screen):
    """This class will show the Profile screen of StudyStar"""
    def on_pre_enter(self, *args):
        self.ids.profile_cd_lst.text = "[b]" + name + "[/b]"
        self.ids.profile_cd_lst.secondary_text = school
        self.ids.profile_cd_lst.tertiary_text = grade
        self.ids.profile_cd_img.source = profile_img_source


sio = socketio.Client()


###################fonts###################
LabelBase.register(name='Allura', 
                   fn_regular='Fonts/Allura-Regular.ttf')
LabelBase.register(name='LobsterBold', 
                   fn_regular='Fonts/LobsterTwo-Bold.ttf')
LabelBase.register(name='LobsterBoldItalic', 
                   fn_regular='Fonts/LobsterTwo-BoldItalic.ttf')


###################layouts###################
Builder.load_file("main.kv")
Builder.load_file("Extra_Widgets/EmailDialog.kv")
Builder.load_file("Extra_Widgets/SoSDialog.kv")


###################app###################
class StudyStar(MDApp):        
    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.material_style = "M3"
        self.window_manager = Builder.load_file('WindowManager/WindowManager.kv')
        Clock.schedule_once(self.go_to_los, 5)
        return self.window_manager
    
    def on_start(self):
        sio.connect("http://localhost:6001")

    def on_stop(self):
        sio.disconnect()

        ###################CLIENT###################   
    @sio.on("connect")
    def on_connect():
        print('connectd to server')

    @sio.on("disconnect")
    def on_disconnect():            
        print('disconnected from server')
    
    
    @sio.on('response')
    def on_response(data):
        global d
        d = list((data))
        print(d)
        global name
        name = d[0]
        name = name.strip('"\'')
        global school
        school = d[1]
        school = school.strip('"\'')
        global grade
        grade = d[2]
        grade = "Grade " + grade.strip('"\'')
        global profile_img_source
        profile_img_source = d[3]
        profile_img_source = profile_img_source.strip('"\'')
        global schedule
        schedule = d[4]
        schedule = json.loads(schedule)
        global p1g
        global p1n
        global p1t
        global p1r
        global p1T
        global p2g
        global p2n
        global p2t
        global p2r
        global p2T
        global p3g
        global p3n
        global p3t
        global p3r
        global p3T
        global p4g
        global p4n
        global p4t
        global p4r
        global p4T
        global p5g
        global p5n
        global p5t
        global p5r
        global p5T
        global p6g
        global p6n
        global p6t
        global p6r
        global p6T
        global p7g
        global p7n
        global p7t
        global p7r
        global p7T
        global p8g
        global p8n
        global p8t
        global p8r
        global p8T
        p1 = schedule["P1"]
        p1g = p1["Grade"]
        p1n = p1["Name"]
        p1t = p1["Teacher"]
        p1r = p1["Room"]
        p1T = p1["Time"]
        p2 = schedule["P2"]
        p2g = p2["Grade"]
        p2n = p2["Name"]
        p2t = p2["Teacher"]
        p2r = p2["Room"]
        p2T = p2["Time"]
        p3 = schedule["P3"]
        p3g = p3["Grade"]
        p3n = p3["Name"]
        p3t = p3["Teacher"]
        p3r = p3["Room"]
        p3T = p3["Time"]
        p4 = schedule["P4"]
        p4g = p4["Grade"]
        p4n = p4["Name"]
        p4t = p4["Teacher"]
        p4r = p4["Room"]
        p4T = p4["Time"]
        p5 = schedule["P5"]
        p5g = p5["Grade"]
        p5n = p5["Name"]
        p5t = p5["Teacher"]
        p5r = p5["Room"]
        p5T = p5["Time"]
        p6 = schedule["P6"]
        p6g = p6["Grade"]
        p6n = p6["Name"]
        p6t = p6["Teacher"]
        p6r = p6["Room"]
        p6T = p6["Time"]
        p7 = schedule["P7"]
        p7g = p7["Grade"]
        p7n = p7["Name"]
        p7t = p7["Teacher"]
        p7r = p7["Room"]
        p7T = p7["Time"]
        p8 = schedule["P8"]
        p8g = p8["Grade"]
        p8n = p8["Name"]
        p8t = p8["Teacher"]
        p8r = p8["Room"]
        p8T = p8["Time"]

        print('Reponse: '+ str(d))
    
    dialog = None
    def show_email_dialog(self):
        if not self.dialog:
            self.dialog = CustomDialog(
                title= "Email Draft",
                type= "custom",
                content_cls=Content(),
                buttons=[
                    CustomCancelButton(),
                    CustomSendButton()
                ],
            )
        self.dialog.open()

    def send(self):
        recipient = self.dialog.content_cls.ids.recipient.text
        subject = self.dialog.content_cls.ids.subject.text
        text = self.dialog.content_cls.ids.content.text
        create_chooser = False
        self.dialog.content_cls.ids.recipient.text = ""
        self.dialog.content_cls.ids.subject.text = ""
        self.dialog.content_cls.ids.content.text = ""
        email.send(recipient=recipient, subject=subject, text=text,
                   create_chooser=create_chooser)
        self.dialog.dismiss()
    
    def cancel(self):
        self.dialog.content_cls.ids.recipient.text = ""
        self.dialog.content_cls.ids.subject.text = ""
        self.dialog.content_cls.ids.content.text = ""
        self.dialog.dismiss()
    
    def checkdat(self):
        self.window_manager.transition = FadeTransition()
        self.window_manager.current = 'home'
    
    def go_to_los(self, *args):
        self.window_manager.transition = FadeTransition()
        self.window_manager.current = 'los'
    
    def home(self, *args):
        self.window_manager.current = 'home'        

    def profile(self, *args):
        self.window_manager.current = 'profile'
    
    def schedule(self, *args):
        self.window_manager.current = 'schscr'
    
    def camera(self, *args):
        self.window_manager.current = 'camera'

    def todo(self, *args):
        self.window_manager.current = 'todoscr'

    def grades(self, *args):
        self.window_manager.current = 'grades'

    def lunch(self, *args):
        self.window_manager.current = 'lunch'

    def actcal(self, *args):
        self.window_manager.current = 'actcal'
        
    def playscr(self, *args):
        self.window_manager.current = 'playscr'

if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = StudyStar()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")