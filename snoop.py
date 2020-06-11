#! /usr/bin/env python3
# Copyright (c) 2020 Snoop Project <snoopproject@protonmail.com> 

import base64
import certifi
import csv
import json
import locale
import networktest
import os
import platform
import random
import re
import requests
import subprocess
import sys
import time
import webbrowser

from argparse import ArgumentTypeError
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from collections import Counter
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor
from playsound import playsound
from requests_futures.sessions import FuturesSession
try:
    from rich.progress import (BarColumn, Progress,TimeRemainingColumn)
except ModuleNotFoundError:
    print(f"Install Module 'rich', в GNU team:\n" + \
    Style.BRIGHT + Fore.RED + "cd ~/snoop && python3 -m pip install -r requirements.txt" + \
    Style.RESET_ALL)
    sys.exit(0)

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, '')
init(autoreset=True)

print ("""\033[36m
  ___|                          
\___ \  __ \   _ \   _ \  __ \  
      | |   | (   | (   | |   | 
_____/ _|  _|\___/ \___/  .__/  
                         _|    \033[0m \033[37mv1.2.1\033[34;1m_rus_\033[31;1mSource Demo\033[0m
""")

if sys.platform == 'win32':
	print (Fore.CYAN + "#Example:" + Style.RESET_ALL)
	print (Fore.CYAN + " cd с:\snoop" + Style.RESET_ALL)	
	print (Fore.CYAN + " python snoop.py --help" + Style.RESET_ALL, "#Reference")
	print (Fore.CYAN + " python snoop.py username" + Style.RESET_ALL, "#Search user-a")
	print (Fore.CYAN + "============================================\n" + Style.RESET_ALL)
else:
	print (Fore.CYAN + "#Example:" + Style.RESET_ALL)
	print (Fore.CYAN + " cd ~/snoop" + Style.RESET_ALL)
	print (Fore.CYAN + " python3 snoop.py --help" + Style.RESET_ALL, "#Reference")
	print (Fore.CYAN + " python3 snoop.py username" + Style.RESET_ALL, "#Search user user-a")
	print (Fore.CYAN + "=============================================\n" + Style.RESET_ALL)

module_name = (Fore.CYAN + "Snoop: Search on all fronts!" + Style.RESET_ALL)
version = "1.2.1_rus Snoop (source demo)"

dirresults = os.getcwd()
timestart = time.time()
time_data = time.localtime()
censor = 0

def fff():
    try:
        with open('BDdemo', "r", encoding="utf8") as z:
            dd = z.read() 
            b1 = dd.encode("UTF-8") 
            d1 = base64.b64decode(b1) 
            rt1 = d1[::-1] 
            d2 = base64.b64decode(rt1)
            s12 = d2.decode("UTF-8") 
            bbb1 = json.loads(s12) 
            return bbb1
    except:
        print(Style.BRIGHT + Fore.RED + "Oops, something went wrong..." + Style.RESET_ALL)
        sys.exit(0)

def kkk():
    try:
        with open('BDflag', "r", encoding="utf8") as z1:
            d11 = z1.read()
            b11 = d11.encode("UTF-8") 
            t11 = base64.b64decode(b11) 
            rt11 = t11[::-1] 
            d22 = base64.b64decode(rt11)
            s112 = d22.decode("UTF-8") 
            ccc1 = json.loads(s112) 
            return ccc1
    except:
        print(Style.BRIGHT + Fore.RED + "Oops, something went wrong...." + Style.RESET_ALL)
        sys.exit(0)

# Flag BS
def baza():
    BS = fff()
    flagBS = len(BS)
    return BS
flagBS = len(baza())

# Creating Results Directories.
try:
    os.makedirs(str(dirresults + "/results"))
except:
    pass
try:
    os.mkdir(str(dirresults + "/results/html"))
except:
    pass
try: 
    os.mkdir(str(dirresults + "/results/txt"))
except:
    pass
try:
    os.mkdir(str(dirresults + "/results/csv"))
except:
    pass
try:
    os.makedirs(str(dirresults + "/results/save reports"))
except:
    pass

################################################################################
class ElapsedFuturesSession(FuturesSession):
    """test_metrica"""
    def request(self, method, url, *args, **kwargs):
        """test"""
        return super(ElapsedFuturesSession, self).request(method, url, *args, **kwargs)

def print_info(title, info, color=True):
    if color:
        print(Fore.GREEN + "[" +
            Fore.YELLOW + "*" +
            Fore.GREEN + f"] {title}" +
            Fore.RED + "\033[5m <\033[0m" +
            Fore.WHITE + f" {info}" +
            Fore.RED + "\033[5m >\033[0m")
    else:
        print(f"\n[*] {title} {info}:")


def print_error(err, errstr, var, verbose=False, color=True):
    if color:
        print(Fore.CYAN + "[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.CYAN + "]" +
            Style.BRIGHT + Fore.RED + f" {errstr}" +
            Style.BRIGHT + Fore.YELLOW + f" {err if verbose else var}")
        try:
            playsound('err.wav')
        except:
            pass
    else:
        print(f"[-] {errstr} {err if verbose else var}")


# Printing on different platforms.
if sys.platform == 'win32':
    def print_found_country(social_network, url, countryB, response_time=False, verbose=False, color=True):
        if color:
            print(Style.BRIGHT + Fore.CYAN + f" {countryB}" + 
                Fore.GREEN + f" {social_network}:", url)
        else:
            print(f"[+] {social_network}: {url}")
else:            
    def print_found_country(social_network, url, countryA, response_time=False, verbose=False, color=True):
        if color:
            print(countryA, (Style.BRIGHT +
                Fore.GREEN + f" {social_network}:"), url)
        else:
            print(f"[+] {social_network}: {url}")


def print_not_found(social_network, response_time, verbose=False, color=True):
    if color:
        print((Fore.CYAN + "[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.CYAN + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.BRIGHT + Fore.YELLOW + " Увы!"))
    else:
        print(f"[-] {social_network}: Увы!")


def print_invalid(mes, social_network, message, color=True):
    """Error Output Result"""
    if color:
        print((Fore.RED + "............[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.RED + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.RESET_ALL + Fore.YELLOW + f" {message}"))
    else:
        print(f"[-] {social_network} {message}")

def print_invalid2(mes, social_network, message, color=True):
    """Verbose result output error"""
    if color:
        print((Fore.RED + ".............[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.RED + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.RESET_ALL + Fore.YELLOW + f" {message}"))
    else:
        print(f"[-] {social_network} {message}")

def get_response(request_future, error_type, social_network, verbose=False, retry_no=None, color=True):
    try:
        rsp = request_future.result()
        if rsp.status_code:
            return rsp, error_type, rsp.elapsed
    except requests.exceptions.HTTPError as errh:
        print_error(errh, "HTTP Error:", social_network, verbose, color)

    except requests.exceptions.ConnectionError as errc:
        def gebb():
            global censor
            censor +=1
            print_error(errc, "Connection Error:", social_network, verbose, color)
        gebb()            
    except requests.exceptions.Timeout as errt:
        print_error(errt, "Timeout Error:", social_network, verbose, color)
    except requests.exceptions.RequestException as err:
        print_error(err, "Keyboard layout error / * characters", social_network, verbose, color)
    return None, "", -1

def snoop(username, site_data, verbose=False, reports=False, user=False, country=False, print_found_only=False, timeout=None, color=True):
    username = re.sub(" ", "%20", username)

# Prevention of 'DDoS' due to invalid logins; phone numbers, search errors due to special characters.
    ermail=[]
    with open('domainlist.txt', 'r', encoding="utf-8") as err:
        for line in err.readlines():
            errdata=line[:-1]
            ermail.append(errdata)
    if any(ermail in username for ermail in ermail):
        print(Style.BRIGHT + Fore.RED + "\nE-mail the address will be truncated to a valid state")
        username = username.rsplit(sep='@', maxsplit=1)[0]

    with open('specialcharacters', 'r', encoding="utf-8") as errspec:
        s1 = errspec.read()
        my_list = list(s1)
        if any(my_list in username for my_list in my_list):
            print(Style.BRIGHT + Fore.RED + f"Invalid characters in username: {username}")
            sys.exit(0)

    ernumber=['79', '89', "38", "37"]
    if any(ernumber in username[0:2] for ernumber in ernumber):
        if len(username) >= 10 and len(username) <= 13:
            if username.isdigit() == True:
                print(Style.BRIGHT + Fore.RED + "\nSnoop tracks user accounts but not phone numbers...")
                sys.exit(0)
    elif username[0] == "+" or username[0] == ".":
        print (Style.BRIGHT + Fore.RED + "\nA public login starting with such a character is almost always invalid...")
        sys.exit(0)
    elif username[0] == "9" and len(username) == 10 and username.isdigit() == True:
        print (Style.BRIGHT + Fore.RED + "\nSnoop tracks user accounts but not phone numbers...")
        sys.exit(0)

# Print the first info line.
    if '%20' in username:
        usernameA = re.sub("%20", " ", username)
        print_info("Looking For:", usernameA, color)
    else:
        print_info("Looking For:", username, color)

# Create Session Based on Request Methodology.
    underlying_session = requests.session()
    underlying_request = requests.Request()

# Work Limit 20+
    try:
        if len(site_data) >= 50:
            max_workers=18
        else:
            max_workers=len(site_data)
    except:
        sys.exit(0)
# Create a multi-threaded session for all requests
    session = ElapsedFuturesSession(max_workers=max_workers, session=underlying_session)

# Результаты анализа всех сайтов.
    results_total = {}

# Create futures for all queries. This will allow you to send requests.
    for social_network, net_info in site_data.items():
#        print([iz for iz in site_data]) #Key output test (site names)
#        print(social_network) #(site names, strings)
# Site-specific analysis results.
        results_site = {}

# Record the URL of the main site and the country flag (mapping с data.json).
        results_site['flagcountry'] = net_info.get("country")
        results_site['flagcountryklas'] = net_info.get("country_klas")
        results_site['url_main'] = net_info.get("urlMain")

# Browser user-agent, some sites depend on this directly. 302 
# So as not to think that requests come from bots.

        RandHead = (["{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.109'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}"
        ])
        RH = random.choice(RandHead)
        headers = json.loads(RH.replace("'",'"'))

        if "headers" in net_info:
# Override / add any additional headers needed for this site.
            headers.update(net_info["headers"])

# Do not make a request if the username is not suitable for the site.
        exclusionYES = net_info.get("exclusion")
        if exclusionYES and re.search(exclusionYES, username):
# No need to do a check on the site: if this username is not allowed.
            if not print_found_only:
                print_invalid("", social_network, f"Invalid name format for this site", color)

            results_site["exists"] = "dash"
            results_site["url_user"] = ""
            results_site['countryCSV'] = ""
            results_site['http_status'] = ""
            results_site['response_text'] = ""
            results_site['check_time_ms'] = ""
            results_site['response_time_ms'] = ""
            results_site['response_time_site_ms'] = ""

        else:
# URL of the user on the site (if one exists).
            url = net_info["url"].format(username)
            results_site["url_user"] = url
            url_probe = net_info.get("urlProbe")
            if url_probe is None:
# URL - is the usual one that people see on the Internet.
                url_probe = url
            else:
# There is a special URL (usually we do not know about it / api) to check for the existence of a separate user.
                url_probe = url_probe.format(username)

# If you only need the status of the code, do not download the page code.
            if reports:
                request_method = session.get
            else:
                try:
                    if net_info["errorTypе"] == 'status_code' or net_info["errorTypе"] == "redirection":
                        request_method = session.head
                    else:
                        request_method = session.get
                except:
                    sys.exit(0)
            if net_info["errorTypе"] == "response_url":
# The site redirects the request to a different URL if the username does not exist.
# Name found. Disable redirection to capture code status from the original url.
                allow_redirects = False
            else:
# Allow any redirect that the site wants to make.
# The final result of the request will be what is available.
                allow_redirects = True

            future = request_method(url=url_probe, headers=headers, allow_redirects=allow_redirects, timeout=timeout)

# Save future in data for later access.
            net_info["request_future"] = future

# Add the results of this site to the final dictionary with all other results.
        results_total[social_network] = results_site

# Open a file containing links to your account.
# Basic logic: if current requests, make them. If multithreaded requests, wait for answers.

# print (results_site) # Check the record for success.
    li_time = []
    if color == True and verbose == False:
        progress1 = Progress(BarColumn(bar_width=6),
        "[progress.percentage]{task.percentage:>3.0f}%", auto_refresh=False)
    else:
        progress1 = Progress(auto_refresh=False)
    if verbose == True:
        if color:
            progress1 = Progress(TimeRemainingColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%", auto_refresh=False)
        else:
            progress1 = Progress(auto_refresh=False)

    for social_network, net_info in progress1.track(site_data.items(),description=""):
        if color:
            progress1.refresh()
#Get results again.
        results_site = results_total.get(social_network)

# Get other site information again.
        url = results_site.get("url_user")
        countryA = results_site.get("flagcountry")
        countryB = results_site.get("flagcountryklas")
        exists = results_site.get("exists")
        if exists is not None:
            continue

#Get the expected data type of 4 methods.
        error_type = net_info["errorTypе"]

# Default data in the event of any failure to complete the request.
        http_status = "*???"
        response_text = ""

# Get the future and make sure it is finished.
        future = net_info["request_future"]
        r, error_type, response_time = get_response(request_future=future,
                                                    error_type=error_type,
                                                    social_network=social_network,
                                                    verbose=verbose,
                                                    retry_no=3, 
                                                    color=color)

# Attempt to get request information.
        try:
            http_status =  r.status_code
        except:
            pass
        try:
            response_text = r.text.encode(r.encoding)
        except:
            pass

#Saving reports option(-S)
        def sreports():
            codingWin = "charset=windows"
            codingWin2 = "charset=\"windows"
            try:
                os.makedirs(str(dirresults + f"/results/save reports/{username}"))
            except:
                pass
            if codingWin in r.text or codingWin2 in r.text:
                try:
                    with open(f"results/save reports/{username}/{social_network}.html", 'w',
                    encoding="cp1251") as rep:
                        rep.write(r.text)
                except:
                    with open(f"results/save reports/{username}/{social_network}.html", 'w',
                    encoding="utf-8") as rep:
                        rep.write(r.text)
            else:
                with open(f"results/save reports/{username}/{social_network}.html", 'w',
                encoding="utf-8") as rep:
                    rep.write(r.text)

# Verification, 4 methods; #1.
# Answers message (different locations).
        if error_type == "message":
            error = net_info.get("errorMsg") 
            error2 = net_info.get("errorMsg2")
            if error2 in r.text:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "Not Found"
            elif error in r.text:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "Not Found"
            else:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                exists = "Found!"
                if reports:
                    sreports()
# print (r.text) # Check response
# Verification, 4 methods; # 2
# Check username with status 301 and 303 (redirection and salt).
        elif error_type == "redirection":
            rr = requests.get(url, allow_redirects=False)
            if rr.status_code == 301 or rr.status_code == 303:
#                print (r.text) # check response (+ - '-S')
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "Found!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "Not Found!"

# Verification, 4 methods; # 3
# Checks if response status code is 2 ..
        elif error_type == "status_code":
            if not r.status_code >= 300 or r.status_code < 200:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "Found!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "Not Found!"

# Verification, 4 methods; #4
# Redirection.
elif error_type == "response_url":

            if 200 <= r.status_code < 300:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "Found!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "Not Found!"
# print (r.text) # Check response

# If all 4 methods did not work, for example, due to an access error (red) or due to captcha (yellow)
	else:
            if not print_found_only and verbose == False:
                print_invalid("", social_network, "*PASS", color)
            elif not print_found_only and verbose == True:
                print_invalid2("", social_network, "*PASS", color)    
            exists = "Blocked"

# Count Approx. timings.
        ello = float(time.time() - timestart)
        li_time.append(ello)
        dif_time = []

# Count timings with high accuracy.
        try:
            time_site = str(response_time).rsplit(sep=':', maxsplit=1)[1]
            time_site=round(float(time_site)*1000)
        except:
            time_site = str("-")

        for i in (li_time[-2:-1]):
            i
            for i1 in (li_time[-1:]):
                i1
            dif = (i1-i)
            dif_time.append(dif)

# '-v' option.
            if verbose == True:
                if color == False:
                    if print_found_only == True:
                        if exists == "found!" or exists == "block":
                            print (f "[* {time_site} ms response]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                    else:
                        print(f"[*{time_site} ms response]" + \
                        f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                if color == True:
                    if print_found_only == True:
                        if exists == "found!" or exists == "block":
                            if dif > 5:
                                print(Style.BRIGHT + Fore.RED + f"[**{time_site} ms response]"
                                f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                            else:
                                print(Style.BRIGHT + Fore.CYAN + f"[**{time_site} ms response]" + \
                                f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                    else:
                        if dif > 5:
                            print(Style.BRIGHT + Fore.RED + f"[**{time_site} ms response]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                        else:
                            print(Style.BRIGHT + Fore.CYAN + f"[**{time_site} ms response]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")

# Service Information for CSV.
        response_time_site_ms = 0
        for response_time_site_ms in dif_time:
            response_time_site_ms

# Save Existing Flag
        results_site['exists'] = exists

# Save the results from the query.
        results_site['countryCSV'] = countryB
        results_site['http_status'] = http_status
        results_site['response_text'] = response_text
        results_site['check_time_ms'] = time_site
        results_site['response_time_ms'] = round(float(ello*1000))
        if response_time_site_ms*1000 < 250:
            results_site['response_time_site_ms'] = "нет"
        else:
            results_site['response_time_site_ms'] = round(float(response_time_site_ms*1000))
# Adding the results of this site to the final dictionary with all other results.
        results_total[social_network] = results_site
    return results_total


# Опция '-t'.
def timeout_check(value):
    try:
        global timeout
        timeout = int(value)
    except:
        raise ArgumentTypeError (f "\ n \ 033 [31; 1mTimeout '{value}' Err, \ 033 [0m \ 033 [36m indicate the time in 'seconds'. \ 033 [0m")
     if timeout <= 0:
         raise ArgumentTypeError (f "\ 033 [31; 1mTimeout '{value}' Err, \ 033 [0m \ 033 [36m indicate time> 0sec. \ 033 [0m")
     return timeout


# Update Snoop.
def update_snoop ():
     if sys.platform == 'win32':
         upd = str (input ("" "Do you really want:
                    __             _  
   ._  _| _._|_ _  (_ ._  _  _ ._   ) 
|_||_)(_|(_| |_(/_ __)| |(_)(_)|_) o  
   |                           |    
press 'y' "" ")))
     else:
         upd = str (input ("" "\ 033 [36mYou really want:
                    __             _  
   ._  _| _._|_ _  (_ ._  _  _ ._   ) 
|_||_)(_|(_| |_(/_ __)| |(_)(_)|_) o  
   |                           |    
press \ 033 [0m 'y' "" "))

     if upd == "y":
         if sys.platform == 'win32':
             print (Fore.RED + "Snoop update function requires <Git> on Windows OS")
             os.startfile ("update.bat")
         else:
             print (Fore.RED + "Snoop update function requires installing <Git> on GNU / Linux OS")
             os.system ("./ update.sh")


# THE BASIS.
def main ():

# Request a license.
    with open('COPYRIGHT', 'r', encoding="utf8") as copyright:
        cop = copyright.read()

    version_snoop = f"\033[37m{cop}\033[0m\n" + \
                     f"\033[36m%(prog)s: {version}\033[36m\n" +  \
                     f"\033[36mOS: {platform.platform(aliased=True, terse=0)}\033[36m\n" + \
                     f"\033[36mPython: {platform.python_version()}\033[36m\n\n"
                     


# Donation.

                
# Assigning Snoop options.
    parser = ArgumentParser (formatter_class = RawDescriptionHelpFormatter,
                             description = f "{module_name} (Version {version})",
                             epilog = (Fore.CYAN + f "Snoop" + Style.BRIGHT + Fore.RED + f "Demo Version" + Style.RESET_ALL + \
                             Fore.CYAN + f "support: \ 033 [31; 1m {flagBS} \ 033 [0m \ 033 [36mWebsites! \ N" + Fore.CYAN +
                             f "Snoop \ 033 [36; 1mFull Version \ 033 [0m \ 033 [36mSupport: \ 033 [36; 1m1100 + \ 033 [0m \ 033 [36mWebsites !!! \ 033 [0m \ n English version, see release \ n \ n ")
                             )
    parser.add_argument ("- version", "--about", "-V",
                         action = "version", version = (version_snoop),
                         help = "\ 033 [31; 1m START! Printing versions: OS; Snoop; Python and Licenses \ 033 [0m"
                         )
     parser.add_argument ("- verbose", "-v",
                         action = "store_true", dest = "verbose", default = False,
                         help = "Print verbalization while printing 'username'"
                         )
     parser.add_argument ("- base", "-b",
                         dest = "json_file", default = "BDdemo", metavar = '',
                         help = "To specify another database for the search 'username' (Local) / The function is disabled in the demo version"
                         )
    parser.add_argument ("- web-base", "-w",
                        action = "store_true", dest = "web",
                        help = "Connect to search for 'username' to the updated web_BD (Online)"
                        )
    parser.add_argument ("- site", "-s",
                        action = "append", metavar = '',
                        dest = "site_list", default = None,
                        help = "Specify a site name from the database '--list all'. Search 'username' on one specified resource"
                        )
    parser.add_argument ("- time-out", "-t 9",
                        action = "store", metavar = '',
                        dest = "timeout", type = timeout_check, default = 5,
                        help = "Set the allocation of max time to wait for a response from the server (seconds). \ n"
                             "Affects search duration. Affects 'error timeout:'"
                             "\ 033 [31; 1mOn. This option is almost always necessary when slow \
                             Internet connection \ 033 [0m to avoid prolonged freezes \
                             in case of network problems (the default value is set to 5s) "
                        )
    parser.add_argument ("- found-print", "-f",
                        action = "store_true", dest = "print_found_only", default = False,
                        help = "Print only found accounts"
                        )
    parser.add_argument ("- no-func", "-n",
                        action = "store_true", dest = "no_func", default = False,
                        help = "" "✓ Monochrome terminal, do not use colors in url \ n
                                ✓Turn off the sound \ n
                                ✓Disable opening the web browser \ n
                                ✓ Disable printing of country flags
                                ✓ Turn off the indication and progress status "" "
                        )
    parser.add_argument ("username",
                        nargs = '+', metavar = 'USERNAMES',
                        action = "store",
                        help = "Wanted user nickname, multiple names supported"
                        )
    parser.add_argument ("- userload", "-u", metavar = '',
                        action = "store", dest = "user", default = False,
                        help = "Specify a file with a list of users. Linux example: 'python3 snoop.py -u ~ / listusers.txt start' \ n"
                             "Windows example: 'python snoop.py -u c: \ snoop \ listusers.txt start'"
                        )
    parser.add_argument ("- list all",
                        action = "store_true", dest = "listing",
                        help = "Print out information about the local Snoop database"
                        )
    parser.add_argument ("- country", "-c",
                        action = "store_true", dest = "country", default = False,
                        help = "Sorting 'print / record_results' by country, not alphabetically"
                        )
    parser.add_argument ("- save-report", "-S",
                        action = "store_true", dest = "reports", default = False,
                        help = "Save found user pages to local files"
                        )
    parser.add_argument ("- update y",
                         action = "store_true", dest = "update",
                         help = "Update Snoop"
                         )

     args = parser.parse_args ()

   
# Informative output:
# Option '-w'.
     if args.web:
         print (Fore.CYAN + "[+] the '-w' option is activated:" connection to external web_database "")
# Option '-S'.
     if args.reports:
         print (Fore.CYAN + "[+] the '-S' option is activated:" save pages of found accounts "")

# Option '-n'.
    if args.no_func:
        print (Fore.CYAN + "[+] the '-n' option is activated:" disabled :: colors; sound; flags; browser; progress "")

# Option '-t'.
    try:
        if args.timeout:
            print (Fore.CYAN + f "[+] the '-t' option is activated:" snoop will wait for a response from the site \ 033 [36; 1m <= {timeout} _sec \ 033 [0m \ 033 [36m. ”\ 033 [ 0m ")
    except:
        pass

# Sort by country '-s'.
    if args.country:
        patchjson = ("{}". format (args.json_file))
        jsonjson = fff ()
        print (Fore.CYAN + "[+] '-c' option activated:" sort / write HTML results by country "")
        site_country = dict (jsonjson)
        country_sites = sorted (jsonjson, key = lambda k: ("country" not in k, jsonjson [k] .get ("country", sys.maxsize)))
        sortC = {}
        for site in country_sites:
            sortC [site] = site_country.get (site)

# Option '-f'.
    if args.print_found_only:
        print (Fore.CYAN + "[+] the '-f' option is activated:" print only found accounts "")

# Option '-s'.
    if args.site_list:
        print (Fore.CYAN + "[+] the '-s' option is activated:" user-a will be searched on the 1st selected website "\ n"
        "it is permissible to use the -s option several times \ n"
        "option '-s' is not compatible with option '-c'")

# Option '-v'
    if args.verbose:
        print (Fore.CYAN + "[+] the '-v' option is activated:" verbalization in CLI verbose "")
        networktest.nettest ()

# Option '--list all'.
    if args.listing:
        from rich.console import Console
        from rich.table import Table

        if sys.platform == 'win32':
            sortY = str (input ("Sort the Snoop database by country, by site name or by summary? \ nby country - 1 by name - 2 all - 3 \ n"))
        else:
            sortY = str (input ("\ 033 [36mSort the Snoop database by country, by site name or generically? \ n" + \
            "by country - \ 033 [0m 1 \ 033 [36m by name - \ 033 [0m 2 \ 033 [36mall - \ 033 [0m 3 \ n" + \
            "\ 033 [36mSelect the action ... \ 033 [0m \ n"))
# General conclusion of countries (3!).
        if sortY == "3":
            print (Fore.CYAN + "======================== \ nOk, print All Country: \ n")
            datajson0 = fff ()
            cnt0 = Counter ()
            li0 = []
            for con0 in datajson0:
                if sys.platform == 'win32':
                    aaa0 = datajson0.get (con0) .get ("country_klas")
                else:
                    aaa0 = datajson0.get (con0) .get ("country")
                li0.append (aaa0)
            for word0 in li0:
                cnt0 [word0] + = 1
            flag_str0 = str (cnt0)
            try:
                flag_str_sum0 = (flag_str0.split ('{') [1]). replace ("'", "") .replace ("}", "") .replace (")", "")
            except:
                pass
            table = Table (title = Style.BRIGHT + Fore.RED + "Snoop Demo Version" + Style.RESET_ALL, style = "green")
            table.add_column ("Country: No. of websites", style = "magenta")
            table.add_column ("All", style = "cyan", justify = 'full')
            table.add_row (flag_str_sum0, str (len (datajson0)))
            console = Console ()
            console.print (table)
# Output for full Version
            datajson00 = kkk ()
            cnt00 = Counter ()
            li00 = []
            for con00 in datajson00:
                if sys.platform == 'win32':
                    aaa00 = datajson00.get (con00) .get ("country_klas")
                else:
                    aaa00 = datajson00.get (con00) .get ("country")
                li00.append (aaa00)
            for word00 in li00:
                cnt00 [word00] + = 1
            flag_str00 = str (cnt00)
            try:
                flag_str_sum00 = (flag_str00.split ('{') [1]). replace ("'", "") .replace ("}", "") .replace (")", "")
            except:
                pass
            table = Table (title = Style.BRIGHT + Fore.GREEN + "Snoop Full Version" + Style.RESET_ALL, style = "green")
            table.add_column ("Country: No. of websites", style = "magenta")
            table.add_column ("All", style = "cyan", justify = 'full')
            table.add_row (flag_str_sum00, str (len (datajson00)))
            console = Console ()
            console.print (table)
            sys.exit (0)

# Sort alphabetically (2!).
# Sort for Win Full Version OS.
        elif sortY == "2":
            print (Fore.CYAN + "======================== \ nOk, sort alphabetically: \ n")
            print (Fore.GREEN + "++ Whitelist Full Version ++")
            datajson = kkk ()
            i = 0
            if sys.platform == 'win32':
                for con in datajson:
                    aaa = datajson.get (con) .get ("country_klas")
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{aaa} {con}")
                    print (Fore.CYAN + "=================")
# Sort for GNU OS Full Version ..
            else:
                for con in datajson:
                    aaa = datajson.get (con) .get ("country")
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{aaa} {con}")
                    print (Fore.CYAN + "=================")
# Sort for OS Win Demo Version.
            print (Fore.GREEN + "\ n ++ White List Demo Version ++")
            datajson = fff ()
            i = 0
            if sys.platform == 'win32':
                for con in datajson:
                    aaa = datajson.get (con) .get ("country_klas")
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{aaa} {con}")
                    print (Fore.CYAN + "=================")
# Sort for the GNU Demo Version OS.
            else:
                for con in datajson:
                    aaa = datajson.get(con).get("country")
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{aaa}  {con}")
                    print(Fore.CYAN + "================")        
            sys.exit(0)

# Sort by country (1!).
# Sort for Win Full Version OS.
        elif sortY == "1":
            if sys.platform == 'win32':
                listwindows = []
                datajson = kkk ()
                for con in datajson:
                    aaa = (datajson.get (con) .get ("country_klas"))
                    listwindows.append (f "{aaa} {con} \ n")
                sort_spisok = sorted (listwindows)
                print (Fore.CYAN + "======================== \ nOk, sorted by country: \ n")
                print (Fore.GREEN + "++ Whitelist Full Version ++")
                for i, numerlist in enumerate (sort_spisok):
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{numerlist}", end = '')
                    print (Fore.CYAN + "=================")
# Sort for GNU OS Full Version.
            else:
                listlinux = []
                datajson = kkk ()
                for con in datajson:
                    aaa = (datajson.get (con) .get ("country"))
                    listlinux.append (f "{aaa} {con} \ n")
                sort_spisok = sorted (listlinux)
                print (Fore.CYAN + "======================== \ nOk, sorted by country: \ n")
                print (Fore.GREEN + "++ Whitelist Full Version ++")
                for i, numerlist in enumerate (sort_spisok):
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{numerlist}", end = '')
                    print (Fore.CYAN + "=================")
# Sort for OS Win Demo Version.
            if sys.platform == 'win32':
                listwindows = []
                datajson = fff ()
                for con in datajson:
                    aaa = (datajson.get (con) .get ("country_klas"))
                    listwindows.append (f "{aaa} {con} \ n")
                sort_spisok = sorted (listwindows)
                print (Fore.GREEN + "\ n ++ White List Demo Version ++")
                for i, numerlist in enumerate (sort_spisok):
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{numerlist}", end = '')
                    print (Fore.CYAN + "=================")
# Sort for GNU Demo Version ..
            else:
                listlinux = []
                datajson = fff ()
                for con in datajson:
                    aaa = (datajson.get (con) .get ("country"))
                    listlinux.append (f "{aaa} {con} \ n")
                sort_spisok = sorted (listlinux)
                print (Fore.GREEN + "\ n ++ White List Demo Version ++")
                for i, numerlist in enumerate (sort_spisok):
                    i + = 1
                    print (Style.BRIGHT + Fore.GREEN + f "{i}.", Fore.CYAN + f "{numerlist}", end = '')
                    print (Fore.CYAN + "=================")
            sys.exit (0)
# No action selected.
        else:
            print (Style.BRIGHT + Fore.RED + "Sorry, but you did not select the action \ nout")
            sys.exit (0)

# Donut option '-d y'.
    if args.donation:
        print (donate)
        print ("|| \ n",
              Fore.CYAN + f "Limitations of Demo Version: {flagBS} Websites (Database Snoop reduced by> 19 times); || \ n"
              f "some options are disabled; non-updated and unsupported Database_Snoop. || \ n"
              f "Snoop Full Version: 1100+ Websites; support and update Database Snoop. || \ n"
f "\ 033 [36; 1m Connection to Web_Database Snoop (online), which is expanding / updating. || \ 033 [0m \ n"
              f "================================================= ================================= \ n ")
        webbrowser.open ("https://yasobe.ru/na/snoop_project")
        print (Style.BRIGHT + Fore.RED + "Exit")
        sys.exit (0)

# Option to specify file list of wanted users '-u'.
    if args.user:
        userlist = []
        patchuserlist = ("{}". format (args.user))
        userfile = patchuserlist.split ('/') [- 1]
        with open (patchuserlist, "r", encoding = "utf8") as u1:
            try:
                for lineuserlist in u1.readlines ():
                    lineuserlist.strip ()
                    userlist.append (lineuserlist)
                userlist = [line.rstrip () for line in userlist]
            except:
                print ("\ 033 [31; 1mCan not find_read! \ 033 [0m \ 033 [36mPlease specify the text file in the encoding - \ 033 [0m \ 033 [36; 1mutf-8. \ 033 [0m \ n")
                print ("\ 033 [36m By default, notepad on OS Windows saves text encoded - ANSI \ 033 [0m")
                print ("\ 033 [36mOpen your list of users and change the encoding [file ---> save as ---> utf-8]")
                print ("\ 033 [36mOr delete unreadable characters from the dictionary.")
                sys.exit (0)
        print (Fore.CYAN + f "[+] the '-u' option is activated:“ search for users from a file: \ 033 [36; 1m {userfile} \ 033 [0m \ 033 [36m ”\ 033 [0m")
        print (Fore.CYAN + "We will search:" + f "{userlist [: 3]}" + "and others ..." + Style.RESET_ALL)

# Finish updating Snoop.
    if args.update:
        print ("\ 033 [36m ======================= \ 033 [0m")
        update_snoop ()
        print ("\ 033 [36m ======================= \ n", Style.BRIGHT + Fore.RED + "\ nExit")
        sys.exit (0)

# Check other options.
    response_json_online = None
    site_data_all = None

    baseput = ("{}". format (args.json_file))
# print (baseput) # checking the base path

# Work with the database.
    if site_data_all is None:
# Check if an alternative database exists, otherwise exit.
        if not os.path.exists (baseput):
            print ("\ 033 [31; 1mBase file does not exist. \ 033 [0m")
            sys.exit (0)
        else:
            try:
                a1 = fff ()
            except:
                print ("\ 033 [31; 1m Unsupported database format \ 033 [0m")
        try:
            if args.web == False:
                site_data_all = a1
                print (Fore.CYAN + f "\ nlocal database loaded:" +
                Style.BRIGHT + Fore.CYAN + f "{len (site_data_all)}" + "_Websites" + Style.RESET_ALL)
        except:
            print ("\ 033 [31; 1mInvalid loadable database. \ 033 [0m")

# Option '-w'
    if args.web:
        print ("\ n \ 033 [37m \ 033 [44m {}". format ("The function is valid only for users of Full version ..."))
        print (donate)
        print ("\ 033 [31mOutput \ 033 [0m")
        webbrowser.open ("https://yasobe.ru/na/snoop_project")
        sys.exit (0)

    if args.site_list is None:
# It is not advisable to look at a subset of sites.
        site_data = site_data_all
    else:

# Option '-s'.
# The user wants to selectively run queries on a subset of the list of sites.
# Make sure that sites are supported, create a shortened site database.
        site_data = {}
        site_missing = []
        for site in args.site_list:
            for existing_site in site_data_all:
                if site.lower () == existing_site.lower ():
                    site_data [existing_site] = site_data_all [existing_site]
            if not site_data:

# Create a list of sites that are not supported for a future error message.
                site_missing.append (f "'{site}'")

        if site_missing:
            print (
                f "\ 033 [31; 1mError: \ 033 [0m \ 033 [36mThe desired site was not found in the Snoop database :: {',' .join (site_missing)} \ 033 [0m")
            sys.exit (0)

# Run with the option '-u' (get 'username' from the file).
# We twist the list of users.
    if args.user:
        kef_user = 0
        for username in userlist:
            kef_user + = 1
            file = open ("results / txt /" + username + ".txt", "w", encoding = "utf-8")
            try:
                file = open ("results / txt /" + username + ".txt", "w", encoding = "utf-8")
            except (SyntaxError, ValueError):
                pass

            try:
                if args.country == True:
                    results = snoop (username,
                                   sortC,
                                   country = args.country,
                                   user = args.user,
                                   verbose = args.verbose,
                                   reports = args.reports,
                                   print_found_only = args.print_found_only,
                                   timeout = args.timeout,
                                   color = not args.no_func)
                else:
                    results = snoop (username,
                                   site_data
                                   country = args.country,
                                   user = args.user,
                                   verbose = args.verbose,
                                   reports = args.reports,
                                   print_found_only = args.print_found_only,
                                   timeout = args.timeout,
                                   color = not args.no_func)
            except:
                results = snoop (username,
                               site_data
                               country = args.country,
                               user = args.user,
                               verbose = args.verbose,
                               reports = args.reports,
                               print_found_only = args.print_found_only,
                               timeout = args.timeout,
                               color = not args.no_func)

            exists_counter = 0
            file.write ("Address | resource" + "\ n \ n")
            for website_name in results:
                timefinish = time.time () - timestart
                dictionary = results [website_name]
                if dictionary.get ("exists") == "found!":
                    exists_counter + = 1
                    file.write (dictionary ["url_user"] + "|" + (website_name) + "\ n")
            file.write ("\ n" f "Requested object: <{username}> found: {exists_counter} times.")
            file.write ("\ n" f "Base Snoop (DemoVersion):" + str (flagBS) + "Websites.")
            file.write ("\ n" f "Updated:" + time.strftime ("% d /% m /% Y_% H:% M:% S", time_data) + ".")
            print (Fore.CYAN + "├─Search results:", "found ->", exists_counter, "url (% .0f"% float (timefinish) + "sec)")
            print (Fore.CYAN + "├──The results are saved in:" + Style.RESET_ALL + "results / * /" + str (username) + ". *")

    # Record in html.
            file = open ("results / html /" + username + ".html", "w", encoding = "utf-8")
            try:
                file = open ("results / html /" + username + ".html", "w", encoding = "utf-8")
            except (SyntaxError, ValueError):
                pass
            file.write ("<! DOCTYPE html> \ n <head> \ n <meta charset = 'utf-8'> \ n <style> \ nbody {background: url (../../ web / public.png ) \
            no-repeat 20% 0%; } \ n </style> \ n <link rel = 'stylesheet' href = '.. / .. / web / style.css'> \ n </head> \ n <body> \ n \ n \
            <div id = 'particles-js'> </div> \ n \
            <div id = 'report'> \ n \ n \
            <h1> <a class='GL'href='file://" + str(dirresults) + "/results/html/'> Home </a> "+" </h1> \ n ")
            file.write ("" "\ t \ t \ t <h3> Snoop Project (Demo Version) </h3>
            <p> Press: 'sort by country', return: 'F5': </p>
            <button onclick = "sortList ()"> Sort by country </button> <br> <br> \ n \ n "" ")
            file.write ("Object" + "<b>" + (username) + "</b>" + "was found on the following" + "<b>" + str (exists_counter) +
            "</b> resources: \ n" + "<br> <ol" + "id = 'id777'> \ n")
            
            cnt = Counter ()
            for website_name in results:
                dictionary = results [website_name]
                flag_sum = dictionary ["flagcountry"]
                if dictionary.get ("exists") == "found!":
                    li = []
                    li.append (flag_sum)
                    exists_counter + = 0
                    for word in li:
                        cnt [word] + = 1
                    file.write ("<li>" + dictionary ["flagcountry"] + "<a target='_blank' href='" + dictionary ["url_user"† + "'>" +
                    (website_name) + "</a>" + "</li> \ n")
            flag_str = str (cnt)
            try:
                flag_str_sum = (flag_str.split ('{') [1]). replace ("'", "") .replace ("}", "") .replace (")", "") .replace (", "," ↯ ") .replace (": "," ⇔ ")
                file.write ("</ol> GEO:" + str (flag_str_sum) + ". \ n")
            except:
                pass
            file.write ("<br> The requested object <<b>" + str (username) + "</b>> found: <b>" + str (exists_counter) + "</b> times (a)." )
            file.write ("<br> Report elapsed time:" + "<b>" + "% .0f"% float (timefinish) + "</b>" + "c. \ n")
            file.write ("<br> Base Snoop (DemoVersion): <b>" + str (flagBS) + "</b>" + "Websites. \ n")
            file.write ("<br> Updated:" + "<i>" + time.strftime ("% d /% m /% Y_% H:% M:% S", time_data) + ". </i> <br> <br> \ n ")
            file.write ("" "
    <script>
    function sortList () {
      var list, i, switching, b, shouldSwitch;
      list = document.getElementById ('id777');
      switching = true;
      while (switching) {
        switching = false;
        b = list.getElementsByTagName ("LI");
        for (i = 0; i <(b.length - 1); i ++) {
          shouldSwitch = false;
          if (b [i] .innerHTML.toLowerCase ()> b [i + 1] .innerHTML.toLowerCase ()) {
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          b [i] .parentNode.insertBefore (b [i + 1], b [i]);
          switching = true;
        }
      }
    }
    </script>

<script src = "../../ web / particles.js"> </script>
<script src = "../../ web / app.js"> </script>
<audio controls="controls" autoplay="autoplay" loop="loop">
<source src="../../web/Megapolis (remix).mp3" type="audio/mpeg">
</audio>

<br>
<audio controls="controls" loop="loop">
<source src="../../web/for snoop in cyberpunk.mp3" type="audio/mpeg">
</audio>

<br><br>

<a target='_blank' href='https://github.com/snooppr/snoop' class="SnA"> <span class = "SnSpan"> 💊 Source Source code </span> </a>
<a target='_blank' href='https://yasobe.ru/na/snoop_project' class="DnA"> <span class = "DnSpan"> 💊 Donation Donation </span> </a>
<br> <br> <br> <br>

</body>
</html> "" ")
            file.close ()

    # Record in csv.
            with open ("results / csv /" + username + ".csv", "w", newline = '', encoding = "utf-8") as csv_report:
                usernamsCSV = re.sub ("", "_", username)
                if censor> = 11 * int (kef_user):
                    writer = csv.writer (csv_report)
                    writer.writerow (['Object',
                                     'Resource',
                                     'Country',
                                     'Url',
                                     'Url_username',
                                     'Status',
                                     'Status_http',
                                     'Total_slow / ms',
                                     'Response / ms',
                                     'Total_time / ms',
                                     'Caution! _Search_was_with_unstable_Internet_connection_or_Internet-Censorship. ''
                                     'Results_can_be_complete.'
                                     ])
                else:
                    writer = csv.writer (csv_report)
                    writer.writerow (['Object',
                                     'Resource',
                                     'Country',
                                     'Url',
                                     'Url_username',
                                     'Status',
                                     'Status_http',
                                     'Total_slow / ms',
                                     'Response / ms',
                                     'Total_time / ms'
                                     ])
                for site in results:
                    writer.writerow ([usernamsCSV,
                                     site
                                     results [site] ['countryCSV'],
                                     results [site] ['url_main'],
                                     results [site] ['url_user'],
                                     results [site] ['exists'],
                                     results [site] ['http_status'],
                                     results [site] ['response_time_site_ms'],
                                     results [site] ['check_time_ms'],
                                     results [site] ['response_time_ms']
                                     ])
                writer.writerow (['"---------------------------------------',
                                 '--------', '----', '------------------------------- --- ',
                                 '------------------------------------------------- ------- ',
                                 '-------------', '-----------------', '------------- ------------------- ',
                                 '-------------', '----------------------- ”'])
                writer.writerow (['Base_Snoop (DemoVersion) =' + str (flagBS) + '_Websites'])
                writer.writerow ('')
                writer.writerow (['Date'])
                writer.writerow ([time.strftime ("% d /% m /% Y_% H:% M:% S", time_data)])
                file.close ()
    # Finishing output.
        if censor> = 11 * int (kef_user):
            print (Fore.CYAN + "├───Search date:", time.strftime ("% d /% m /% Y_% H:% M:% S", time_data))
            print (Fore.CYAN + "└──── \ 033 [31; 1mAttention! \ 033 [0m", Fore.CYAN + "Unstable connection or Internet Censorship:",
                              "* use VPN")
            print ("\ n \ 033 [37m \ 033 [44m {}". format ("License: copyright"))
        else:
            print (Fore.CYAN + "└───Search date:", time.strftime ("% d /% m /% Y_% H:% M:% S", time_data))
            print ("\ n \ 033 [37m \ 033 [44m {}". format ("License: copyright"))

# Default search (without the '-u' option).
    else:
        for username in args.username:
            
            file = open ("results / txt /" + username + ".txt", "w", encoding = "utf-8")
            try:
                file = open ("results / txt /" + username + ".txt", "w", encoding = "utf-8")
            except (SyntaxError, ValueError):
                pass

            try:
                if args.country == True:
                    results = snoop (username,
                                   sortC,
                                   country = args.country,
                                   user = args.user,
                                   verbose = args.verbose,
                                   reports = args.reports,
                                   print_found_only = args.print_found_only,
                                   timeout = args.timeout,
                                   color = not args.no_func)
                else:
                    results = snoop (username,
                                   site_data
                                   country = args.country,
                                   user = args.user,
                                   verbose = args.verbose,
                                   reports = args.reports,
                                   print_found_only = args.print_found_only,
                                   timeout = args.timeout,
                                   color = not args.no_func)
            except:
                results = snoop (username,
                               site_data
                               country = args.country,
                               user = args.user,
                               verbose = args.verbose,
                               reports = args.reports,
                               print_found_only = args.print_found_only,
                               timeout = args.timeout,
                               color = not args.no_func)
            exists_counter = 0
            file.write ("Address | resource" + "\ n \ n")
            for website_name in results:
                timefinish = time.time () - timestart
                dictionary = results [website_name]
                if dictionary.get ("exists") == "found!":
                    exists_counter + = 1
                    file.write (dictionary ["url_user"] + "|" + (website_name) + "\ n")
            file.write ("\ n" f "Requested object: <{username}> found: {exists_counter} times.")
            file.write ("\ n" f "Base Snoop (DemoVersion):" + str (flagBS) + "Websites.")
            file.write ("\ n" f "Updated:" + time.strftime ("% d /% m /% Y_% H:% M:% S", time_data) + ".")
            print (Fore.CYAN + "├─Search results:", "found ->", exists_counter, "url (% .0f"% float (timefinish) + "sec)")
            print (Fore.CYAN + "├──The results are saved in:" + Style.RESET_ALL + "results / * /" + str (username) + ". *")
			
    # Record in html.
            file = open ("results / html /" + username + ".html", "w", encoding = "utf-8")
            try:
                file = open ("results / html /" + username + ".html", "w", encoding = "utf-8")
            except (SyntaxError, ValueError):
                pass
            file.write ("<! DOCTYPE html> \ n <head> \ n <meta charset = 'utf-8'> \ n <style> \ nbody {background: url (../../ web / public.png ) \
            no-repeat 20% 0%; } \ n </style> \ n <link rel = 'stylesheet' href = '.. / .. / web / style.css'> \ n </head> \ n <body> \ n \ n \
            <div id = 'particles-js'> </div> \ n \
            <div id = 'report'> \ n \ n \
            <h1> <a class='GL'href='file://" + str(dirresults) + "/results/html/'> Home </a> "+" </h1> \ n ")
            file.write ("" "\ t \ t \ t <h3> Snoop Project (Demo Version) </h3>
            <p> Press: 'sort by country', return: 'F5': </p>
            <button onclick = "sortList ()"> Sort by country </button> <br> <br> \ n \ n "" ")
            file.write ("Object" + "<b>" + (username) + "</b>" + "was found on the following" + "<b>" + str (exists_counter) +
            "</b> resources: \ n" + "<br> <ol" + "id = 'id777'> \ n")
            
            cnt = Counter ()
            for website_name in results:
                dictionary = results [website_name]
                flag_sum = dictionary ["flagcountry"]
                if dictionary.get ("exists") == "found!":
                    li = []
                    li.append (flag_sum)
                    exists_counter + = 0
                    for word in li:
                        cnt [word] + = 1
                    file.write ("<li>" + dictionary ["flagcountry"] + "<a target='_blank' href='" + dictionary ["url_user"† + "'>" +
                    (website_name) + "</a>" + "</li> \ n")
            flag_str = str (cnt)
            try:
                flag_str_sum = (flag_str.split ('{') [1]). replace ("'", "") .replace ("}", "") .replace (")", "") .replace (", "," ↯ ") .replace (": "," ⇔ ")
                file.write ("</ol> GEO:" + str (flag_str_sum) + ". \ n")
            except:
                pass
            file.write ("<br> The requested object <<b>" + str (username) + "</b>> found: <b>" + str (exists_counter) + "</b> times (a)." )
            file.write ("<br> Report elapsed time:" + "<b>" + "% .0f"% float (timefinish) + "</b>" + "c. \ n")
            file.write ("<br> Base Snoop (DemoVersion): <b>" + str (flagBS) + "</b>" + "Websites. \ n")
            file.write ("<br> Updated:" + "<i>" + time.strftime ("% d /% m /% Y_% H:% M:% S", time_data) + ". </i> <br> <br> \ n ")
            file.write ("" "
    <script>
    function sortList () {
      var list, i, switching, b, shouldSwitch;
      list = document.getElementById ('id777');
      switching = true;
      while (switching) {
        switching = false;
        b = list.getElementsByTagName ("LI");
        for (i = 0; i <(b.length - 1); i ++) {
          shouldSwitch = false;
          if (b [i] .innerHTML.toLowerCase ()> b [i + 1] .innerHTML.toLowerCase ()) {
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          b [i] .parentNode.insertBefore (b [i + 1], b [i]);
          switching = true;
        }
      }
    }
    </script>

<script src = "../../ web / particles.js"> </script>
<script src = "../../ web / app.js"> </script>

<audio controls = "controls" autoplay = "autoplay" loop = "loop">
<source src = "../../ web / Megapolis (remix) .mp3" type = "audio / mpeg">
</audio>

<br>
<audio controls = "controls" loop = "loop">
<source src = "../../ web / for snoop in cyberpunk.mp3" type = "audio / mpeg">
</audio>

<br> <br>

<br><br><br><br>

</body>
</html>""")
            file.close ()

    # Record in csv.
            with open ("results / csv /" + username + ".csv", "w", newline = '', encoding = "utf-8") as csv_report:
                usernamCSV = re.sub ("", "_", username)

                if censor> = 11:
                    writer = csv.writer (csv_report)
                    writer.writerow (['Object',
                                     'Resource',
                                     'Country',
                                     'Url',
                                     'Url_username',
                                     'Status',
                                     'Status_http',
                                     'Total_slow / ms',
                                     'Response / ms',
                                     'Total_time / ms',
                                     'Caution! _Search_was_with_unstable_Internet_connection_or_Internet-Censorship. ''
                                     'Results_can_be_complete.'
                                     ])
                else:
                    writer = csv.writer (csv_report)
                    writer.writerow (['Object',
                                     'Resource',
                                     'Country',
                                     'Url',
                                     'Url_username',
                                     'Status',
                                     'Status_http',
                                     'Total_slow / ms',
                                     'Response / ms',
                                     'Total_time / ms'
                                     ])
                for site in results:
                    writer.writerow ([usernamCSV,
                                     site
                                     results [site] ['countryCSV'],
                                     results [site] ['url_main'],
                                     results [site] ['url_user'],
                                     results [site] ['exists'],
                                     results [site] ['http_status'],
                                     results [site] ['response_time_site_ms'],
                                     results [site] ['check_time_ms'],
                                     results [site] ['response_time_ms']
                                     ])
                writer.writerow (['"---------------------------------------',
                                 '--------', '----', '------------------------------- --- ',
                                 '------------------------------------------------- ------- ',
                                 '-------------', '-----------------', '------------- ------------------- ',
                                 '-------------', '----------------------- ”']])
                writer.writerow (['Base_Snoop (DemoVersion) =' + str (flagBS) + '_Websites'])
                writer.writerow ('')
                writer.writerow (['Date'])
                writer.writerow ([time.strftime ("% d /% m /% Y_% H:% M:% S", time_data)])
                file.close ()

    # Finishing output.
        if censor> = 11:
            print (Fore.CYAN + "├───Search date:", time.strftime ("% d /% m /% Y_% H:% M:% S", time_data))
            print (Fore.CYAN + "└──── \ 033 [31; 1mAttention! \ 033 [0m", Fore.CYAN + "Unstable connection or Internet Censorship:", "* use VPN")
            print ("\ n \ 033 [37m \ 033 [44m {}". format ("License: copyright"))
        else:
            print (Fore.CYAN + "└───Search date:", time.strftime ("% d /% m /% Y_% H:% M:% S", time_data))
            print ("\ n \ 033 [37m \ 033 [44m {}". format ("License: copyright"))

# Open / no browser with search results.
    if args.no_func == False:
        if exists_counter> = 1:
            webbrowser.open (str ("file: //" + str (dirresults) + "/ results / html /" + str (username) + ".html"))
#Music.
        try:
            playsound ('end.wav')
        except:
            pass

if __name__ == "__main__":
    main ()
