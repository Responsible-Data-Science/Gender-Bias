import os
import glob
import shutil
import random
import warnings

from GenderDetection.age_gender_predictor import AgeGenderPredictor


def read_images_from_folder():
    # try:
    #     shutil.rmtree(os.getcwd()+"/GenderDetection/ScrapedImages")
    #     # shutil.rmtree('mydir')
    #     shutil.rmtree(os.getcwd()+"/Male")
    #     shutil.rmtree(os.getcwd()+"/Female")
    #     shutil.rmtree(os.getcwd()+"/reranked_images")
    #     print("% s removed successfully")
    # except OSError as error:
    #     print(error)
    #     print("File path can not be removed")
    
    folder_path=os.getcwd()+"/GenderDetection/ScrapedImages"
    male=0
    female=0
    images = []
    age_instance=AgeGenderPredictor()
    #print(folder_path)
    counter=0
    dict_bias={}
    
    
    #dictonary[0]={"Gender":"Male","Gender":"Female","Gender":"Male"}
    for img_path in glob.glob(folder_path + '/*.*'):
        warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP: known incorrect sRGB profile.*")
        j=age_instance.process_image_file(img_path)  # For image file detection
        if j[0]>0 and j[1]>0:
            choice=random.randint(0,1)
            if choice ==0:
                dict_bias[counter]={'gender':'Man'}
                counter+=1
            if choice ==1:
                dict_bias[counter]={'gender':'Woman'}
                counter+=1
        elif j[0]>0:
            dict_bias[counter]={'gender':'Man'}
            counter+=1
        elif j[1]>0:
            dict_bias[counter]={'gender':'Woman'}
            counter+=1
    return dict_bias
        



# read_images_from_folder('Doctor')

