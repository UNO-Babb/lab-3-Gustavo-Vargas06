#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  TempF = input("Enter a fahrenheit temperature: ")
  TempF = int(TempF)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  TempC = 5 / 9 * (TempF - 32)
  TempC = round(TempC, 1)
  #Output converted temperature.


  print(TempF, "is ", TempC, "degrees celsius.")
if __name__ == '__main__':
  main()
