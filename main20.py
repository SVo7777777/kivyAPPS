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
from kivy.uix.screenmanager import ScreenManager, Screen


class LabelX(Label):
    def set_bgcolor(self, r, b, g, o):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(r, g, b, o)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect,
                  size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class PopupX(Popup):
    def __init__(self, text1, **kwargs):
        super(PopupX, self).__init__(**kwargs)
        label = Label(text=text1, font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])
        self.title = 'внимание!'
        self.size_hint = (None, None)
        self.size = (700, 220)
        self.pos_hint = {'x': 0.0 / Window.width, 'y': 500.0 / Window.height}
        self.add_widget(label)
        self.open()


class MainApp(App):
    def build(self):
        sm.add_widget(SpisokScreen('spisok',3))
        sm.add_widget(TabelScreen('tabel', 1))#self.ks + 1))
        return sm


class SpisokScreen(Screen):
    def __init__(self, name, col2,**kwargs):
        super(SpisokScreen, self).__init__(**kwargs)
        self.name = name
        # setting the screen name value for the screen manager
        # (it's more convenient to call by name rather than by class)
        # self.id = 'main'
        # main = ObjectProperty(None)
        # second = ObjectProperty(None)
        self.col1 = 0
        self.col2 = col2
        # tabel = Tabel()
        # tabel.build(0,21)
        today = datetime.datetime.now()
        data = today.strftime("%m-%y")
        month = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль',
                 '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
        self.m_y = month[data[0:2]] + ' 20' + data[3:5] + 'г.'
        m_y1 = month[data[0:2]] + '\n20' + data[3:5] + 'г.'
        print(month)
        print(month[data[0:2]])
        self.spisik_estj = False
        self.crsp = False
        self.ks = 1
        print(self.spisik_estj)
        print(self.crsp)
        with open("tabel_sotrudnikov.txt", "r") as f:
            r = f.read()
            sp_all = r.splitlines()
            self.ks = len(sp_all)
            print(self.ks)
            if self.m_y in r:
                self.spisik_estj = True
            # self.show_spisok()

        lay = BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        label = LabelX(halign="center", font_size=40, padding=0, size_hint=(1, .2), color=[0, 0, 0, 1])
        label.set_bgcolor(1, 1, 1, 1)
        label.text = 'Внесите сотрудника , нажимая на "+".\nУдалите сотрудника , нажимая на "-".'
        lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 1))
        self.layoutgr = GridLayout(cols=1, spacing=0, size_hint=(1, None))
        self.layoutgr.bind(minimum_height=self.layoutgr.setter('height'))
        self.layoutgr.bind(minimum_width=self.layoutgr.setter('width'))
        lay_01 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay_0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay_1 = BoxLayout(orientation="vertical", padding=0, size_hint=(.5, 1))
        self.lay1 = LabelX(halign="center", text='', font_size=50, size_hint=(1, 1), color=[0, 0, 0, 1])
        self.lay1.set_bgcolor(1, 1, 1, 1)
        self.lay1.text = 'Сегодня\n' + m_y1
        hide = Button(text='скрыть список\nсотрудников', markup=True, font_size=28, size_hint=(1, 1),
                      color=[1, 1, 0, 1])
        show = Button(text='показать список\nсотрудников', font_size=28, size_hint=(1, 1))
        show_tabel = Button(text='перейти к \nтабелю', font_size=28, size_hint=(1, 1))
        b1 = Button(text='создать список', markup=True, font_size=28, size_hint=(1, 1), color=[1, 1, 0, 1])
        b2 = Button(text='какой сегодня \nмесяц', font_size=28, size_hint=(1, 1))
        delete_all = Button(text='удалить\n всю \nинформацию', font_size=28, size_hint=(1, 1))
        lay_1.add_widget(self.lay1)
        lay_0.add_widget(show)
        lay_0.add_widget(hide)
        lay_0.add_widget(show_tabel)
        lay_01.add_widget(b1)
        lay_01.add_widget(b2)
        lay_01.add_widget(delete_all)

        b1.on_press = lambda: create_spisok()
        b2.on_press = lambda: show_month()
        show.on_press = lambda: self.show_spisok()
        hide.on_press = lambda: hide_spisok()
        show_tabel.on_press = lambda: self.to_tabel_screen()

        def create_spisok():
            # global crsp, spisik_estj

            # self.crsp = True
            self.show_spisok()
            print(self.spisik_estj)
            with open("tabel_sotrudnikov.txt", "r") as f:
                r = f.read()
                if r == '':
                    self.lay1.text = 'введите\nсотр-ов\nкак \nсказано\nвыше\n'
                else:
                    if self.spisik_estj == False:
                        print(self.ks)
                        for i in range(1, self.ks + 1):
                            print(self.ks)
                            add(i, 2)
                        self.spisik_estj = True
                        self.crsp = False
                        label = Label(text='список на этот месяц \nуспешно  создан!!', font_size=42, size_hint=(1, 1),
                                      color=[1, 0, 0, 1])
                        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 220),
                                            pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                        popupWindow.add_widget(label)
                        popupWindow.open()
                    else:
                        label = Label(text='список на этот  месяц уже \nсуществует!!', font_size=42, size_hint=(1, 1),
                                      color=[1, 0, 0, 1])
                        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 220),
                                            pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                        popupWindow.add_widget(label)
                        popupWindow.open()

        def show_month():
            # global spisik_estj

            today = datetime.datetime.now()
            data = today.strftime("%m-%y")
            month = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь',
                     '07': 'июль', '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
            m_y = month[data[0:2]] + ' 20' + data[3:5] + 'г.'
            m_y1 = month[data[0:2]] + '\n20' + data[3:5] + 'г.'
            self.lay1.text = 'Сегодня\n' + m_y1
            with open("tabel_sotrudnikov.txt", "r") as f:
                r = f.read()
                lines = f.readlines()
                if r == '':
                    self.lay1.text = self.lay1.text + '\nвведите\nсотр-ов\nкак \nсказано\nвыше\n'
                else:
                    print('тут')
                    # for line in lines:
                    # print('месяц и год', m_y)
                    if m_y in r:
                        print(m_y)
                        # print(line)
                        self.lay1.text = self.lay1.text + '\nсписок\nесть '
                        self.spisik_estj = True
                        self.crsp = False
                        print(self.spisik_estj)
                        # break
                    else:
                        self.lay1.text = self.lay1.text + '\nсоздайте\nсписок\nна этот\nмесяц'
                        self.spisik_estj = False
                        self.crsp = True
                        # show_spisok()
                        # break

        def hide_spisok():
            for i in range(12):
                self.entry[i + 1, 1].text = ''

        

        def butt_del(i, j):
            self.but[i, j].on_press = lambda: delete(i, j)

        def delete(r, c):
            if self.entry[r, c - 2].text == '':
                pass
            else:
                h_layout = BoxLayout(orientation="vertical", padding=1, size_hint=(1, 1))
                an_layout = BoxLayout(orientation="horizontal", padding=1, size_hint=(1, 1))
                yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
                no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
                an_layout.add_widget(yes)
                an_layout.add_widget(no)
                yes.on_press = lambda: (dele(r, c), close())
                no.on_press = lambda: (close())

                def close():
                    popupWindow.dismiss()

                popupWindow = Popup(title="Вы уверены, что хотите удалить? ", size_hint=(None, None), size=(400, 220),
                                    pos_hint={'x': 200.0 / Window.width, 'y': 800.0 / Window.height})
                h_layout.add_widget(an_layout)
                popupWindow.add_widget(h_layout)
                popupWindow.open()

                def dele(r, c):
                    print(str(r) + '-' + str(c))
                    print(self.entry[r, c - 2].text)
                    sotrudnik = self.entry[r, c - 2].text
                    for i in range(24):
                        if self.entry[i + 1, 1].text == sotrudnik:
                            self.entry[i + 1, 1].text = ''
                    with open("tabel_sotrudnikov.txt", "r") as f:
                        lines = f.readlines()
                        with open("tabel_sotrudnikov.txt", "w") as f:
                            for line in lines:
                                if line.split()[2] != sotrudnik:
                                    f.write(line)
                    hide_spisok()
                    self.show_spisok()

            '''with open('tabel_sotrudnikov.txt', 'a+') as k:
                k.write('\n' + sotrudnik)
                sotrud[r] = sotrudnik
                label = Label(text='sotrudnik успешно удалён!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
                popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 50.0 / Window.width, 'y': 500.0 / Window.height})
                popupWindow.add_widget(label)
                popupWindow.open()  '''

        

        self.but = {}
        self.entry = {}
        self.sotrud = {}
        self.z = 0
        print(self.sotrud)
        #self.setka(self.col1,self.col2+1)
        root1 = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root1.add_widget(self.layoutgr)

        lay0.add_widget(root1)  # список сотрудников
        lay0.add_widget(lay_1)
        lay.add_widget(label)
        lay.add_widget(lay0)
        lay.add_widget(lay_01)
        lay.add_widget(lay_0)

        self.show_spisok()
        self.add_widget(lay)  # I return the manager to work with him later

    def to_tabel_screen(self, *args):

        self.manager.transition.direction = 'left'
        self.manager.current = 'tabel'  # selecting the screen by name (in this case by name "tabel")
        return 0
    def setka(self,i1, i2):
            # для списка сотрудников
            for i in range(i1, i2):
                h_layout = BoxLayout(height=61, size_hint=(1, None))
                for j in range(4):
                    if j == 0 or j == 2 or j == 3:
                        self.but[i, j] = Button(text='', halign="center", font_size=28, size_hint=(None, 1), width=50)
                        if j == 0:
                            self.but[i, j].text = str(i)
                            if i == 0:
                                self.but[i, j].text = 'N°'
                        if j == 2:
                            self.but[i, j].text = '+'
                            self.but[i, j].width = 70
                            self.butt_add(i, j)
                            if i == 0:
                                self.but[i, j].text = ''
                        if j == 3:
                            self.but[i, j].text = '-'
                            self.but[i, j].width = 70
                            #butt_del(i, j)
                            if i == 0:
                                self.but[i, j].text = ''
                        h_layout.add_widget(self.but[i, j])
                    else:
                        self.entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=45,
                                                     size_hint=(1, 1), width=50, multiline=False)
                        # entry[i, j].set_bgcolor(1,1,1,1)
                        h_layout.add_widget(self.entry[i, j])
                        if j == 1:
                            self.entry[i, j].markup = True
                            self.entry[i, j].width = 240
                            self.entry[i, j].foreground_color = [0, 0, 1, 1]
                            if i == 0:
                                self.entry[i, j].text = 'Сотрудник'
                                self.entry[i, j].font_size = 40
                                self.entry[i, j].background_color = [1, 1, 0, 1]
                                self.entry[i, j].foreground_color = [0, 0, 0, 1]
                self.layoutgr.add_widget(h_layout)
    
    def butt_add(self,i, j):

        self.but[i, j].on_press = lambda: add(i, j)

        def add(r, c):
            print(str(r) + '-' + str(c))
            # print(entry[r, c-1].text)
            self.setka(r+1, r+2)
            today = datetime.datetime.now()
            data = today.strftime("%m-%y")
            print(data)
            self.sotrudnik = self.entry[r, c - 1].text
            self.lay1.text = self.lay1.text + '\n ' + data + '\n ' + self.entry[r, c - 1].text
            # print(num[0, r].text)
            hours = ''
            for i in range(32):
                hours = hours + '-'
                # sotrudnik =entry[r, c-1].text
            if self.crsp == False:
                with open('tabel_sotrudnikov.txt', 'r') as f:
                    if self.sotrudnik in f.read():
                        self.lay1.text = self.sotrudnik + '\nв списке\nуже есть'
                        if self.sotrudnik == '':
                            self.lay1.text = ''
                    else:
                        
                        TabelScreen('tabel', r+2).setka(r+1, r+2)
                        self.manager.get_screen('tabel').entry[r, c - 1].text = self.sotrudnik
                        with open('tabel_sotrudnikov.txt', 'a+') as k:
                            k.write(self.m_y + ' ' + self.sotrudnik + ' ' + hours + '\n')
                            popupWindow = PopupX('sotrudnik успешно сохранен!')
            else:
                with open('tabel_sotrudnikov.txt', 'a+') as k:
                    k.write(m_y + ' ' + sotrudnik + ' ' + hours + '\n')
    
    def show_spisok(self):
        # global ks
        #sm.add_widget(TabelScreen('tabel', self.ks + 1))
        with open('tabel_sotrudnikov.txt', 'r') as k:
            f = k.read()
            if f == '':
                self.lay1.text = 'файл \nпустой' + '\nвведите\nсотр-ов\nкак \nсказано\nвыше\n'
                self.setka(0 ,2)
                self.z = 2
            else:
                self.ks = 1
                #self.setka(self.ks ,self.ks +1)
                sp_all = f.splitlines()
                print(sp_all)
                s = sp_all[0].split()
                self.setka(self.ks ,self.ks +1)
                self.sotrud = []
                self.entry[1, 1].text = s[2]
                # sotr = s[2]
                self.sotrud.append(s[2])
                for i in range(1, len(sp_all)):
                    self.setka(self.ks+1 ,self.ks +2)
                    s = sp_all[i].split()
                    print(s)
                    '''if s[0] in ['январь', 'февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']:
                        pass
                    else:'''
                    if s[2] in self.sotrud:
                        pass
                    else:
                        
                        self.entry[i + 1, 1].text = s[2]
                        # tb_panel.content.children[0].entry[i+1].text=s[2]
                        # print('tb_panel.content.children[0]', tb_panel.content.children[0])
                        # tb_panel.swich_to(ids['1-12']).
                        # print('tb_panel.swich_to(id) ', tb_panel.swich_to(ids['1-12'])])
                        # Th_head('от 1 до 12', 'green', 0, 13) .entry[i+1].text=s[2]
                        self.sotrud.append(s[2])
                        self.ks = self.ks + 1
                self.lay1.text = 'всего\nчеловек:\n ' + str(self.ks)


class TabelScreen(Screen):
    def __init__(self, name, col2, **kwargs):
        super(TabelScreen, self).__init__(**kwargs)
        self.name = name
        self.col1 = 0

        lay = BoxLayout(orientation="vertical", padding=0, size_hint=(1, 1))
        # layfor0 = GridLayout(cols=1, spacing=0, size_hint=(1, None))
        lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, 2))
        laytop = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        lay1 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .2))
        self.layoutgr = GridLayout(cols=1, spacing=0, size_hint=(1, 1))
        self.layout_itog = GridLayout(cols=1, spacing=0, size_hint=(.28, 1))
        self.layout = GridLayout(rows=1, spacing=0, size_hint=(None, 1))  # , size_hint_x=None)
        copy = Button(text='обновить', markup=True, font_size=35, size_hint=(.7, 1), color=[1, 1, 0, 1])
        # delete = Button(text='', markup=True, font_size=35, size_hint=(1, 1), color=[1, 1, 0, 1])
        to_spisok = Button(text='перейти  к\nсозданию списка', markup=True, font_size=35, size_hint=(1, 1),
                           color=[1, 1, 0, 1])
        clear = Button(text='очистить', font_size=35, size_hint=(.7, 1))
        laybutton = BoxLayout(size_hint=(1, .16))
        lab1 = LabelX(halign="center",
                      text='Выберите год и месяц! Введите часы!\n Чтобы добавить, жмите на "+"! Обновите! ',
                      font_size=35, size_hint=(1, .2), color=[0, 0, 0, 1])
        lab1.set_bgcolor(.8, .8, 1, 1)
        lay1.add_widget(copy)
        lay1.add_widget(clear)
        # delete_allay1.add_widget(delete)
        lay1.add_widget(to_spisok)
        clear.on_press = lambda: clear_all()
        copy.on_press = lambda: vivod_sotrudnikov()
        # delete.on_press = lambda: delete_all()
        to_spisok.on_press = lambda: self.to_spisok_screen()
        # layfor0.bind(minimum_height=layfor0.setter('height'))
        # layoutgr.bind(minimum_height=layoutgr.setter('height'))
        self.layout.bind(minimum_width=self.layout.setter('width'))
        today = datetime.datetime.now()
        print(today.isoweekday())
        data = today.strftime("%m-%y")
        y = ' 20' + data[3:5]
        self.month_choose = False
        dropdown = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        dropdownyear = DropDown(size_hint_y=1, size_hint_x=1, height=44, width=100)
        for index in ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                      'ноябрь', 'декабрь']:
            btn = Button(text=index, size_hint_y=None, size_hint_x=None, font_size=40, height=64, width=200)
            btn.bind(on_release=lambda btn: (dropdown.select(btn.text), vivod_sotrudnikov()))
            dropdown.add_widget(btn)
        mainbutton = Button(text='выберите месяц', font_size=40,
                            size_hint=(1, 1))  # pos_hint: {"top": 1})
        mainbutton.bind(on_release=lambda btn: dropdown.open(btn))
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        years = [int(y) - 2, int(y) - 1, int(y), int(y) + 1, int(y) + 2, int(y) + 3, int(y) + 4]
        for year in years:
            btn1 = Button(text=str(year), size_hint_y=None, size_hint_x=None, font_size=40, height=64, width=200)
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
            label = Label(text='вы уверены, что хотите\nудалить всю информацию?', font_size=42, size_hint=(1, 1),
                          color=[1, 0, 0, 1])
            yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
            no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
            an_layout.add_widget(yes)
            an_layout.add_widget(no)
            yes.on_press = lambda: (dele(), close(), clear_all())
            no.on_press = lambda: (close())

            def close():
                popupWindow.dismiss()

            popupWindow = Popup(title="внимание!", size_hint=(None, None), size=(750, 320),
                                pos_hint={'x': 0.0 / Window.width, 'y': 500.0 / Window.height})
            h_layout.add_widget(label)
            h_layout.add_widget(an_layout)
            popupWindow.add_widget(h_layout)
            popupWindow.open()

            def dele():
                with open('tabel_sotrudnikov.txt', 'w'):
                    popupWindow = PopupX('часы за все месяцы\nуспешно удалены!')

        '''def create_tabel():
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
            vivod_sotrudnikov()'''

        def clear_all():
            yearbutton.text = 'выберите год'
            mainbutton.text = 'выберите месяц'
            self.month_choose = False
            for i in range(4):
                self.itog[i + 1].text = ''
                for j in range(32):
                    self.num[j, i + 1].text = ''
                    self.num[j, i + 1].background_color = [1, 1, 1, 1]
                    if i == 0:
                        self.num[j, i].text = str(j + 1)
                        if j == 31:
                            self.num[j, i].text = 'Итог'

        def vivod_sotrudnikov():
            mo = {'январь': '1', 'февраль': '2', 'март': '3', 'апрель': '4', 'май': '6', 'июнь': '6', 'июль': '7',
                  'август': '8', 'сентябрь': '9', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12'}
            day_week = {'1': 'пн', '2': 'вт', '3': 'ср', '4': 'чт', '5': 'пт', '6': 'сб', '7': 'вс'}
            month = mainbutton.text
            year = yearbutton.text
            data = month + ' ' + year + 'г.'
            print('data=', data)
            j = 0
            with open("tabel_sotrudnikov.txt", "r") as f:
                r = f.read()
                if r == '':
                    popupWindow = PopupX('Спиок сотрудников не создан!\nПерейдите к созданию списка!!')
                else:
                    if year != 'выберите год' and month != 'выберите месяц':
                        py = year
                        pm = month
                        with open('tabel_sotrudnikov.txt', 'r') as k:
                            f = k.read()
                            if data in f:
                                sp_all = f.splitlines()
                                if self.month_choose == False:
                                    for i in range(len(sp_all)):
                                        s = sp_all[i].split()
                                        print(s)
                                        if data == s[0] + ' ' + s[1]:
                                            j = j + 1
                                            self.entry[j, 1].text = s[2]
                                            h = s[3].split('-')
                                            for i1 in range(32):
                                                if i1 < 31:
                                                    try:
                                                        day = datetime.datetime(int(year), int(mo[month]), i1 + 1)
                                                        weekend = day.isoweekday()
                                                        self.num[i1, j].text = h[i1]
                                                    except ValueError:  # day is out of range for month
                                                        pass
                                                    if weekend == 6 or weekend == 7:
                                                        self.num[i1, j].background_color = [1, 1, 0.5, 1]
                                                if i1 == 31:
                                                    self.itog[j].text = h[i1]
                                                    self.num[i1, j].text = h[i1]
                                    for i1 in range(31):
                                        try:
                                            day = datetime.datetime(int(year), int(mo[month]), i1 + 1)
                                            weekend = day.isoweekday()
                                            self.num[i1, 0].text = self.num[i1, 0].text + day_week[str(weekend)]
                                        except ValueError:
                                            pass
                                    self.month_choose = True
                                else:
                                    y = yearbutton.text
                                    m = mainbutton.text
                                    clear_all()
                                    yearbutton.text = y
                                    mainbutton.text = m
                                    vivod_sotrudnikov()
                            else:
                                h_layout = BoxLayout(orientation="vertical", padding=1, size_hint=(1, 1))
                                an_layout = BoxLayout(orientation="horizontal", padding=1, size_hint=(1, 1))
                                label = Label(text='на ' + data + '  нет табеля!\nсоздать табель на ' + data + '?',
                                              font_size=42, size_hint=(1, 1), color=[1, 0, 0, 1])
                                yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160,
                                             height=100)
                                no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160,
                                            height=100)
                                an_layout.add_widget(yes)
                                an_layout.add_widget(no)
                                yes.on_press = lambda: (self.create_tabel(), close())
                                no.on_press = lambda: (clear_all(), close())

                                def close():
                                    popupWindow.dismiss()
                                popupWindow = Popup(title="внимание!", size_hint=(None, None), size=(750, 320),
                                                        pos_hint={'x': 0.0 / Window.width, 'y': 500.0 / Window.height})
                                h_layout.add_widget(label)
                                h_layout.add_widget(an_layout)
                                popupWindow.add_widget(h_layout)
                                popupWindow.open()

        self.but = {}
        self.entry = {}
        self.num = {}
        self.itog = {}
        self.setka(self.col1, col2)

        root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        root.add_widget(self.layout)
        # root1= ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        # root1.add_widget(layoutgr)

        lay0.add_widget(self.layoutgr)  # список сотрудников
        lay0.add_widget(root)  # даты
        lay0.add_widget(self.layout_itog)
        # layfor0.add_widget(lay0)

        lay.add_widget(lab1)
        lay.add_widget(laybutton)
        lay.add_widget(lay0)
        lay.add_widget(lay1)
        self.add_widget(lay)

    def setka(self, i1, i2):
        # для списка сотрудников
        for i in range(i1, i2):
            h_layout = BoxLayout(height=45, size_hint=(1, None))
            for j in range(3):
                if j == 0 or j == 2:
                    self.but[i, j] = Button(text='+', halign="center", font_size=28, size_hint=(None, 1), width=50)
                    if j == 2:
                        self.butt_add(i, j)
                    if j == 0:
                        self.but[i, j].text = str(i)
                        if i == self.col1:
                            self.but[i, j].text = 'N°'
                    if j == 2 and i == self.col1:
                        self.but[i, j].text = ''
                    h_layout.add_widget(self.but[i, j])
                else:
                    self.entry[i, j] = LabelX(halign="center", font_size=35, size_hint=(1, 1), color=[0, 0, 0, 1], width=50,
                                         text='')  # multiline=False, cursor_color=[0, 0, 1, 1],
                    self.entry[i, j].set_bgcolor(1, 1, 1, 1)
                    h_layout.add_widget(self.entry[i, j])
                    if j == 1:
                        self.entry[i, j].markup = True
                        self.entry[i, j].width = 240
                        self.entry[i, j].foreground_color = [0, 0, 1, 1]
                        if i % 2 == 0:
                            self.entry[i, j].set_bgcolor(1, .5, 1, 1)
                        if i == self.col1:
                            self.entry[i, j].text = 'Сотрудники'
                            self.entry[i, j].font_size = 38
                            self.entry[i, j].color = [0, 0, 1, 1]
            self.layoutgr.add_widget(h_layout)
        # для часов по дням в мeсяце
        for i in range(32):
            h_layout = BoxLayout(height=45 * i2, orientation="vertical", size_hint=(None, None))  # height=794,
            for j in range(i1, i2):
                self.num[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=30, size_hint=(1, 1),
                                      width=60, multiline=False, text='')
                h_layout.add_widget(self.num[i, j])
                if j == 0:
                    self.num[i, j].foreground_color = [0, 0, 1, 1]
                    self.num[i, j].background_color = [1, 1, 0.5, 1]
                    self.num[i, j].markup = True
                    self.num[i, j].text = str(i + 1)
                    self.num[i, j].font_size = 30
                if i == 31:
                    self.num[i, j].font_size = 30
                    self.num[i, j].foreground_color = [1, 0, 0, 1]
                    self.num[i, j].background_color = [1, 1, 0.5, 1]
                    self.num[i, j].markup = True
                    if j == 0:
                        self.num[i, j].text = 'Итог'
                    if i == 31:
                        self.num[i, j].width = 70
            self.layout.add_widget(h_layout)
        for i in range(i2):
            self.itog[i] = LabelX(halign="right", height=45, width=130, font_size=35, size_hint=(1, None),
                             color=[1, 0, 0, 1])
            self.itog[i].set_bgcolor(1, 1, 1, 1)
            self.layout_itog.add_widget(self.itog[i])
            if i % 2 == 0:
                self.itog[i].set_bgcolor(1, .5, 1, 1)
            if i == 0:
                self.itog[i].text = 'Итог'

    def butt_add(self, i, j):
        self.but[i, j].on_press = lambda: add(i, j)

        def add(r, c):
            print(str(r) + '-' + str(c))
            m = self.mainbutton.text
            y = self.yearbutton.text
            m_y = m + ' ' + y + 'г.'
            print(self.entry[r, c - 1].text)
            print(self.num[0, r].text)
            k = 0
            print('k=', k)
            hours = ''
            if self.entry[r, c - 1].text == '':
                pass
            else:
                for i in range(32):
                    if i != 31:
                        try:
                            k = k + float(self.num[i, r].text)
                            print('k=', k)
                        except ValueError:
                            pass
                        hours = hours + self.num[i, r].text + '-'
                    else:
                        hours = hours + str(k)
                sotrudnik = self.entry[r, c - 1].text
                with open("tabel_sotrudnikov.txt", "r") as f:
                    lines = f.readlines()
                    with open("tabel_sotrudnikov.txt", "w") as f1:
                        for line in lines:
                            if m_y + ' ' + sotrudnik in line:
                                new_line = m_y + ' ' + sotrudnik + ' ' + hours + '\n'
                                print('new_line=', new_line)
                                f1.write(new_line)
                            else:
                                f1.write(line)
                    if m_y == 'выберите месяц выберите годг.':
                        pass
                    else:
                        popupWindow = PopupX('часы успешно добавлены!')

    def to_spisok_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'spisok'


sm = ScreenManager()
if __name__ == '__main__':
    MainApp().run()