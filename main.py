from tkinter import *
from tkinter import ttk
import random
from Algorithms import bubbleSort




root = Tk()
root.title("Sorting Visualization")
root.maxsize(900,700)
root.config(bg="black")
#variables
selected_alg=StringVar()
data = []

def drawData(data, colorArray):
    
    canvas.delete("all")
    c_height = 380
    c_width = 680
    x_width = c_width/(len(data)+1)
    offset = 20
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i*x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i+1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0, anchor=SW, fill = "red", text=str(data[i]))
    root.update_idletasks()


def StartAlgo():
    speed= speedScale.get()
    global data
    bubbleSort(data, drawData,speed)





def Generate():
    
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    print("Generated..." + selected_alg.get() + " "+str(maxVal) + " " +str(minVal)+ " " +str(size))
    data = [random.randint(minVal,maxVal) for i in range(size)]
    drawData(data, ["red"]*size)

#frame

UI_frame = Frame(root, width=700, height=260, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)


canvas = Canvas(root, width=700, height=380)
canvas.grid(row=1, column=0, padx=10, pady=5)



# UI
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column= 0, padx=5, pady=5)

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1,padx=5, pady=5)
algMenu.current(0)

# speed 
speedScale = Scale(UI_frame,from_=0.01, to=2.0,length=200,digits=2,resolution=0.1, orient=HORIZONTAL, label="Speed [s]")
speedScale.grid(row=0, column=2, padx = 5,pady=5)
Button(UI_frame, text="Start", command=StartAlgo, bg="red").grid(row=0,column=3,padx=5, pady=5)

# size
sizeEntry = Scale(UI_frame,from_=3, to=50,resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column= 0, padx=5, pady=5)

# min value
minEntry = Scale(UI_frame,from_=0, to=25,resolution=1, orient=HORIZONTAL, label="Min Size")
minEntry.grid(row=1, column= 1, padx=5, pady=5)

# max value
maxEntry = Scale(UI_frame,from_=25, to=100,resolution=1, orient=HORIZONTAL, label="Max SIze")
maxEntry.grid(row=1, column= 2, padx=5, pady=5)


Button(UI_frame, text="Generate", command=Generate, bg="white").grid(row=1 ,column=3,padx=5, pady=5)























root.mainloop()













