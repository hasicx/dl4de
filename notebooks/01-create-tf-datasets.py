#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf


# In[ ]:


ds_keras = tf.keras.utils.image_dataset_from_directory(
    directory="../datasets/kitti/training/image_2/", 
    labels=None,
    image_size=[375,1242]
)


# In[ ]:


ds_features = tf.data.Dataset.list_files(
    file_pattern="../datasets/kitti/training/image_2/*.png",
    shuffle=False
)
ds_targets = tf.data.Dataset.list_files(
    file_pattern="../datasets/kitti/training/semantic/*.png",
    shuffle=False
)


# In[ ]:


def decode_img(img):
    img = tf.io.decode_png(img)
    img = tf.image.resize(img, [375, 1242])
    return img

def process_path(file_path):
    img = tf.io.read_file(file_path)
    img = decode_img(img)
    return img


# In[ ]:


ds_features = ds_features.map(process_path)
ds_targets = ds_targets.map(process_path)

