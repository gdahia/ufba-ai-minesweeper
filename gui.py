from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from six.moves import range
from six.moves import tkinter

import functools


class GUI(tkinter.Frame, object):
  @classmethod
  def main(cls, width, height, callback):
    root = tkinter.Tk()
    window = cls(root, width, height, callback)
    root.mainloop()

  def __init__(self, master, width, height, callback):
    super(GUI, self).__init__(master)
    self.__width = width
    self.__height = height

    # carrega imagens
    self.__flag_image = tkinter.PhotoImage(file="./images/flag.png")
    self.__blank_image = tkinter.PhotoImage(file="./images/blank.png")
    self.__mine_image = tkinter.PhotoImage(file="./images/mine.png")
    self.__zero_image = tkinter.PhotoImage(file="./images/0.png")
    self.__one_image = tkinter.PhotoImage(file="./images/1.png")
    self.__two_image = tkinter.PhotoImage(file="./images/2.png")
    self.__three_image = tkinter.PhotoImage(file="./images/3.png")
    self.__four_image = tkinter.PhotoImage(file="./images/4.png")
    self.__five_image = tkinter.PhotoImage(file="./images/5.png")
    self.__six_image = tkinter.PhotoImage(file="./images/6.png")
    self.__seven_image = tkinter.PhotoImage(file="./images/7.png")
    self.__eight_image = tkinter.PhotoImage(file="./images/8.png")

    self.__build_buttons()
    self.grid()
    callback(self._push)

  def __build_buttons(self):
    self.__buttons = []
    for y in range(self.__height):
      row = []
      for x in range(self.__width):
        button = tkinter.Button(self)
        button.grid(row=y, column=x)
        button['text'] = '  '
        command = functools.partial(self._push, y, x)
        row.append(button)
      self.__buttons.append(row)

  def _push(self, **kwargs):
    if kwargs['val'] == 'F':
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__flag_image, height=20, width=30)
    elif kwargs['val'] == ' ':
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__blank_image, height=20, width=30)
    elif kwargs['val'] == '*':
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__mine_image, height=20, width=30)
    elif kwargs['val'] == 0:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__zero_image, height=20, width=30)
    elif kwargs['val'] == 1:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__one_image, height=20, width=30)
    elif kwargs['val'] == 2:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__two_image, height=20, width=30)
    elif kwargs['val'] == 3:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__three_image, height=20, width=30)
    elif kwargs['val'] == 4:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__four_image, height=20, width=30)
    elif kwargs['val'] == 5:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__five_image, height=20, width=30)
    elif kwargs['val'] == 6:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__six_image, height=20, width=30)
    elif kwargs['val'] == 7:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__seven_image, height=20, width=30)
    elif kwargs['val'] == 8:
      self.__buttons[kwargs['row'] - 1][kwargs['col']
                                      - 1].config(image=self.__eight_image, height=20, width=30)
    self.update()
