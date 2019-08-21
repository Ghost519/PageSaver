#! /user/bin/python3
#This script downloads a gevin website and stores it in Downloades/Websites

import requests, os, sys, webbrowser


print('*** Welcome to PageSaver 1.0! ***\n')
print('Please enter "save" if you want to save a webpage, "list" if you want to list your downloaded pages, and "open" to open a webpage.')
order = input()

if order == 'save': 
    print('Enter the url of the page you want to save')
    url = input()
    fileName = input('\nplease enter the name of the saved page\n')

    page = requests.get(url)
    page.raise_for_status()

    if os.path.exists('../Downloads/Websites'):
        os.chdir('../Downloads/Websites')
        savedPage = open(fileName, 'wb')
        for chunks in page.iter_content(10000):
            savedPage.write(chunks)    

        savedPage.close()

elif order == 'list':
    os.chdir('../Downloads/Websites')
    print(os.listdir())

elif order == 'open':
    print('Enter the name of the page')
    pagename = input()
    webbrowser.open('../Downloads/Websites/' + pagename)