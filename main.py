from kivymd.app import MDApp
from kivy.lang import Builder 
#from kivymd.uix.card import MDCard
#from kivymd.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivy.properties import DictProperty



KV = '''


MDScreen:
    MDIconButton:
        pos_hint: {'x': .76, 'y': .57}
        icon: 'eye'
    MDIconButton:
        pos_hint: {'x': .01, 'y': .01}  
        icon: 'account-cog'
        icon_size: '25sp'
    
    MDIconButton:
        pos_hint: {'x': .425, 'y': .68}  
        icon: 'account'
        icon_size: '100sp'
        
                          
    MDTextButton:
        text:
            'Esqueceu sua senha?'
        pos_hint:{'x': .06, 'center_y': .049}
        font_size: '11sp'
   
   

    
    MDTextButton:
        text:
            'Precisa de ajuda?'
        pos_hint:{'x': .425, 'center_y': .06}
        font_size: '15sp'
    
    MDRaisedButton:
        text: 'Cadastrar'
        size_hint_x: .5
        size_hint_y: .001
        pos_hint: {'center_x': .5, 'center_y': .13}
        
    MDTextField:
        hint_text: 'Senha'
        max_text_length: 20
        size_hint_x: .5
        pos_hint: {'center_x': .5, 'center_y': .6}
        password: True
        helper_text_mode: 'on_focus'
        line_color_normal:1,1,1,1
        right_icon: 'eye'

        
    MDRaisedButton:
        text: 'Logar'
        size_hint_x: .5
        size_hint_y: .09
        pos_hint: {'center_x': .5, 'center_y': .5}
        font_size: '25sp'
        
    MDFloatingActionButtonSpeedDial:
        id: speed_dial
        data: app.data
        root_button_anim: True
        hint_animation: True
    
    
        
    MDIconButton:
        icon: 'alpha-n' 
        size_hint_x: .60
        size_hint_y: .01
        pos_hint: {'center_x': .52, 'center_y': .9}
    MDIconButton:
        icon: 'alpha-u' 
        size_hint_x: .40
        size_hint_y: .01
        pos_hint: {'center_x': .48, 'center_y': .9}
        theme_icon_color: 'Custom'
        icon_color: app.theme_cls.primary_color
    MDIconButton:
        icon: 'alpha-n' 
        size_hint_x: .60
        size_hint_y: .01
        pos_hint: {'center_x': .56, 'center_y': .85}
        icon_color: app.theme_cls.primary_color
        theme_icon_color: 'Custom'
    MDIconButton:
        icon: 'alpha-r' 
        size_hint_x: .40
        size_hint_y: .01
        pos_hint: {'center_x': .44, 'center_y': .85}
    MDIconButton:
        icon: 'alpha-o' 
        size_hint_x: .60
        size_hint_y: .01

        pos_hint: {'center_x': .6, 'center_y': .80}
    MDIconButton:
        icon: 'alpha-b' 
        theme_icon_color: 'Custom'
        size_hint_x: .40
        icon_color: app.theme_cls.primary_color
        size_hint_y: .01
        pos_hint: {'center_x': .4, 'center_y': .8}

    MDTextField:
        hint_text: 'Email'

        size_hint_x: .5
        pos_hint: {'center_x': .5, 'center_y': .7}
        password: False
        helper_text_mode: 'on_focus'
        line_color_normal:1,1,1,1
    

        
'''

class SenhaCard():
    pass

class TelaLogin():
    pass

class Botao():
    pass
        

class MeuApp(MDApp):
    data = DictProperty()
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.data = {
            '@brun.nomsants': 'instagram',
            '(41) 99830-3946': 'whatsapp',
            'brunnomurilo1': 'gmail',
            'brunnomsants': 'github',
        }
        return Builder.load_string(KV)
    def callback(self, *args):
        print(args)

MeuApp().run()