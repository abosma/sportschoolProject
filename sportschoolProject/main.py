import helper as h
import databaseController as dc
import qrController as qc
import motorController as mc
import cameraController as cc
import webhostController as whc
import graphController as gc
import tkinter as tk
from tkinter import messagebox
import pygubu

class mainWindow:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('mainWindow.ui')
        self.mainwindow = builder.get_object('main', master)
        builder.connect_callbacks(self)

    def createUser(self):
        self.master.destroy()
        root = tk.Tk()
        app = createUser(root)
        root.mainloop()
    
    def updateUser(self):
        self.master.destroy()
        root = tk.Tk()
        app = updateUser(root)
        root.mainloop()

    def deleteUser(self):
        self.master.destroy()
        root = tk.Tk()
        app = deleteUser(root)
        root.mainloop()

class createUser:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('createUser.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)

    def nextBtn(self):
        if (self.builder.tkvariables['naamVar'].get() == "" or 
            self.builder.tkvariables['geslachtVar'].get() == "" or
            self.builder.tkvariables['dagVar'].get() == "" or
            self.builder.tkvariables['maandVar'].get() == "" or
            self.builder.tkvariables['jaarVar'].get() == "" or
            self.builder.tkvariables['plaatsVar'].get() == "" or
            self.builder.tkvariables['pcodeVar'].get() == "" or
            self.builder.tkvariables['locatieVar'].get() == "" or
            self.builder.tkvariables['nummerVar'].get() == "" or
            self.builder.tkvariables['mailVar'].get() == "" or
            self.builder.tkvariables['abVar'].get() == ""):
            self.builder.tkvariables['errorBox'].set("Een of meer van de velden zijn niet ingevuld")
        else:
            randomString = h.id_generator(10)
            code = self.builder.tkvariables['naamVar'].get() + "." + randomString
            datum = h.eindDatum()
            dc.createUser(self.builder.tkvariables['naamVar'].get(), 
                          self.builder.tkvariables['geslachtVar'].get(),
                          code, 
                          self.builder.tkvariables['plaatsVar'].get(),
                          self.builder.tkvariables['pcodeVar'].get(),
                          self.builder.tkvariables['nummerVar'].get(),
                          self.builder.tkvariables['mailVar'].get(),
                          (self.builder.tkvariables['dagVar'].get() + "-" + self.builder.tkvariables['maandVar'].get() + "-" + self.builder.tkvariables['jaarVar'].get()),
                           self.builder.tkvariables['locatieVar'].get(),
                           self.builder.tkvariables['abVar'].get(),
                           datum)
            self.builder.tkvariables['errorBox'].set("Gebruiker aangemaakt")

    def backBtn(self):
        self.master.destroy()
        root = tk.Tk()
        app = mainWindow(root)
        root.mainloop()

class updateUser():
    def __init__(self, master):
        self.master = master
        self.buttonCounter = 0
        self.varList = []
        self.table = ""
        self.key = ""
        self.newvar = ""
        self.id = ""
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('updateUser.ui')
        self.mainwindow = builder.get_object('updateFrame', master)
        builder.connect_callbacks(self)
        for id, naam in dc.readUsers().items():
            self.builder.get_object("updateInfoBox", master).insert(tk.INSERT, "ID: " + str(id) + "  Naam: " + str(naam) + "\n")
        self.builder.get_object("updateInfoBox", master).config(state=tk.DISABLED)

    def updNextBtn(self):
        if self.buttonCounter == 0:
            if(self.builder.tkvariables["updateVar"].get() == ""):
                self.builder.tkvariables["updateLabel"].set("Geen ID ingevoerd");
            else:
                for id, naam in dc.readUsers().items():
                    if(str(id) == self.builder.tkvariables["updateVar"].get()):
                        self.builder.tkvariables["updateLabel"].set("Welk Tabel wil je updaten?")
                        self.builder.get_object("updateInfoBox", self.master).config(state=tk.NORMAL)
                        self.builder.get_object("updateInfoBox", self.master).delete(1.0, tk.END)
                        self.builder.get_object("updateInfoBox", self.master).insert(tk.INSERT, "KLANT\nKLANT_APPARAAT\nKLANT_ABONNEMENT\nKLANT_SPORTSCHOOL")
                        self.builder.get_object("updateInfoBox", self.master).config(state=tk.DISABLED)
                        self.id = self.builder.tkvariables["updateVar"].get()
                        self.builder.tkvariables["updateVar"].set("")
                        self.buttonCounter += 1
                        break;
                    else:
                        self.builder.tkvariables["updateLabel"].set("Geen gebruiker met ID " + self.builder.tkvariables["updateVar"].get() + " gevonden");
        if self.buttonCounter == 1:
            tabelList = ["KLANT", "KLANT_APPARAAT", "KLANT_ABONNEMENT", "KLANT_SPORTSCHOOL"]
            if(self.builder.tkvariables["updateVar"].get() == ""):
                self.builder.tkvariables["updateLabel"].set("Geen Tabel ingevoerd");
            else:
                if(self.builder.tkvariables["updateVar"].get() in tabelList):
                    self.table = self.builder.tkvariables["updateVar"].get()
                    self.builder.tkvariables["updateLabel"].set("Welk Variabel wil je updaten?")
                    self.builder.get_object("updateInfoBox", self.master).config(state=tk.NORMAL)
                    self.builder.get_object("updateInfoBox", self.master).delete(1.0, tk.END)
                    test = zip(dc.getTableNames(self.id, self.table), dc.readData(self.id, self.table)[0])
                    for x in list(test):
                        self.builder.get_object("updateInfoBox", self.master).insert(tk.INSERT, str(x[0]) + ": " + str(x[1]) + "\n")
                        self.varList.append(str(x[0]))
                    self.builder.get_object("updateInfoBox", self.master).config(state=tk.DISABLED)
                    self.builder.tkvariables["updateVar"].set("")
                    self.buttonCounter += 1
                else:
                    self.builder.tkvariables["updateLabel"].set("Geen tabel met naam " + self.builder.tkvariables["updateVar"].get() + " gevonden");
        if self.buttonCounter == 2:
            if(self.builder.tkvariables["updateVar"].get() == ""):
                self.builder.tkvariables["updateLabel"].set("Geen Key ingevoerd");
            else:
                if(self.builder.tkvariables["updateVar"].get() in self.varList):
                    self.key = self.builder.tkvariables["updateVar"].get()
                    self.builder.tkvariables["updateLabel"].set("Wat is het nieuwe value?")
                    self.builder.get_object("updateInfoBox", self.master).config(state=tk.NORMAL)
                    self.builder.get_object("updateInfoBox", self.master).delete(1.0, tk.END)
                    test = zip(dc.getTableNames(self.id, self.table), dc.readData(self.id, self.table)[0])
                    for x in list(test):
                        if self.builder.tkvariables["updateVar"].get() in x:
                            self.builder.get_object("updateInfoBox", self.master).insert(tk.INSERT, "Gekozen Key\n" + str(x[0]) + ": " + str(x[1]) + "\n")
                    self.builder.get_object("updateInfoBox", self.master).config(state=tk.DISABLED)
                    self.builder.tkvariables["updateVar"].set("")
                    self.buttonCounter += 1
                else:
                    self.builder.tkvariables["updateLabel"].set("Geen Key met naam " + self.builder.tkvariables["updateVar"].get() + " gevonden");
        if self.buttonCounter == 3:
            if(self.builder.tkvariables["updateVar"].get() == ""):
                self.builder.tkvariables["updateLabel"].set("Geen nieuwe value ingevoerd");
            else:
                self.newvar = self.builder.tkvariables["updateVar"].get()
                self.builder.tkvariables["updateLabel"].set("User is geupdatet")
                self.builder.get_object("updateInfoBox", self.master).config(state=tk.NORMAL)
                self.builder.get_object("updateInfoBox", self.master).delete(1.0, tk.END)
                self.builder.get_object("updateInfoBox", self.master).insert(tk.INSERT, "De nieuwe value is " + self.builder.tkvariables["updateVar"].get())
                self.builder.get_object("updateInfoBox", self.master).config(state=tk.DISABLED)
                self.builder.tkvariables["updateVar"].set("")
                dc.updateUser(self.table, self.key, self.newvar, self.id)
                self.buttonCounter = 0
    def updBackBtn(self):
        self.master.destroy()
        root = tk.Tk()
        app = mainWindow(root)
        root.mainloop()

class deleteUser():
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('deleteUser.ui')
        self.mainwindow = builder.get_object('deleteFrame', master)
        builder.connect_callbacks(self)
        for id, naam in dc.readUsers().items():
            self.builder.get_object("userList", master).insert(tk.INSERT, "ID: " + str(id) + "  Naam: " + str(naam) + "\n")
        self.builder.get_object("userList", master).config(state=tk.DISABLED)

    def verwijderBtn(self):
        if(self.builder.tkvariables['deleteIdVar'].get() == ""):
            self.builder.tkvariables['delErrorBox'].set("Er is geen ID ingevuld")
        else:
            try:
                dc.deleteUser(int(self.builder.tkvariables['deleteIdVar'].get()))
                self.builder.tkvariables['delErrorBox'].set("Gebruiker verwijderd")
                self.builder.get_object("userList", self.master).config(state=tk.NORMAL)
                self.builder.get_object("userList", self.master).delete(1.0, tk.END)
                for id, naam in dc.readUsers().items():
                    self.builder.get_object("userList", self.master).insert(tk.INSERT, "ID: " + str(id) + "  Naam: " + str(naam) + "\n")
                self.builder.get_object("userList", self.master).config(state=tk.DISABLED)
            except Exception as e:
                self.builder.tkvariables['delErrorBox'].set("ID " + self.builder.tkvariables['deleteIdVar'].get() + " niet gevonden")
    
    def delBackBtn(self):
        self.master.destroy()
        root = tk.Tk()
        app = mainWindow(root)
        root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()

#h.checkImageThread()

#save_location = "C:/Users/User/Desktop/QRCodes/" + code + ".png"
#qc.createQR(code, save_location)
#dc.updateUser("KLANT", "naam", "UpdateTest", 7)

#locatieData = dc.getAdminData()
#gc.createAdminDataGraph(locatieData[0], locatieData[1], locatieData[2], locatieData[3], locatieData[4], locatieData[5])

#gc.createGraph([1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15])

#dataList = dc.getUserData("Atilla.Bosma.AGNFTKMWF6")
#gc.createUserDataGraph(dataList[0][0], dataList[1][0], dataList[3][0], dataList[4][0], dataList[2][0], dataList[0][1], dataList[1][1], dataList[3][1], dataList[4][1], dataList[2][1])
#whc.openWebsite()