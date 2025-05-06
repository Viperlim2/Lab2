def calculate_bmi(height, weight):
    print("Height=",height)
    print("Weight= ",weight)
    bmi = weight/(height*height) 
    print("bmi " ,bmi)

    return bmi

def classify_bmi(bmi):
    if(bmi < 18.5):
         print("underweight")
    elif(bmi >= 18.5 and bmi <= 25 ):
        print("normal weight")
    else:
        print("overweight, exercise!")
    return

def app(): 
    output=calculate_bmi(57,2.7)
    classify_bmi(output)
    return

if __name__ == "__main__":
    app()
