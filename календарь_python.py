from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime
from datetime import timedelta
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from calendar import monthrange

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
        
class CalendarLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.cols = 7  # Set the number of columns for the calendar       
        col_day = { '01':31, '02':28}
        self.mo= { 'январь':'1','февраль':'2', 'март':'3', 'апрель':'4',  'май':'6',  'июнь':'6', 'июль':'7',  'август':'8', 'сентябрь':'9','октябрь':'10', 'ноябрь':'11', 'декабрь':'12'}   
        self.day_week = {'1':'пн', '2':'вт','3':'ср','4':'чт','5':'пт','6':'сб','7':'вс'}
        self.days = {'0':'пн', '1':'вт', '2':'ср', '3':'чт', '4':'пт', '5':'сб', '6':'вс'}
        self.month = ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
        self.orientation="vertical"
        self.padding=0
        self. size_hint=(1, 1)
        self.layoutcalendar = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 1))
        self.layout_num_week = BoxLayout(orientation="vertical", padding=0, size_hint=(.1, 1))
        self.layout_day = BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        self.layoutgr= GridLayout(cols=7, spacing=0, size_hint=(1, 1))
        self.layoutweek= GridLayout(cols=7, spacing=0, size_hint=(1, .08))
        layoutdata = BoxLayout(orientation="vertical", padding=0, size_hint=(1, .1))
        layoutdata1 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        addbutton = Button(text='внести \nизменения', background_color= [.6,0,0.5,1],background_normal='',  font_size=40, size_hint=(1, 1))
        
        self.sumprint = LabelX(color =[1,0,0,1], halign = 'right', font_size=50, size_hint=(1, 1))
        self.sumprint.set_bgcolor(1,0,1,.8)
        
        self.sumprint.text='всего часов: '+'\n'
        layoutadd_sum = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        layoutadd_sum.add_widget(addbutton)
        layoutadd_sum.add_widget(self.sumprint)
        self.lay2layout = {}  
        lay2 = LabelX(halign="center", text='', font_size=50, size_hint=(1, None), height=60, color=[0, 0 ,0, 1])
        self.layout_num_week.add_widget(lay2)
        lay2.set_bgcolor(1,1,1,.8)
        
        print('сегодня=неделя =', datetime.datetime.now().isocalendar().week)
        num = datetime.datetime.now().isocalendar().week
        current_month =datetime. datetime.now().month
        current_year = datetime.datetime.now().year
        n = datetime.date(current_year, current_month, 1).isocalendar().week
        print('неделя первого дня месяца=', n)
        
        '''for day in range(6):           
                self.lay2layout[day] =BoxLayout(orientation="vertical",height=60, size_hint=(1, .5))     
                lay3 = LabelX(halign="center", text=str(n), font_size=50, size_hint=(1, 1), color=[0, 0 ,0, 1])
                lay3.set_bgcolor(1,1,1,.8)
                n +=1
                self.lay2layout[day].add_widget(lay3)
                self.layout_num_week.add_widget(self.lay2layout[day])'''
        
        self.btnbottom = Button(text='', font_size=40, size_hint=(1, .3),  background_color= [.8,0,.8,1] )
        current_year = datetime.datetime.now().year       
        days = monthrange(current_year, 3) [1]
        print(current_year)
        print(days)
        today = datetime.datetime.now()
        #print((datetime.datetime.now() – datetime.timedelta(1)).strftime('%Y-%m-%d'))
        pred_data= (today -timedelta(1)).strftime('%Y-%m-%d')
        print('pred_data=', pred_data)
        #today = datetime.date.today()
        
        first = today.replace(day=1)
        last_month = first - timedelta(days=1)
        pred_month=last_month.strftime("%m")
        print('pred_month=', pred_month)
        current_year = datetime.datetime.now().year       
        days = monthrange(current_year, int(pred_month)) [1]
        print(days)
        
        print(today.isoweekday())
        data = today.strftime("%m-%y")        
        y = '20' + data[3:5]
        print(y)
        m = data[0:2]
        print(m)
        if m == '01':            
            pred_mon= self.month[11]
        else:
            pred_mon= self.month[int(m)-2]
        mon = self.month[int(m)-1]
        print(mon)
        print(pred_mon)
        #day1 = datetime.datetime(int(y), int(self.mo[m]), 1)
        #self.month_choose = False      
        
        self.but = {}
        self.entry = {}
        self.h_layout2 = {}
        self.lay1layout = {}  
        self.first = 0
        self.last = 0
        self.strokajest = False 
        dropdown = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        dropdownyear = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        for index in self.month:                 
            btn = Button(text=index, size_hint_y=None, size_hint_x=None, font_size=40, height=64, width=200, background_color=[.8,0,.8,1] )
            btn.bind(on_release=lambda btn: (dropdown.select(btn.text), self.vivod_calendar()))      
            dropdown.add_widget(btn)               
        self.mainbutton = Button(text = mon,  background_color= [.8,0,.8,1] , font_size=40, size_hint=(1, 1)) #pos_hint: {"top": 1})                
        self.mainbutton.bind(on_release=lambda btn: dropdown.open(btn)) 
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))  
        
        years = [int(y)-2, int(y)-1, int(y), int(y)+1, int(y)+2, int(y)+3, int(y)+4]        
        for year in years:
            btn1= Button(text=str(year), background_color= [.8,0,.8,1] , size_hint_y=None, size_hint_x=None, font_size=40,height=64, width=200)
            btn1.bind(on_release=lambda btn1: (dropdownyear.select(btn1.text), self.vivod_calendar()))
            dropdownyear.add_widget(btn1)
        self.yearbutton = Button(text=y, background_color= [.8,0,.8,1] , font_size=40, size_hint=(1, 1))
        self.yearbutton.bind(on_release=lambda btn1: dropdownyear.open(btn1))
        dropdownyear.bind(on_select=lambda instance, x: setattr(self.yearbutton, 'text', x))  
        layoutdata1.add_widget(self.mainbutton)    
        layoutdata1.add_widget(self.yearbutton) 
        layoutdata.add_widget(layoutdata1) 
        for day in range(7):           
                self.lay1layout[day] =BoxLayout(orientation="horizontal",height=60, size_hint=(1, .5))     
                lay1 = LabelX(halign="center", text=self.days[str(day)], font_size=50, size_hint=(1, 1), color=[0, 0 ,0, 1])
                lay1.set_bgcolor(1,1,1,.8)
                self.lay1layout[day].add_widget(lay1)
                self.layoutweek.add_widget(self.lay1layout[day])
        #self.layoutcalendar.add_widget(self.layoutgr)
        self.layoutcalendar.add_widget(self.layout_num_week)
        self.layoutcalendar.add_widget(self.layout_day)
        self.layout_day.add_widget(self.layoutweek)
        self.layout_day.add_widget(self.layoutgr)
        self.vivod_calendar()
        #self.vivod_chasov()       
        
        self.add_widget(layoutdata)
        #self.add_widget(self.layoutweek)
        self.add_widget(self.layoutcalendar)
        #self.add_widget(layoutadd_sum)
        self.add_widget(self.btnbottom)
        
        addbutton.bind(on_press=lambda ad: self.addchanges())    
            
    def clear(self):
        self.strokajest = False
        self.layoutcalendar.clear_widgets()
        self.layoutcalendar.add_widget(self.layout_num_week)
        self.layoutcalendar.add_widget(self.layout_day)
        #self.layoutcalendar.add_widget(self.layoutgr)
        if self.h_layout2 != {}:
            for day in range(6):  
                self.layout_num_week.remove_widget(self.lay2layout[day])
            for day in range(7):  
                self.layoutgr.remove_widget(self.lay1layout[day])
            for i in range(1,43):
                self.layoutgr.remove_widget(self.h_layout2[i])
                                                                               
    def vivod_calendar(self):           
        self.clear()
        day3 = 1
        year = self.yearbutton.text
        month = self.mainbutton.text
        print('mo[month]=', self.mo[month])
        n = datetime.date(int(year), int(self.mo[month]), 1).isocalendar().week
        print('неделя первого дня месяца=', n)
        
        for day in range(6):           
                self.lay2layout[day] =BoxLayout(orientation="vertical",height=60, size_hint=(1, .5))     
                lay3 = LabelX(halign="center", text=str(n), font_size=50, size_hint=(1, 1), color=[0, 0 ,0, 1])
                lay3.set_bgcolor(1,1,1,.8)
                n +=1
                self.lay2layout[day].add_widget(lay3)
                self.layout_num_week.add_widget(self.lay2layout[day])
        
        m_y =month + ' ' +year                               
        if year != 'выберите год' and  month != 'выберите месяц':                                            
            day1 = datetime.datetime(int(year), int(self.mo[month]), 1)                     
            print('сегодня=', day1)
            weekend1 = day1.isoweekday()  
            print(weekend1)
            c = weekend1-2
            den_nedely = self.day_week[str(weekend1)]
            print(den_nedely)
            for day in range(1, 43 ):                               
                self.h_layout2[day] = BoxLayout(orientation="vertical",height=60, size_hint=(1, 1))                
                self.but[day] = LabelX(text='' ,  font_size = 65, height=130, width=100, size_hint=(None, None)) 
                self.but[day].set_bgcolor(1,1,1,1) 
                #self.but[day].background_down=''
                self.h_layout2[day].add_widget(self.but[day])                
                self.layoutgr.add_widget(self.h_layout2[day])       
                if day < weekend1:        
                    self.first = day+1
                    #self.h_layout2[day].remove_widget(self.entry[day])                              
                    #print(c)
                    today = datetime.datetime.now()
                    print('today=', today)
                    first = today.replace(day=1)
                    last_month = first - timedelta(days=1)
                    pred_month=last_month.strftime("%m")
                    print('pred_month=', pred_month)
                    current_year = datetime.datetime.now().year       
                    self.days = monthrange(current_year, int(pred_month)) [1]
                    print('дней в месяце=', self.days)
                    day0 = self.days-c
                    #print('day=', day)
                    self.but[day].text=str(day0)
                    self.but[day].color = [0, 0 ,0, .2]
                    c -= 1                                              
                else:
                    try:                                                                         
                        day1 = datetime.datetime(int(year), int(self.mo[month]), day-weekend1+1)
                        now = datetime.datetime.now()
                        data = now.strftime("%d ")
                        day2 =str(day-weekend1+1)
                        last = day-weekend1+1
                        print('day2=',day2)
                        print('data=', data[0:])
                        current_month =datetime. datetime.now().month
                        current_year = datetime.datetime.now().year
                        
                        weekend = day1.isoweekday()  
                        print(str(day-weekend1+1)+self.day_week[str(weekend)] )
                        if weekend == 6 or weekend == 7:                                                     
                            self.but[day].set_bgcolor(.4,.3,0,1)
                            
                            self.but[day].text= str(day-weekend1+1)#+self.day_week[str(weekend)]        
                        else:   
                            self.but[day].color = [0, 0 ,0, 1]
                            self.but[day].set_bgcolor(.9,0,0.9,1)
                            self.but[day].text= str(day-weekend1+1)#+self.day_week[str(weekend)] 
                        #print('мы тут')
                       
                        if current_year == int(year):
                            if current_month == int(self.mo[month]):
                                if int(day2) == int(data[0:]):
                                    print('совпало')
                                    self.but[day].set_bgcolor(0,1,0,1)    
                            
                    except ValueError:                            
                                          
                        #print('ValueError')                       
                        self.but[day].text=str(day3)
                        self.but[day].color = [0, 0 ,0, .2]
                        day3 += 1
                        if day == 34 or day == 35:
                            self.but[day].set_bgcolor(1,1,1,.8)
                        if day == 41 or day == 42:
                            self.but[day].set_bgcolor(1,1,1,.8)
                                                                                                                          
class CalendarApp(App):
    def build(self):     
        return CalendarLayout()
if __name__ == '__main__':
    CalendarApp().run()