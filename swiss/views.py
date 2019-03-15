from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.utils.html import escape
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import paramiko
import subprocess
import re
# Create your views here.

@csrf_exempt 
def index(request):
    data=json.load(request)
    print(data["ip"])
    k=online(request,data["ip"])
    pc=ssh("192.168.43.46","aryan","a12345")
    pc.connect()
    j=pc.free(request)
    print(j)
    return HttpResponse(k)
@csrf_exempt 
def ram(request):
    data=json.load(request)
    print(data["ip"])
    pc=ssh(data["ip"],"aryan","a12345")
    pc.connect()
    j=pc.free(request)
    return HttpResponse(j)
def sendmessage(request):
    data=json.load(request)
    print(data["ip"])
    pc=ssh(data["ip"],"aryan","a12345")
    pc.sendmessage(request["text"])
    j=pc.free(request)
    return HttpResponse(j)
class ssh:
    def __init__(self,hostname1,username1,password1):
	    self.ssh_output=None
	    self.ssh_error=None
	    self.client=None
	    self.host=hostname1
	    self.username=username1
	    self.password=password1
	  #  self.timeout=
	    self.pkey="/home/wolfflow/.ssh/id_rsa"
	    self.port=22
    

    def connect(self):
        "Login to the remote server"
        try:
            print("Establishing ssh connection")
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password,timeout=100.0, allow_agent=False,look_for_keys=False)    
            print("Connected to the server",self.host)
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
            result_flag = False
        else:
            result_flag = True
 
        return result_flag
    def ls(self,request):
        "ls request for linux"
        stdin,stdout,stderr=self.client.exec_command('ls',timeout=10)
        l=str(stdout.read())[2:].split("\\n")
        return JsonResponse({"files":l})
    def ps(self,request):
        "ps request for linux"
        stdin,stdout,stderr=self.client.exec_command('ps aux',timeout=10)
        print(stdout.read())
        out=str(stdout.read()).replace("\n"," \n ")
        return HttpResponse("hello")
    def free(self,request):
        stdin,stdout,stderr=self.client.exec_command('free -h',timeout=10)
        print(str(stdout))
        out=re.findall(r'\d.\dG',str(stdout.read()))
        print(out)
        return JsonResponse({"ram":out})
    def shutdown(self,request):
        
        return "hello"
    def sendmessage(self,text):
        stdin,stdout,stderr=self.client.exec_command('zenity --warning --text "'+text+'"',timeout=10)
        print(str(stdout))

def online(request,ip):
    
    try:
        stdout=subprocess.check_output("ping -c 1 "+ip,shell=True)
    except:
        return JsonResponse({'status':'0'})
    #print(stdout)
    out=re.findall(r'\d',str(stdout))
    return JsonResponse({'status':out[0]})

    
    

        
