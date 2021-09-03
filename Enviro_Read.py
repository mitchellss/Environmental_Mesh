from SerialProcessor import SerialProcessor
from multiprocessing import Process, Queue
import sys
import json
import ast

if len(sys.argv) == 1:
    print("Usage:\n python Enviro_Read.py <Port>")
    sys.exit(0)

sp = SerialProcessor(str(sys.argv[1]), 9600, 'test')
sp.go()
while sp.is_running:
    line =  str(sp.queue.get())
    if "{" in line:
        try:
            line_dict = ast.literal_eval(line)
            print(line_dict)
        except:
            print("fail")
    else:
        print(line)
    #json_derulo = json.loads(eval(line))
    #print(json_derulo["406908213773201128"])
sp.quit()