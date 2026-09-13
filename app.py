from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class ALNMRODApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=20, spacing=15)

        title = Label(text="ALNMROD_OTHMAN", font_size=42, bold=True)
        self.info = Label(text="تطبيق أندرويد يعمل!", font_size=20)

        self.field = TextInput(hint_text="اكتب اسمك", font_size=28, multiline=False)

        btn = Button(text="نعم", font_size=26, background_color=(0.2, 0.8, 0.4, 1))
        btn.bind(on_press=self.go)

        box.add_widget(title)
        box.add_widget(self.field)
        box.add_widget(self.info)
        box.add_widget(btn)
        return box

    def go(self, *a):
        name = self.field.text.strip() or "صديق"
        self.info.text = f"مرحبا {name} 👋\nWelcome to ALNMROD_OTHMAN"

if __name__ == "__main__":
    ALNMRODApp().run()