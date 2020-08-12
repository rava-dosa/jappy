import json
import pykakasi
import random
control={
    "..r":[0,"reset"],"..s":[1,"search"],"..wps":[2,"watch practice short"],"..wpl":[3,"watch practice long"],"..swp":[4,"short write practice"],"..lwp":[5,"long write practice"],"..gm":[6,"Kanji god mode"]
    }
params={"short":2,"long":6,"comprehensive":100}

def green(str1):
    return "\033[92m{}\033[00m".format(str1)

def get_kanji_mnemonics():
    ret=json.loads(open("data/mnemonics.json").read())
    return ret
def get_kanji_similar():
    ret=json.loads(open("data/simk.json").read())
    return ret
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
    elif(gs==1):
        search_kanji("")

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

def search_kanji(input_str):
    l=read_all()
    kanji_dic={}
    for x in l:
        kanji_dic[x["kanji"]]=x["meta"]
    mnemo=get_kanji_mnemonics()
    simk=get_kanji_similar()
    while(1):
        kanji=input()
        kanji=kanji.strip()
        try:
            meta=kanji_dic[kanji]
            print("Meaning wa {}".format(meta["meaning"]))
            print("Kun wa {}".format(meta["kun"]))
            print("On wa {}".format(meta["on"]))
            printMnemo(kanji,mnemo)
            printSimilar(kanji,simk)
        except:
            print("kanji not found")
        

def watch_practice(params):
    l=read_all()
    f=int(input("From: "))
    t=int(input("To: "))
    mnemo=get_kanji_mnemonics()
    simk=get_kanji_similar()
    for x in range(f,t+1):
        kanji=l[x]
        print("What is this Kanji: {}".format(kanji["kanji"]))
        input()
        meta=kanji["meta"]
        print("Meaning - {}".format(meta["meaning"]))
        printMnemo(kanji["kanji"],mnemo)
        printSimilar(kanji["kanji"],simk)
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