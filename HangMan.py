#Hang Man game written by Mehrnoosh Hazrati

import sys
import os

def play_again():
    python = sys.executable
    os.execl(python, python, * sys.argv)


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

win = Tk()
win.title("Hang Man")
win.geometry("625x325")
win.resizable(False,False)

allowed_guesses = 6

image_paths=['hang.jpg','img6.jpg','img5.jpg','img4.jpg','img3.jpg','img2.jpg','img1.jpg']
img = Image.open(image_paths[allowed_guesses])
img= ImageTk.PhotoImage(img)
panel = Label(win, image = img)
panel.grid(row=7, column=7, rowspan=10, columnspan=10)

wordslist = ['python', 'computer', 'hero', 'linux', 'favorite', 'game'] #list of words

word = random.choice(wordslist)

str1 = ("_ "*(len(word)))
lb1 = Label(win, text=str1)
lb1.grid(row=20, column=7, rowspan=10, columnspan=10)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
bts = []
for x in range(26):
    n = letters[x]
    bt = Button(win, text=n, width=2, height=1, command=lambda word=word, n=n : func1(word, n))
    bt.grid(row=0,column=x)
    bts.append(bt)


def func1(word, n):

    global allowed_guesses
    global str1
    global image_paths
    global play_again

    if n in word:
       s = word.find(n)
       str1 = str1[:2*s] + n + str1[2*s+1:]
       lb1.config(text = str1)
       if "_ " not in str1:
           messagebox.showinfo('YOU WON!')
           msgbox = messagebox.askquestion(title='HangMan', message='Would You Like to Play Again?')
           if msgbox == 'no':
               win.destroy()
               exit()
           else:
               play_again()
    
    else:
           if allowed_guesses > 0:
               image = Image.open(image_paths[allowed_guesses])
               imgnew = ImageTk.PhotoImage(image)
               panel.config(image=imgnew)
               panel.image = imgnew
               allowed_guesses -= 1
               strv = StringVar()
               strv.set(allowed_guesses + 1)
               lb2 = Label(win, text = 'remained guesses:')
               lb3 = Label(win, textvariable = strv)
               lb2.grid(row=30, column=7, rowspan=10, columnspan=10)
               lb3.grid(row=40, column=7, rowspan=10, columnspan=10)
           else:
               img2 = ImageTk.PhotoImage(Image.open('hang.jpg'))
               panel.config(image=img2)
               strv = StringVar()
               strv.set(0)
               lb2 = Label(win, text = 'remained guesses:')
               lb3 = Label(win, textvariable = strv)
               lb2.grid(row=30, column=7, rowspan=10, columnspan=10)
               lb3.grid(row=40, column=7, rowspan=10, columnspan=10)
               messagebox.showinfo('YOU FAILED!')
               msgbox = messagebox.askquestion(title='HangMan', message='Would You Like to Play Again?')
               if msgbox == 'no':
                   win.destroy()
                   exit()
               else:
                   play_again()
mainloop()
