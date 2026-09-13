from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='مرحبا بك في ALNMROD_OTHMAN', font_size=28))
        self.add_widget(Button(text='اضغط هنا', on_press=self.on_press))

    def on_press(self, btn):
        btn.text = 'ضغطت!'

class AlnmrodApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    AlnmrodApp().run()
