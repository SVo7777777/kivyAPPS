from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import datetime
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class LabelX(Label):
    def set_bgcolor(self,r,b,g,o):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(r,g,b,o)
            self.rect = Rectangle(pos=self.pos,size=self.size)
        self.bind(pos=self.update_rect,
                  size=self.update_rect)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size        
        
class MainApp(App):
    def build(self):
        # here I add the main and second screens to the manager, this class does nothing else
        tb_panel.add_widget(Th_head('от 1 до 12', 'green', 0, 13) )   
        tb_panel.add_widget(Th_head('от 13 до 24', 'green', 12, 25) )   
        
        tb_panel.default_tab_text = 'Главная'       
        tb_panel.default_tab_background_color = 'green'
        tb_panel.default_tab_width = tb_panel.width /3      
        tb_panel.background_color = 'green'
        
        today = datetime.datetime.now()
        data = today.strftime("%m-%y")
        month = {'01': 'январь','02': 'февраль', '03': 'март','04': 'апрель', '05': 'май', '06': 'июнь','07': 'июль', '08': 'август','09': 'сентябрь','10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
        m_y = month[data[0:2]]+' 20' + data[3:5] + 'г.'
        m_y1 = month[data[0:2]]+'\n20' + data[3:5] + 'г.'
        print(month)
        print(month[data[0:2]])
        self.spisik_estj = False
        self.crsp = False
        self.ks = 1
        print(self.spisik_estj)        
        print(self.crsp)
        
        lay= BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        label = LabelX(halign="center", font_size=50, size_hint=(1, .5), color=[0, 0 ,0, 1])
        label.set_bgcolor(1,1,1,1)
        label.text = 'Внесите сотрудника , нажимая \nна "+" рядом с каждой фамилией.\nУдалите сотрудника , нажимая \nна "-" рядом с каждой фамилией.'
        lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 1))
        layoutgr= GridLayout(cols=1, spacing=0, size_hint=(1, None))
        layoutgr.bind(minimum_height=layoutgr.setter('height'))
        lay_01= BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay_0= BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay_1= BoxLayout(orientation="vertical", padding=0, size_hint=(.5, 1))
        lay1 = LabelX(halign="center", text='', font_size=50, size_hint=(1, 1), color=[0, 0 ,0, 1])
        lay1.set_bgcolor(1,1,1,1)
        lay1.text = 'Сегодня\n' + m_y1
        hide = Button(text='скрыть список\nсотрудников', markup=True, font_size=28, size_hint=(1, 1), color=[1, 1, 0, 1])
        show = Button(text='показать список\nсотрудников', font_size=28, size_hint=(1, 1))
        b1 = Button(text='создать список', markup=True, font_size=28, size_hint=(1, 1), color=[1, 1, 0, 1])
        b2 = Button(text='какой сегодня месяц', font_size=28, size_hint=(1, 1))
        lay_1.add_widget(lay1)
        lay_0.add_widget(show)
        lay_0.add_widget(hide)
        lay_01.add_widget(b1)
        lay_01.add_widget(b2)
        
        b1.on_press = lambda: create_spisok()
        b2.on_press = lambda: show_month()
        show.on_press = lambda: show_spisok()
        hide.on_press = lambda: hide_spisok()
        
        def create_spisok():            
            #global crsp, spisik_estj
            
            self.crsp = True
            print(self.spisik_estj)
            if self.spisik_estj == False and self.ks == 0:
                print(self.ks)
                for i in range(1, self.ks):
                    print(self.ks)
                    add(i,2)
                self.spisik_estj = True
                self.crsp = False
                label = Label(text='список на этот месяц \nуспешно  создан!!', font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,220), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()  
            else:
                label = Label(text='список на этот  месяц уже \nсуществует!!', font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,220), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()    
           
            
        def show_month():
            #global spisik_estj
            
            today = datetime.datetime.now()
            data = today.strftime("%m-%y")
            month = {'01': 'январь','02': 'февраль', '03': 'март','04': 'апрель', '05': 'май', '06': 'июнь','07': 'июль', '08': 'август','09': 'сентябрь','10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
            m_y = month[data[0:2]]+' 20' + data[3:5] + 'г.'
            m_y1 = month[data[0:2]]+'\n20' + data[3:5] + 'г.'
            lay1.text = 'Сегодня\n' + m_y1
            with open("tabel_sotrudnikov.txt", "r") as f:
                lines = f.readlines()                                
                for line in lines:
                    print(m_y)
                    if m_y  in line:      
                        lay1.text = lay1.text + '\nсписок\nесть ' 
                        self.spisik_estj = True
                        print(self.spisik_estj)
                        break
                    else:                    
                        lay1.text = lay1.text + '\nсоздайте\nсписок\nна этот\nмесяц'
                        self.spisik_estj = False
                        show_spisok()
                        break
                        
                            
        def hide_spisok():
            for i in range(24):
                entry[i+1, 1].text = ''
                
        def show_spisok():
            #global ks
            with open('tabel_sotrudnikov.txt', 'r') as k:
                f =k.read() 
                self.ks=1
                sp_all = f.splitlines()
                print(sp_all)
                s = sp_all[0].split()
                entry[1, 1].text = s[2]
                for i in range(1,len(sp_all)):
                    s = sp_all[i].split()
                    print(s)
                    '''if s[0] in ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']:
                        pass
                    else:'''
                    if entry[i, 1].text != s[2]:
                        entry[i+1, 1].text = s[2]
                        self.ks = self.ks +1
                lay1.text = 'всего\nчеловек:\n ' + str(self.ks)
                        
        def setka(i1, i2):
            #для списка сотрудников
            for i in range(i1, i2):
                h_layout = BoxLayout(height=61, size_hint=(1, None))
                for j in range(4):
                    if j == 0 or  j == 2 or j == 3:
                        but[i, j] = Button(text='', halign="center", font_size=28, size_hint=(None, 1), width=50)
                        
                        
                        if j == 0:
                            but[i, j].text = str(i) 
                            if i == 0:
                                but[i, j].text = 'N°'
                        if j ==2:
                           but[i, j].text = '+' 
                           but[i, j].width =70
                           butt_add(i,j)
                           if i == 0:
                               but[i, j].text = '' 
                        if j ==3:
                           but[i, j].text = '-' 
                           but[i, j].width =70
                           butt_del(i,j)
                           if i == 0:
                               but[i, j].text = '' 
                        h_layout.add_widget(but[i, j])
                    else:
                        entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50, size_hint=(1, 1),  width=50, multiline=False)
                        #entry[i, j].set_bgcolor(1,1,1,1)
                        h_layout.add_widget(entry[i, j])
                        if j == 1:
                            entry[i, j].markup=True
                            entry[i, j].width = 240
                            entry[i, j].foreground_color = [0, 0, 1, 1]
                            if i == 0:
                                entry[i,j].text = ' ФИО'
                                entry[i,j].foreground_color = [0, 0, 1, 1]
                                entry[i,j].background_color = [1,1,0.5,1]            
                layoutgr.add_widget(h_layout)
                
        def butt_del(i,j):
            but[i, j].on_press=lambda: delete(i, j)
        def delete(r, c):
            print(str(r) + '-' + str(c)) 
            print(entry[r, c-2].text)           
            sotrudnik =entry[r, c-2].text
            for i in range(24):
                if entry[i+1,1].text == sotrudnik:
                    entry[i+1,1].text = ''
            with open("tabel_sotrudnikov.txt", "r") as f:
                lines = f.readlines()
                with open("tabel_sotrudnikov.txt", "w") as f:
                    for line in lines:
                        if line.split()[2] != sotrudnik:
                            f.write(line)
            '''with open('tabel_sotrudnikov.txt', 'a+') as k:
                k.write('\n' + sotrudnik)
                sotrud[r] = sotrudnik
                label = Label(text='sotrudnik успешно удалён!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()  '''      
            
        def butt_add(i,j):
            but[i, j].on_press=lambda: add(i, j)
        def add(r, c):
            print(str(r) + '-' + str(c)) 
            print(entry[r, c-1].text)
            today = datetime.datetime.now()
            data = today.strftime("%m-%y")
            print(data)
            sotrudnik =entry[r, c-1].text
            lay1.text = lay1.text +'\n ' + data + '\n ' + entry[r, c-1].text
            #print(num[0, r].text)
            hours = ''
            for i in range(32):              
                hours = hours + '-'                
            sotrudnik =entry[r, c-1].text     
            
            with open('tabel_sotrudnikov.txt', 'a+') as k:
                k.write(m_y + ' ' + sotrudnik + ' ' +  hours +'\n' )
                if crsp == False:
                    label = Label(text='sotrudnik успешно сохранен!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                    popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                    popupWindow.add_widget(label)
                    popupWindow.open()    
        but = {}
        entry = {}
        sotrud= {}
        print(sotrud)
        setka(0,25)
        root1= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root1.add_widget(layoutgr)
        
        lay0.add_widget(root1)#список сотрудников
        lay0.add_widget(lay_1)
        lay.add_widget(label)
        lay.add_widget(lay0)
        lay.add_widget(lay_01)
        lay.add_widget(lay_0)        
        tb_panel.default_tab_content = lay
        return tb_panel  # I return the manager to work with him later
        
class Th_head(TabbedPanelHeader):
    def __init__(self, text, color, col1, col2):
        super().__init__()
        self.butk = {}
        self.tab_width =200
        self.text = text
        self.background_color = color
        lay= BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 2))
        #laytop= BoxLayout(orientation="horizontal", padding=0, size_hint=(.1, .05))
        lay1 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .47))
        layoutgr= GridLayout(cols=1, spacing=0, size_hint=(1, None))
        layout = GridLayout(rows=1,  spacing=0, size_hint_x=None)#, size_hint_x=None)
        #new_spisok = Button(text='[b]>>[/b]', font_size=22, size_hint=(.87, 1), markup=True)
        copy = Button(text='сохранить', markup=True, font_size=28, size_hint=(1, 1), color=[1, 1, 0, 1])
        clear = Button(text='очистить', font_size=28, size_hint=(1, 1))
        laybutton=BoxLayout(size_hint=(1, .46))
        #laybutton= FloatLayout(size=(100, 200))
        lay1.add_widget(copy)
        lay1.add_widget(clear)
        #lay1.add_widget(laybutton)
        #laytop.add_widget(new_spisok)
        # Make sure the height is such that there is something to scroll.
        layoutgr.bind(minimum_height=layoutgr.setter('height'))
        layout.bind(minimum_width=layout.setter('width'))
        today = datetime.datetime.now()
        data = today.strftime("%m-%y")
        month = {'01': 'январь','02': 'февраль', '10':'октябрь'}
        m_y = month[data[0:2]]+' 20' + data[3:5] + 'г.'
        y = ' 20' + data[3:5]
        
        dropdown = DropDown(size_hint_y=None, size_hint_x=None, height=44, width=100)
        dropdownyear = DropDown(size_hint_y=None, size_hint_x=None, height=44, width=100)
        for index in ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
        
            btn = Button(text=index, size_hint_y=None, size_hint_x=None, height=44, width=100)
        
            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: (dropdown.select(btn.text), vivod_sotrudnikov()))
        
            # then add the button inside the dropdown
            dropdown.add_widget(btn)
        
        # create a big main button
        mainbutton = Button(text='выберите месяц', font_size=40, size_hint=(.6, .6)) #pos_hint: {"top": 1})
        
        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=lambda btn: dropdown.open(btn))
        
        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))  
        years = [int(y), int(y)+1, int(y)+2, int(y)+3, int(y)+4]
        for year in years:
            btn1= Button(text=str(year), size_hint_y=None, size_hint_x=None, height=44, width=100)
            btn1.bind(on_release=lambda btn1: (dropdownyear.select(btn1.text), vivod_sotrudnikov()))
            dropdownyear.add_widget(btn1)
        yearbutton = Button(text='выберите год', font_size=40, size_hint=(.6, .6))
        yearbutton.bind(on_release=lambda btn1: dropdownyear.open(btn1))
        dropdownyear.bind(on_select=lambda instance, x: setattr(yearbutton, 'text', x))  
        laybutton.add_widget(mainbutton)    
        laybutton.add_widget(yearbutton) 
        def vivod_sotrudnikov():
            month = mainbutton.text
            j = 0
            with open('tabel_sotrudnikov.txt', 'r') as k:
                f =k.read() 
                sp_all = f.splitlines()
                print(sp_all)
                for i in range(len(sp_all)):
                    s = sp_all[i].split()
                    print(s)
                    if s[0] == month:
                        j = j+1                      
                        entry[j,1].text = s[2]
                        h = s[3].split('-')
                        print(h)
                        for i1 in range(32):
                            num[i1, j].text = h[i1]
                         
                            
                        
        
        def setka(i1, i2):
            #для списка сотрудников
            for i in range(i1, i2):
                h_layout = BoxLayout(height=61, size_hint=(1, None))
                for j in range(3):
                    if j == 0 or  j == 2:
                        but[i, j] = Button(text='+', halign="center", font_size=28, size_hint=(None, 1), width=50)
                        butt_add(i,j)
                        if j == 0:
                            but[i, j].text = str(i) 
                            if i == col1:
                                but[i, j].text = 'N°'
                        if j ==2 and i == col1:
                           but[i, j].text = '' 
                        h_layout.add_widget(but[i, j])
                    else:
                        entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50, size_hint=(1, 1),  width=50, multiline=False)
                        #entry[i, j].set_bgcolor(1,1,1,1)
                        h_layout.add_widget(entry[i, j])
                        if j == 1:
                            entry[i, j].markup=True
                            entry[i, j].width = 240
                            entry[i, j].foreground_color = [0, 0, 1, 1]
                            if i == col1:
                                entry[i,j].text = ' ФИО'
                                entry[i,j].foreground_color = [0, 0, 1, 1]
                                entry[i,j].background_color = [1,1,0.5,1]            
                layoutgr.add_widget(h_layout)
            # для часов по дням в мнсяце
            for i in range(32):
                h_layout = BoxLayout(height=61,orientation="vertical", size_hint=(None, 1))
                for j in range(i1, i2):
                    num[i,j]= TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50, size_hint=(1, 1),  width=100, multiline=False, text='',  size_hint_x=None, size_hint_y=1)    
                    h_layout.add_widget(num[i,j])                                
                    if j == 0:
                        num[i,j].foreground_color = [0, 0, 1, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        num[i,j].text = str(i+1)
                    if i == 31:                                 
                        num[i,j].width = 140
                        num[i,j].foreground_color = [1, 0, 0, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        if j == 0:
                            num[i,j].text = 'Итог' 
                layout.add_widget(h_layout)       
        
        def butt_add(i,j):
            but[i, j].on_press=lambda: add(i, j)
        def add(r, c):
            print(str(r) + '-' + str(c)) 
            print(m_y)
            print(entry[r, c-1].text)
            print(num[0, r].text)
            k = 0
            hours = ''
            for i in range(32):
                if i != 31:
                    if num[i, r].text.isdigit() == True:
                        k= k+int(num[i, r].text)
                    hours = hours + num[i, r].text + '-'
                else:                  
                    hours = hours +str(k)
            sotrudnik =entry[r, c-1].text     
            with open("tabel_sotrudnikov.txt", "r") as f:
                lines = f.readlines()
                
                with open("tabel_sotrudnikov.txt", "w") as f1:
                    print(lines)
                    for line in lines:
                        print(m_y + ' ' + sotrudnik)
                        print(line)
                        if m_y + ' ' + sotrudnik in line:                            
                            new_line = m_y + ' ' + sotrudnik + ' ' + hours + '\n'    
                            print('new_line=',new_line)                            
                            f1.write(new_line)    
                        else:
                            f1.write(line)     
                            print('мы тут')               
            
                label = Label(text='sotrudnik успешно сохранен!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()    
        but = {} 
        entry = {}
        num = {}
        setka(col1, col2) 
        
        root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root.add_widget(layout)
        root1= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root1.add_widget(layoutgr)
        lay0.add_widget(root1)#список сотрудников
        lay0.add_widget(root)# даты
        
        #lay.add_widget(laytop)
        lay.add_widget(lay0)
        lay.add_widget(laybutton)
        lay.add_widget(lay1)
        
        self.content = lay
        
tb_panel = TabbedPanel()

if __name__ == '__main__':
    MainApp().run()