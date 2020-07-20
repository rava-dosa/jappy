import pdb

prefix=[
    ("mai","every"),("dai","very")
    ]
activities=[
    ("arubaito","part-time job"),("kaimono","shopping"),("kurasu","class")
    ]
peopleThings=[
    ("anata","you"),("isu","chair"),("inu","dog"),("omiyage","souvenir"),
    ("kodomo","child"),("gohan","rice"),("shoshin","picture"),("tsukue","desk"),
    ("togami","letter"),("neko","cat"),("pan","bread"),("hito","person"),
    ("meeru","e-mail")
    ]
general1=[
    ("ima","now"),("eego","english"),("ee","yes"),("gakusee","student"),("kookoo","high school"),
    ("senkoo","major"),("sensee","teacher"),("daigaku","college"),("tomodachi","friend"),
    ("nensee","year student"),("han","half"),("bangoo","number"),("ryuugakkusee","international student"),
    ("gaijin","foreigner")
]
countries=[
    ("Igirisu","Britain"),("Kankoku","Korea"),("Chuugoku","China")
]
majors=[
    ("kagaku","science"),("ajia kenkyuu","Asian Studies"),("keezai","economics"),("kokusaikankee","international relations"),
    ("jinruigaku","anthropology"),("seeji","politics"),("bijinesu","business"),("bungaku","literature"),
    ("rekishi","history")
]
occupations=[
    ("shigoto","work"),("isha","doctor"),("kaishain","office worker"),("kookoosee","high school student"),
    ("shufu","housewife"),("daigakuinsee","graduate student"),("daigakusee","college student"),("bengoshi","lawyer")
]
family=[
    ("okaasan","mother"),("otoosan","father"),("oneesan","older sister"),("oniisan","older brother"),
    ("imooto","younger sister"),("otooto","younger brother")
]
things=[
    ("enpitsu","pencil"),("kasa","umbrella"),("kaban","bag"),("kutsu","shoes"),("saifu","wallet"),("jinzu","jeans"),("jisho","dictionary"),
    ("jitensha","bicycle"),("shinbun","newspaper"),("tiishatsu","t-shirt"),("tokee","watch"),("nooto","notebook"),
    ("pen","pen"),("booshi","hat"),("hon","book")
]

places=[
    ("otera","temple"),("kouen","park"),("suupaa","supermarket"),("depaato","department store"),
    ("basutei","bus stop"),("byouin","hospital"),("hoteru","hotel"),("honya","bookstore"),
    ("mochi","town/city"),("resutoran","restaurent"),("kissaten","cafe"),("ginkoo","bank"),("toire","toilet"),
    ("toshokan","library"),("yuubinkyoku","post office"),("ie","home"),("uchi","my home"),("gakkou","school")
]
fun=[
    ("eiga","movie"),("ongaku","music"),("zasshi","magazine"),("supaatsu","sports"),
    ("deto","date"),("tenisu","tennis"),("terubi","television")
]
food1=[
    ("asagohan","breafast"),("hirugohan","lunch"),("bangohan","dinner"),
    ("mizu","water"),("osake","alcohol"),("ocha","green tea"),("koohii","coffee"),()
]
food2=[
    ("oishii","delicious"),("sakana","fish"),("tonkatsu","pork cutlet"),("niku","meat"),("menyuu","menu"),("yasai","vegetable")
]
time=[
    ("konban","tonight"),("shumatsu","weekend"),("getsuyoubi","monday"),("kayoubi","tuesday"),
    ("suiyoubi","wednesday"),("mokuyoubi","wednesday"),("kinyoubi","friday"),("doyoubi","saturday"),("nichiyoubi","sunday"),
    ("ichijinka","one hour")
]
location=[
    ("migi","right"),("hidari","left"),("mae","front"),("ushiro","back"),("naka","inside"),("ue","on"),
    ("shita","under"),("chikaku","nearby"),("tonari","next"),("aida","between")
]
general2=[
    ("ue","sea"),("kitte","postal stamps"),("kippu","ticket"),("saafuin","surfing"),("shukudai","homework"),
    ("tabemono","food"),("tanjiyoubi","birthday"),("tesuto","test"),("tenki","weather"),("nomimono","drink"),("hagaki","postcard"),
    ("basu","bus"),("hikouki","airplane"),("heya","room"),("boku","I(used by men)"),("yasumi","holiday"),("ryokuu","travel")
]
adji=[
    ("ii","good"),("hayai","early"),("oishii","delicious"),("atarashii","new"),("atsui","hot"),("isogashii","busy"),("ookkii","large"),
    ("omashiroi","interesting/funny"),("kakkoii","good-looking"),("kowai","frightening"),("samui","cold"),("tanoshii","fun"),
    ("chisai","small"),("tsumaranai","boring"),("furui","old"),("mujukashii","difficult"),("yasashi","easy/kind"),("yasui","cheap")
]
adjna=[
    ("kirai","dislike/disgust"),("kirei","beautiful"),("genki","healthy"),("sujuka","quiet"),("suki","fond/like"),
    ("daikirai","very hate"),("daisuki","very fond/very love"),("nigiyaka","lively"),("hima","not busy")
]
negativeAdv=[
    ("amari","not much"),("zenzen","not at all")
]
positiveAdv=[
    ("taitei","usually"),("chotto","little"),("tokidoki","sometimes"),
    ("yoku","often/much")
]
verbs=[
    {"go":["iku","u"]},{"return":["kaeru","u"]},{"listen":["kiku","u"]},
    {"drink":["nomu","u"]},{"speak":["hanasu","u"]},{"read":["yomu","u"]},
    {"get up":["okiru","ru"]},{"eat":["taberu","ru"]},{"sleep":["neru","ru"]},
    {"see/watch":["miru","ru"]},{"come":["kuru","ire"],"do":["suru","ire"]},
    {"study":["benkyosuru","ire"]},

    {"meet":["au","u"]},{"there is":["aru","u"]},{"buy":["kau","u"]},
    {"write":["kaku","u"]},{"wait":["motsu","u"]},{"to take a pic":["yoru","u"]},
    {"understand":["wakaru","u"]},{"is in/stays at":["iru","ru"]},

    {"swim":["oyogu","u"]},{"ask":["miku","u"]},{"nori":["ride/board"]},{"yari":["do/perform"]},
    {"dekakeri":["to go out","ru"]}
    ]

etc=[
    ("tomo","with"),("hitori","alone"),("futari","two people"),("takara","so"),("hito","man/people"),
    ("takusan","a lot"),("demo","but"),("goro","around"),("gurai","approximate"),("hitoride","alone")
    ]
# pdb.set_trace()
noun={
    "activities":activities,"peopleThings":peopleThings,"general1":general1,"countries":countries,"majors":majors,
    "occupations":occupations,"family":family,"things":things,"places":places,"fun":fun,"food1":food1,"food2":food2,
    "time":time,"location":location,"general2":general2,"etc":etc
    }
adjective={
    "adji":adji,"adjna":adjna
    }

adverbs={
    "negativeAdv":negativeAdv,"positiveAdv":positiveAdv
    }

all_vocab=[noun,adjective,adverbs,verbs]