#  Copyright (c) 2025.
import numpy as np
class LinearAlgPowerCalculation:
    model_one = 1
    model_two = 4
    model_two_start = 30
    def __init__(self):
        pass
def main():
    get_models_power_cal()
def avg_power():
    avg_power_generation_one_two = (LinearAlgPowerCalculation.model_one+LinearAlgPowerCalculation.model_two)/2
    return avg_power_generation_one_two
def model_one_total():
    model_one_total_two = (LinearAlgPowerCalculation.model_one * LinearAlgPowerCalculation.model_two_start)
    return model_one_total_two
def model_two_total():
     model_two_total_one = (model_one_total()/LinearAlgPowerCalculation.model_two)+model_one_total()
     return model_two_total_one
def get_models_power_cal():
    #print(f'Model One at Model Two Start: {model_two_total()}')
    #print(f'Model One at Model Two Reach, Model two start point @ {model_two_total()} : {model_one_total()}')
    while model_one_total() < model_two_total() :
        model_one = model_two_total()+(avg_power() *1)
        model_two = model_one_total()+(avg_power() * 4)
        if model_one==model_two:
            print(f'Power production of Model One :{model_one} and Power production of Model Two :{model_two}  kj')
            print(f'Total production of Model One and Model Two : {model_one+model_two} kj')
        break
if __name__ == '__main__':
    main()