#!/bin/python3

import math
import os
import random
import re
import sys
import requests
def getNumDraws(year):
ans=0
for i in range(0,11):
url="[https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team1goals="+str(i)+"&team2goals=](https://jsonmock.hackerrank.com/api/football_matches?year=%22+str(year)+%22&team1goals=%22+str(i)+%22&team2goals=)"+str(i)
### fetching every url with equal goal of both team and adding the total matches played to answer
response=requests.get(url)
result=response.json()
ans+=int(result['total'])
return ans
if **name** == '**main**':
fptr = open(os.environ['OUTPUT_PATH'], 'w')
year = int(input().strip())

result = getNumDraws(year)

fptr.write(str(result) + '\\n')

fptr.close()