from PIL import Image
import cv2
import argparse
import numpy as np

def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", help = "input path")
    parser.add_argument('-o', "--output", help = "output path")
    parser.add_argument('--fn', type=str, help = "function name")
    parser.add_argument('--img_shape', type=str, help = "desired image shape H,W")
    parser.add_argument('--img_format', type=str, help = "format of raw data")

    args = parser.parse_args()
    return args
        
def convert_raw_image(img, img_shape = (224,224), img_format = "NHWC"):
    resized_img = cv2.resize(img,img_shape)
    raw_data = np.expand_dims(resized_img, axis=0)
    if img_format == "NCHW":
        raw_data = np.transpose(raw_data, (0, 3, 1, 2))
    if img_format == "HW":
        rd = []
        for color in range(raw_data.shape[3]):
            for 
    raw_data = raw_data.astype(np.float32)
    return raw_data

if __name__ == '__main__':
    args = getArg()
    if args.fn == "convert_raw_image":
        input_param = dict()
        img = cv2.imread(args.input)
        input_param["img"] = img
        if args.img_shape:
            input_param["img_shape"] = tuple(map(int, args.img_shape.split(',')))
        if args.img_format:
            input_param["img_format"] = args.img_format
            
        raw_img = convert_raw_image(**input_param)
        output_file_path = args.output
        raw_img.tofile(output_file_path)
        