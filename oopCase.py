###################################
#                                 #
# Author : Berke Kocadere         #
#                                 #
# WEB3 OOP-CASE                   #
# 11.09.2022                      #
###################################

# imports 
from datetime import datetime

# Parent Class 
class AutoClass():
    def __init__(self, number, name, Balance):
        # Attributes 
        self.number = number
        self.name = name
        self.Balance = int(Balance)
        self.datetime = self.getDateTime()
        print(self.number ,"\n" , self.name ,"\n" , self.Balance
              , "\n", self.datetime)

    def getDateTime(self):
        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def getNumber(self):
        return self.number

    def getName(self):
        return self.name

    def getBalance(self):
        return int(self.Balance)

    def changeBalance(self, tollFee):
        self.Balance = self.Balance - tollFee

# Inherited Automobile Class 
class automobile(AutoClass):
    def __init__(self, number, name, Balance):
        AutoClass.__init__(self, number, name, Balance)
        self.vehicleClass = "automobile"
        print(self.vehicleClass)

    def getVehicleClass(self):
        return self.vehicleClass

# Inherited minibus Class
class minibus(AutoClass):
    def __init__(self, number, name, Balance):
        AutoClass.__init__(self, number, name, Balance)
        self.vehicleClass = "minibus"
        print(self.vehicleClass)

    def getVehicleClass(self):
        return self.vehicleClass

# Inherited autobus Class
class autobus(AutoClass):
    def __init__(self, number, name, Balance):
        AutoClass.__init__(self, number, name, Balance)
        self.vehicleClass = "autobus"
        print(self.vehicleClass)

    def getVehicleClass(self):
        return self.vehicleClass

# Management Class 
class Management():
    def __init__(self, toll):
        self.toll = toll
        self.totalBalance = 0

    def getTotalBalance(self):
        # Function to get total Daily Balance
        for vehicle in self.toll.getVehicleArray():
            self.totalBalance = self.totalBalance + int(vehicle.getBalance())

        print("Daily Total Balance : " , int(self.totalBalance))

# Toll Class 
class tollClass():
    def __init__(self):
        self.vehicleArray = list()

    def Payment(self, vehicleInfo):
        #Function for fee payment for each vehicle in toll 
        self.vehicleArray.append(vehicleInfo)
        print(self.vehicleArray)
        if vehicleInfo.getVehicleClass() == "automobile":
            vehicleInfo.changeBalance(10)
        elif vehicleInfo.getVehicleClass() == "minibus":
            vehicleInfo.changeBalance(20)
        elif vehicleInfo.getVehicleClass() == "autobus":
            vehicleInfo.changeBalance(30)

        print("Payment for ", vehicleInfo.getVehicleClass()
              ,"class vehicle." , "New Balance is" , vehicleInfo.getBalance())

    def getVehicleArray(self):
        return self.vehicleArray

# Main function
if __name__ == "__main__":
    toll = tollClass() # Toll class creation 
    management = Management(toll) # Management class creation

    # Infinite Loop 
    while(True):
        number = input("Get HGS number : ") 
        name = input("Get name and surname: ")
        vehicleClass = input("Get vehicle class : ")
        Balance = input("Get Balance : ")

        # Check which type of vehicle is it and create that type class
        if vehicleClass == "automobile":
            vehicleInfo = automobile(number, name, Balance)
        elif vehicleClass == "minibus":
            vehicleInfo = minibus(number, name, Balance)
        elif vehicleClass == "autobus":
            vehicleInfo = autobus(number, name, Balance)

        toll.Payment(vehicleInfo) # Payment method 
        management.getTotalBalance() # Daily Total Balance method 