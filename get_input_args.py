#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Saidul Islam
# DATE CREATED: Oct 15, 2019                        
# REVISED DATE: Oct 19, 2019
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg' Options are resnet, alexnet, or vgg
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """

    parser = argparse.ArgumentParser()

    """
    nargs='?' means 0-or-1 arguments
    default=<default value> sets the default when there are 0 arguments
    type=str converts the argument to str
    help=<help string>
    """

    parser.add_argument('--dir', nargs='?', default='pet_images', type=str, 
      help='path to the folder of pet images')
    parser.add_argument('--arch', nargs='?', default='vgg', type=str, 
      help='CNN model architecture to use. Choices are resnet, alexnet, or vgg')
    parser.add_argument('--dogfile', nargs='?', default='dognames.txt', type=str, 
      help='file that contains the list of valid dognames. Example: dognames.txt')

    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()