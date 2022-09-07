#!/usr/bin/env python3

import requests
import json
import time
import sys
import os





# Clear Terminal
os.system("cls" if os.name == "nt" else "clear")





# X-RapidAPI-Key
APi_Key = "Your X-RapidAPI-Key here"




# Colors
black='\033[1;90m'      # Black
red='\033[1;91m'        # Red
green='\033[1;92m'      # Green
yellow='\033[1;93m'     # Yellow
blue='\033[1;94m'       # Blue
purple='\033[1;95m'     # Purple
cyan='\033[1;96m'       # Cyan
white='\033[1;97m'      # White
reset='\033[0m'         # Reset
flash='\033[5m'         # Flash





# Ascii art
art = f"""

{reset}{green}  ██████{red}  ██████ {cyan} ██    ██{yellow} ██{purple} ██████   {flash}{white}  ██  █████  
{reset}{green} ██     {red} ██    ██{cyan} ██    ██{yellow} ██{purple} ██   ██  {flash}{white} ███ ██   ██ 
{reset}{green} ██     {red} ██    ██{cyan} ██    ██{yellow} ██{purple} ██   ██  {flash}{white}  ██  ██████ 
{reset}{green} ██     {red} ██    ██{cyan}  ██  ██ {yellow} ██{purple} ██   ██  {flash}{white}  ██      ██ 
{reset}{green}  ██████{red}  ██████ {cyan}   ████  {yellow} ██{purple} ██████   {flash}{white}  ██  █████  
{reset}{white}  CoronaVirus By SlavPH{reset}               
                                                     
"""





def GetCovid(country):
    global APi_Key, purple, cyan, green, white, flash, reset

    URL = f"https://covid-193.p.rapidapi.com/statistics?country={country}"

    headers = {
        "X-RapidAPI-Key": APi_Key,
    }

    response = requests.request("GET", URL, headers=headers)
    result = response.json()

    if result["results"] == 0:
        return f"{red}ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴠᴀʟɪᴅ ᴄᴏᴜɴᴛʀʏ!{reset}"
    else:
        data = result["response"]
        continent = str(data[0]["continent"])
        country = str(data[0]["country"])
        population = str(data[0]["population"])

        cases = data[0]["cases"]
        new = str(cases["new"])
        active = str(cases["active"])
        critical = str(cases["critical"])
        recovered = str(cases["recovered"])
        M_pop_Case = str(cases["1M_pop"])
        total = str(cases["total"])

        deaths = data[0]["deaths"]
        new_d = str(deaths["new"])
        M_pop_Deaths = str(deaths["1M_pop"])
        total_d = str(deaths["total"])

        tests = data[0]["tests"]
        M_pop_Tests = str(tests["1M_pop"])
        total_t = str(tests["total"])

        day = str(data[0]["day"])

        text = f"""
{white}#===============# {flash}{white}{country}{reset}
{white}# {cyan}ᴄᴏɴᴛɪɴᴇɴᴛ{reset} : {continent}
{white}# {cyan}ᴘᴏᴘᴜʟᴀᴛɪᴏɴ{reset} : {population}
{white}# {cyan}ᴅᴀᴛᴇ{reset} : {day}

{white}#===============# {flash}{white}𝐂𝐚𝐬𝐞𝐬 🦠{reset} 
{white}# {yellow}ɴᴇᴡ{reset} : {new}
{white}# {yellow}ᴀᴄᴛɪᴠᴇ{reset} : {active}
{white}# {yellow}ᴄʀɪᴛɪᴄᴀʟ{reset} : {critical}
{white}# {yellow}ʀᴇᴄᴏᴠᴇʀᴇᴅ{reset} : {recovered}
{white}# {yellow}1ᴍ ᴘᴏᴘ{reset} : {M_pop_Case}
{white}# {yellow}ᴛᴏᴛᴀʟ{reset} : {total}

{white}#===============# {flash}{white}𝐃𝐞𝐚𝐭𝐡𝐬 ⚰️{reset} 
{white}# {purple}ɴᴇᴡ{reset} : {new_d}
{white}# {purple}1ᴍ ᴘᴏᴘ{reset} : {M_pop_Deaths}
{white}# {purple}ᴛᴏᴛᴀʟ{reset} : {total_d}

{white}#===============# {flash}{white}𝐓𝐞𝐬𝐭𝐬 🧪{reset} 
{white}# {green}1ᴍ ᴘᴏᴘ{reset} : {M_pop_Tests}
{white}# {green}ᴛᴏᴛᴀʟ{reset} : {total_t}
"""
        return text





def main():
    global white, red, flash, cyan, purple, reset, art

    print(art)

    text = f"{white}Please Enter Country\n{reset}"
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    country = input(f"{red}>{cyan}>{purple}> {reset}")
    
    text1 = f"{white}Looking for {red}{country}{reset}...\n"
    for char in text1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    print(GetCovid(country))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        text2 = f"\n{red}Bye Bye :){reset}"
        for char in text2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
