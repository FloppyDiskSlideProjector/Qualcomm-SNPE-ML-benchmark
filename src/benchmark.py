import os
import subprocess
from utils import file_process, makefile_maker, json_maker


def setup_path():
    os.system("export PATH=$PATH:/opt/qcom/aistack/snpe/2.16.0.231029/bin/x86_64-linux-clang")
    os.system("export PYTHONPATH=$PYTHONPATH://opt/qcom/aistack/snpe/2.16.0.231029/lib/python")


def setup_files(data_dir, model_path):
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    # copy data
    source_folder = data_dir
    destination_folder = os.path.join(model_name, "data", "cropped")
    os.system(f"cp -r {source_folder} {destination_folder}")
    
    # copy model
    source_folder = model_path
    destination_folder = os.path.join(model_name, "model")
    os.system(f"cp {source_folder} {destination_folder}")


def setup_list(data_dir, model_path):
    # target raw list
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    param = dict()
    param["input_file_path"] = os.path.join(model_name, "data", "cropped")
    param["output_file_path"] = os.path.join(model_name, "data")
    param["filename"] = "target_raw_list.txt"
    param["mode"] = "target"
    file_process.raw_list_maker(**param)
    
    # input list
    param = dict()
    param["input_file_path"] = os.path.join(model_name, "data", "cropped")
    param["output_file_path"] = model_name
    param["filename"] = "input_list.txt"
    param["mode"] = "file"
    file_process.raw_list_maker(**param)


def setup(data_dir, model_dir):
    setup_path()
    
    file_process.setup_dir(model_dir)
    
    setup_files(data_dir, model_dir)
    
    setup_list(data_dir, model_dir)
    
    mk_maker = makefile_maker.makefile_text(model_dir = model_dir)
    mk_maker.write()
    
    json_maker.make_json(model_dir = model_dir)
    
    
def prepare_device(model_dir):
    model_name = os.path.splitext(os.path.basename(model_dir))[0]
    os.system(f"cd {model_name} && make prepare_device && cd ..")
    print(f"prepare _device for {model_name} is done")
        
        
def validate_device(model_dir):
    model_name = os.path.splitext(os.path.basename(model_dir))[0]
    os.system(f"cd {model_name} && make validate_device && cd ..")
    print(f"validate device for {model_name} have finisheed")


def benchmark_model(model_dir):
    model_name = os.path.splitext(os.path.basename(model_dir))[0]
    os.system(f"cd {model_name} && make benchmark_model_on_device && cd ..")
    print(f"benchmarking for {model_name} have finisheed")


def benchmark(data, model, quantization):
    # setup
    setup(data, model)
    
    # prepare device
    prepare_device(model)
    
    # validate device
    validate_device(model)
    
    # run benchmark model on device
    benchmark_model(model)
    
    