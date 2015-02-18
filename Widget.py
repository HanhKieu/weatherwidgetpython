from urllib.request import urlopen
from tkinter import *
from tkinter.font import Font
from urllib.request import * #urlmodule getting func.

def main():
    myURL="http://weather.yahooapis.com/forecastrss?w=2389646" #gets url
    try:
        open_url=urlopen(myURL) #trys to open url
    except:
        print('unable to open URL: ERROR') #if unable to open prints this

    for line in open_url: 
        line=line.decode() #toreadablecode
        line=line.strip() #removeslines


        if 'yweather:forecast' in line: #iflinecontains yweather:forecast
            line=line.replace("=",'"') #replace = with spaces
            line=line.split('"') #split it by the spaces
            

            day=line[2] #oftheweek
            date=line[5] #actual date
            weather=line[14] #how the weather is looking
            weathertext='On'+' '+day+' '+date+'  it will be  '+weather #combines them into one variable
            
            
    root=Tk()
    root.title('Weather Forecast')
    root.geometry('800x800') #givesresolution
    frame=Frame(root)
    frame.grid()

    font=Font(family='Helvetica',size=20) #givesfont
    picture=PhotoImage(file='cloud.gif')#gets an image and puts into variable picture
    pic=Label(frame,image=picture) 
    pic.grid(column=4,row=3,columnspan=5,rowspan=8) #splitsupintogrids

    label=Label(frame,text=weathertext,font=font)#creates label and what is on label
    
    label.grid(row=4,column=4,rowspan=5,columnspan=5) #says where label is at on grid
    #where label is on grid

    root.mainloop() #loops
        
        
            
            
        

main()
        
