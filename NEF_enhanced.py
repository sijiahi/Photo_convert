#!/usr/bin/env python
# coding: utf-8

# In[5]:


import rawpy
import imageio
from tqdm import tqdm
import rawpy.enhance


# In[6]:


def is_image(filename):
    return any(filename.endswith(extension) for extension in ['.NEF', ''])


# In[7]:


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


# In[10]:


if not os.path.exists(path+'/enhanced/'):
    os.mkdir(path+'/enhanced/')
bad_pixels+=rawpy.enhance.find_bad_pixels(image_filenames)
for i in tqdm(range(len(image_filenames))):
    image = image_filenames[i]
    with rawpy.imread(image) as raw:
        rawpy.enhance.repair_bad_pixels(raw, bad_pixels, method='median')
        rgb = raw.postprocess()
    file_path,file_name = os.path.split(image);
    imageio.imsave(file_path+"/enhanced/"+os.path.splitext(file_name)[0]+ '.jpg', rgb)


# In[ ]:


import rawpy.enhance

paths = ['image1.nef', 'image2.nef', 'image3.nef']
bad_pixels = rawpy.enhance.find_bad_pixels(paths)

for path in paths:
    with rawpy.imread(path) as raw:
        rawpy.enhance.repair_bad_pixels(raw, bad_pixels, method='median')
        rgb = raw.postprocess()
    imageio.imsave(path + '.tiff', rgb)

