import time
import winsound
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)

def bubbleSort(data,drawData,speed):
    colorArray = ["red"]*len(data)
    for _ in range(len(data)-1):

        for j in range(len(data)-1):
            colorArray[j], colorArray[j+1] = "green", "green"
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data,colorArray)
                
                
                time.sleep(speed)
   
            colorArray[j], colorArray[j+1] = "red", "red"
    colorArray = ["green"]*len(data)
    drawData(data,colorArray)
    return data
