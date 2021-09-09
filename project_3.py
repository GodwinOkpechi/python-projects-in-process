from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#we will create a variable and a function that will allow our downloader have access to the files and
#file locations on the computer system
Folder_Name=""
def openFileLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if (len(Folder_Name)> 1):
        pathError.config(text=Folder_Name,foreground='black')
    else:
        pathError.config(text='Please choose Folder',foreground='black')

#we will create a function that will allow the downloader download videos and audio
def DownloadVideo():
    choice=choices.get()
    url=Entry.get()
    if (len(url)> 1):
        Error.config(text="")
        yt=YouTube(url)
        if (choice==choices[0]):
            select=yt.streams.filter(only_audio=True).first()
        elif (choice==choices[1]):
            select=yt.streams.filter(progressive=True).first()
        elif (choice==choices[2]):
            select=yt.streams.filter(progressive=True,file_extension='mp4')
        elif (choice==choices[3]):
            select=yt.streams.filter(progressive=True,file_extension='mp4')
        elif (choice==choices[4]):
            select=yt.streams.filter(progressive=True,file_extension='mp4')
        elif (choice==choices[5]):
            select=yt.streams.filter(progressive=True,file_extension='mp4').last()
        else:
            Error.config(text="Paste Link again",foreground='red')

#we will create a function for that will pass a message when the download is done
#Select.download(Folder_Name)
#Error.config(text='Download Complete')
#then we will pass this function to our 'saveEntry'(after the text component) by wrting -- command=openFileLocation
#and 'downloadButton' button (after the foreground component) we will write -- command=DownloadVideo 
root=Tk()
root.title('CodeX YTD Downloader')            #set's the title of the downloader
root.geometry('400x400')                      #set's the size of the downloader's window
root.columnconfigure(0,weight=1)              #set's all the content to the center of the window

#to set the label for the url
label=Label(root,text='enter the URL of the video',font=('Algerian',15))
label.grid()

#to create the entry box for the url
Entryvar=StringVar()
Entry=Entry(root,width=55,textvariable=Entryvar)   
Entry.grid()

#set an error message caption if a wrong url is inputed into the url box
Error=Label(root,text='Error Message',foreground='red',font=('jost',10))
Error.grid()

#to create the label that will ask if and where u want to save the file 
savelabel=Label(root,text='Save the video File',font=('Algerian',15,'bold'))
savelabel.grid()

#to create the button dat will save the file
saveEntry=Button(root,width=20,background='red',foreground='black',text='choose download path',command=openFileLocation)
saveEntry.grid()

#set the error message for the save file path
pathError=Label(root,text='Error message for file path',foreground='red',font=('jost',10))
pathError.grid()

#to create the label that will ask for download quality
Quality=Label(root,text='Select Download Quality',font=('jost',15))
Quality.grid()

#to create the combo box for the download qualitys
choices=['only audio','1080p','720p','480p','240p','144p']
choices=ttk.Combobox(root,values=choices)
choices.grid()

#to create the download button will
downloadButton=Button(root,text='Download',width=10,background='red',foreground='black',command=DownloadVideo)
downloadButton.grid()

#to create a signature/comment label
signature=Label(root,text='CodeX',font=('Algerian',20))
signature.grid()
root.mainloop()