from kivy.lang import Builder
import requests
from bs4 import BeautifulSoup
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.utils import asynckivy
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, IconRightWidget, ThreeLineAvatarIconListItem, ThreeLineListItem, TwoLineAvatarIconListItem, TwoLineListItem
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from kivy.clock import Clock
from sqlite3 import *

Window.size = (400, 500)

KV = '''


ScreenManager:
    Nav:
    Add:
    Profile:
    setting:
    Edit:
    Password:
    WelcomeScreen:
    UsernameScreen:
    DOB:
    MainScreen:
    contactus:
    Feedback:
#------------------------------------------------------------- Nav Screen ------------------------------------------------------------------------
<Nav>
    name: '1s'
    FitImage:
        source:'main.jpg'
        opacity: 0.2
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.15, "center_y":0.79}
        halign: 'center'
        elevation:'8dp'
        
        MDLabel:
            id : rrr
            text: app.priceTracker()
            theme_text_color: "Primary"
            pos_hint: {"center_x":0.50, "center_y":0.99}
            height: self.texture_size[1]
     
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.79}
        halign: 'center'
        elevation:'8dp'
        
        MDLabel:
            id : sss
            text: app.priceTracker1()
            theme_text_color: "Primary"
            pos_hint: {"center_x":0.55, "center_y":0.99}
            height: self.texture_size[1]

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "120dp", "80dp"
        pos_hint: {"center_x":0.83, "center_y":0.79}
        halign: 'center'
        elevation:'8dp'
        
        MDLabel:
            id : ooo
            text: "1234532"
            halign : 'center'
            theme_text_color: "Primary"
            pos_hint: {"center_x":0.50, "center_y":0.99}
            height: self.texture_size[1]

        
            
    BoxLayout:
        orientation:'vertical'
        pos_hint: {'center_x':0.50,'center_y':0.20}
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "400dp", "40dp"
            pos_hint: {"center_x":0.50, "center_y":0.95}
            elevation:'8dp'
            
            MDLabel:
                text: "Portfolio"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
           
   
         
        ScrollView:
            MDList:
                id: dock     

    MDFloatingActionButton:
        icon  : "plus"
        elevation_normal : 12
        on_press : root.manager.current='add'
        pos_hint: {"center_x":0.9, "center_y":0.15}
        text_color: 0,0,1,1
        elevation : '8dp'
                
            
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "Stockerr  "
            elevation : '8dp'
            left_action_items : [['menu' , lambda x : nav_drawer.toggle_nav_drawer()]]
            
        Widget:
            
    MDNavigationDrawer:
        id : nav_drawer
        BoxLayout:
            orientation : 'vertical'
            spacing : '8dp'
            padding : '8dp'
            
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        on_release: root.manager.current = 'pro'
                        IconLeftWidget:
                            icon : 'account-details'
                    OneLineIconListItem:
                        text: 'Settings'
                        on_release: root.manager.current = 's'
                        IconLeftWidget:
                            icon : "cogs"  
                    OneLineIconListItem:
                        text: 'Logout'
                        on_release: root.manager.current = 'welcomescreen'
                        IconLeftWidget:
                            icon : 'logout'
                    OneLineIconListItem:
                        text: 'Contact us'
                        on_release: root.manager.current = 'cu'
                        IconLeftWidget:
                            icon : 'chat'
                    OneLineIconListItem:
                        text: 'Feedback'
                        on_release: root.manager.current = 'fb'
                        IconLeftWidget:
                            icon : 'star'
#-------------------------------------------------------- Add Screen -------------------------------------------------------
<Add>
    name: 'add'
    FitImage:
        source:'main1.jpg'
        opacity: 0.2
    MDRaisedButton:
        text: "Save"
        elevation: 12
        size_hint: (0.2,0.08)
        font_size: '20sp'
        pos_hint: {'center_x':0.2,'center_y':0.10}
        size_hint_x: None
        width:300
        text_color: 1, 1, 0, 1
        on_press: app.savestock()
        on_release: app.showstock1()

    MDRaisedButton:
        text: "Cancel"
        elevation_normal : 12
        size_hint: (0.22,0.08)
        font_size: '20sp'
        pos_hint: {'center_x':0.80,'center_y':0.10}
        size_hint_x: None
        width:300
        text_color : 1,1,0,1
        on_press:
            root.manager.current = '1s'
            root.manager.transition.direction = 'down'
    MDLabel:
        text: "ADD STOCK"
        font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.93}
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        size_hint_x: None
        width:500
   
    MDTextField:
        id: company
        hint_text: "Company Name"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.80}
        size_hint_x: None
        width:300
        required: True

    # MDCard:
    #     orientation: "vertical"
    #     padding: "8dp"
    #     size_hint: None, None
    #     size: "310dp", "60dp"
    #     pos_hint: {"center_x":0.43, "center_y":0.70}
    #     elevation: '10dp'
        
    #     MDLabel:
    #         text: "Company's Current Price"
    #         theme_text_color: "Secondary"
    #         size_hint_y: None
    #         height: self.texture_size[1]

    #     MDLabel:
    #         id: current_price
    #         text: "abc"

    MDTextField:    
        id: invest
        hint_text: "Investment Price"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.50}
        size_hint_x: None
        width:300
        required: True

    MDTextField:   
        id: quantity
        hint_text: "Quantity"
        helper_text: "Text is always here"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.43, "center_y":0.20}
        size_hint_x: None
        width:300
        required: True

    # MDCard:
    #     orientation: "vertical"
    #     padding: "8dp"
    #     size_hint: None, None
    #     size: "310dp", "65dp"
    #     pos_hint: {"center_x":0.43, "center_y":0.22}
    #     elevation: '10dp'
        
    #     MDLabel:
    #         text: "Gross"
    #         theme_text_color: "Secondary"
    #         size_hint_y: None
    #         height: self.texture_size[1]

    #     MDLabel:
    #         id: gross
    #         text: "abc"
#--------------------------------------------------- Profile Screen --------------------------------------------------------------
<Profile>
    name: 'pro'
    MDCard:
        orientation: "horizontal"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "60dp"
        pos_hint: {"center_x":0.50, "center_y":0.95}
        elevation: '10dp'
        
        MDIconButton:
            icon: "arrow-left"
            size_hint_y: None
            pos_hint: {"center_x":0.50, "center_y":0.48}
            on_press : root.manager.current = '1s'
                          
        MDLabel:
            text: " Your Profile"
            theme_text_color: "Primary"
            size_hint_y: None
            pos_hint: {"center_x":0.50, "center_y":0.48}
            height: self.texture_size[1]
            
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.78}
        elevation: '10dp'
        
        MDLabel:
            text: "username"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uname
            text: " "
            
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.58}
        elevation: '10dp'
        
        MDLabel:
            text: "Email ID"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uemail
            text: " "
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x":0.50, "center_y":0.38}
        elevation: '10dp'
        
        MDLabel:
            text: "phone"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            id: uphone
            text: " "
    
    

       
#-------------------------------------------------------- Settings Screen ----------------------------------------------------------------------
<setting>
    name:'s'
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300
        
        
        Widget:
              
    Screen :
            
        ScrollView:
            MDList:
                        
                OneLineAvatarIconListItem:
                    text: "Change Theme"
                    on_size:
                        self.ids._right_container.width = container.width
                        self.ids._right_container.x = container.width

                    IconLeftWidget:
                        icon: "brightness-6"
                        

                    Container:
                        id: container

                        MDFloatLayout:

                        MDSwitch:
                            pos_hint: {"center_x":0.5, "center_y":.6}
                            width: dp(45)
                            on_active: app.check(*args)
                
                OneLineIconListItem:
                    text: 'Edit Profile'
                    width : 300
                    on_release: root.manager.current = 'edit'
                    IconLeftWidget :
                        icon : "account-arrow-right"
                 
            
                OneLineIconListItem:
                    text: 'Change Password'
                    width : 300
                    on_release: root.manager.current = 'password'
                    IconLeftWidget:
                        icon: "eye-plus"



        Screen :
                    
        MDRaisedButton:
            text: "Back"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.2}
            text_color: 1, 1, 0, 1
            on_release: root.manager.current = '1s'
#----------------------------------------------------------- Edit Screen -----------------------------------------------------------------------------------------------------      
<Edit>
    name : 'edit' 
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300
        spacing:'20dp'
        padding: "45dp"
        
        
    Screen :
        
        MDLabel:
            text : "Username"
            pos_hint :{"center_x":.6,"center_y":.9}
            
        MDTextField:
            id: username
            mode : "rectangle"
            icon_right:"account"
            hint_text:"Enter Username      "
            helper_text_mode:"on_focus"
            helper_text: "Always write here"
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.82}
            width:300
            required: True
            
        MDLabel:
            text : "Email"
            pos_hint :{"center_x":.6,"center_y":.7}
            
        MDTextField:
            id: email
            mode : "rectangle"
            icon_right:"email"
            hint_text:"Enter E-mail Id      "
            helper_text_mode:"on_focus"
            helper_text: "Always write here"
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.62}
            width:300
            required: True
        
        MDLabel:
            text : "Contact No."
            pos_hint :{"center_x":.6,"center_y":.5}
            
        MDTextField:
            id:contact
            mode : "rectangle"
            icon_right:"phone"
            hint_text:"Enter Phone No.      "
            helper_text_mode:"on_focus"
            helper_text: "Enter 10 digit Phone No."
            size_hint_x: None
            pos_hint : {"center_x":.5,"center_y":.42}
            width:300
            max_text_length:10
            required: True
            
        MDRaisedButton:
            text: "Back"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.2}
            text_color: 1, 1, 0, 1
            on_release: root.manager.current = 's'
        
        MDRaisedButton:
            text: "Save"
            width : 300
            elevation : 12
            font_size: '20sp'
            pos_hint: {"center_x": 0.8, "center_y": 0.3}
            text_color: 1, 1, 0, 1
            on_press: app.saveprofile()
    
#------------------------------------------------------- Password Screen ------------------------------------------------------------
<Password>
    name:'password'
    BoxLayout:
        orientation:'vertical'
        pos_hint: {"center_x":0.55, "center_y":0.4}
        width : 300
        spacing:'20dp'
        padding: "45dp"
    
    Screen :
    
    MDLabel:
        text : "Current Password"
        pos_hint :{"center_x":.6,"center_y":.9}
    
    MDTextField:
        id: cur_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-off'
        hint_text: 'Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.82}
        required: True
        
    MDLabel:
        text : "New Password"
        pos_hint :{"center_x":.6,"center_y":.7}
    
    MDTextField:
        id: new_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-plus'
        hint_text: 'Enter Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.62}  
        required: True
        
    MDLabel:
        text : "Confirm Password"
        pos_hint :{"center_x":.6,"center_y":.5}
    
    MDTextField:
        id: con_pass
        mode : "rectangle"
        icon_left: 'key-variant'
        icon_right: 'eye-check'
        hint_text: 'Enter Password    '
        helper_text:"Text is always here"
        helper_text_mode:"on_focus"
        password : True
        size_hint_x: None
        width:300
        pos_hint : {"center_x":.5,"center_y":.42}
        required: True
                   
    MDRaisedButton:
        text: "Back"
        width : 300
        elevation : 12
        font_size: '20sp'
        pos_hint: {"center_x": 0.8, "center_y": 0.2}
        text_color: 1, 1, 0, 1
        on_release: root.manager.current = 's'
    
    MDRaisedButton:
        text: "Save"
        width : 300
        elevation : 12
        font_size: '20sp'
        pos_hint: {"center_x": 0.8, "center_y": 0.3}
        text_color: 1, 1, 0, 1
        on_press: app.changepass()
#--------------------------------------------------------- Welcome Screen -----------------------------------------------------  
<WelcomeScreen>:
    name : 'welcomescreen'
    FitImage:
        source:'welcome.jpg'
        opacity: 0.2
    MDLabel:
        text:'Get Started With Stocker'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.65}
    MDFloatingActionButton:
        icon:'account-arrow-right-outline'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint: {'center_x':0.5,'center_y':0.15}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:30
        pos_hint:{'center_y' : 0.04}
#------------------------------------------------------ Username Screen ---------------------------------------------------------------------------
<UsernameScreen>
    name:'usernamescreen'
    
    FitImage:
        source:'signupbg.jpg'
        opacity: 0.2
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'dob'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'Enter username and password'
        text_color: 1, 1, 1, 1
        font_style: 'H4'
        halign: 'center'
        pos_hint : {'center_y':0.85}
    MDTextField:
        id:username_text_fied
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:pw_text
        pos_hint: {'center_x':0.5,'center_y':0.49}
        size_hint: (0.7,0.1)
        hint_text : 'password'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'key'
        icon_right_color: app.theme_cls.primary_color
        required : True
        password: True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.30}
        user_font_size: '50sp'
        on_press: app.check_username()
#---------------------------------------------------- DOB Screen -------------------------------------------------------------------
<DOB>:
    name:'dob'
    MDLabel:
        text:'Date of Birth'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.75} 
    MDRaisedButton:
        id:date_picker
        text:'Date Picker'
        user_font_size : '70sp'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        on_press:
            app.show_date_picker()
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'usernamescreen'
    MDFloatingActionButton:
        id: second_disabled
        disabled: True
        icon:'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'mainscreen'
#---------------------------------------------------- Main Screen ----------------------------------------------------------
<MainScreen>:
    name : 'mainscreen'
    FitImage:
        source:'main2.jpg'
        opacity: 0.1
    MDLabel:
        id:profile_name
        text:'main screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        
    MDRectangleFlatButton:
        text:"Proceed"
        halign: 'center'
        line_color: 1, 1, 1, 1
        pos_hint: {'center_x':.50,'center_y':.25} 
        on_press : root.manager.current = '1s'
#---------------------------------------------------------------------- Contact us ------------------------------------------------------------------------            
<contactus>
    name:'cu'
    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.95}
        
        MDRoundFlatIconButton:
            text : "social connect"
            icon : 'arrow-left'
            on_press : root.manager.current = '1s'
                     
    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        
        MDLabel:
            text: "instagram"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "@stocker_handle" 
            
    MDCard:
        orientation:'vertical'
        padding : '8dp'
        size_hint: None, None
        size: "400dp", "80dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        
        MDLabel:
            text: "Email"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "stockersmail@gmail.com"  
#------------------------------------------------------------------- Feedback --------------------------------------------------------------           
<Feedback>                
    name: 'fb'
    FitImage:
        source:'feedback.jpg'
        opacity: 0.1
    MDRoundFlatIconButton:
        text : "Back"
        icon : 'arrow-left'
        pos_hint: {'center_x':0.2,'center_y':0.9}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        on_press : root.manager.current = '1s'
    MDLabel:
        text: 'Rate Our App'
        pos_hint: {'center_x':0.9,'center_y':0.9}
        font_style: 'H4'
        bold: True
        theme_text_color: 'Custom'
        text_color: 231/255,64/255,98/255,1

    MDIconButton:
        id: star1
        icon: "emoticon-devil"
        pos_hint: {'center_x':.2,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(1)
    MDIconButton:
        id: star2
        icon: "emoticon-confused"
        pos_hint: {'center_x':.35,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(2)
    MDIconButton:
        id: star3
        icon: "emoticon-happy"
        pos_hint: {'center_x':.50,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(3)
    MDIconButton:
        id: star4
        icon: "emoticon-excited"
        pos_hint: {'center_x':.65,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(4)
    MDIconButton:
        id: star5
        icon: "emoticon-cool"
        pos_hint: {'center_x':.8,'center_y':.35}
        theme_text_color: 'Custom'
        text_color: 0,0,0,1
        opacity: 0.5
        on_release: app.select(5)
    MDLabel:
        id: text
        text: ""
        pos_hint: {'center_y':.20}
        halign: 'center'
        font_style: "H5"
        bold: True
        theme_text_color: 'Custom'
        text_color: 67/255,247/255,58/255,1
    MDRaisedButton:
        text: "Submit"
        pos_hint: {'center_x':.5,'center_y':.05}
        md_bg_color: 1,0,0,1
        on_press: app.feedback()
'''

class Nav(Screen):
    pass
class Add(Screen):
    pass
class Profile(Screen):
    pass
class setting(Screen):
    pass
class Edit(Screen):
    pass
class Password(Screen):
    pass
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
class DOB(Screen):
    pass
class MainScreen(Screen):
    pass
class contactus(Screen):
    pass
class Feedback(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Nav(name='1s'))
sm.add_widget(Add(name='add'))
sm.add_widget(Profile(name='pro'))
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
sm.add_widget(DOB(name='dob'))
sm.add_widget(MainScreen(name='main_screen'))
sm.add_widget(setting(name='s'))
sm.add_widget(Password(name='password'))
sm.add_widget(contactus(name='cu'))
sm.add_widget(Feedback(name='fb'))

class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class Stoker(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        self.background_hue = 900
        self.strng = Builder.load_string(KV)
        Clock.schedule_interval(self.set_heading,3)
        Clock.schedule_interval(self.set_heading1,3)
        Clock.schedule_interval(self.updatecv,3)
        con = connect('stocker.db')
        cursor = con.cursor()
        res = cursor.execute("select * from profileinfo").fetchall()
        for d in res:
            name = d[0]
            email = d[1]
            phone = d[2]
        self.strng.get_screen('pro').ids.uname.text = name
        self.strng.get_screen('pro').ids.uemail.text = email
        self.strng.get_screen('pro').ids.uphone.text = phone
        self.showstock()
        self.cv()
        return self.strng

    def check(self,checkbox,value):
        if value:
            self.theme_cls.theme_style="Dark"
        else:
            self.theme_cls.theme_style = "Light"


    def priceTracker(a):
        url = "https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return ("   Sensex \n" + price)
    def set_heading(self,dt):
        async def set_heading():
            await asynckivy.sleep(0.1)
            text_heading = self.strng.get_screen('1s').ids.rrr
            text_heading.text = self.priceTracker()

        asynckivy.start(set_heading())

    def priceTracker1(a):
        url = "https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return ("    Nifty \n" + price )
    def set_heading1(self,dt):
        async def set_heading1():
            await asynckivy.sleep(0.1)
            text_heading = self.strng.get_screen('1s').ids.sss
            text_heading.text = self.priceTracker1()

        asynckivy.start(set_heading1())

    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        self.password_text = self.strng.get_screen('usernamescreen').ids.pw_text.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == [] and self.password_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Enter Username And password', text="Please input  username and password for registration", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date, year=1999, month=1, day=1, )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.second_disabled.disabled = False

        # Storing of DATA
        self.store.put('UserInfo', name=self.username_text,password=self.password_text ,dob=str(self.dob))
        self.username_changer()

    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('1s').manager.current = '1s'

        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'
    def select(self,number):
        if number == 1:
            self.strng.get_screen('fb').ids.star1.opacity = 1
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "I Just Hate It!"
        elif number == 2:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 1
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "I Don't Like It!"
        elif number == 3:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 1
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "It is Good!"
        elif number == 4:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 1
            self.strng.get_screen('fb').ids.star5.opacity = 0.5
            self.strng.get_screen('fb').ids.text.text = "It is Awesome!"
        elif number == 5:
            self.strng.get_screen('fb').ids.star1.opacity = 0.5
            self.strng.get_screen('fb').ids.star2.opacity = 0.5
            self.strng.get_screen('fb').ids.star3.opacity = 0.5
            self.strng.get_screen('fb').ids.star4.opacity = 0.5
            self.strng.get_screen('fb').ids.star5.opacity = 1
            self.strng.get_screen('fb').ids.text.text = "I Just Love It!"

    def savestock(self):
        a = self.strng.get_screen('add').ids.company.text
        b = float(self.strng.get_screen('add').ids.invest.text)
        c = self.strng.get_screen('add').ids.quantity.text
        if a.split() == [] or b == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please fill the required fields", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif a.isalnum() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please enter valid company name", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif c.isnumeric() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text="Please enter valid price", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            try:
                con = connect('stocker.db')
                cursor = con.cursor()
                sql = "insert into stockinfo values('%s','%s','%s')"
                cursor.execute(sql % (a,b,c))
                con.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Saved', text="Stock Added", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
                con.close()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
    
    def saveprofile(self):
        a = self.strng.get_screen('edit').ids.username.text
        b = self.strng.get_screen('edit').ids.email.text
        c = self.strng.get_screen('edit').ids.contact.text
        if a.split() == [] or b.split() == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Please fill the required details', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif a.isalnum() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Enter valid username', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif c.isnumeric() == False:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Enter valid mobile number', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            try:
                con = connect('stocker.db')
                cursor = con.cursor()
                sql = "insert into profileinfo values('%s','%s','%s')"
                cursor.execute(sql % (a,b,c))
                con.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Saved', text="Profile Created Successfully", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
                con.close()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

    def changepass(self):
        a = self.strng.get_screen('password').ids.cur_pass.text
        b = self.strng.get_screen('password').ids.new_pass.text
        c = self.strng.get_screen('password').ids.con_pass.text
        if a.split() == [] or b.split() == [] or c.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Issue', text='Please fill the required details', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            if b == c:
                try:
                    con = connect('stocker.db')
                    cursor = con.cursor()
                    sql = "insert into changepass values('%s','%s','%s')"
                    cursor.execute(sql % (a,b,c))
                    con.commit()
                    cancel_btn_username_dialogue = MDFlatButton(text='Ok', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='Saved', text="Password Changed Successfully", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
                    con.close()
                except Exception as e:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='Issue', text="Some Error occured", size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Issue', text='Password does not match', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

    def feedback(self):
        cancel_btn_username_dialogue = MDFlatButton(text='OK', on_release=self.close_username_dialogue)
        self.dialog = MDDialog(title='Done', text='Feedback submitted', size_hint=(0.7, 0.2),buttons=[cancel_btn_username_dialogue])
        self.dialog.open()
    
    def showstock(self):
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select company_name,(investment_price * quantity) from stockinfo where (investment_price * quantity)>0"
        data = cursor.execute(sql).fetchall()
        for d in data:
            result = str(d[0])
            result1 = str(d[1])
            con.commit()
            item = TwoLineListItem()
            item.text = result
            a9 = result
            url = "https://www.google.com/finance/quote/" + a9 + ":NSE"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
            item.secondary_text = price
            item.tertiary_text = result1
            self.strng.get_screen("1s").ids["dock"].add_widget(item)

    def showstock1(self):
        global result
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select company_name,(investment_price * quantity) from stockinfo where (investment_price * quantity)>0"
        data = cursor.execute(sql).fetchall()
        for d in data:
            result = str(d[0])
            result1 = str(d[1])
        con.commit()
        item = ThreeLineListItem()
        item.text = result
        a9 = result
        url = "https://www.google.com/finance/quote/" + a9 + ":NSE"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': 'rPF6Lc'})[0].find('span').text
        item.secondary_text = price
        item.tertiary_text = result1
        self.strng.get_screen("1s").ids["dock"].add_widget(item)
    
    def cv(self):
        sum = 0
        con = connect('stocker.db')
        cursor = con.cursor()
        sql = "select (investment_price * quantity) from stockinfo where (investment_price * quantity)>0"
        res = cursor.execute(sql).fetchall()
        for i in res:
            sum = sum + float(i[0])
        total = "  Net worth\n" + str(sum)
        return total
    def updatecv(self,dt):
        self.strng.get_screen('1s').ids.ooo.text = self.cv()

Stoker().run()