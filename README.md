## Things you should have
1. It's running in the linux system. Make sure it runs linux native machine or wsl.
2. Device with qualcomm's chip is needed. S22 is the device I used.
3. Install qualcomm's snpe and hexagon. Use https://developer.qualcomm.com/sites/default/files/docs/snpe/setup.html for reference.

## Setup
  ### qualcomm's ML model. 
    Deep Learning Container (DLC).
    use this link for rederence https://developer.qualcomm.com/sites/default/files/docs/snpe/overview.html

  ### raw data for ML model.
    Use the information in this link https://developer.qualcomm.com/sites/default/files/docs/snpe/image_input.html
    to make raw image

## benchmark the model
  ### prepare the file and data
    move ML model into the xrbench-snapdragon/input/input_model
    move all data into the xrbench-snapdragon/input/input_data

  ### run the model
    go to the xrbench-snapdragon and run the command 
    python3 main.py --data input/input_data --model input/input_model/{model_name}
    makesure you replace the name of model into model_name
      ex: python3 main.py --data input/input_data --model input/input_model/resnet50.dlc

## see the result
  ### find the result
    In the xrbench-snapdragon, new folder is created. name of the folder is same as name of model name.
    go to the created folder -> output -> model name -> results -> most recent one

## Things to be careful about
  ### Different device
  this is made for galaxy S22 and galaxy S22's qualcomm chip. To make it run on the other machine, you may make some changes on the utils or src.

  ### Different SNPE version
  this is made for SNPE with version 2.16.0.231029. To make it run on the other version, you may make some changes on makefile_maker.py on utils.

## demo video
  https://drive.google.com/file/d/1D5aRv_VQdiTpXsGEMCoGxKxBpaccG6X-/view?usp=sharing
  
