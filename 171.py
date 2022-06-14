from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz # pythom timezone
import time

root = Tk()
root.geometry("700x900")
US_img = ImageTk.PhotoImage(Image.open ("usa.jpg"))
India_img = ImageTk.PhotoImage(Image.open ("india.jpg"))
Australia_img = ImageTk.PhotoImage(Image.open ("australia.jpg"))
Japan_img = ImageTk.PhotoImage(Image.open ("japan.jpg"))

#-------------------India--------------------------------
india_label= Label(root, text = "India")
india_label.place(relx = 0.25, rely = 0.02, anchor = CENTER)

india_map = Label(root)
india_map["image"] = India_img
india_map.place(relx = 0.25, rely = 0.21,anchor = CENTER)
india_time = Label(root)
india_time.place(relx = 0.25, rely = 0.4, anchor = CENTER)

#------------------US------------------------------------
us_label = Label(root, text = "US")
us_label.place(relx = 0.75, rely = 0.02, anchor = CENTER)

US_map = Label(root)
US_map["image"] = US_img
US_map.place(relx = 0.75, rely = 0.21,anchor = CENTER)
US_time = Label(root)
US_time.place(relx = 0.75, rely = 0.4, anchor = CENTER)

#-----------------Australia------------------------------
aus_label = Label(root, text = "Australia")
aus_label.place(relx = 0.25, rely = 0.5, anchor = CENTER)

AUS_map = Label(root)
AUS_map["image"] = Australia_img
AUS_map.place(relx = 0.25, rely = 0.69,anchor = CENTER)
AUS_time = Label(root)
AUS_time.place(relx = 0.25, rely = 0.86, anchor = CENTER)

#-------------------Japan--------------------------------

jp_label = Label(root, text = "Japan")
jp_label.place(relx = 0.75, rely = 0.5, anchor = CENTER)

jp_map = Label(root)
jp_map["image"] = Japan_img
jp_map.place(relx = 0.75, rely = 0.69,anchor = CENTER)
jp_time = Label(root)
jp_time.place(relx = 0.75, rely = 0.86, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time['text'] ="Time : " + current_time
        india_time.after(200,self.times)
    
class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        US_time['text'] ="Time : " + current_time
        US_time.after(200,self.times)
        
class Japan():
    def times(self):
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        jp_time['text'] ="Time : " + current_time
        jp_time.after(200,self.times)
        
class Australia():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        AUS_time['text'] ="Time : " + current_time
        AUS_time.after(200,self.times)
        
obj_india = India()
obj_japan= Japan()
obj_usa = USA()
obj_aus = Australia()
india_btn = Button(root,text = "Show Time", command = obj_india.times)
india_btn.place(relx = 0.25, rely = 0.44, anchor = CENTER)
us_btn = Button(root,text = "Show Time", command = obj_usa.times)
us_btn.place(relx = 0.75, rely = 0.44, anchor = CENTER)
japan_btn = Button(root,text = "Show Time", command = obj_japan.times)
japan_btn.place(relx = 0.75, rely = 0.9, anchor = CENTER)
aus_btn = Button(root,text = "Show Time", command = obj_aus.times)
aus_btn.place(relx = 0.25, rely = 0.9, anchor = CENTER)
root.mainloop()