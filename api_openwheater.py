# coding: utf-8

# simple class to retrieve wheater data (current of forecast)
import requests

# create object with one parameter = city name
class Wheather:

    # get AAPID from the txt file
    def __init__(self, city, par=0):

        self.city = city
        self.par = par

# get AAPID from the txt file 
    def auth(self,author = "AAPID"):
        self.author = author
        file = open("auth.txt","r")
        author = file.read()
        return author
        
# call function to retrieve current wheather data (possible parameters: temp, pressure, humidity, visibility)         
    def current_w(self,*arg):
        author = self.auth()
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}".format(self.city,author))
        r = r.json()
        dic = {}
        for item in arg:
            dic[item] = r["main"][item]
        return dic

# call function to retreive and print out forecast wheather data for next 5 days (possible parameters: temp, pressure, humidity, visibility)             
    def forecast_w(self,*arg):
        author = self.auth()
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&units=metric&APPID={}".format(self.city,author))
        r = r.json()
        dic = {}
        dic2 ={}
        for item in r["list"]:
            print(item["dt_txt"])
            for key, value in item["main"].items():
                for item2 in arg:
                    if item2 == key:
                        print(str(key) + " : " + str(value))
                        
