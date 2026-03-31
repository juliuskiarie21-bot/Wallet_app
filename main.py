from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WalletLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.balance = 0

        self.balance_label = Label(
            text=f"Balance: KES {self.balance}",
            font_size=24
        )

        deposit_btn = Button(
            text="Deposit +100",
            font_size=20
        )
        deposit_btn.bind(on_press=self.deposit)

        self.add_widget(self.balance_label)
        self.add_widget(deposit_btn)

    def deposit(self, instance):
        self.balance += 100
        self.balance_label.text = f"Balance: KES {self.balance}"

class WalletApp(App):
    def build(self):
        return WalletLayout()

if __name__ == "__main__":
    WalletApp().run()
