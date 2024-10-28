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
        
class BoxLayoutX(BoxLayout):
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
        col1 = 0
        col2= 5
        lay= BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        lay0 = BoxLayoutX(orientation="horizontal", padding=0, size_hint=(1, 1))
        lay0.set_bgcolor(0.8,.8,1,1)
        laytop= BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay1 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .3))
        layoutgr= GridLayout(cols=1, spacing=0, size_hint=(1, None))
        layout_itog = GridLayout(cols=1, spacing=0, size_hint=(.2, 1))
        layout = GridLayout(rows=1,  spacing=0, size_hint_x=None)#, size_hint_x=None)
        #new_spisok = Button(text='[b]>>[/b]', font_size=22, size_hint=(.87, 1), markup=True)
        copy = Button(text='', markup=True, font_size=28, size_hint=(1, 1), color=[1, 1, 0, 1])
        clear = Button(text='очистить', font_size=40, size_hint=(1, 1))
        
        laybutton=BoxLayoutX(size_hint=(1, .3))
        laybutton.set_bgcolor(.8,.8,1,1)
        lab1 = LabelX(halign="center", text='', font_size=50, size_hint=(1, .5), color=[0, 0 ,0, 1])
        lab1.set_bgcolor(.8,.8,1,1)
        #laybutton.add_widget(lab1)
        #laybutton= FloatLayout(size=(100, 200))
        lay1.add_widget(copy)
        lay1.add_widget(clear)
        clear.on_press = lambda: clear_all()
        #lay1.add_widget(laybutton)
        #laytop.add_widget(new_spisok)
        # Make sure the height is such that there is something to scroll.
        layoutgr.bind(minimum_height=layoutgr.setter('height'))
        layout.bind(minimum_width=layout.setter('width'))
        #layout_itog.bind(minimum_width=layout.setter('width'))
        y=2024
        m= 5
        d = 7
        day = datetime.datetime(y, m, d)
        da = day.strftime("%d-%m-%Y")
        print(da)
        today = datetime.datetime.now()
        print(today.isoweekday())
        data = today.strftime("%m-%y")
        month = {'01': 'январь','02': 'февраль', '10':'октябрь'}
        m_y = month[data[0:2]]+' 20' + data[3:5] + 'г.'
        y = ' 20' + data[3:5]
        self.month_choose = False
        
        dropdown = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        dropdownyear = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        for index in ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
        
            btn = Button(text=index, size_hint_y=None, size_hint_x=None, font_size=40, height=64, width=200)
        
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
        years = [int(y)-2, int(y)-1, int(y), int(y)+1, int(y)+2, int(y)+3, int(y)+4]
        for year in years:
            btn1= Button(text=str(year), size_hint_y=None, size_hint_x=None, font_size=40,height=64, width=200)
            btn1.bind(on_release=lambda btn1: (dropdownyear.select(btn1.text), vivod_sotrudnikov()))
            dropdownyear.add_widget(btn1)
        yearbutton = Button(text='выберите год', font_size=40, size_hint=(.6, .6))
        yearbutton.bind(on_release=lambda btn1: dropdownyear.open(btn1))
        dropdownyear.bind(on_select=lambda instance, x: setattr(yearbutton, 'text', x))  
        laybutton.add_widget(mainbutton)    
        laybutton.add_widget(yearbutton) 
        
        def create_tabel():
            m=mainbutton.text
            y=yearbutton.text
            m_y = m + ' ' + y + 'г.'
            hours = ''
            for i in range(31):              
                hours = hours + '-'        
            with open('tabel_sotrudnikov.txt', 'a+') as k:
                                k.write(m_y + ' ' + 'мои_часы' + ' ' +  hours +'\n' )
                                k.write(m_y + ' ' + 'часы_1' + ' ' +  hours +'\n' )
                                k.write(m_y + ' ' + 'часы_2' + ' ' +  hours +'\n' )
                                k.write(m_y + ' ' + 'часы_3' + ' ' +  hours +'\n' )
                                label = Label(text='табель на ' + m_y + '\nуспешно создан!', font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])      
                                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,220), pos_hint={'x': 50.0 / Window.width, 'y': 600.0 / Window.height})
                                popupWindow.add_widget(label)
                                popupWindow.open()    
        def clear_all():
            #global month_choose
            yearbutton.text = 'выберите год'
            mainbutton.text = 'выберите месяц'
            self.month_choose = False
            for i in range(4):
               #entry[i+1, 1].text = ''
                itog[i+1].text = ''
                for j in range(32):
                    num[j, i+1].text= ''
                    num[j, i+1].background_color= [1,1,1,1]
                    if i == 0:
                        num[j,i].text = str(j+1)
                        if j == 31:
                            num[j,i].text = 'Итог'
                    
        def vivod_sotrudnikov():
            #global month_choose
            mo= { 'январь':'1','февраль':'2', 'март':'3', 'апрель':'4',  'май':'6',  'июнь':'6', 'июль':'7',  'август':'8', 'сентябрь':'9','октябрь':'10', 'ноябрь':'11', 'декабрь':'12'}       
            day_week = {'1':'пн', '2':'вт','3':'ср','4':'чт','5':'пт','6':'сб','7':'вс'}
            month = mainbutton.text            
            year = yearbutton.text
            data = month + ' ' + year + 'г.'
            print('data=', data)
            j = 0
            if year != 'выберите год' and  month != 'выберите месяц':
                #clear_all()
                py=year
                pm=month
                with open('tabel_sotrudnikov.txt', 'r') as k:
                    f =k.read() 
                    if data in f:
                        print('data estj')                    
                        sp_all = f.splitlines()
                        print(sp_all)
                        if self.month_choose == False:
                            for i in range(len(sp_all)):
                                s = sp_all[i].split()
                                print(s)
                                print(s[0] + ' ' +s[1])
                                if data == s[0] + ' ' +s[1]:                       
                                        j = j+1                      
                                        entry[j,1].text = s[2]
                                        h = s[3].split('-')
                                        print(h)
                                        for i1 in range(32):
                                            if i1<31:
                                                try:
                                                    day = datetime.datetime(int(year), int(mo[month]), i1+1)
                                                    #da = day.strftime("%d-%m-%Y")
                                                    #print(day)     
                                                    weekend = day.isoweekday()  
                                                    #print(day.isoweekday())                         
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
                            #yearbutton.text = 'выберите год' 
                            #mainbutton.text  = 'выберите месяц'
                            y =yearbutton.text
                            m =mainbutton.text 
                            clear_all()
                            yearbutton.text=y
                            mainbutton.text=m 
                            vivod_sotrudnikov()
                            '''label = Label(text='выберите  ' + data, font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                            popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,220), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                            popupWindow.add_widget(label)
                            popupWindow.open()       '''   
                                
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
                        popupWindow = Popup(title="внимание!", size_hint=(None,None),size=(750,320), pos_hint={'x': 40.0 / Window.width, 'y': 600.0 / Window.height})
                        h_layout.add_widget(label)
                        h_layout.add_widget(an_layout)
                        popupWindow.add_widget(h_layout)
                        popupWindow.open()                                                                                                                                                              
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
                        entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50, size_hint=(1, 1),  width=50, multiline=False, text='часы_'+str(i-1))
                        #entry[i, j].set_bgcolor(1,1,1,1)
                        h_layout.add_widget(entry[i, j])
                        if j == 1:
                            entry[i, j].markup=True
                            entry[i, j].width = 240
                            entry[i, j].foreground_color = [0, 0, 1, 1]
                            if i == 1:
                               entry[i,j].text = 'мои_часы'
                            if i == col1:
                                entry[i,j].text = ''
                                entry[i,j].foreground_color = [0, 0, 1, 1]
                                entry[i,j].background_color = [1,1,0.5,1]            
                layoutgr.add_widget(h_layout)
            # для часов по дням в мнсяце
            for i in range(32):
                h_layout = BoxLayout(height=305,orientation="vertical", size_hint=(None, None))
                for j in range(i1, i2):
                    num[i,j]= TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50, size_hint=(1, 1),  width=60, multiline=False, text='')    
                    h_layout.add_widget(num[i,j])                                
                    if j == 0:
                        num[i,j].foreground_color = [0, 0, 1, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        num[i,j].text = str(i+1)
                        num[i,j].font_size = 40
                    if i == 31:                                 
                        num[i,j].font_size = 40
                        num[i,j].foreground_color = [1, 0, 0, 1]
                        num[i,j].background_color = [1,1,0.5,1]
                        num[i,j].markup=True
                        if j == 0:
                            num[i,j].text = 'Итог' 
                        #layout_itog.add_widget(h_layout)
                layout.add_widget(h_layout) 
            for i in range(5):
                  #itog[i]= TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=50,height=61, #size_hint=(None, None),  width=100, multiline=False, text='')#,  size_hint_x=1, size_hint_y=1) 
                  itog[i] = LabelX(halign="right", height=61, width= 80, font_size=30, size_hint=(None, None), color=[1, 0 ,0, 1])
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
            #print(m_y)
            m=mainbutton.text
            y=yearbutton.text
            m_y = m + ' ' + y + 'г.'
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
            
                label = Label(text='часы успешно добавлены!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()    
        but = {} 
        entry = {}
        num = {}
        itog ={}
        setka(col1, col2) 
        
        root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root.add_widget(layout)
        #root_itog= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        #root_itog.add_widget(layout_itog)
        root1= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root1.add_widget(layoutgr)
        lay0.add_widget(root1)#список сотрудников
        lay0.add_widget(root)# даты
        lay0.add_widget(layout_itog)
        
        #lay.add_widget(laytop)
        lay.add_widget(laybutton)
        lay.add_widget(lay0)        
        lay.add_widget(lay1)
        lay.add_widget(lab1)
        
        return  lay

if __name__ == '__main__':
    MainApp().run()
