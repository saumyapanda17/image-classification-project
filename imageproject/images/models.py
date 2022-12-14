import io

from django.db import models
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
from keras.applications.vgg16 import preprocess_input, decode_predictions


# Create your models here.
class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classfied at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = load_img(self.picture.path, target_size=(299, 299))
            img_array = img_to_array(img)
            to_pred = np.expand_dims(img_array, axis=0)
            prep = preprocess_input(to_pred)
            model = InceptionResNetV2(weights='imagenet')
            prediction = model.predict(prep)
            decoded = decode_predictions(prediction)[0][0][1]
            self.classified = str(decoded)
            Image.objects.filter(pk=self.id).update(classified=self.classified)
            print('success')
        except Exception as e:
            print(f"Classification failed: {e}")



    # def save(self, *args, **kwargs):
    #     try:
    #         img = load_img(io.BytesIO(self.picture), target_size=(299, 299))
    #         # img = load_img(self.picture, target_size=(299,299))
    #         img_arry = img_to_array(io.BytesIO(img))
    #         # img_arry = img_to_array(img)
    #         to_pred = np.expand_dims(img_arry, axis=0) #(1, 299, 299, 3)
    #         prep = preprocess_input(to_pred)
    #         model = InceptionResNetV2(weights='imagenet')
    #         prediction = model.predict(prep)
    #         decoded = decode_predictions(prediction)[0][0][1]
    #         self.classified = str(decoded)
    #         print(str(decoded))
    #         print('success')
    #     except Exception as e:
    #         print('classification failed', e)
    #     super().save(*args, **kwargs)
