from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from random import randint
from kivy.uix.gridlayout import GridLayout

m=0
g=0

i=["Ты хороший?_Да",
    "Ты любишь маму?_Да",
    "Самый популярный сайт Инстаграм?_Нет",
    "Мне 10 лет?_Нет",
    "Медведь врадает в спячку зимой? _Да", 
    "Ананасы растут на деревьях? _Нет","СССР распался в 1990?_Нет",
    "Путин правит с 2000-х_Да",
    "Первый кто полетел на Луну был Гагарин?_Нет",
    "Всего планет восемь?_Да",
    "У кошки девять жизней?_Нет"] 
o=len(i)-1
f=randint(0,o)
k=i[f]
h=k.split("_")
d=h[1]
s=h[0]
class MyApp(App):
    def proverka(self,instance):
        global s,f,k,h,d,s,g,m
        if instance.text==d:
            g+=1
            self.da.text=f"Правельных ответов:{g}"
        else:
            m+=1
            self.net.text=f"Неправельных ответов:{m}"
            
            
        f=randint(0,o) 
        k=i[f]
        h=k.split("_")
        d=h[1]
        s=h[0]
        self.vop.text=str(s)
        
        
    def build(self):
        gr=GridLayout(cols=2)
        bx=BoxLayout(orientation="vertical")
        gr1=GridLayout(cols=2)
        self.da=(Label(text=f"Правельных ответов:{g}"))
        gr1.add_widget(self.da)
        self.net=(Label(text=f"Неправельных ответов:{m}"))
        gr1.add_widget(self.net)
        bx.add_widget(gr1) 
        gr.add_widget(Button(text="Да", background_color=[0,255,0],on_press=self.proverka)) 
        gr.add_widget(Button(text="Нет", background_color=[255,0,0], on_press=self.proverka)) 
        self.vop=(Label(text=s))
        bx.add_widget(self.vop)
        bx.add_widget(gr) 
        
        
        
        
        return bx
        
        



if __name__ == "__main__":
    MyApp().run()