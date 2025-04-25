#  Copyright (c) 2025.
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
     while model_one_total() < model_two_total() :
        model_one = model_two_total()+(avg_power() * LinearAlgPowerCalculation.model_one)
        model_two = model_one_total()+(avg_power() * LinearAlgPowerCalculation.model_two)
        if model_one==model_two:
            print(f'Power production of Model One :{model_one} and Power production of Model Two :{model_two}  kj')
            print(f'Total production of Model One and Model Two : {model_one+model_two} kj')
            print(f'Model One Total Days : {model_one} , Model Two Total Days : {model_two-LinearAlgPowerCalculation.model_two_start} ')
        else:
            print(f'Model One : {model_one} and Model Two : {model_two} never meet ')
        break
if __name__ == '__main__':
    main()