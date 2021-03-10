from SerialProcessor import SerialProcessor
from multiprocessing import Process, Queue

sp = SerialProcessor('COM11', 9600, 'test')
sp.go()
while sp.is_running:
    print(str(sp.queue.get()))