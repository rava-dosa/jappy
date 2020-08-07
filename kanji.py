import json
import pykakasi
import random
control={
    "..r":[0,"reset"],"..s":[1,"search"],"..wps":[2,"watch practice short"],"..wpl":[3,"watch practice long"],"..swp":[4,"short write practice"],"..lwp":[5,"long write practice"],"..gm":[6,"Kanji god mode"]
    }
params={"short":2,"long":6,"comprehensive":100}
def take_input():
    gs=0
    while(1):
        if(gs==0):
            for x in control.keys():
                print(x,control[x][1])
        input_str=input()
        if(input_str.startswith("..")):
            gs=take_control(input_str,gs)
            if(gs==0 or gs==1):
                continue         
        get_output(input_str,gs)
        # gs=output["gs"]
        # print(output["output"])

def take_control(input_str,gs):
    # r for reset
    if(input_str==".."):
        sys.exit()
    elif(input_str in control.keys()):
        return control[input_str][0]
    else:
        sys.exit()

def get_output(input_str,gs):
    if(gs==2):
        watch_practice(params["short"])
    elif(gs==3):
        watch_practice(params["long"])
    

def read_all():
    l=[]
    for x in range(1,7):
        temp=json.loads(open("data/kanji{}.json".format(x)).read())
        l=l+temp
    return l


def getromanji(string):
    kks = pykakasi.kakasi()
    result = kks.convert(string)
    ret=""
    for x in result:
        ret=ret+x["passport"]+" "
    return ret

def print_word(word):
    print("{} - {} - {}".format(word[0],getromanji(word[1]),word[2]))

def watch_practice(params):
    l=read_all()
    f=int(input("From: "))
    t=int(input("To: "))
    for x in range(f,t+1):
        kanji=l[x]
        print("What is this Kanji: {}".format(kanji["kanji"]))
        input()
        meta=kanji["meta"]
        print("Meaning - {}".format(meta["meaning"]))
        input()
        print("kun wa - {}, on wa - {}".format(meta["kun"],meta["on"]))
        input()
        words=kanji["words"]
        for x in range(0,params-1):
            try:
                print(words[x][0])
                input()
                print_word(words[x])
            except IndexError as error:
                continue
        x=random.randint(0,len(words)-1)
        print_word(words[x])
        input()

def write_practice(params):
    return

if __name__ == "__main__": 
    take_input()