#  Copyright (c) 2025.
import numpy as np
class LinearAlgPowerCalculation:
    model_one = 1
    model_two = 4
    model_two_start = 30
    def __init__(self):
        pass
def main():
    get_models_power()
def avg_power():
    avg_power_generation_one_two = (LinearAlgPowerCalculation.model_one+LinearAlgPowerCalculation.model_two)/2
    return avg_power_generation_one_two

def get_models_power():
    model_one__two_start = (LinearAlgPowerCalculation.model_one * LinearAlgPowerCalculation.model_two_start)
    model_one__total_at_model_one__two_start = (model_one__two_start/LinearAlgPowerCalculation.model_two)+model_one__two_start
    model_one = model_one__total_at_model_one__two_start
    model_two = model_one__two_start
    print(f'Model One at Model Two Start: {model_one__two_start}')
    print(f'Model One at Model Two Reach, Model two start point : {model_one__total_at_model_one__two_start}')
    while model_two < model_one :
        model_one += LinearAlgPowerCalculation.model_one
        model_two += LinearAlgPowerCalculation.model_two
        print(model_two+avg_power())
        if model_one<model_two:
            model_one -=.5
            model_two -=2
            if model_one==model_two:
                print(f'Number of days to reach same production of power :{model_two} kj')
                print(f'Total production @ {model_two} : {model_one+model_two} kj')
            break

if __name__ == '__main__':
    main()