import os
import csv
from pathlib import Path


def prepare_dict(path):
    temp_dict = {}
    files = os.listdir(path)
    for file in files:
        with open(Path(path,file),'r') as fd:
            file_data = fd.readlines()
        temp_dict[file] = {'hostname':file_data[0],'mac':file_data[1],'user':file_data[2]}
    return temp_dict

def create_csv(data):
    with open(Path('result.csv'), 'w',newline='') as tmp:
        writer = csv.writer(tmp)
        writer.writerow(['Active','hostname','ipaddr','mac','descr'])
        for el in data.items():
            el = el[1]
            row = ['y',el['hostname'],'ipaddr',el['mac'],el['user']]
            row = [x.strip('\n') for x in row]
            writer.writerow(row)
    with open('result.csv', 'r') as res:
        return print(res.read())
    

file_dict = dict(prepare_dict(Path('files')))
create_csv(file_dict)
