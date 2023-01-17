# Student_4926137_on_17_01_2023
import json

with open ("precipitation.json", encoding='utf-8') as file:
    my_file = json.load(file)

# Part 1
# Sorting theough location
#for dict_item in my_file:
 #   if(dict_item["station"] == "GHCND:US1WAKG0038"):
  #      print(dict_item["value"])
    
# Grouping by months

# months_dictionary corresponds to total_monthly_precipitation in the exercise instructions

months_dictionary = {'1':0, '2': 0, '3': 0, '4': 0, '5': 0,'6': 0,'7': 0,'8': 0,'9': 0, '10': 0, '11': 0, '12': 0}

# Barbarian Method - it works, but if you want to see my shot at transforming it into loop, look below

for dict_item in my_file:
    if(dict_item["station"] == "GHCND:US1WAKG0038"):
        if dict_item["date"].startswith("2010-12"):
            months_dictionary['12'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-11"):
            months_dictionary['11'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-10"):
            months_dictionary['10'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-09"):
            months_dictionary['9'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-08"):
            months_dictionary['8'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-07"):
            months_dictionary['7'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-06"):
            months_dictionary['6'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-05"):
            months_dictionary['5'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-04"):
            months_dictionary['4'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-03"):
            months_dictionary['3'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-02"):
            months_dictionary['2'] += (dict_item["value"]) 
        if dict_item["date"].startswith("2010-01"):
            months_dictionary['1'] += (dict_item["value"]) 
    
print(months_dictionary)

# Smart method - transforming into loop

#for dict_item in my_file:
 #   if(dict_item["station"] == "GHCND:US1WAKG0038"):
  #      for month in months_dictionary:
   #      if dict_item["date"].startswith("2010-"+month):
    #        months_dictionary[month] += (dict_item["value"])


# Saving to json file

with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(months_dictionary, json_file, indent=4)


# Part 2

#  total_yearly_precipitation,

total_yearly_precipitation = sum(months_dictionary.values())
print("Total yearly precipitation eqals", total_yearly_precipitation)

# relative_monthly_precipitation

relative_monthly_precipitation = {'1':0, '2': 0, '3': 0, '4': 0, '5': 0,'6': 0,'7': 0,'8': 0,'9': 0, '10': 0, '11': 0, '12': 0}

for month in months_dictionary.values():
    print(int(month)/int(total_yearly_precipitation))

# Part 3


# Part 3

#import csv

#stations_file = open('stations.csv', 'r')

#file = csv.DictReader(stations_file)

#station = []

#for col in file:
    #station.append(col['Station'])