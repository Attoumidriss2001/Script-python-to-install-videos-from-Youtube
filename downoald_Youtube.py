# Attoumi Driss :devloper
from email import message
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
from tkinter import filedialog
from turtle import title
from pytube import YouTube #pip install pytube3

Folder_Name=""
#file location
def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="please,choose one",fg="red")
# downoald video
def DownloadVideo():
    choice=ytdchoices.get()
    url=ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt=YouTube(url)
        if(choice==choices[0]):
            select=yt.streams.filter(progressive=True).first()
        elif(choice==choices[1]):
            select=yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice==choices[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Coller le lien de nouveau",fg='red')
#downoald fonction
    select.download(Folder_Name)
    messagebox.showinfo(title = "Téléchargement", message = "Téléchargement terminé")
    #ytdError.config(text="le téléchargement est terminé")



root=Tk()
root.title("Downoald from youtube")
root.geometry("650x410+310+10")
root.resizable(False,False)
root.columnconfigure(0,weight=1)

f1=Frame(root,width=580,height=100,bg='whitesmoke',bd=3,relief=GROOVE)
f1.place(x=30,y=130)

f2=Frame(root,width=580,height=55,bg='whitesmoke',bd=3,relief=GROOVE)
f2.place(x=30,y=250)

t=Label(root,text='Télécharger vos  vidéos préférées',bg='red',fg='white',font=("Tajawal",15,'bold'))
t.pack(fill=X)
ytdLabel=Label(root,text="Entrer le lien de votre  vidéo",font=("Tajawal",15,'bold'))
ytdLabel.pack()
# Entry Box

ytdEntryVar=StringVar()
ytdEntry=Entry(root,width=70,justify='center',font=("Tajawal",15),fg='blue',textvariable=ytdEntryVar)
ytdEntry.pack()
#Error Msg
ytdError=Label(root,text="Remarques de téléchargement",fg="red",font=("Tajawal",10))

ytdError.pack()
#asking save file label
saveLabel=Label(root,text="Choisir l'emplacement ",bg='whitesmoke',font=("Tajawal",15,"bold"))

saveLabel.place(x=390,y=140)

#btn of save file
saveEntry=Button(root,width=20,font=("Tajawal",12),bg="red",fg="white",text="Chemin d'enregistrement",command=openLocation)

saveEntry.place(x=410,y=180)

#Error msg location
locationError=Label(root,text="Tu n'as pas choisi le chemin ",bg='whitesmoke',fg='red',font=("Tajawal",12))
locationError.place(x=100,y=190)

#downoald quality
ytdQuality=Label(root,text="Choisir la qualité",bg='whitesmoke',font=("Tajawal",15,'bold'))

ytdQuality.place(x=430,y=255)

# combobox
choices=["720p","144p"," le son seulement"]
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.place(x=260,y=265)

#downoald btn
downloadbtn=Button(root,text="Début du téléchargement",width=20,font=("Tajawal",12),bg="white",command=DownloadVideo)

downloadbtn.place(x=40,y=255)

#developer label

developerlabel1=Label(root,text="Fait par Attoumi ",font=("Tajawal",10))
developerlabel1.place(x=265,y=350)


root.mainloop()

