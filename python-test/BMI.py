def BMI(w,h):
    return round((w/h**2),2)

def category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"

if __name__ == "__main__":
    w = float(input("Enter your weight in kg: "))
    h = float(input("Enter your height in meters: "))
    bmi = BMI(w,h)
    print("Your BMI is: ",bmi)
    print("Your category is: ",category(bmi))