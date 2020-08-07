import os
from PIL import Image
import numpy as np
import cv2
import math
import numpy as np
import sklearn.preprocessing as sk
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.color import rgb2gray
from scipy.misc import toimage


def get_pad_width(im, new_shape, is_rgb=True):

    pad_diff = new_shape - im.shape[0], new_shape - im.shape[1]

    t, b = math.floor(pad_diff[0]/2), math.ceil(pad_diff[0]/2)

    l, r = math.floor(pad_diff[1]/2), math.ceil(pad_diff[1]/2)

    if is_rgb:

        pad_width = ((t,b), (l,r), (0, 0))

    else:

        pad_width = ((t,b), (l,r))

    return pad_width

 

def crop_image_from_gray(img,tol=7):

    if img.ndim ==2:

        mask = img>tol

        return img[np.ix_(mask.any(1),mask.any(0))]

    elif img.ndim==3:

        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        mask = gray_img>tol

       

        check_shape = img[:,:,0][np.ix_(mask.any(1),mask.any(0))].shape[0]

        if (check_shape == 0): # image is too dark so that we crop out everything,

            return img # return original image

        else:

            img1=img[:,:,0][np.ix_(mask.any(1),mask.any(0))]

            img2=img[:,:,1][np.ix_(mask.any(1),mask.any(0))]

            img3=img[:,:,2][np.ix_(mask.any(1),mask.any(0))]

    #         print(img1.shape,img2.shape,img3.shape)

            img = np.stack([img1,img2,img3],axis=-1)

    #         print(img.shape)

        return img

   

def preprocess_image(image, sigmaX=40):   

    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image1 = crop_image_from_gray(image1)

    image1=cv2.resize(image1,(512,512), Image.ANTIALIAS)
    return image1


       



#files = next(os.walk('A:/HealthAnalytics/image_Processing/Project/images'))[2]
path='.\Project'
files = next(os.walk(path+'/Train_data'))[2]
for filename in files:
    #path='A:/HealthAnalytics/image_Processing/Project/images/'+filename    
    path=path+'/Train_data'+filename
    image  = cv2.imread(path)
    color_processed = preprocess_image(image)    
    shape = color_processed.shape
    image_scaled = sk.minmax_scale(color_processed.ravel(), feature_range=(0,1)).reshape(shape)   
#plt.imshow(color_processed)

#plt.hist(color_processed.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram
#plt.hist(entr_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram


    rgbimage = rgb2gray(image_scaled)

    entr_img = entropy(rgbimage, disk(10))

    entr_img_resize = cv2.resize(entr_img,(256,256), Image.ANTIALIAS)
#plt.imshow(entr_img_resize)
    image_entropy = toimage(entr_img_resize)
#plt.imshow(image_entropy)
    image_entropy.save(path+filename)


