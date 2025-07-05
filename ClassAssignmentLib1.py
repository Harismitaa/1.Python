class MulFuncLib():
    list1=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
    def SubFields():
        print("Sub-fields in AI are:")
        for temp in MulFuncLib.list1:
            print(temp)
    def OddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print("The number is Even")
        else:
           print("The number is Odd")     
    def Marriage_Eligibility():
        Gender=input("Your Gender(Male/Female):")
        Age=int(input("Your Age:"))
        if(Gender=="Male"):
            if(Age>=21):
                message="Eligible"
            else:
                message="Not Eligible"
        elif(Gender=="Female"):
            if(Age>=18):
                message="Eligible"
            else:
                message="Not Eligible"
        return message
    def Percentage_10th():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total=",Total)
        Percentage=Total/5
        print("Percentage=",Percentage)
    def Area(h,b):
        print("Area formula: (Height*Breadth)/2")
        Area=(h*b)/2
        print("Area of Triangle:",Area) 
    def Perimeter(h1,h2,b1):
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter=h1+h2+b1
        print("Perimeter of Triangle:",Perimeter)


