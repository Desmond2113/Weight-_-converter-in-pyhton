#This programme is designed for weight convertion from Pounds to Kilogram OR Kilogram to Pound

name = input('what is your name ?  ')
weight_input = int(input('Please enter your weight-->  '))
kilo_pounds_unit = input('Please enter unit of weight: kg or lbs:  ')
conv_to_pounds = weight_input / 0.45359237
conv_to_kg = weight_input * 0.45359237
if kilo_pounds_unit == 'kg':
    print('Hi human your weight in kilogram is ', + conv_to_pounds)
elif kilo_pounds_unit == "lbs":
    print('Hi human your weight in kilogram is ', + conv_to_kg)
else:
    print('Please read instructions again and stop being a human lol haha')




