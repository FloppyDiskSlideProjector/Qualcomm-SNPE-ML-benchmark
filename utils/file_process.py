import argparse
import os


def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", help = "input path")
    parser.add_argument('-o', "--output", help = "output path")
    parser.add_argument('--fn', type=str, help = "function name")
    parser.add_argument('--filename', type=str, help = "name of file you want to create")
    parser.add_argument('--mode', type=str, help = "type of information in the file")
    args = parser.parse_args()
    return args
    
    
def raw_list_maker(input_file_path, output_file_path, filename, mode = "path"):
    files = os.listdir(input_file_path)
    file_list = [file for file in files if file.endswith('.raw')]
    file = open(os.path.join(output_file_path, filename), "w")
    if mode == "path":
        for file_name in file_list:
            file.write(os.path.join(input_file_path, file_name)+'\n')
    if mode == "file":
        for file_name in file_list:
            file.write(file_name+'\n')
    if mode == "target":
        for file_name in file_list:
            file.write("cropped/"+file_name+'\n')
    file.close()


def setup_dir(model_path):
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    data_dir = os.path.join(model_name, "data")
    cropped_dir = data_dir
    model_dir = os.path.join(model_name, "model")
    
    os.makedirs(model_name, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(cropped_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)


if __name__ == "__main__":
    args = getArg()
    if args.fn == "raw_list_maker":
        input_param = dict()
        input_param["input_file_path"] = args.input
        input_param["output_file_path"] = args.output
        input_param["filename"] = args.filename
        if args.mode:
            input_param["mode"] = args.mode
        raw_list_maker(**input_param)
    if args.fn == "setup_dir":
        setup_dir(args.input)
    