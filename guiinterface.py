import tkinter as tk
import requests

height = 700
width = 800

def format_responmse(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = round((weather['main']['temp']-32)*5/9)
        return str(name) + "\n" + str(desc) + "\n" + str(temp) + " Celsius Degress"
    except:
        return "We cannot find a city"

# 549b0f45bc4049f4138f3b08098e55cf
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def get_weather(city):
    weather_key = "549b0f45bc4049f4138f3b08098e55cf"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID" : weather_key, 'q':city, 'units':"Imperial"}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_responmse(weather)

root = tk.Tk()
canvas = tk.Canvas(root,height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg ='blue', bd=5)
frame.place(relx=0.5,rely=0.05,relwidth= 0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text = "Get Wether",command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3, relheight=1)



entry = tk.Entry(frame, font = 40)
entry.place(relwidth=0.65,relheight = 1)

lower_frame = tk.Frame(root,bg="blue",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor ='n')

label = tk.Label(lower_frame,font= 50)
label.place(relwidth=1,relheight=1)

root.mainloop()