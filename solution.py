from collections import OrderedDict
import datetime 
import unittest

# Function to find the day of the key values which are in YYYY-MM-DD format
def findDay(date): 
    try:
        year, month, day = (int(i) for i in date.split('-'))     
        days = datetime.date(year, month, day) 
        return days.strftime("%a")
    except Exception:
        False
        pass

# Funtion that returns the solution to the problem
def solution(D):

    if len(D)<2:
        return False
#     creating ordered dictionary variable
    days=OrderedDict()
#     creating a dictionary with abbreviated date values
    days={'Mon':None,'Tue':None,'Wed':None,'Thu':None,'Fri':None,'Sat':None,'Sun':None}
    
#     creating a list of abbreviated days
    days_list=list(days)
    
#     This loop adds sum of integer values of key(Dates) respective to their days in the dictionary
    for i in D:
        if days[findDay(i)]==None:
            days[findDay(i)]=0+D[i]
        else:
            days[findDay(i)]=days[findDay(i)]+D[i]

    if days['Mon']==None or days['Sun']==None:
        return False       
#     if the days are missing in the dictionary 
#     this loops checks those days and add the mean of prev and next day integer value to this missing day
    for i in days_list:

        if days[i]==None:   #checks whether the day is missing
            
                days[i] = 2*days[days_list[days_list.index(i)-1]] - days[days_list[days_list.index(i)-2]] #this will assign integer value to the missing day
                
    return days    
    
        