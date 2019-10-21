1>2# : ^
'''
@echo off
echo Switch to python
call C:/Users/%USERNAME%/Anaconda3/Scripts/activate.bat
python "%~f0"
pause
exit /b
rem ^
'''
import numpy as np
import os, glob, io 
from PIL import Image
import json
os.chdir("E:\\Direction_20191018")
json_list = glob.glob("./**/*.json",recursive=True)

def read_labelme_json(json_path):
    file_json = io.open(json_path,'r',encoding='utf-8') 
    json_data = file_json.read()
    data = json.loads(json_data)
    filename=data['imagePath']
    classes, xmin, ymin, xmax, ymax = [],[],[],[],[]
    for i in range(len(data['shapes'])):
        classes.append(data['shapes'][i]['label'])
        xmin.append(data['shapes'][i]['points'][0][0])
        ymin.append(data['shapes'][i]['points'][0][1])
        xmax.append(data['shapes'][i]['points'][1][0])
        ymax.append(data['shapes'][i]['points'][1][1])
    box_info = np.stack([classes,xmin,ymin,xmax,ymax],axis=1)
    file_json.close()
    return [filename,box_info]

def return_bboxImg(img, bbox_array):
    x1 = min(int(float(bbox_array[1])),int(float(bbox_array[3])))
    y1 = min(int(float(bbox_array[2])),int(float(bbox_array[4])))
    x2 = max(int(float(bbox_array[1])),int(float(bbox_array[3])))
    y2 = max(int(float(bbox_array[2])),int(float(bbox_array[4])))
    bbox = img[y1:y2,x1:x2,:]        
    return bbox

if not os.path.exists('./Cropped_box'):
    os.mkdir('./Cropped_box')
print(f"共{len(json_list)}個Json file")
print("正在裁剪圖片至Cropped_box資料夾....")
missing_count = 0
for i in json_list:
    try:
        dataset_name = os.path.basename(os.path.dirname(i))
        json_content = read_labelme_json(i)
        img_path = dataset_name+"/"+json_content[0]
        img = np.array(Image.open(img_path))
        for count,b in enumerate(json_content[1]):
            cropped_box = Image.fromarray(return_bboxImg(img,b))
            cropped_box.save("cropped_box/"+dataset_name+"-"+json_content[0].split(".")[0]+"-"+str(count)+".jpg","JPEG")
    except:
        print(f"Can not found image : {img_path}")
        missing_count += 1
print("完成!")
print(f"共{missing_count}張圖片遺失")
