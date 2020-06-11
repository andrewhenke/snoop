
| Platform                    |  Support  |
| --------------------------- |:---------:|
| GNU / Linux                 |    ✅    |
| Windows 7/10 (32/64)        |    ✅    |
| Android / Termux / Andrax   |    ✅    |
| macOS                       |     ❗️     |
| WSL                         |     ❗️     |
| IOS                         |    🚫    |


** Native Installation **
Note: The required version of python is 3.7 and higher.

`` ``
# Clone repository
$ git clone https://github.com/snooppr/snoop

# Enter the working directory
$ cd ~ / snoop

# Install python3 and python3-pip if they are not installed
$ apt-get update && apt-get install python3

# Install dependencies 'requirements'
$ pip install --upgrade pip
$ python3 -m pip install -r requirements.txt
# Either install all the dependencies from 'requirements.txt' manually through
$ pip3 install module
# If special characters are displayed instead of country flags, deliver a font package, for example, monochrome
$ apt-get install ttf-ancient-fonts or color apt-get install fonts-noto-color-emoji
`` ``
## Snoop for Android
** Native Installation **

Install [Termux] (https://play.google.com/store/apps/details?id=com.termux&hl=en "Google Play")
`` ``
# Enter the Termux home folder (i.e. just open Termux)
$ termux-setup-storage
$ ls # / data / data / com.termux / files / home default / home directory

# Install python3 and dependencies
# Note: long time installation
$ apt update && pkg upgrade && pkg install python libcrypt libxml2 libxslt git
$ pip install --upgrade pip

# Clone repository
$ git clone https://github.com/snooppr/snoop
# (If the flash drive is FAT (nor ext4), in this case,
# clone the repository only in the TERMux HOME directory)

# Enter the Snoop working directory
$ cd ~ / snoop
# Install dependencies 'requirements'
$ python3 -m pip install -r requirements.txt


Addition for obsolete gadgets (Android 6)
# Note on modern gadgets packages are already preinstalled and configured
# add any 'random' name and mail [^ 1]:
$ git config --global user.email "you@example.com"
$ git config --global user.name "username"
# Install coreutils
$ pkg install coreutils
`` ``
## Using
`` ``
$ python3 snoop.py --help

usage: snoop.py [-h] [--donate y] [--version] [--verbose] [--base]
                [--web-base] [--site] [--time-out] [--found-print] [--no-func]
                [--userload] [--list all] [--country] [--save-report]
                [--update y]
                USERNAMES [USERNAMES ...]

Snoop: nickname search on all fronts! (Version 1.2.1_rus Snoop Full)

positional arguments:
  USERNAMES wanted user nickname, supported
                        several names

optional arguments:
  -h, --help show this help message and exit
  --donate y, -d y Donate to the development of the Snoop Project
  --version, --about, -V
                        START! Printing versions: OS; Snoop;
                        Python and Licenses
  --verbose, -v When searching for 'username' print
                        verbalization in detail
  --base, -b Indicate another database to search for 'username' (Local)
  --web-base, -w Connect to search for 'username' to update
                        web_db (Online)
  --site, -s Specify the site name from the database '--list all'. Search 'username'
                        on one specified resource
  --time-out, -t 9 Set the allocation of max time to wait for a response
                        from the server (seconds). Affects the duration
                        search. Affects 'Timeout errors:' On this
                        the option is almost always necessary when slow
                        internet connection to avoid lengthy
                        network freezes (default value
                        9c set)
  --found-print, -f Print only found accounts
  --no-func, -n ✓ Monochrome terminal, do not use colors in url
                        ✓ Mute. ✓ Prevent the opening of a web browser.
                        ✓ Disable printing of country flags ✓ Disable
                        indication and status of progress
  --update y Update Snoop source code
`` ``

** Example **
`` ``
# To search for only one user:
$ python3 snoop.py username1
# Or, for example, Cyrillic is supported:
$ python3 snoop.py olesya
# To search for a name containing a space:
$ python3 snoop.py "ivan ivanov"
$ python3 snoop.py ivan_ivanov
$ python3 snoop.py ivan-ivanov

# Launch on Windows OS:
$ python snoop.py username1

# To search for one or more users:
$ python3 snoop.py username1 username2 username3 username4

# Search for many users - sorting output by country;
# Avoiding freezes on sites (more often the 'dead zone' depends on your ip-address);
# print only found accounts; save pages found
# accounts locally; specify a file with a list of wanted accounts:
$ python3 snoop.py -c -t 13 -f -S -u ~ / file.txt start

# 'ctrl-c / z' - abort the search
`` ``
The found accounts will be stored in ~ / snoop / results / * / username. {Txt.csv.html}.
To access the browser to the search results on the Android platform, root rights are required.
open csv in * office in utf-8 encoding, separator 'comma'.

Destroy ** all ** search results - delete the directory '~ / snoop / results'.

`` ``
#Update Snoop to test new features in the software:
$ python3 snoop.py --update y
[^ 1]: Requires Git installation.
`` ``

## Major errors

| Party | Problem | Solution |
|: ---------: | -------------------------------------------------- ---- |: -------: |
| ========= | ========================================= ================ | ======= |
| Client | Connection Blocking by Proactive Defense (* Kaspersky) | 1 |
| | Insufficient Internet connection speed EDGE / 3G | 2 |
| | Too low value of option '-t' | 2 |
| | invalid username | 3 |
| | Errors: [GipsysTeam; RamblerDating; Mamochki] | 7 |
| ========= | ========================================= ================ | ======= |
| Provider | Internet Censorship | 4 |
| ========= | ========================================= ================ | ======= |
| Server | Site changed its response / API; updated CF / WAF | 5 |
| | Server blocking the range of client IP addresses | 4 |
| | Activation / protection of the resource captch | 4 |
| | Some sites are temporarily unavailable, technical work | 6 |
| ========= | ========================================= ================ | ======= |

Solutions:
1. Reconfigure your Firewall (for example, Kaspersky blocks Adult Resources).

2. Check the speed of your Internet connection:
$ python3 snoop.py -v username
If any of the network parameters is highlighted in red, Snoop may hang during the search.
At low speed, increase the value of the 'x' option '--time-out x':
$ python3 snoop.py -t 15 username

3. In fact, this is not a mistake. Fix username
(for example, on some sites Cyrillic characters are not allowed; "spaces"; or 'Vietnamese-Chinese_encoding'
in user names, in order to save time: - requests are filtered).

4. ** Change your ip address **
(The "Gray" ip and censorship are the most common because of what you get skip / false positive errors / and in some cases '** Alas **'.
For example, the most effective way to solve the problem is to use a VPN, Tor is not very suitable for this task.
Rule: one scan from one ip is not enough to get the maximum return from Snoop).

5. Open Snoop repositories on Github-e Issue / Pull request
(inform the developer about this).

6. Do not pay attention, sites sometimes go to repair work and return to duty.

7. [Problem] (https://wiki.debian.org/ContinuousIntegration/TriagingTips/openssl-1.1.1 "the problem is simple and solvable") with some GNU / Linux distributions
Decision
`` ``
$ sudo nano /etc/ssl/openssl.cnf

# Change at the very bottom of the line file:
[CipherString = DEFAULT @ SECLEVEL = 2]
on the
[CipherString = DEFAULT @ SECLEVEL = 1]
`` ``
