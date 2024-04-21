#!/bin/python3

import math
import os
import random
import re
import sys
import requests
def getWinnerTotalGoals(competition, year):
    url="https://jsonmock.hackerrank.com/api/football_competitions?name="+str(competition)+"&year="+str(year)
    response=requests.get(url)
    result=response.json()
    #print(result)
    winner=str(result['data'][0]['winner'])
    url_1="https://jsonmock.hackerrank.com/api/football_matches?competition="+str(competition)+"&year="+str(year)+"&team1="+str(winner)
    url_2="https://jsonmock.hackerrank.com/api/football_matches?competition="+str(competition)+"&year="+str(year)+"&team2="+str(winner)
    response_1=requests.get(url_1)
    response_2=requests.get(url_2)
    result_1=response_1.json()
    result_2=response_2.json()
    ans=0
    for i in range(1,int(result_1['total_pages'])+1):
        temp_url="https://jsonmock.hackerrank.com/api/football_matches?competition="+str(competition)+"&year="+str(year)+"&team1="+str(winner)+"&page="+str(i)
        temp_response=requests.get(temp_url)
        temp_result=temp_response.json()
        for i in temp_result['data']:
            ans+=int(i['team1goals'])
    for i in range(1,int(result_2['total_pages'])+1):
        temp_url2="https://jsonmock.hackerrank.com/api/football_matches?competition="+str(competition)+"&year="+str(year)+"&team2="+str(winner)+"&page="+str(i)
        temp_response2=requests.get(temp_url2)
        temp_result2=temp_response2.json()
        for i in temp_result2['data']:
            ans+=int(i['team2goals'])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()