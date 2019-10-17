1>2# : ^
'''
@echo off
echo Switch to python
call C:/Users/ChiHang/Anaconda3/Scripts/activate.bat
python "%~f0"
pause
exit /b
rem ^
'''
import numpy as np
import os, glob, shutil, io 
from PIL import Image
import json
import matplotlib.pyplot as plt
import cv2
from IPython.display import clear_output

def dump_json(json_path,box_id,class_id):
    try:
        file_json = io.open(json_path, 'r',encoding='utf-8')
    except:
        print(f"Json file missing : {json_path}")
        return False
    json_data = file_json.read()
    data = json.loads(json_data)
    data['shapes'][int(box_id)]['label'] = class_id
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)
        return True
    file_json.close()
    
box_list = glob.glob("./Classes/**/*.jpg",recursive=True)
print(f"Classes資料夾共{len(box_list)}個已分類Bounding Box圖片")
print("正在合併Bounding Box類別至Json...")
for count,i in enumerate(box_list):
    class_ = os.path.basename(os.path.dirname(i))
    split_name = os.path.basename(i).split("-")
    dataset_name = split_name[0]
    image_name = split_name[1]
    box_id = split_name[2].split(".")[0]
    json_path = "./"+dataset_name+"/"+image_name+".json"
    dump_json(json_path,box_id,class_)
print("完成!")