import os
import json

def make_json(model_dir, user_id = "qkrtmddus11"):
    model_name = os.path.splitext(os.path.basename(model_dir))[0]
    dlc_name = os.path.basename(model_dir) 
    
    d = {"Name": model_name,
        "HostRootPath": model_name,
        "HostResultsDir": os.path.join(model_name,"results"),
        "DevicePath": "/data/local/tmp/snpebm",
        "Devices": [
            "R3CT60H611X"
        ],
        "HostName": "localhost",
        "Runs": 2,
        "Model": {
            "Name": model_name,
            "Dlc": os.path.join("/home",user_id,"xrbench-snapdragon",model_name,"model",dlc_name),
            "InputList": "input_list.txt",
            "Data": [
                os.path.join("/home",user_id,"xrbench-snapdragon",model_name,"data","cropped/")
            ]
        },
        "Runtimes": [
            "GPU",
            "CPU",
            "DSP"
        ],
        "Measurements": [
            "timing"
        ]}
        
    file = open(os.path.join(model_name, "benchmark.json"),'w')
    json.dump(d,file,indent=4)
    file.close()