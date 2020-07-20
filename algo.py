from vocab import *
import sys
from fuzzywuzzy import process
#gs=1, search words
#gs=2, practice nouns
#gs=3, practice verbs
#gs=4, practice kanji
#gs=5, practice adjective
#gs=6, practice adverbs
control={
    "..r":[0,"reset"],"..s":[1,"search"],"..pw":[2,"practice words"],"..pv":[3,"practice verbs"],"..pk":[4,"practice kanji"],"..padv":[5,"practice adjective"],
    "..padj":[6,"practice adverb"]
    }
def take_input():
    gs=0
    while(1):
        if(gs==0):
            for x in control.keys():
                print(x,control[x][1])
        input_str=input()
        if(input_str.startswith("..")):
            gs=take_control(input_str,gs)
            continue
        output=get_output(input_str,gs)
        gs=output["gs"]

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
    for x in verb:
        temp=list(x.keys())[0]
        temp1=x[temp][0]
        temp2=(temp,temp1)
        all_str.append(temp2)
    # print(all_str)
    all_strx=[]
    for x in all_str:
        if(len(x)>=2):
            all_strx.append(x[0])
            all_strx.append(x[1])
    matched=process.extract(input_str, all_strx, limit=2)
    ret=[]
    for x in all_str:
        temp_l=[]
        for y in matched:
            temp_l.append(y[0])
        for z in temp_l:
            if(len(x)>=2):
                if(x[0]==z or x[1]==z):
                    print(x)
                    ret.append(x)
    # print(ret)
    return ret
if __name__ == "__main__": 
    take_input()