from names import forenames, surnames
from random import seed, randint
from functools import partial
from datetime import datetime
from tkinter import *
from math import ceil

seed(datetime.now())
window = Tk()
window.title("Name Generator")
genBtnList, raceBtnList =  [], []
name = StringVar()
inputGender = StringVar(window, 'null')
inputRace = StringVar(window, 'null')

class nameGenerator:
    def __init__(self, master):
        self.genderLabel = Label(master, text="Gender")
        self.raceLabel = Label(master, text="Race")
        self.namesButton = Button(master, text="Get Names", command=self.getNames)
        self.textBox = Text(master, height=5, width=30)
        self.genderLabel.grid(row=0, column=0, columnspan=3)
        self.raceLabel.grid(row=3, column=0, columnspan=3)
        self.namesButton.grid(row=6, column=4)
        self.textBox.grid(row=1, column=4, rowspan=5)

        genderOptions = ['Male','Female']
        for i in range(len(genderOptions)):
            self.btn = Button(master, text=genderOptions[i], command=partial(self.setGender, genderOptions[i], i), width=8)
            self.btn.grid(row=1, column=i)
            genBtnList.append(self.btn)

        raceOptions = ['Dwarf','Elf','Goblin','Halfling','Human','Orc']
        for i in range(ceil(len(raceOptions)/3)):
            for j in range(3):
                if j+i*3 > len(raceOptions)-1:break
                self.btn = Button(master, text=raceOptions[j+i*3], command=partial(self.setRace, raceOptions[j+i*3], j+i*3), width=8)
                self.btn.grid(row = 5+i, column=j)
                raceBtnList.append(self.btn)

    def setGender(self,gen,index):
        inputGender.set(gen.lower())
        for i in range(len(genBtnList)):genBtnList[i].config(relief=RAISED)
        genBtnList[index].config(relief=SUNKEN)

    def setRace(self,race,index):
        inputRace.set(race.lower())
        for i in range(len(raceBtnList)):raceBtnList[i].config(relief=RAISED)
        raceBtnList[index].config(relief=SUNKEN)

    def reset(self):
        inputGender.set('null')
        inputRace.set('null')
        for i in range(len(genBtnList)):genBtnList[i].config(relief=RAISED)
        for i in range(len(raceBtnList)):raceBtnList[i].config(relief=RAISED)

    def getNames(self):
        gender = inputGender.get()
        race = inputRace.get()
        if gender != 'null' and race != 'null':
            self.textBox.delete('1.0', END)
            if forenames[gender][race]['syl_based'] == True:
                for _ in range(5):
                    for syl in [forenames[gender][race]['first_syl'],forenames[gender][race]['second_syl']]:
                        self.textBox.insert(END, syl[randint(0, len(syl)-1)])
                    self.textBox.insert(END, ' '+surnames[race][randint(0,len(surnames[race])-1)]+'\n')
            else:
                forename = forenames[gender][race]['name']
                for _ in range(5):
                    self.textBox.insert(END,forename[randint(0, len(forename)-1)])
                    self.textBox.insert(END, ' '+surnames[race][randint(0, len(surnames[race])-1)]+'\n')

nameGen = nameGenerator(window)

window.mainloop()
