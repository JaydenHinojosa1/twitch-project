#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:59:04 2018

@author: jaydencarr
"""


from twitch import TwitchClient
import csv
import os
import datetime

client = TwitchClient(client_id='20aue0ca5p6vezl8f3tqkxk7stircs', oauth_token='oauth:cbnohhym7l3kk882hse5ts5nzqex4v')
channel = client.channels.get_by_id(226896585)
print(datetime.datetime.now())
print(channel.id)
print(channel.name)
print(channel.display_name)
print(channel.items)
print(channel.get)
print(channel.construct_from)
print(channel.refresh_from)


game = client.games.get_top(100)
json_data_list = (game)
#read data from json data list
for json_data in json_data_list:  
    game_data = json_data["game"]

    print("{:<40} {:<12} {:<10} {:<10} {:<10}".format(game_data["name"],game_data["popularity"],game_data["id"],json_data["viewers"],json_data["channels"]))

#os.remove('games.csv')
    
with open('games.csv', 'a') as writeFile:
    
    fieldnames = ['name','popularity','viewers','channels','datetime']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames, delimiter = '\t')

    # write fieldnames 
    writer.writeheader()

    # initialize for loop to iterate over json-Data-List
    for json_data in json_data_list:
        game_data = json_data["game"]
        writer.writerow(dict(zip(fieldnames,[game_data["name"],game_data["popularity"],json_data["viewers"],json_data["channels"]],)))
    
writeFile.close()
import time, sys

def writeText(string, t):
    i = 0
    while i < len(string):
        sys.stdout.write(string[i])
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()
writeText("Starting Again", 1.60)


from twitch import TwitchClient
import csv
import os
import datetime

client = TwitchClient(client_id='20aue0ca5p6vezl8f3tqkxk7stircs', oauth_token='oauth:cbnohhym7l3kk882hse5ts5nzqex4v')
channel = client.channels.get_by_id(226896585)
print(datetime.datetime.now())
print(channel.id)
print(channel.name)
print(channel.display_name)
print(channel.items)
print(channel.get)
print(channel.construct_from)
print(channel.refresh_from)


game = client.games.get_top(100)
json_data_list = (game)
#read data from json data list
for json_data in json_data_list:  
    game_data = json_data["game"]

    print("{:<40} {:<12} {:<10} {:<10} {:<10}".format(game_data["name"],game_data["popularity"],game_data["id"],json_data["viewers"],json_data["channels"]))

#os.remove('games.csv')
    
with open('games.csv', 'a') as writeFile:
    
    fieldnames = ['name','popularity','viewers','channels','datetime']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames, delimiter = '\t')

    # write fieldnames 
    writer.writeheader()

    # initialize for loop to iterate over json-Data-List
    for json_data in json_data_list:
        game_data = json_data["game"]
        writer.writerow(dict(zip(fieldnames,[game_data["name"],game_data["popularity"],json_data["viewers"],json_data["channels"]],)))
    
writeFile.close()
import time, sys

def writeText(string, t):
    i = 0
    while i < len(string):
        sys.stdout.write(string[i])
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()
writeText("Starting Again", 1.60)


from twitch import TwitchClient
import csv
import os
import datetime

client = TwitchClient(client_id='20aue0ca5p6vezl8f3tqkxk7stircs', oauth_token='oauth:cbnohhym7l3kk882hse5ts5nzqex4v')
channel = client.channels.get_by_id(226896585)
print(datetime.datetime.now())
print(channel.id)
print(channel.name)
print(channel.display_name)
print(channel.items)
print(channel.get)
print(channel.construct_from)
print(channel.refresh_from)


game = client.games.get_top(100)
json_data_list = (game)
#read data from json data list
for json_data in json_data_list:  
    game_data = json_data["game"]

    print("{:<40} {:<12} {:<10} {:<10} {:<10}".format(game_data["name"],game_data["popularity"],game_data["id"],json_data["viewers"],json_data["channels"]))

#os.remove('games.csv')
    
with open('games.csv', 'a') as writeFile:
    
    fieldnames = ['name','popularity','viewers','channels','datetime']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames, delimiter = '\t')

    # write fieldnames 
    writer.writeheader()

    # initialize for loop to iterate over json-Data-List
    for json_data in json_data_list:
        game_data = json_data["game"]
        writer.writerow(dict(zip(fieldnames,[game_data["name"],game_data["popularity"],json_data["viewers"],json_data["channels"]],)))
    
writeFile.close()
import time, sys

def writeText(string, t):
    i = 0
    while i < len(string):
        sys.stdout.write(string[i])
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()
writeText("Starting Again", 1.60)


from twitch import TwitchClient
import csv
import os
import datetime

client = TwitchClient(client_id='20aue0ca5p6vezl8f3tqkxk7stircs', oauth_token='oauth:cbnohhym7l3kk882hse5ts5nzqex4v')
channel = client.channels.get_by_id(226896585)
print(datetime.datetime.now())
print(channel.id)
print(channel.name)
print(channel.display_name)
print(channel.items)
print(channel.get)
print(channel.construct_from)
print(channel.refresh_from)


game = client.games.get_top(100)
json_data_list = (game)
#read data from json data list
for json_data in json_data_list:  
    game_data = json_data["game"]

    print("{:<40} {:<12} {:<10} {:<10} {:<10}".format(game_data["name"],game_data["popularity"],game_data["id"],json_data["viewers"],json_data["channels"]))

#os.remove('games.csv')
    
with open('games.csv', 'a') as writeFile:
    
    fieldnames = ['name','popularity','viewers','channels','datetime']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames, delimiter = '\t')

    # write fieldnames 
    writer.writeheader()

    # initialize for loop to iterate over json-Data-List
    for json_data in json_data_list:
        game_data = json_data["game"]
        writer.writerow(dict(zip(fieldnames,[game_data["name"],game_data["popularity"],json_data["viewers"],json_data["channels"]],)))
    
writeFile.close()
import time, sys

def writeText(string, t):
    i = 0
    while i < len(string):
        sys.stdout.write(string[i])
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()
writeText("Starting Again", 1.60)


from twitch import TwitchClient
import csv
import os
import datetime

client = TwitchClient(client_id='20aue0ca5p6vezl8f3tqkxk7stircs', oauth_token='oauth:cbnohhym7l3kk882hse5ts5nzqex4v')
channel = client.channels.get_by_id(226896585)
print(datetime.datetime.now())
print(channel.id)
print(channel.name)
print(channel.display_name)
print(channel.items)
print(channel.get)
print(channel.construct_from)
print(channel.refresh_from)


game = client.games.get_top(100)
json_data_list = (game)
#read data from json data list
for json_data in json_data_list:  
    game_data = json_data["game"]

    print("{:<40} {:<12} {:<10} {:<10} {:<10}".format(game_data["name"],game_data["popularity"],game_data["id"],json_data["viewers"],json_data["channels"]))

#os.remove('games.csv')
    
with open('games.csv', 'a') as writeFile:
    
    fieldnames = ['name','popularity','viewers','channels','datetime']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames, delimiter = '\t')

    # write fieldnames 
    writer.writeheader()

    # initialize for loop to iterate over json-Data-List
    for json_data in json_data_list:
        game_data = json_data["game"]
        writer.writerow(dict(zip(fieldnames,[game_data["name"],game_data["popularity"],json_data["viewers"],json_data["channels"]],)))
    
writeFile.close()
