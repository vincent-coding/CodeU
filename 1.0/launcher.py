# CodeU
# Version 1.0
# Licences : MIT
# Created by vincent-coding

# Si vous décidez d'utiliser le code source, mentionnez-moi comme créateur de base !
# If you decide to use the source code, please mention me as the basic creator!

# SOURCE CODES

# !usr/bin/env python
# -*- coding: utf-8 -*-


# Import
import os
import webbrowser
from tkinter import *
import tkinter.messagebox



#Variables
version = '1.0'
languages = "English"
copyvalide = "2019"


#MK8 COMMAND
def cc500():  # 500cc
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("500CC\n020200A0 30699564\n4151999A 00000004\n00000000 00000000\n\n")
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def stareffect(): # StarEffect
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Always In Star Effect\n30000000 3FBA92BC\n35000000 50000000\n31000000 00000020\n30100000 00000000\n35000000 50000000\n31000000 00000160\n00120000 00000010\nD0000000 DEADCAFE\n\n")
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')    
def boostracestart(): #boostracestart
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Always boost on race start\n30000000 3FBA92BC\n10000000 50000000\n31000000 00000020\n30100000 00000000\n10000000 50000000\n31000000 00000075\n03120000 00000000\n00000000 00000000\n30000000 3FBA92BC\n35000000 50000000\n31000000 00000020\n30100000 00000000\n35000000 50000000\n31000000 0000015C\n00120000 3F7D2F1B\nD0000000 DEADCAFE\n\n")
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showwarning('CodeU - MarioKart8', 'Warning\n\nBoosts at the maximum distance at the start. Only works if you do not hold accelerate until after you have boosted otherwise you will blow out.')
def mk8antigravity():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Always in anti-gravity\n30000000 4443BB4C\n35000000 50000000\n05120000 00000075\n00000000 00000000\n30000000 3FBA92BC\n35000000 50000000\n31000000 00000020\n30100000 00000000\n35000000 50000000\n31000000 00000154\n00120000 3F800000\nD0000000 DEADCAFE\n\n")    
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8bobomnoexplos():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Bob-omb No Damage Explosion\n00020000 10517B8C\n80800000 00000000\n\n")    
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8freezcpu():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Freeze all CPU (offline only)\n30000000 4443BB4C\n44000000 49000000\n31000000 001A6F5C\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\n31000000 001A1C78\n00120000 00000000\nD0000000 DEADCAFE\n\n")    
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showwarning('CodeU - MarioKart8', 'Warning\n\nFreezes all CPU\'s. (offline only)')
def mk8cantfiritem():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Can't Fire Items\n00020000 1051F3FC\n40400000 00000000\n\n")
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8rtboomerang():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Boomerang Deleter\n00020000 105182DC\n43000000 00000000\n\n")
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')    
    tkinter.messagebox.showwarning('CodeU - MarioKart8', 'Warning\n\nThis code deletes the boomerang thrown by any player, you will never receive damage by this item.')
def mk8dpaditempshacks():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("D-PAD Items Hack\n30000000 4443BB4C\n35000000 50000000\n05120000 00000075\n00000000 00000000\nC0000011 60000000\n3C00FFFF 6000FFFF\n3C40C044 60424BB7\n3CC0FBFC 60C6FDFF\n3C20EEFF 6021FF7F\n7C021278 7C010A78\n7C063278 80420000\n80210000 38620044\n90230000 38820054\n38A00000 90A40000\n38E2003C 80E70000\n38E70028 90C70000\n39000006 3922003C\n81290000 39490044\n39290048 910A0000\n91090000 60000000\n3C40010F 60426AE0\n7C4903A6 4E800420\n30000000 4443BB4C\n35000000 50000000\n05120000 00000075\n00000000 00000000\n09020000 102F48A8\n00000100 00000000\n00020000 11000080\n00000000 00000000\nD0000000 DEADCAFE\n09020000 1F604EA0\n00000200 00000000\n00020000 11000080\n00000004 00000000\nD0000000 DEADCAFE\n09020000 1F604EA0\n00000400 00000000\n00020000 11000080\n00000002 00000000\nD0000000 DEADCAFE\n09020000 1F604EA0\n00000800 00000000\n00020000 11000080\n0000000E 00000000\nD0000000 DEADCAFE\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showinfo('CodeU - MarioKart 8', "The code was created by myself. It is compatible only with the directional cross of the gamepad.\n\nD-Pad Down -> Banana\nD-Pad Left -> Boomerang\nD-Pad Up -> Bo-Bomb\nD-Pad Right -> Red shell\n\nBe careful, if you activate the code that disables the boomerangs, it will also disable these boomerangs!")
def mk8goldmushroomalwayswhite():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Golden Mushroom is always white\n00020000 1051AF10\n00000000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8lakitukillcommand():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Kill lakitu\n00020000 105B9038\n3FC00000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showinfo('CodeU - MarioKart 8', "Information\n\nThis code eliminates the annoying lakitu that appears when the player drives backwards, now you can drive freely backwards without lakitu appearing.")
def mk8removelakitu():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Remove lakitu\n30000000 3FBA92BC\n35000000 49000000\n31000000 00000028\n30100000 00000000\n30000000 50000000\n31000000 FFFFF494\n00120000 00000000\n00120194 00000000\nD0000000 DEADCAFE\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8buttslid():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Butt-Sliding\n00020000 105232D0\n3C000000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8delstagestartcam():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Remove Stage Start Camera\n00020000 10510AC4\n358637BD 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8anim32():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Weird Animations\n00020000 105F3310\n42000000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'Information\n\nIncreases Animation Speed by x32. Results in some funny looking stuff')
def mk8blooperikonscreen():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("No Blooper Ink on Screen\n00020000 1051A248\n00000000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'Information\n\nThis code deletes the blooper effect on the player\'s screen, but still maintains the effect of the ink.')
def mk8nocountdown():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("No Countdown\n30000000 4443BB4C\n35000000 50000000\n00110075 00000001\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8jumpboom():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Jumping Bombs\n00020000 10517B0C\n3FC00000 00000000\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'Information\n\nGives the effect of continuous jumping to Bomb-Ombs when being thrown.')
def mk8instantaccel():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Instant Acceleration\n30000000 4443BB4C\n35000000 50000000\n05120000 00000075\n00000000 00000000\n09000000 1F604EA2\n00000080 00000000\n30000000 3FBA92BC\n46000000 49000000\n31000000 00000020\n30100000 00000000\n46000000 48000000\n12100000 000053AC\n13100000 000052E4\nD0000000 DEADCAFE\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
def mk8instantorangedrift():
    with open("export/AMKP01.txt", "a") as mk8files:
        mk8files.write("Instant orange drift\n30000000 4443BB4C\n35000000 50000000\n05120000 00000075\n00000000 00000000\n30000000 3FBA92BC\n35000000 50000000\n31000000 00000020\n30100000 00000000\n35000000 50000000\n31000000 000055A8\n00120000 00000002\nD0000000 DEADCAFE\n\n")  
    tkinter.messagebox.showinfo('CodeU - MarioKart8', 'The modification of the file "AMKP01.txt" was successful.')
    

# MK8 Def
def mk8start():
    
    #MK8 Creating code files
    with open("export/AMKP01.txt", "w") as mk8files:
        mk8files.write("Mario Kart™ 8 [AMKP01]\n\n")    
    
    launch.destroy()
    mk8 = Tk()
    mk8.title('CodeU - MarioKart8')
    
    # Dimensions
    mk8largeur      = 753
    mk8hauteur      = 155
    mk8largeurEcran = mk8.winfo_screenwidth()
    mk8hauteurEcran = mk8.winfo_screenheight()
    mk8x            = (mk8largeurEcran / 2) - (mk8largeur / 2)
    mk8y            = (mk8hauteurEcran / 2) - (mk8hauteur /2)
    
    mk8.geometry('%dx%d+%d+%d' % (mk8largeur, mk8hauteur, mk8x, mk8y))
    mk8.resizable(width = False, height = False)   
    
    
    # Component
    mk8500cc = Button(mk8, text="500CC", command=cc500, width=20).grid(row=0, column=0)
    mk8stareffect = Button(mk8, text="Always star effect", command=stareffect, width=20).grid(row=0, column=1)
    mk8booststarrace = Button(mk8, text="Always boost race start", command=boostracestart, width=20).grid(row=0, column=2)
    mk8antigravitybtn = Button(mk8, text="Always anti-gravity", command=mk8antigravity, width=20).grid(row=0, column=3)
    mk8bobomnoexplo = Button(mk8, text="Bo-Bomb ", command=mk8bobomnoexplos, width=20).grid(row=1, column=0)
    mk8freezecpubtn = Button(mk8, text="Freeze all CPU", command=mk8freezcpu, width=20).grid(row=1, column=1)
    mk8cantfireitembtn = Button(mk8, text="Can't fire items", command=mk8cantfiritem, width=20).grid(row=1, column=2)
    mk8boomerangdeletersbtn = Button(mk8, text="Boomerang deleters", command=mk8rtboomerang, width=20).grid(row=1,column=3)
    mk8dpadhackbtn = Button(mk8, text="D-Pad Items Hack", command=mk8dpaditempshacks, width=20).grid(row=2, column=0)
    mk8goldenmushroombtn = Button(mk8, text="Golden mushroom", command=mk8goldmushroomalwayswhite, width=20).grid(row=2, column=1)
    mk8lakitukillbtn = Button(mk8, text="Kill lakitu", command=mk8lakitukillcommand, width=20).grid(row=2, column=2)
    mk8removelakitubtn = Button(mk8, text="Remove lakitu", command=mk8removelakitu, width=20).grid(row=2, column=3)
    mk8buttslidingbtn = Button(mk8, text="Butt-Sliding", command=mk8buttslid, width=20).grid(row=3, column=0)
    mk8removestagestartcamerabtn = Button(mk8, text="Remove Stage Start Camera", command=mk8delstagestartcam, width=20).grid(row=3, column=1)
    mk8weirdanimationbtn = Button(mk8, text="Weird Animations", command=mk8anim32, width=20).grid(row=3, column=2)    
    mk8noblooperinkbtn = Button(mk8, text="No Blooper Ink on Screen", command=mk8blooperikonscreen, width=20).grid(row=3, column=3)
    mk8nocountdownbtn = Button(mk8, text="No Countdown", command=mk8nocountdown, width=20).grid(row=4, column=0)
    mk8jumpingbombbtn = Button(mk8, text="Jumping Bombs", command=mk8jumpboom, width=20).grid(row=4, column=1)
    mk8instantaccelerationbtn = Button(mk8, text='Instant Acceleration', command=mk8instantaccel, width=20).grid(row=4, column=2)
    mk8orangedrift = Button(mk8, text="Instant orange drift", command=mk8instantorangedrift, width=20).grid(row=4, column=3)
    
    # FIN DE LA FENETRE MK8
    mk8.mainloop()
    

# BOTW START
def botwstart():
    tkinter.messagebox.showerror('CodeU - Error', 'Sorry, but this part is still under development.')

    


# LAUNCH GUI
launch = Tk()
launch.wm_title('CodeU')

# Dimensions
largeur      = 250
hauteur      = 100
largeurEcran = launch.winfo_screenwidth()
hauteurEcran = launch.winfo_screenheight()
x            = (largeurEcran / 2) - (largeur / 2)
y            = (hauteurEcran / 2) - (hauteur /2)

launch.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))
launch.resizable(width = False, height = False)

# Component
label1 = Label(launch, text="© "+copyvalide+" - vincent-coding").pack(side=BOTTOM)
mk8buttonlaunch = Button(launch, text="Mario Kart 8", command=mk8start, width=20).pack()
botwbuttonlaunch = Button(launch, text="Breath Of The Wild", command=botwstart, width=20).pack()

#PopUP
tkinter.messagebox.showinfo('CodeU - Information','Created by vincent-coding\n\nTwitter : @vincent_coding\nDiscord : vcoding#4488\nLicence : MIT\nVersion : '+version+'\nLanguages : '+languages)


launch.mainloop()
