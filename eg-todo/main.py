import kivy
kivy.require('2.1.0')

from kivy.config import Config
# Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivy.core.window import Window
Window.softinput_mode = 'resize'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import random
import os


__author__ = 'eginger'
__version__ = '0.0.3'


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class TodoScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(TodoScreen, self).__init__(**kwargs)
        self._txt_todo = self.ids.txt_todo
        self._popup = None

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self._txt_todo.text = stream.read()
        self.dismiss_popup()

    def get_random(self):
        result = '-'
        list_todo = self._txt_todo.text.rstrip(' \n').split('\n')
        if list_todo:
            n = len(list_todo)
            i = random.randrange(0, n, 1)
            row = list_todo[i]
            result = '№{} из {}: {}'.format(i+1, n, row)
        print(result)
        self.ids.lbl_result.text = result


class TodoApp(App):

    def build(self):
        return TodoScreen()


if __name__ == '__main__':
    TodoApp().run()
