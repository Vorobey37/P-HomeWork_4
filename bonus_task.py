
"""
*****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь
"""

numberDict = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", 
              "7": "семь", "8": "восемь", "9": "девять", "10": "десять", "11": "одиннадцать", 
              "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", 
              "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать", 
              "20": "двадцать", "30": "тридцать", "40": "сорок", "50": "пятьдесят", "60": "шестьдесят", 
              "70": "семьдесят", "80": "восемьдесят", "90": "девяносто", "100": "сто", "200": "двести", 
              "300": "тристо", "400": "четыресто", "500": "пятьсот", "600": "шестьсот", "700": "семьсот", 
              "800": "восемьсот", "900": "девятьсот", "тыс1": "тысяча", "тыс2": "тысячи", "тыс3": "тысяч" }

number = input("Введите число: ")
rankNumber = len(number)
number = int(number)
text = ""
text1 = numberDict['тыс1'] + " "
text2 = numberDict['тыс2'] + " "
text3 = numberDict['тыс3'] + " "

if rankNumber == 1:
    print(numberDict[f'{number}'])
    
if rankNumber == 2:
    if number>9 and number<=20:
        print(numberDict[f'{number}'])
    else:
        a = number - number%10
        b = number%10
        text = text + numberDict[f'{a}'] + " " + numberDict[f'{b}']
        
if rankNumber == 3:
    a = number - number%100
    b = number%100
    c = number%10
    d = number%100-number%10
  
    if b<=20 or c == 0:
        text = text + numberDict[f'{a}'] + " " + numberDict[f'{b}']
    else:
        text = text + numberDict[f'{a}'] + " " + numberDict[f'{d}'] + " " + numberDict[f'{c}']
    
if rankNumber == 4:
    a1 = number//1000
    a = number%1000 - number%100
    b = number%100
    c = number%10
    d = number%100-number%10
    if a1%1000 == 0:
        if a1 == 1:
            text = "одна " + text1
        if a1 == 2:
            text = "две " + text2
        if a1 == 3 and a1 == 4:
            text = numberDict[f'{a1}'] + " " + text2
        if a1 >= 5 and a1 <= 9:
            text = numberDict[f'{a1}'] + " " + text3 
        
    if a<100:
        if b<=20 and b>0 or c == 0:
            texta = text +  numberDict[f'{b}']
        else:
            texta = text + numberDict[f'{d}'] + " " + numberDict[f'{c}']
    else:        
        if b<=20 and b>0 or c == 0:
            texta = text + numberDict[f'{a}'] + " " + numberDict[f'{b}']
        else:
            texta = text + numberDict[f'{a}'] + " " + numberDict[f'{d}'] + " " + numberDict[f'{c}']
    
    if a1 == 1:
        text = "одна " + text1 + texta
    if a1 == 2:
        text = "две " + text2 + texta
    if a1 == 3 and a1 == 4:
        text = numberDict[f'{a1}'] + " " + text2 + texta
    if a1 >= 5 and a1 <= 9:
        text = numberDict[f'{a1}'] + " " + text3 + texta
    
        
    
    
        
        
        
print(rankNumber)
print(text)