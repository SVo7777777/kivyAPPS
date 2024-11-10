from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import math
import os
from kivy.uix.popup import Popup
from datetime import datetime, timedelta
from kivy.graphics import Color, Rectangle

layout0 = BoxLayout(orientation="vertical", padding=0)  # главный слой
lay0 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .13))
layout1 = BoxLayout(orientation="vertical", padding=0, size_hint=(1, 3))
layout2 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .3))
layout3 = BoxLayout(orientation="horizontal", padding=0, size_hint=(1, .7))
base_layout = BoxLayout(size_hint=(1, 3))
layoutgr = GridLayout(cols=1, spacing=0, size_hint=(1, 1))
layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
root.add_widget(layout)
quantity = Label(text='', font_size=22, size_hint=(.6, 1))  # , color=[1, 0, 0, 1])
price = Label(text='', font_size=22, size_hint=(.8, 1))  # , color=[1, 0, 0, 1])
cost = Label(text='', font_size=22, size_hint=(1, 1))  # , color=[1, 0, 0, 1])
clear_layout1 = Button(text='[b]скрыть кнопки[/b]', font_size=22, size_hint=(.87, 1), markup=True)
clear = Button(text='[b]C[/b]', font_size=82, markup=True)
solution = Label(text='0.0', font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
summer = Button(text='0.0', markup=True, font_size=120, size_hint=(1, 1), color=[1, 1, 0, 1])
change = Button(text='Сдача', font_size=28, size_hint=(1, 1))
ch = TextInput(hint_text='введите сумму', halign="center", font_size=28, size_hint=(1, 1))
# rew = Button(text='', font_size=22)))()
proc = Button(text='[b]%[/b]', font_size=62, markup=True)
toch = Button(text='.', font_size=62, markup=True)  # multiline=False, readonly=True, )
lay0.add_widget(clear_layout1)
lay0.add_widget(quantity)
lay0.add_widget(price)
lay0.add_widget(cost)

layout1.add_widget(summer)
layout1.add_widget(solution)
layout1.add_widget(layout2)
layout2.add_widget(change)
layout2.add_widget(ch)
# layout1.add_widget(clear)
layout1.add_widget(layout3)
layout3.add_widget(clear)
layout3.add_widget(proc)
layout3.add_widget(toch)
layout1.add_widget(base_layout)
# для прокрутки
layout.bind(minimum_height=layout.setter('height'))
layout0.add_widget(lay0)
layout0.add_widget(root)
layout0.add_widget(layout1)


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


but = {}
entry = {}


def remove(t):
    global cl_lay1
    if t == True:
        layout0.remove_widget(layout1)
        clear_layout1.text = 'показать кнопки'
        lay0.size_hint = (1, .0319)
        cl_lay1 = False
    else:
        layout0.add_widget(layout1)
        clear_layout1.text = 'скрыть кнопки'
        lay0.size_hint = (1, .13)
        cl_lay1 = True


def setka(i1, i2):
    for i in range(i1, i2):
        h_layout = BoxLayout(height=60, size_hint=(None, None))
        for j in range(6):
            if j == 5:
                but[i, j] = Button(text='del', halign="center", font_size=28, size_hint=(None, None), height=60)
                h_layout.add_widget(but[i, j])
            else:
                entry[i, j] = LabelX(halign="center", font_size=50, size_hint=(None, None), height=60, width=80,
                                     color=[0, 0, 0, 1])
                entry[i, j].set_bgcolor(1, 1, 1, 1)
                h_layout.add_widget(entry[i, j])
                if j == 1:
                    entry[i, j].text = 'x'
                    entry[i, j].markup = True
                    entry[i, j].set_bgcolor(1, 1, 1, .8)
                    # entry[i, j].font_size=60
                if j == 3:
                    entry[i, j].text = '='
                    entry[i, j].markup = True
                    entry[i, j].set_bgcolor(1, 1, 1, .8)
                    # entry[i, j].font_size=60
                if j == 0:
                    entry[i, j].halign = 'right'
                    entry[i, j].width = 120
                if j == 2:
                    entry[i, j].halign = 'left'
                    entry[i, j].width = 150
                if j == 4:
                    entry[i, j].width = 240
                    entry[i, j].color = [1, 0, 1, 1]
        entry[0, 0].set_bgcolor(1, 0, 1, 1)
        layout.add_widget(h_layout)


i2 = 5
setka(0, i2)
print('len(but)=', len(but))
b = len(but)
butk = {}
s = 0
r = 0
k = 0
# entry[0, 0].background_color = [1, 1, 0, 1]
for i in range(4):
    h2_layout = BoxLayout()
    for j in range(3):
        k = k + 1
        butk[k] = Button(text=str(k), markup=True, halign="center", font_size=68, size_hint=(1, 1))
        h2_layout.add_widget(butk[k])
        if k == 10:
            butk[k].text = '0'
        if k == 11:
            butk[k].text = 'bs'
            butk[k].color = [1, 0, 1, 1]
        if k == 12:
            butk[k].text = '|--->>'
            butk[k].color = [1, 1, 0, 1]
    layoutgr.add_widget(h2_layout)
butk[13] = toch


# print(butk)
def vvsimbol(i, f, z):
    butk[i].on_press = lambda: vvodsim(i, f, z)


for n in range(1, 14):
    vvsimbol(n, s, r)
base_layout.add_widget(layoutgr)


def vvodsim(k, f, z):
    global s, zapisej2, r, i2
    try:
        t = entry[z, f].text
        but[z, 5].on_press = lambda: del_str(z)
        if k == 11:
            t = t[:-1]
            entry[z, f].text = t
        elif k == 12:
            if f == 0:
                if entry[z, f].text == '':
                    entry[z, f].text = '1'
                else:
                    entry[r, 2].set_bgcolor(1, 0, 1, 1)
                    for n in range(1, 14):
                        vvsimbol(n, 2, r)
            elif f == 2:
                if entry[z, f].text == '':
                    entry[z, f].text = '1'
                else:
                    zapisej2 = z
                    print('zapisej2=', zapisej2)
                    if i2 == z + 1:
                        i2 = i2 + 1
                        setka(z + 1, z + 2)
                    chek_stoimost(z)
                    # entry[r, 4].set_bgcolor(1,0,1,1)
                    entry[r + 1, 0].set_bgcolor(1, 0, 1, 1)
                    r = r + 1
                    print('vvodsim f2 r=', r)
                    for n in range(1, 14):
                        vvsimbol(n, 0, r)
        else:
            entry[z, f].text = t + butk[k].text
            entry[z, f].set_bgcolor(1, 0, 1, 1)
    except KeyError:
        print('end')
        print('vvodsim except r=', r)
        r = r + 1
        for n in range(1, 14):
            vvsimbol(n, 0, r)


chek_full = False
pust_chek = True


# очищаем калькулятор
def clear_calk():
    global pust_chek, s, r
    # s = 0
    # r = 0
    if pust_chek == True:
        print('hello')
    else:
        h_layout = BoxLayout(orientation="vertical", padding=1, size_hint=(1, 1))
        an_layout = BoxLayout(orientation="horizontal", padding=1, size_hint=(1, 1))
        yes = Button(text='да', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
        no = Button(text='нет', halign="center", font_size=30, size_hint=(1, 1), width=160, height=100)
        an_layout.add_widget(yes)
        an_layout.add_widget(no)
        yes.on_press = lambda: (chek_up(), close())
        no.on_press = lambda: (close())

        def close():
            popupWindow.dismiss()

        popupWindow = Popup(title="Вы уверены, что хотите удалить? ", size_hint=(None, None), size=(400, 220),
                            pos_hint={'x': 0.0 / Window.width, 'y': 400.0 / Window.height})
        h_layout.add_widget(an_layout)
        popupWindow.add_widget(h_layout)
        popupWindow.open()


def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek, vvod_not, ito, entry_focus, r
    if pust_chek == True:
        print('привeт')
    else:
        try:
            print('here')
            for i in range(zapisej2 + 2):
                print('here2')
                if entry[i, 0].text != '':
                    entry[i, 0].text = ''
                    entry[i, 2].text = ''
                    entry[i, 4].text = ''
                    entry[i, 0].set_bgcolor(1, 1, 1, 1)
                    entry[i, 2].set_bgcolor(1, 1, 1, 1)
                    entry[i, 4].set_bgcolor(1, 1, 1, 1)
                    entry[i + 1, 0].set_bgcolor(1, 1, 1, 1)
                    entry[i + 1, 2].set_bgcolor(1, 1, 1, 1)
                    entry[i + 2, 0].set_bgcolor(1, 1, 1, 1)
                    entry[0, 0].set_bgcolor(1, 0, 1, 1)
                    print('here3')
        except KeyError:
            print('end')
            entry[i + 1, 0].text = ''
            entry[i + 1, 2].text = ''
    sum_sp = []
    print('список сумм пуст - ', sum_sp)
    pust_chek = True
    vvod_not = False  # выбор растe ния в поиске возможенTypeError
    summer.text = '[b]0.0[/b]'
    solution.text = '0.0'
    change.text = 'Сдача'
    ch.text = ''
    # entry[0, 0].set_bgcolor(1,1,1,1)
    r = 0
    for n in range(1, 14):
        vvsimbol(n, 0, r)


def skidka():
    global vvodi, pust_chek
    if pust_chek == True:
        print('привeт')
    else:
        label = Label(text='введите скидку:', font_size=42, color=[1, 1, 0, 1])
        vvodi = TextInput(text='', halign="center", font_size=45, size_hint=(None, None), width=100, height=70)
        vivod = Button(text='скидка', halign="center", font_size=28, size_hint=(None, None), width=120, height=70)
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
        vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
        popupWindow = Popup(title="скидка", size_hint=(None, None), size=(650, 200),
                            pos_hint={'x': 40.0 / Window.width, 'y': 550.0 / Window.height})
        vvod_layout.add_widget(label)
        vvod_layout.add_widget(vvodi)
        vvod_layout.add_widget(vivod)
        h_layout.add_widget(vvod_layout)
        vvodi.unfocus_on_touch = False
        vvodi.focus = True

        def vivo():
            procent = vvodi.text
            sum = summer.text
            if procent.isdigit():
                p = float(sum) * float(procent) * 0.01
                ot = round(float(sum) - p, 2)
                print(p)
                vivod.text = str(round(p, 2))
                summer.text = str(ot)
            else:
                vivod.text = 'только\nчисло'
                vvodi.text = ''

        vivod.on_press = lambda: vivo()
        popupWindow.add_widget(h_layout)
        popupWindow.open()


sum_sp = []


def chek_stoimost(t):
    global chek_full, name_tara, pust_chek, sum_sp
    price = entry[t, 0].text
    colich = entry[t, 2].text
    print(price)
    print(colich)
    s = '..'
    if s in price:
        st = price.split('.')
        print(st)
        if st[0] != '':
            print('price=', st[0])
            price = st[0]
        elif st[0] == '' and st[-1] == '':
            price = '0'
        else:
            print('price=', st[-1])
            price = '.' + st[-1]
    if s in colich:
        st = colich.split('.')
        if st[0] != '':
            print('colich=', st[0])
            colich = st[0]
        elif st[0] == '' and st[-1] == '':
            colich = '0'
        else:
            print('colich=', st[-1])
            colich = '.' + st[-1]
    if price == '.' or colich == '.':
        price = '0'
        colich = '1'
    stoi = float(price) * float(colich)
    print('stoi=', stoi)
    stoim = round(stoi, 2)
    print('stoim=', stoim)
    if entry[t, 4].text == '':
        entry[t, 4].text = str(stoim)
        chek_full = False
        sum_sp.append(stoim)
        print(sum_sp)
        s1 = round(math.fsum(sum_sp), 2)
        print(s1)
        summer.text = str(round(math.fsum(sum_sp), 2))
        solution.text = str(round(math.fsum(sum_sp), 2))
    else:
        entry[t, 4].text = ''
        sum_sp.pop(t)
        print(sum_sp)
        print(math.fsum(sum_sp))
        entry[t, 4].text = str(stoim)
        summer.text = str(math.fsum(sum_sp))
        solution.text = str(math.fsum(sum_sp))
        chek_full = False
        # удалить сумму из списка
        print(sum_sp)
    pust_chek = False


def sum():
    global sum_sp
    if pust_chek == True:
        print('привeт')
    else:
        summer.text = str(math.fsum(sum_sp))


def sdacha():
    global sum_sp
    if pust_chek == True or ch.text == '':
        ch.text = ''
        print('привeт')
    else:
        oplata = ch.text
        sum = summer.text
        if oplata.isdigit():
            sd = round(float(oplata) - float(sum), 2)
            change.text = 'Сдача: ' + str(sd)
        else:
            ch.text = ''
            change.text = 'только числа'
        # для кнопок удалить


def del_str(z):
    global zapisej2, vvod_not, r
    vvod_not = False  # выбор растения в поиске возможен
    r = r - 1
    try:
        print('удаляем ' + str(z) + ' строку')
        print('удаляем ' + str(sum_sp[z]))
        entry[z, 0].text = ''
        entry[z, 2].text = ''
        entry[z, 4].text = ''
        sum_sp.pop(z)
        summer.text = str(math.fsum(sum_sp))
        solution.text = str(math.fsum(sum_sp))
        print(zapisej2)
        d = zapisej2
        for n in range(zapisej2):
            print('проверяем строку ' + str(n))
            if entry[n, 0].text == '':
                print('строка ' + str(n) + ' пустая')
                if entry[n + 1, 0].text != '':
                    print('строка ' + str(n + 1) + ' непустая')
                    m0 = entry[n + 1, 0].text
                    print(m0)
                    m2 = entry[n + 1, 2].text
                    m4 = entry[n + 1, 4].text
                    entry[n, 0].text = m0
                    entry[n, 2].text = m2
                    entry[n, 4].text = m4
                    entry[n + 1, 0].text = ''
                    entry[n + 1, 2].text = ''
                    entry[n + 1, 4].text = ''
                else:
                    d = d - 1
        entry[d, 2].set_bgcolor(1, 1, 1, 1)
        entry[d, 4].set_bgcolor(1, 1, 1, 1)
        entry[d + 1, 0].set_bgcolor(1, 1, 1, 1)
        if entry[d + 1, 0].text != '':
            entry[d + 1, 2].set_bgcolor(1, 1, 1, 1)
            entry[d + 1, 0].text = ''
            entry[d + 1, 2].text = ''
        for n in range(1, 14):
            vvsimbol(n, 0, d)
    except IndexError or KeyError:
        print('except del_str')
        entry[z, 0].text = ''
        entry[z, 2].text = ''
        entry[z, 4].text = ''
        entry[z, 2].set_bgcolor(1, 1, 1, 1)
        if i2 == z + 1:
            print('ku-ku')
        else:
            entry[z + 1, 0].set_bgcolor(1, 1, 1, 1)
        r = r + 1
        for n in range(1, 14):
            vvsimbol(n, 0, r)


all = True
cl_lay1 = True
proc.on_press = lambda: skidka()
clear.on_press = lambda: clear_calk()
summer.on_press = lambda: sum()
change.on_press = lambda: sdacha()
clear_layout1.on_press = lambda: remove(cl_lay1)
runTouchApp(layout0)