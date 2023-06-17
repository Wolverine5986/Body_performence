import pickle
from . import CONFIG as path
import numpy as np
import os

class Prediction():
    def __init__(self,data):
        self.data = data


    def load_raw(self):
        print(os.getcwd())
        with open(path.model_path,'rb') as file:
            self.model = pickle.load(file)

    def output_prediction(self):
        self.load_raw()
        age = self.data['age']
        height = self.data['height']
        bodyfat = self.data['bodyfat']
        systolic= self.data['systolic']
        gripForce= self.data['gripForce']
        sit_and_bend_forward_cm= self.data['sit_and_bend_forward_cm']
        sit_ups_counts = self.data['sit_ups_counts']
        broad_jump_cm = self.data['broad_jump_cm']

        data_list = np.array([age,height,bodyfat,systolic,gripForce,sit_and_bend_forward_cm,sit_ups_counts,broad_jump_cm], dtype=float).tolist()

        result = self.model.predict([data_list])
        print(result)
        return (f'{(str(result[0]))}')
    

if __name__ == "__main__":
    obj = Prediction()
    obj.load_raw()
