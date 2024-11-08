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

class PopupX(Popup):
    def __init__(self,text1,**kwargs):
        super(PopupX,self).__init__(**kwargs)
        label = Label(text=text1, font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])      
        self.title='внимание!'
        self.size_hint=(None,None)
        self.size=(700,220)
        self.pos_hint={'x': 0.0 / Window.width, 'y': 500.0 / Window.height}
        self.add_widget(label)
        self.open()     
                               
class MainApp(App):
    def build(self):
        col1 = 0
        col2= 21
        lay= BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        #layfor0 = GridLayout(cols=1, spacing=0, size_hint=(1, None))
        lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 2))        
        laytop= BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay1 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        layoutgr= GridLayout(cols=1, spacing=0, size_hint=(1, 1))
        layout_itog = GridLayout(cols=1, spacing=0, size_hint=(.28, 1))
        layout = GridLayout(rows=1,  spacing=0, size_hint=(None, 1))#, size_hint_x=None)       
        copy = Button(text='обновить', markup=True, font_size=40, size_hint=(1, 1), color=[1, 1, 0, 1])
        delete = Button(text='', markup=True, font_size=35, size_hint=(1, 1), color=[1, 1, 0, 1])
        clear = Button(text='очистить', font_size=40, size_hint=(1, 1))        
        laybutton=BoxLayout(size_hint=(1, .16))        
        lab1 = LabelX(halign="center", text='Выберите год и месяц! Введите часы!\n Чтобы добавить, жмите на "+"! Обновите! ', font_size=35, size_hint=(1, .2), color=[0, 0 ,0, 1])
        lab1.set_bgcolor(.8,.8,1,1)        
        lay1.add_widget(copy)
        lay1.add_widget(clear)
        lay1.add_widget(delete)
        clear.on_press = lambda: clear_all()  
        copy.on_press = lambda: vivod_sotrudnikov()   
        delete.on_press = lambda: delete_all()     
        #layfor0.bind(minimum_height=layfor0.setter('height'))
        #layoutgr.bind(minimum_height=layoutgr.setter('height'))
        layout.bind(minimum_width=layout.setter('width'))       
        today = datetime.datetime.now()
        print(today.isoweekday())
        data = today.strftime("%m-%y")        
        y = ' 20' + data[3:5]
        self.month_choose = False      
        dropdown = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        dropdownyear = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        for index in ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']:                 
            btn = Button(text=index, size_hint_y=None, size_hint_x=None, font_size=40, height=64, width=200)
            btn.bind(on_release=lambda btn: (dropdown.select(btn.text), vivod_sotrudnikov()))      
            dropdown.add_widget(btn)               
        mainbutton = Button(text='выберите месяц', font_size=40, size_hint=(1, 1)) #pos_hint: {"top": 1})                
        mainbutton.bind(on_release=lambda btn: dropdown.open(btn)) 
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))  
        
        years = [int(y)-2, int(y)-1, int(y), int(y)+1, int(y)+2, int(y)+3, int(y)+4]        
        for year in years:
            btn1= Button(text=str(year), size_hint_y=None, size_hint_x=None, font_size=40,height=64, width=200)
            btn1.bind(on_release=lambda btn1: (dropdownyear.select(btn1.text), vivod_sotrudnikov()))
            dropdownyear.add_widget(btn1)
        yearbutton = Button(text='выберите год', font_size=40, size_hint=(1, 1))
        yearbutton.bind(on_release=lambda btn1: dropdownyear.open(btn1))
        dropdownyear.bind(on_select=lambda instance, x: setattr(yearbutton, 'text', x))  
        laybutton.add_widget(mainbutton)    
        laybutton.add_widget(yearbutton) 
        def delete_all():
            h_layout = BoxLayout(orientation="vertical", padding=1, size_hint=(1, 1))
            an_layout = BoxLayout(orientation="horizontal", padding=1, size_hint=(1, 1))
            label = Label(text='вы уверены, что хотите\nудалить всю информацию?', font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])     
            yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
            no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)        
            an_layout.add_widget(yes)
            an_layout.add_widget(no)
            yes.on_press=lambda: (dele(), close(),clear_all())
            no.on_press=lambda: (close())
            def close():
                popupWindow.dismiss()        
            popupWindow = Popup(title="внимание!", size_hint=(None,None),size=(750,320), pos_hint={'x': 0.0 / Window.width, 'y': 500.0 / Window.height})
            h_layout.add_widget(label)
            h_layout.add_widget(an_layout)
            popupWindow.add_widget(h_layout)
            popupWindow.open()
            def dele():
                with open('tabel_sotrudnikov.txt', 'w'):
                    popupWindow = PopupX('часы за все месяцы\nуспешно удалены!')
                                                    
        def create_tabel():
            m=mainbutton.text
            y=yearbutton.text
            m_y = m + ' ' + y + 'г.'
            sp = ['СветаВ', 'АйнураЖ','АллаЧ','РозаФ','СашаВ','ВасилийД','НазарЧ','ЗакирШ','СергейК','ИгорьБ']
            hours = ''
            for i in range(31):              
                hours = hours + '-'        
            with open('tabel_sotrudnikov.txt', 'a+') as k:
                                for chel in sp:
                                    k.write(m_y + ' ' + chel + ' ' +  hours +'\n' )                                                        
                                popupWindow = PopupX('табель на ' + m_y + '\nуспешно создан!')        
            vivod_sotrudnikov()
            
        def clear_all():           
            yearbutton.text = 'выберите год'
            mainbutton.text = 'выберите месяц'
            self.month_choose = False
            for i in range(4):               
                itog[i+1].text = ''
                for j in range(32):
                    num[j, i+1].text= ''
                    num[j, i+1].background_color= [1,1,1,1]
                    if i == 0:
                        num[j,i].text = str(j+1)
                        if j == 31:
                            num[j,i].text = 'Итог'
                    
        def vivod_sotrudnikov():
            mo= { 'январь':'1','февраль':'2', 'март':'3', 'апрель':'4',  'май':'6',  'июнь':'6', 'июль':'7',  'август':'8', 'сентябрь':'9','октябрь':'10', 'ноябрь':'11', 'декабрь':'12'}       
            day_week = {'1':'пн', '2':'вт','3':'ср','4':'чт','5':'пт','6':'сб','7':'вс'}
            month = mainbutton.text            
            year = yearbutton.text
            data = month + ' ' + year + 'г.'
            print('data=', data)
            j = 0
            if year != 'выберите год' and  month != 'выберите месяц':
                py=year
                pm=month
                with open('tabel_sotrudnikov.txt', 'r') as k:
                    f =k.read() 
                    if data in f:                                          
                        sp_all = f.splitlines()                      
                        if self.month_choose == False:
                            for i in range(len(sp_all)):
                                s = sp_all[i].split()
                                print(s)                                
                                if data == s[0] + ' ' +s[1]:                       
                                        j = j+1                      
                                        entry[j,1].text = s[2]
                                        h = s[3].split('-')                                     
                                        for i1 in range(32):
                                            if i1<31:
                                                try:
                                                    day = datetime.datetime(int(year), int(mo[month]), i1+1)            
                                                    weekend = day.isoweekday() 
                                                    num[i1, j].text = h[i1]
                                                except ValueError: #day is out of range for month
                                                    pass
                                                if weekend == 6 or weekend == 7:
                                                    num[i1, j].background_color= [1,1,0.5,1]
                                            if i1 == 31:
                                                itog[j].text = h[i1]
                                                num[i1, j].text = h[i1]
                            for i1 in range(31):       
                                try:                        
                                    day = datetime.datetime(int(year), int(mo[month]), i1+1)
                                    weekend = day.isoweekday()  
                                    num[i1,0].text = num[i1,0].text + day_week[str(weekend)] 
                                except ValueError:
                                    pass
                            self.month_choose = True
                        else:                          
                            y =yearbutton.text
                            m =mainbutton.text 
                            clear_all()
                            yearbutton.text=y
                            mainbutton.text=m 
                            vivod_sotrudnikov()                                                           
                    else:                        
                        h_layout = BoxLayout(orientation="vertical", padding=1, size_hint=(1, 1))
                        an_layout = BoxLayout(orientation="horizontal", padding=1, size_hint=(1, 1))
                        label = Label(text='на '+data+'  нет табеля!\nсоздать табель на ' + data+ '?', font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])     
                        yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
                        no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)        
                        an_layout.add_widget(yes)
                        an_layout.add_widget(no)
                        yes.on_press=lambda: (create_tabel(), close())
                        no.on_press=lambda: (clear_all(), close())
                        def close():
                            popupWindow.dismiss()        
                        popupWindow = Popup(title="внимание!", size_hint=(None,None),size=(750,320), pos_hint={'x': 0.0 / Window.width, 'y': 500.0 / Window.height})
                        h_layout.add_widget(label)
                        h_layout.add_widget(an_layout)
                        popupWindow.add_widget(h_layout)
                        popupWindow.open()                                                                                                                                                              
        def setka(i1, i2):
            #для списка сотрудников
            for i in range(i1, i2):
                h_layout = BoxLayout(height=31, size_hint=(1, 1))
                for j in range(3):
                    if j == 0 or  j == 2:
                        but[i, j] = Button(text='+', halign="center", font_size=28, size_hint=(None, 1), width=50)                        
                        if j == 2:
                            butt_add(i,j)
                        if j == 0:
                            but[i, j].text = str(i) 
                            if i == col1:
                                but[i, j].text = 'N°'
                        if j ==2 and i == col1:
                           but[i, j].text = '' 
                        h_layout.add_widget(but[i, j])
                    else:
                        entry[i, j] = LabelX(halign="center", font_size=35, size_hint=(1, 1),  color=[0, 0, 0, 1], width=50, text='')#multiline=False, cursor_color=[0, 0, 1, 1],                       
                        entry[i, j].set_bgcolor(1,1,1,1)
                        h_layout.add_widget(entry[i, j])
                        if j == 1:
                            entry[i, j].markup=True
                            entry[i, j].width = 240
                            entry[i, j].foreground_color = [0, 0, 1, 1]                            
                            if i%2==0:
                                entry[i, j].set_bgcolor(1,.5,1,1)     
                            if i == col1:
                                entry[i,j].text = 'Сотрудники'
                                entry[i,j].font_size = 38
                                entry[i,j].color = [0, 0, 1, 1]                                         
                layoutgr.add_widget(h_layout)
            # для часов по дням в мeсяце
            for i in range(32):
                h_layout = BoxLayout(orientation="vertical", size_hint=(None, 1))#height=794,
                for j in range(i1, i2):
                    num[i,j]= TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=30, size_hint=(1, 1),  width=60, multiline=False, text='')    
                    h_layout.add_widget(num[i,j])                                
                    if j == 0:
                        num[i,j].foreground_color = [0, 0, 1, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        num[i,j].text = str(i+1)
                        num[i,j].font_size = 30
                    if i == 31:                                 
                        num[i,j].font_size = 30
                        num[i,j].foreground_color = [1, 0, 0, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        if j == 0:
                            num[i,j].text = 'Итог'       
                        if i == 31:
                            num[i,j].width=70                  
                layout.add_widget(h_layout) 
            for i in range(i2):                  
                  itog[i] = LabelX(halign="right", height=61, width= 130, font_size=35, size_hint=(1, 1), color=[1, 0 ,0, 1])
                  itog[i].set_bgcolor(1,1,1,1) 
                  layout_itog.add_widget(itog[i]) 
                  if i%2==0:
                      itog[i].set_bgcolor(1,.5,1,1)                
                  if i == 0:
                        itog[i].text = 'Итог'       
        
        def butt_add(i,j):
            but[i, j].on_press=lambda: add(i, j)
        def add(r, c):
            print(str(r) + '-' + str(c))             
            m=mainbutton.text
            y=yearbutton.text
            m_y = m + ' ' + y + 'г.'
            print(entry[r, c-1].text)
            print(num[0, r].text)
            k = 0
            print('k=', k)
            hours = ''
            if entry[r, c-1].text=='':
                pass
            else:
                for i in range(32):
                    if i != 31:                   
                        try:
                            k= k+float(num[i, r].text)
                            print('k=', k)                      
                        except ValueError:
                            pass
                        hours = hours + num[i, r].text + '-'
                    else:                  
                        hours = hours +str(k)
                sotrudnik =entry[r, c-1].text     
                with open("tabel_sotrudnikov.txt", "r") as f:
                    lines = f.readlines()                
                    with open("tabel_sotrudnikov.txt", "w") as f1:                    
                        for line in lines:                     
                            if m_y + ' ' + sotrudnik in line:                            
                                new_line = m_y + ' ' + sotrudnik + ' ' + hours + '\n'    
                                print('new_line=',new_line)                            
                                f1.write(new_line)    
                            else:
                                f1.write(line)                                          
                    if m_y == 'выберите месяц выберите годг.' :
                        pass
                    else:                      
                        popupWindow = PopupX('часы успешно добавлены!')                   
        but = {} 
        entry = {}
        num = {}
        itog ={}
        setka(col1, col2) 
        
        root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root.add_widget(layout)        
        #root1= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        #root1.add_widget(layoutgr)
        
        lay0.add_widget(layoutgr)#список сотрудников
        lay0.add_widget(root)# даты
        lay0.add_widget(layout_itog)
        #layfor0.add_widget(lay0)
        
   
        lay.add_widget(lab1)    
        lay.add_widget(laybutton)
        lay.add_widget(lay0)        
        lay.add_widget(lay1)            
        return  lay
if __name__ == '__main__':
    MainApp().run()