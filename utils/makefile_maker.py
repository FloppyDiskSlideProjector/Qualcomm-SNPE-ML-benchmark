import os

class makefile_text:
    def __init__(self, model_dir, snpe_version = "2.16.0.231029"):
        self.model_name = os.path.splitext(os.path.basename(model_dir))[0]
        model_dlc = os.path.basename(model_dir)
        self.makefile_text = []
        self.makefile_text.append(f"SNPE_VERSION := {snpe_version}\n")
        self.makefile_text.append(f"MODEL_NAME = {self.model_name}\n")
        self.makefile_text.append(f"MODEL_DLC = {model_dlc}\n")
        
        makefile_structure = open(os.path.join("resource","makefile_structure.txt"),'r')
        
        for line in makefile_structure.readlines():
            self.makefile_text.append(line)
            
        makefile_structure.close()
            
    def write(self):
        file = open(os.path.join(self.model_name,"makefile"),'w')
        
        for line in self.makefile_text:
            file.write(line)
        
        file.close()