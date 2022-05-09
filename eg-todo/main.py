import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.1.0')


class TodoScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(TodoScreen, self).__init__(**kwargs)

    def get_random(self):
        result = '-'
        list_todo = self.ids.txt_todo.text.rstrip(' \n').split('\n')
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