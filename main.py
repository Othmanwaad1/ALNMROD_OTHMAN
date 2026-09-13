from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 20

        self.title_label = Label(text="ALNMROD_OTHMAN", font_size=32)
        self.add_widget(self.title_label)

        self.info_label = Label(text="التطبيق يعمل بنجاح!", font_size=22)
        self.add_widget(self.info_label)

        self.button = Button(text="اضغط للبدء", font_size=24, size_hint=(1, 0.4))
        self.button.bind(on_press=self.on_button)
        self.add_widget(self.button)

    def on_button(self, instance):
        self.info_label.text = "مرحبا بك في تطبيقك! 🎉"

class AlnmrodApp(App):
    def build(self):
        return MainLayout()

    def on_start(self):
        self.title = "ALNMROD_OTHMAN"

if __name__ == "__main__":
    AlnmrodApp().run()
