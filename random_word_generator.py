from tkinter import*
import random

root = Tk()
root.geometry("500x500")
root.title("Random Word Generator")
root.configure(background = 'light blue')

title = Label(root)
title["text"] = "Random Word Generator"
title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

random_word_label = Label(root)
random_word_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)

def random_word():
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    new_random_word = (random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4)
    random_word_label["text"] = new_random_word
    
btn_generate = Button(root, text = "Generate a Random Word", command = random_word)
btn_generate.place(relx = 0.5, rely = 0.45, anchor = CENTER)

root.mainloop()
    
    