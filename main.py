from tkinter import *
import time

state_prof = ''
state_race = ''
state_weapon = ''

# класс героя
class Hero:
    def __init__(self):
        self.prof = ''
        self.race = ''
        self.weapon = ''
        self.hp = 100
        self.dmg = 10
    def create_hero(self):
        if self.race != '' and self.prof != '' and self.weapon != '':
            self.hp = int(self.hp)
            self.dmg = int(self.dmg)
            label_hero.configure(text = f'Ваш герой:\nРаса: {self.race}\nПрофессия: {hero.prof}\nОружие: {hero.weapon}\nhp: {self.hp}\nУрон: {self.dmg}')
            print(f'Ваш герой:\nРаса: {self.race}\nПрофессия: {hero.prof}\nОружие: {hero.weapon}\nhp: {self.hp}\nУрон: {self.dmg}')
            
            


def input_prof(input):
    global state_prof
    state_prof = input
    if state_prof == 'Воин':
        hero.prof = 'Воин'
        hero.hp += 20
        hero.dmg += 30
        print(state_prof)
    if state_prof == 'Волшебник':
        hero.prof = 'Волшебник'
        hero.hp += 10
        hero.dmg += 25
        print(state_prof)
    if state_prof == 'Лучник':
        hero.prof = 'Лучник'
        hero.hp += 5
        hero.dmg += 15
        print(state_prof)

def input_race(input):
    global state_race
    state_race = input
    if state_race == 'Человек':
        hero.race = 'Человек'
        hero.hp += 10
        hero.dmg += 15
        print(state_race)
    if state_race == 'Эльф':
        hero.race = 'Эльф'
        hero.hp += 20
        hero.dmg += 5
        print(state_race)
    if state_race == 'Гном':
        hero.race = 'Гном'
        hero.hp += 50
        hero.dmg += 10
        print(state_race)

def input_weapon(input):
    global state_weapon
    state_weapon = input
    if state_weapon == 'Мечь':
        hero.weapon = 'Мечь'
        hero.dmg += 5
        print(state_weapon)
    if state_weapon == 'Посох':
        hero.weapon = 'Посох'
        hero.dmg += 2
        print(state_weapon)
    if state_weapon == 'Лук':
        hero.weapon = 'Лук'
        hero.dmg += 7
        print(state_weapon)

def dont():
    new_photo = PhotoImage(file="dont_check.gif")
    bg_label.configure(image=new_photo)
    bg_label.image = new_photo
    label_hero.configure(text = 'Powerd by DLCQQ')
    
    

# экземпляры
root = Tk()
hero = Hero()

# создание окна
root.geometry('800x600')
root.title('RPG register')
photo = PhotoImage(file="")
bg_label = Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root['bg'] = 'gray90'

# labels
label_class = Label(root, text = 'Выберете класс:', bg = 'gray90', font = ('Consolas', 20))
label_race = Label(root, text = 'Выберете расу:', bg = 'gray90', font = ('Consolas', 20))
label_weapon = Label(root, text = 'Выберите оружие:', bg = 'gray90', font = ('Consolas', 20))

label_create_hero = Label(root, text = 'Создать персонажа:', bg = 'gray90', font = ('Consolas', 20))

label_hero = Label(root, text = f'Ваш герой: ', bg='gray90', font = ('Consolas', 20))

label_race.grid(row=1, column=1)
label_class.grid(row=2, column=1)
label_weapon.grid(row=3, column=1)
label_hero.grid(row=5, column=1)

# кнопки
btn_warrior = Button(root, text = 'Воин', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_prof('Воин'))
btn_wizard = Button(root, text = 'Волшебник', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_prof('Волшебник'))
btn_archer = Button(root, text = 'Лучник', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_prof('Лучник'))

btn_human = Button(root, text = 'Человек', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_race('Человек'))
btn_elf = Button(root, text = 'Эльф', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_race('Эльф'))
btn_dwarf = Button(root, text = 'Гном', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_race('Гном'))

btn_sword = Button(root, text = 'Мечь', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_weapon('Мечь'))
btn_stuff = Button(root, text = 'Посох', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_weapon('Посох'))
btn_bow = Button(root, text = 'Лук', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = lambda: input_weapon('Лук'))

btn_create_hero = Button(root, text = 'Cоздать', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = hero.create_hero)



btn_dont_click = Button(root, text = 'don`t click', bg = 'gray75', fg = 'black', font = ('Consolas', 20), command = dont)

btn_human.grid(row=1, column=2)
btn_elf.grid(row=1, column=3)
btn_dwarf.grid(row=1, column=4)

btn_warrior.grid(row=2, column=2)
btn_wizard.grid(row=2, column=3)
btn_archer.grid(row=2, column=4)

btn_sword.grid(row=3, column=2)
btn_stuff.grid(row=3, column=3)
btn_bow.grid(row=3, column=4)


btn_create_hero.grid(row=4, column=2, columnspan=2)
btn_dont_click.grid(row=4, column=4)


root.mainloop()