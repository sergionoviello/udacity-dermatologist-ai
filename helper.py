import os
import numpy as np
from keras.preprocessing import image
from PIL import Image
PATH = os.getcwd()

def load_data():
  test_path = PATH+'/data/valid/'
  train_path = PATH+'/data/train/'
  x_train = []
  x_test = []
  classes = []

  cnt = 0
  for subdir, dir, files in os.walk(train_path):
    classes.append(dir)
    for file in files:
      img_path = os.path.join(subdir, file)
      image = Image.open(img_path)
      resize = image.resize((150,150), Image.NEAREST)
      resize.load()
      data = np.asarray( resize, dtype="uint8" )
      x_train.append(data)

  # for subdir, dir, files in os.walk(test_path):
  #   for file in files:
  #     img_path = os.path.join(subdir, file)
  #     x = image.load_img(img_path)
  #     x_test.append(x)

  x_train = np.array(x_train)
  x_test = np.array(x_test)
  return x_train, x_test