def calculate_bmi(height, weight):
    print("Height=",height)
    print("Weight= ",weight)
    bmi = weight/(height*height) 
    print("bmi " ,bmi)

    return bmi

def classify_bmi(bmi):
    if(bmi < 18.5):
         print("-1")
    elif(bmi >= 18.5 and bmi <= 25 ):
        print("0")
    else:
        print("1")
    return

def app(): 
    output=calculate_bmi(57,2.7)
    classify_bmi(output)
    return

if __name__ == "__main__":
    app()
