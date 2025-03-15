#function is a block of code that you can package together with a name and does something
def PrintCar():
    text = "mercedes is cool"
    print(text)
PrintCar()

#if statement with a function 
def school_age_calculator(age,name):
    if age< 5 :
        print("enjoy the time!",name,"is only",age)
    elif age == 5:
        print("enjoy kindergarten",name)
    else:
        print("they grow up so fast")
school_age_calculator(2,"Neema")

#getting a parameter from a function
def add_10_to_age(age):
    new_age = age+10
    return new_age
age_update = add_10_to_age(20)
print(age_update)
