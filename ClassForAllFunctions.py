class AllFunctions:
    def subFields():
        subFiledList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in subFiledList:
            print(temp)

    def  findEvenOdd():
        num=int(input("Enter a number:"))
        if (num %2==0):
            print(num, "is Even number")
            message="Even number"
        else:
            print(num, "is Odd Number")
            message="Odd number"
        return message

    def marriageEligibility():
        gender=input("Your Gender:") 
        age=int(input("Your Age:")) 
        if((gender == "Male" or gender =="MALE" )and age>=21):
            eligibility="ELIGIBLE"
            print(eligibility)
        elif((gender == "Female" or gender == "FEMALE" )and age>=18):
             eligibility="ELIGIBLE"
             print(eligibility)
        else:
            eligibility="NOT ELIGIBLE"
            print(eligibility)
        return eligibility        

    def percentage():
        subject1= int(98) 
        subject2= int(87) 
        subject3= int(95) 
        subject4= int(95) 
        subject5= int(93) 
        total = subject1+ subject2 + subject3+subject4+subject1
        percentage= float((total/500)*100)
        print("Total:",total)
        print("Percentage:", percentage)
        return percentage        

    def triangle():
        height=int(32) 
        breadth=int(34) 
        areaOfTriange= float((height*breadth)/2)
        print("Height :",height) 
        print("Breadth :",breadth) 
        print("Area formula: (Height*Breadth)/2 ")
        print("Area of Triangle:",  areaOfTriange)
        
        height1=int(2) 
        height2=int(4) 
        breadth1=int(4) 
        perimeterOfTriangle=height1+height2+breadth1 
        print("Height1 :",height1)
        print("Height2 :",height2)
        print("Breadth :",breadth1)
        print("Perimeter formula: Height1+Height2+Breadth ")
        print("Perimeter of Triangle:",  perimeterOfTriangle)
        return         