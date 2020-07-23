#!/usr/bin/python
import os
import subprocess
import datetime




import json 
  
# Opening JSON file 
f = open('/home/pi/aws-iot-device-sdk-js-old/examples/commands.json','r') 
 
fw=open('aws.log','w');
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list

print (data['message'])

awsMsg=data['message'];
splitMsg=awsMsg.split(":")
command=splitMsg[1];
print(command);
result = subprocess.check_output(command,shell=True)
print("Command result is",result)
     

fw.write("Last Command Executed:",command);
fw.write("Command Output:",result);
#Execute the Command
# Closing file 
f.close() 
