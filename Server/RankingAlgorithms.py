import os
import shutil
import random
from math import log2
import math

# Image re-ranking algorithms

def epsilon_greedy(num, epsilon):
    """Epsilon greedy algorithm

    Args:
        num (int): the length of list to be sorted 
        epsilon (float): the introduced randomness

    Returns:
        list: a list of randomized indices
    """
    list_index = [i for i in range(num)]
    for idx, item in enumerate(list_index):
        if random.uniform(0, 1) <= epsilon:
            select_idx = random.choice(range(idx, len(list_index)))
            list_index[idx], list_index[select_idx] = list_index[select_idx], list_index[idx]
    return list_index

def relevance_aware_swapping(num, pho):
    """Relevance-aware swapping algorithm

    Args:
        num (int): the length of list to be sorted
        pho (float): control the sensitivity of swapping two items

    Returns:
        list: a list of randomized indices
    """
    list_index = [i for i in range(num)]
    list_weight = [(1 - i / num) / log2(i + 1) for i in range(1, num + 1)]
    dict_weight = {i: weight for i, weight in enumerate(list_weight)}
    for idx, item in enumerate(list_index):
        if random.uniform(0, 1) <= pho * (1 - dict_weight[idx]):
            select_idx = random.choice(range(idx, len(list_index)))
            list_index[idx], list_index[select_idx] = list_index[select_idx], list_index[idx]
    return list_index

def fairness_greedy(dict_bias, dict_ratio_g, attr, method):
    """Fairness greedy algorithm

    Args:
        dict_bias (dict): the data in a dictionary format 
        dict_ratio_g (dict): the dictionary of ground truths of attribute ratio 
        attr (string): the attribution
        method (string): can be 'switch', 'move_down'

    Returns:
        list: a list of re-ranked results
    """
    N = len(dict_bias)
    rank_list = []
    list_reranked_indices = [i for i in range(N)]
    for i in range(N):
        j = list_reranked_indices[i]
        if len(rank_list) == 0:
            rank_list.append(j)
        else:
            dict_ratio_c = calculate_attr_ratio_real_data(rank_list, dict_bias, attr)
            dict_ratio_diff = {}
            for value in dict_ratio_g:
                if value in dict_ratio_c:
                    dict_ratio_diff[value] = dict_ratio_c[value] - dict_ratio_g[value]
                else:
                    dict_ratio_diff[value] = 0 - dict_ratio_g[value]
            value_min_diff = min(dict_ratio_diff, key=lambda k: dict_ratio_diff[k])
            if dict_bias[j][attr] == value_min_diff:
                rank_list.append(j)
            else:
                flag = False
                for idx, k in enumerate(list_reranked_indices[i + 1:]):
                    value = dict_bias[k][attr]
                    if value == value_min_diff:
                        flag = True
                        break
                if flag == False:
                    for idx, k in enumerate(list_reranked_indices[i + 1:]):
                        value = dict_bias[k][attr]
                        if value == 'Both':
                            flag = True
                            break
                ratio_diff = dict_ratio_diff[value_min_diff]
                if ratio_diff != 0:
                    p = 1
                    if random.uniform(0, 1) <= p:
                        try:
                            if flag == True:
                                if method == 'switch':
                                    list_reranked_indices[i], list_reranked_indices[i + 1 + idx] = \
                                        list_reranked_indices[i + 1 + idx], list_reranked_indices[i]
                                    rank_list.append(k)
                                elif method == 'move_down':
                                    for m in range(i + 1 + idx, i, -1):
                                        list_reranked_indices[m] = list_reranked_indices[m - 1]
                                    list_reranked_indices[i] = k
                                    rank_list.append(k)
                                else:
                                    return 'error'
                            else:
                                rank_list.append(j)
                        except:
                            rank_list.append(j)
                else:
                    rank_list.append(j)
    return rank_list

def calculate_attr_ratio_real_data(rank_list, dict_bias, attr):
    """Calculate the attribute bias in the ranked list

    Args:
        rank_list (list): a ranked list
        dict_bias (dict): the raw data
        attr (string): the attribution

    Returns:
        dict: a dictionary with key-value pairs of attribute-value 
    """
    dict_ratio = {}
    for ele in rank_list:
        if ele in dict_bias:
            value = dict_bias[ele][attr]
            if value not in dict_ratio:
                dict_ratio[value] = 1
            else:
                dict_ratio[value] += 1
    dict_count = {'Woman': 0, 'Man': 0}
    for value in dict_ratio:
        if value == 'Female':
            dict_count['Woman'] += 1
        elif value == 'Male':
            dict_count['Man'] += 1
        elif value == 'Both':
            dict_count['Woman'] += 1
            dict_count['Man'] += 1
    if (dict_count['Woman'] + dict_count['Man']) != 0:
        _sum = dict_count['Woman'] + dict_count['Man']
        dict_count['Woman'] = dict_count['Woman'] / _sum
        dict_count['Man'] = dict_count['Man'] / _sum
    else:
        dict_count['Woman'] = 0.5
        dict_count['Man'] = 0.5
    return dict_count

# Function to load preprocessed images
def load_preprocessed_images(path_image):
    """Load preprocessed images from a directory

    Args:
        path_image (string): path to the preprocessed images directory

    Returns:
        list: list of image filenames
    """
    image_filenames = os.listdir(path_image)
    # print("image_filenames: ",image_filenames)
    return image_filenames

# Function to apply re-ranking algorithm
def apply_re_ranking(image_filenames, algorithm,dict_bias):
    """Apply re-ranking algorithm to a list of image filenames

    Args:
        image_filenames (list): list of image filenames
        algorithm (string): re-ranking algorithm ('epsilon_greedy', 'relevance_aware_swapping', 'fairness_greedy')

    Returns:
        list: a list of re-ranked image filenames
    """
    if algorithm == 'epsilon_greedy':
        re_ranked_indices = epsilon_greedy(len(image_filenames), 0.1)
    elif algorithm == 'relevance_aware_swapping':
        re_ranked_indices = relevance_aware_swapping(len(image_filenames), 0.5)
    elif algorithm == 'fairness_greedy':
        ########################
        # generate data 
        ########################
        
        # count = len(image_filenames)
        # gender gender data 
        count=0
        male_c=0
        female_c=0

        for key,value in dict_bias.items():
            if count==20:
                break
            else:
                if value['gender']=='Man':
                    male_c+=1
                else:
                    female_c+=1
                count+=1

        # print("Keyword: Driver; No of images: 30. ")         
            
        print("Before Re Ranking:")
        print("Male Count:",male_c)
        print("Female_count:",female_c)


        
        female_count = sum(1 for value in dict_bias.values() if value['gender'] == 'Woman')
        male_count=sum(1 for value in dict_bias.values() if value['gender'] == 'Man')
        
        female_ratio=(female_count/(male_count+female_count))
        male_ratio=(male_count/(male_count+female_count))
        # if female_ratio>male_ratio:
        #     male_ratio+=0.2
        #     female_ratio-=0.2
        # else:
        #     female_ratio+=0.2
        #     male_ratio-=0.2
        
        # print(female_ratio,male_ratio)

        dict_ratio_g = {'Woman':0.49 ,'Man':0.41}  # Example ground truth ratio
        # print(dict_ratio_g)
        attr = 'gender'  # Example attribute for fairness
        method = 'move_down'  # Example method for fairness greedy
       # print("Before re-reanking:",image_filenames)
        re_ranked_indices = fairness_greedy(dict_bias, dict_ratio_g, attr, method)
        #print("End of Reranking:",re_ranked_indices)
        #print("re_ranked_indices",len(image_filenames))
    else:
        raise ValueError("Invalid re-ranking algorithm")
    
    # random.shuffle(re_ranked_indices)
   # print("Re Ranked:",re_ranked_indices)
    
    re_ranked_image_filenames = [image_filenames[idx] for idx in re_ranked_indices]
    re_ranked_image_dict_bias = [dict_bias[idx] for idx in re_ranked_indices]
   #c re_ranked_image_dict_bias=dict(re_ranked_image_dict_bias)
    
   # print(re_ranked_image_dict_bias)
    count=0
    male_c=0
    female_c=0
    for value in re_ranked_image_dict_bias:
            if count==20:
                break
            else:
                if value['gender']=='Man':
                    male_c+=1
                else:
                    female_c+=1
                count+=1

    print("After Re Ranking:")
    print("Male_Count:",male_c)
    print("Female_Count:",female_c)

    

    return re_ranked_image_filenames

# Function to create a directory for re-ranked images and copy them there
def create_reranked_image_directory(path_image, re_ranked_image_filenames):
    """Create a directory for re-ranked images and copy them there
    
    Args:
        path_image (string): path to the preprocessed images directory
        re_ranked_image_filenames (list): list of re-ranked image filenames
    """
    reranked_dir = './reranked_images/'
    
    os.makedirs(reranked_dir, exist_ok=True)
    for idx, filename in enumerate(re_ranked_image_filenames):
        source_file = os.path.join(path_image, filename)
        destination_file = os.path.join(reranked_dir, f"{idx}.jpg")
        #print("path_image lol: ",source_file,destination_file)
        shutil.copyfile(source_file, destination_file)
       # print(f"Copied {filename} to {destination_file}")

# Main function
def RankingAlgos(path_image:str,algorithm:str,dict_bias:dict):
    # Path to the preprocessed images directory
    # path_image = 'Doctor'
    #print("path_image: ",path_image)
    # Load preprocessed images
    image_filenames = load_preprocessed_images(path_image)

    # Choose re-ranking algorithm
    # algorithm = 'relevance_aware_swapping'  # Change this to the desired algorithm

    # Apply re-ranking algorithm
    re_ranked_image_filenames = apply_re_ranking(image_filenames, algorithm,dict_bias)

    # Create a directory for re-ranked images and copy them there
    create_reranked_image_directory(path_image, re_ranked_image_filenames)
    return "Reranked sucessfully."

# if __name__ == "__main__":
#     main()


#print(load_preprocessed_images("GenderDetection/ScrapedImages"))
