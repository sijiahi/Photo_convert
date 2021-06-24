#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rawpy
import imageio
import os
from tqdm import tqdm


# In[2]:


def is_image(filename):
    return any(filename.endswith(extension) for extension in ['.NEF', ''])


# In[12]:


path = '/Users/sijiazhang/Desktop/20210621张思嘉/'
def get_img_file(file_name):
    image_filenames = []
    for parent, dirnames, filenames in os.walk(file_name):
        for filename in filenames:
            #print(filename)
            if filename.lower().endswith('.nef'):
                image_filenames.append(os.path.join(parent, filename))
        return image_filenames
image_filenames = get_img_file(path)


# In[14]:


if not os.path.exists(path+'/JPG/'):
    os.mkdir(path+'/JPG/')
for i in tqdm(range(len(image_filenames))):
    image = image_filenames[i]
    with rawpy.imread(image) as raw:
        rgb = raw.postprocess()
    file_path,file_name = os.path.split(image);
    imageio.imsave(file_path+"/JPG/"+os.path.splitext(file_name)[0]+ '.jpg', rgb)


# In[ ]:




