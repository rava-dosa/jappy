from data.vocab import *
import sys
from fuzzywuzzy import process
from random import choice
import json
from data.genkikanji import l5
from kanji import getromanji
import re
#gs=1, search words
#gs=2, practice nouns
#gs=3, practice verbs
#gs=4, practice kanji
#gs=5, practice adjective
#gs=6, practice adverbs
control={
    "..r":[0,"reset"],"..s":[1,"search"],"..pw":[2,"practice words"],"..pv":[3,"practice verbs"],"..pk":[4,"practice genki kanji"],"..pke":[7,"practice genki kanji extended"],"..padj":[5,"practice adjective"],
    "..padv":[6,"practice adverb"]
    }

def green(str1):
    return "\033[92m{}\033[00m".format(str1)

def get_kanji_data():
    l=[]
    ret={}
    for x in range(1,7):
        temp=json.loads(open("data/kanji{}.json".format(x)).read())
        l=l+temp
    for t in l:
        ret[t['kanji']]=t
    return ret

def get_kanji_mnemonics():
    ret=json.loads(open("data/mnemonics.json").read())
    return ret

def get_kanji_similar():
    ret=json.loads(open("data/simk.json").read())
    return ret

def get_genki_kanji():
    ret=json.loads(open("data/gk.json").read())
    return ret

def printMnemo(kanji,mnemo):
    try:
        print("To remember : {}".format(green(mnemo[kanji])))
    except:
        print("Mnemonics not found")

def printSimilar(kanji,simk):
    try:
        temp=simk[kanji]
        print("Similar kanji are as follow: ")
        print(temp)
    except:
        print("Similar kanji not found")

def take_input():
    gs=0
    while(1):
        if(gs==0):
            for x in control.keys():
                print(x,control[x][1])
        input_str=input()
        if(input_str.startswith("..")):
            gs=take_control(input_str,gs)
            print(gs)
            if(gs==0 or gs==1):
                continue         
        output=get_output(input_str,gs)
        gs=output["gs"]
        print(output["output"])

def take_control(input_str,gs):
    # r for reset
    if(input_str==".."):
        sys.exit()
    elif(input_str in control.keys()):
        return control[input_str][0]
    else:
        sys.exit()


def get_output(input_str,gs):
    if(gs==1):
        output=getsearch(input_str)
        return({"gs":1,"output":output})
    elif(gs==2):
        output=getnextword(input_str)
        return({"gs":2,"output":output})
    elif(gs==5):
        output=getnextadj(input_str)
        return({"gs":5,"output":output})
    elif(gs==3):
        output=getnextverb(input_str)
        return({"gs":3,"output":output})
    elif(gs==4):
        output=getnextkanji(input_str)
        return({"gs":4,"output":output})
    elif(gs==7):
        output=getnextkanjiextended(input_str)
        return({"gs":7,"output":output})
    else:
        return({"gs":0,"output":"Please enter valid command"})

def getnextword(input_str):
    error={}
    noun=all_vocab[0]
    noun_keys=list(noun.keys())
    print(noun_keys)
    keyx=input("What do you want to practice: ")
    if(keyx in noun_keys):
        l=noun[keyx]
        for x in l:
            comp=input("{}-->  ".format(x[1]))
            if(comp==x[0]):
                print("correct")
            else:
                print("wrong, correct answer is \033[92m {}-->{} \033[00m".format(x[1],x[0]))
                error[x[1]]=x[0]
        while(len(list(error.keys()))!=0):
            temp=choice(list(error.keys()))
            comp=input("{}-->  ".format(temp))
            if(comp==error[temp]):
                print("correct")
                error.pop(temp)
            else:
                print("wrong")


def getnextadj(input_str):
    error={}
    adj=all_vocab[1]
    adj_keys=list(adj.keys())
    print(adj_keys)
    keyx=input("What do you want to practice: ")
    if(keyx in adj_keys):
        l=adj[keyx]
        for x in l:
            comp=input("{}-->  ".format(x[1]))
            if(comp==x[0]):
                print("correct")
            else:
                print("wrong, correct answer is \033[92m {}-->{} \033[00m".format(x[1],x[0]))
                error[x[1]]=x[0]
        while(len(list(error.keys()))!=0):
            temp=choice(list(error.keys()))
            comp=input("{}-->  ".format(temp))
            if(comp==error[temp]):
                print("correct")
                error.pop(temp)
            else:
                print("wrong")

def getnextverb(input_str):
    error={}
    verbs=all_vocab[3]
    verb_keys=list(verbs.keys())
    print(verb_keys)
    keyx=input("What do you want to practice: ")
    if(keyx in verb_keys):
        l=verbs[keyx]
        for x in l:
            t=list(x.keys())[0]
            comp=input("{}-->  ".format(t))
            if(comp==x[t][0]):
                print("correct")
            else:
                print("wrong, correct answer is \033[92m {}-->{} \033[00m".format(t,x[t][0]))
                error[t]=x[t][0]
        while(len(list(error.keys()))!=0):
            temp=choice(list(error.keys()))
            comp=input("{}-->  ".format(temp))
            if(comp==error[temp]):
                print("correct")
                error.pop(temp)
            else:
                print("wrong")


def getnextkanji(input_str):
    print([*l5.keys()])
    allx=get_kanji_data()
    mnemo=get_kanji_mnemonics()
    simk=get_kanji_similar()
    gk=get_genki_kanji()
    chapter=input()
    for temp in l5[chapter]:
        print("What is this Kanji: {}".format(temp))
        try:
            kanji=allx[temp]
            meta=gk[temp]
            input()
            print("Meaning - {}".format(meta[1]))
            print("\nkun, on wa - {}\n".format(meta[0]))
        except:
            quit()
        printMnemo(temp,mnemo)
        printSimilar(temp,simk)
        # words=kanji["words"]
        # for temp1 in words:
        #     print(temp1[0])
        #     input()
        #     print("\033[92m{}\033[00m,\33[33m{}\033[00m".format(getromanji(temp1[1]),temp1[2]))
        #     print("\n\n")
def getnextkanjiextended(input_str):
    print([*l5.keys()])
    allx=get_kanji_data()
    mnemo=get_kanji_mnemonics()
    gk=get_genki_kanji()
    chapter=input()
    for temp in l5[chapter]:
        print("What is this Kanji: {}".format(temp))
        meta=gk[temp]
        try:
            input()
            print("Meaning - {}".format(meta[1]))
            print("\nkun, on wa - {}\n".format(meta[0]))
        except:
            print("",end="")
        try:
            print("\nTo remember : {}\n".format(green(mnemo[temp])))
        except:
            print("",end="")
        
        for x3 in range(0,len(meta[2])):
            if(x3==0):
                print("Press . to go next kanji")
            temp3=input()
            # import pdb;pdb.set_trace()
            if(temp3=='.'):
                break
            # try:
            t4=meta[2][x3]
            print("{} , {} , {}".format(t4["Example"],t4["Reading"],t4["Definition"]))
            # except:
            #     print("",end="")
                

def getsearch(input_str):
    all_str=[]
    noun=all_vocab[0]
    noun_keys=list(noun.keys())
    for x in range(0,len(noun_keys)):
        l=noun[noun_keys[x]]
        for y in l:
            all_str.append(y)
            # all_str.append(y[0])
            # all_str.append(y[1])
    # adjective,adverbs
    adjective=all_vocab[1]
    adjective_keys=list(adjective.keys())
    for x in range(0,len(adjective_keys)):
        l=adjective[adjective_keys[x]]
        for y in l:
            all_str.append(y)
            # all_str.append(y[0])
            # all_str.append(y[1])
    adverb=all_vocab[2]
    adverb_keys=list(adverb.keys())
    for x in range(0,len(adverb_keys)):
        l=adverb[adverb_keys[x]]
        for y in l:
            all_str.append(y)
            # all_str.append(y[0])
            # all_str.append(y[1])
    verb=all_vocab[3]
    for x1 in list(verb.keys()):
        for x in verb[x1]:
            temp=list(x.keys())[0]
            temp1=x[temp][0]
            temp2=(temp,temp1)
            all_str.append(temp2)
        all_strx=[]
        for x in all_str:
            if(len(x)>=2):
                all_strx.append(x[0])
                all_strx.append(x[1])
    matched=process.extract(input_str, all_strx, limit=3)
    ret=set()
    for x in all_str:
        temp_l=[]
        for y in matched:
            temp_l.append(y[0])
        for z in temp_l:
            if(len(x)>=2):
                if(x[0]==z or x[1]==z):
                    ret.add(x)
    # ret=ret[::-1]
    return ret
if __name__ == "__main__": 
    take_input()