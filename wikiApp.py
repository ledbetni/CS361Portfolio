import requests
import json

def splitReq(requestString):
    string = requestString
    n = 500
    out = [(string[i:i+n]) for i in range(0, len(string), n)]
    return(out)

def printLine():
    print("-------------------------------------")

def getItem():
    getItem = input("Enter the topic you would like to learn more about, enter exit to quit: ")
    return getItem

def getTranslate():
    getTrans = input("Would you like to translate this into Spanish? Enter 'Y' for yes or 'N' for no: ")
    return getTrans

def wikiService(requestString):
    #####
    #My Microservice, Functional
    #####
    url = "http://localhost:1400"
    itemDict = {"item": str(requestString)}
    postItem = requests.post(url,data=itemDict)
    postRes = postItem.json()
    resStr = str(postRes["item"])
    return(resStr)

def langDetectService(responseString):
    #####
    #Caroline Microservice, Functional
    #####
    urlDetect = "http://localhost:3000"
    detectDict = {"text": responseString}
    postDetect = requests.post(urlDetect, data=detectDict)
    detectRes = postDetect.text
    return(detectRes)

def translateService(requestString):
    #####
    #Luis Microservice, Functional
    #####
    urlTrans = "http://localhost:4500/translate"
    urlDetect = "http://localhost:3000"
    resStrLen = len(requestString)
    #####
    #Translation API has 500 char limit, so split request into multiple requests if longer than 500 chars
    #####
    print()
    if (resStrLen > 500):
        tranStr= splitReq(requestString)
        for i in range(len(tranStr)):
            textDict = {"text": str(tranStr[i])}
            postTrans = requests.post(urlTrans, json=textDict)
            transRes = json.loads(postTrans.text)
            transText = transRes['translated']
            print(str(transText))
        return(str(transText))
    #####
    #Request is less than or equal to 500 chars, so no splitting is needed
    #####
    elif (resStrLen <= 500):
        textDict = {"text": str(requestString)}
        postTrans = requests.post(urlTrans, json=textDict)
        transRes = json.loads(postTrans.text)
        transText = transRes['translated']
        print(str(transText))
        return(str(transText))
            

def main():
    getTopic = getItem()
    while (getTopic.lower() != ("Exit".lower())):
        if (getTopic.lower() == ("Exit".lower())):
            break
        toWiki = wikiService(getTopic)
        print()
        print(toWiki)
        langString = langDetectService(toWiki)
        printLine()
        print(langString)
        printLine()
        getTrans = getTranslate()
        if (getTrans.lower() == ('y')):
            tranlateString = translateService(toWiki)
            langTransString = langDetectService(tranlateString)
            printLine()
            print(langTransString)
            printLine()
        getTopic = getItem()
        
main()