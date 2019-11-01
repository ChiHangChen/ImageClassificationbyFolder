from MainWindow import default_width, default_height
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QFont
from numpy import stack as npstack
from io import open as iopen
from json import loads as jsloads
from json import dump as jsdump
from glob import glob

# This function is for reading labelme annotation json format
def read_labelme_json(json_path):
    file_json = iopen(json_path,'r',encoding='utf-8') 
    json_data = file_json.read()
    data = jsloads(json_data)
    filename=data['imagePath']
    classes, xmin, ymin, xmax, ymax = [],[],[],[],[]
    for i in range(len(data['shapes'])):
        classes.append(data['shapes'][i]['label'])
        xmin.append(data['shapes'][i]['points'][0][0])
        ymin.append(data['shapes'][i]['points'][0][1])
        xmax.append(data['shapes'][i]['points'][1][0])
        ymax.append(data['shapes'][i]['points'][1][1])
    box_info = npstack([classes,xmin,ymin,xmax,ymax],axis=1)
    file_json.close()
    return [filename,box_info]

# this function is to crop bounding box image given an image an its annotation
def return_bboxImg(img, bbox_array):
    x1 = min(int(float(bbox_array[1])),int(float(bbox_array[3])))
    y1 = min(int(float(bbox_array[2])),int(float(bbox_array[4])))
    x2 = max(int(float(bbox_array[1])),int(float(bbox_array[3])))
    y2 = max(int(float(bbox_array[2])),int(float(bbox_array[4])))
    bbox = img[y1:y2,x1:x2,:]        
    return bbox

# this function is for merging boudning box class back to orginal json file
def dump_json(json_path,box_id,class_id):
    try:
        file_json = iopen(json_path, 'r',encoding='utf-8')
    except:
        print(f"Json file missing : {json_path}")
        return False
    # copyfile(json_path, ospath.dirname(ospath.dirname(json_path))+"/json_backup/"+ospath.basename(ospath.dirname(json_path))+"_"+ospath.basename(json_path))
    json_data = file_json.read()
    data = jsloads(json_data)
    data['shapes'][int(box_id)]['label'] = class_id
    with open(json_path, 'w') as f:
        jsdump(data, f, indent=4)
    file_json.close()
    return True

def list_all_type_of_image():
    ext_types = ('./*.jpg', './*.jpeg','./*.png','./*.bmp')
    image_list = []
    for files in ext_types:
         image_list.extend(glob(files))
    return image_list

def resize_widget(widget,current_window_width,current_window_height,fix_height = False):
    if fix_height:
        widget.setGeometry(QRect(
                widget.x_*current_window_width/default_width, widget.y_*current_window_height/default_height,
                widget.width_*current_window_width/default_width, widget.height*1
        ))
    else:
        widget.setGeometry(QRect(
                widget.x_*current_window_width/default_width, widget.y_*current_window_height/default_height,
                widget.width_*current_window_width/default_width, widget.height_*current_window_height/default_height
        ))

def resize_font(widget,current_window_width,current_window_height):
    widget.setFont(QFont("Roman times",int(12*current_window_width/default_width),QFont.Bold))

def resize_icon(widget,current_window_width,current_window_height):
    new_shape = int(40*current_window_width/default_width)
    widget.setIconSize(QSize(new_shape, new_shape))   