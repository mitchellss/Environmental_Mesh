from SerialProcessor import SerialProcessor
from multiprocessing import Process, Queue
import sys

if len(sys.argv) == 1:
    print("Usage:\n python Enviro_Read.py <Port>")
    sys.exit(0)

sp = SerialProcessor(str(sys.argv[1]), 9600, 'test')
sp.go()
while sp.is_running:
    print(str(sp.queue.get()))