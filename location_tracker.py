from tkinter import*
sp=Tk()
link = ""
import geocoder
import webbrowser


def track():
    global link
    ip=entry_ip.get()
    g=geocoder.ip(ip)
    if g.ok and g.latlng:
        lat=g.latlng[0]
        lon=g.latlng[1]
        link=f"https://www.google.com/maps?q={lat},{lon}"
        result=f"City:{g.city} \n State:{g.state} \n Country:{g.country} \n Latitude:{g.latlng[0]} \n Longitude:{g.latlng[1]}"
        map_link.config(text="🌍 Open Google Maps")
    else:
        result="LOCATION NOT FOUND"
        map_link.config(text="")
    lab2.config(text=result)



sp.title("LOCATION TRACKER")
sp['bg']="#0D0D0D"
sp.geometry("700x700")
sp.resizable(False,False)

lab1=Label(sp,text=" TRACK LOCATION ",font=("Bodoni MT",15,),bg="#8ACCCE")
lab1.place(x=185,y=20,height=70,width=300)

entry_ip=Entry(sp,text="Enter ip",font=("Bodoni MT",15,))
entry_ip.place(x=185,y=190,height=50,width=300)
entry_ip.insert(0,"8.8.8.8")
def open_map(event):
    if link:
        webbrowser.open(link)

map_link = Label(
    sp,
    text="",
    fg="blue",
    bg="#0D0D0D",
    cursor="hand2",
    font=("Arial",12,"underline")
)

map_link.place(x=220,y=590)

map_link.bind("<Button-1>", open_map)
click=Button(sp,text="TRACK LOCATION",font=("Bodoni MT",15,),bg="#8ACCCE",command=track)
click.place(x=185,y=270,height=50,width=300)

lab2 = Label(
    sp,
    text="Enter an IP address and click TRACK LOCATION",
    font=("Arial", 12),
    bg="#0D0D0D",
    fg="white",
    justify=LEFT,
    anchor="nw"
)
lab2.place(x=150, y=400, width=450, height=180)


sp.mainloop()