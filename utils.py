import os
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from matplotlib import image, pyplot as plt

def read_xml(xml_file):
    '''
    Read xml file and return labels that can be "Masked" or "Unmasked"
    
    -------
    input: xml file path
    output: label of the file
    
    '''
    tree = ET.parse(xml_file)
    root = tree.getroot()
    file_name = root.find('object/name').text
    return file_name

def get_file_in_folder(folder):
    '''
    Get all files in a folder
    -------
    input: folder path
    output: a list of all the files in the folder
    '''
    file_list = []
    for file in os.listdir(folder):
        file_list.append(file)
    return file_list


def get_annotations(path_to_folder):
    file_list = get_file_in_folder(path_to_folder)
    annotations = []
    for file in file_list:
        label = read_xml(path_to_folder +'/'+file)
        annotations.append(label)
    annotations = np.array(annotations)
    return annotations


def get_images(path_to_folder):
    file_list = get_file_in_folder(path_to_folder)
    images = []
    print('Loading images...')
    for file in file_list:
        img = image.imread(path_to_folder +'/'+file)
        images.append(img)
    images = np.array(images)
    return images
        