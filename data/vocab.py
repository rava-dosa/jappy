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
    ("jinruigaku","anthropology"),("seiji","politics"),("bijinesu","business"),("bungaku","literature"),
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
    ("machi","town/city"),("resutoran","restaurent"),("kissaten","cafe"),("ginkoo","bank"),("toire","toilet"),
    ("toshokan","library"),("yuubinkyoku","post office"),("ie","home"),("uchi","my home"),("gakkou","school"),
    ("mise","shop / store"),("yaoya","vegetable shop"),("doubutsuen","zoo"),("taishikan","embassy"),("keisatsu","police"),
    ("kouban","police station"),("tatemono","building"),("michi","road"),("kado","edge"),("kousaten","intersection"),
    ("shingou","signal"),("iriguchi","entrance"),("deguchi","exit"),("shi","city"),("ike","pond"),("niwa","garden"),
    ("daidokoro","kitchen"),("kaidan","stairs")
]
fun=[
    ("eiga","movie"),("ongaku","music"),("jasshi","magazine"),("supaatsu","sports"),
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
    ("basu","bus"),("hikouki","airplane"),("heya","room"),("goku","I(used by men)"),("yasumi","holiday"),("ryokuu","travel")
]
general3=[
    ("okane","money"),("ofuru","bath"),("kyoukasho","textbook"),("shiminbyouin","municipal hospital"),("tsugi","next"),("denki","electricity"),
    ("densha","train"),("nimotsu","baggage/luggage"),("pasokon","personal computer"),("peegi","page"),("mado","window"),("yoru","night")
]
bodyparts=[
    ("karada","body"),("atama","head"),("kami","hair"),("kao","face"),("hitai","forehead"),("me","eye"),("mayu","eyebrow"),("mabuta","eyelid"),("matusge","eyelash"),("hana","nose"),("mimi","ear"),("kuchi","mouth"),
    ("kuchibiru","lip"),("ha","teeth"),("shita","tongue"),("nodo","throat"),("ago","jaw"),("kubi","neck"),("kata","shoulder"),("ude","arm"),("hiji","elbow"),("te","hand"),("yubi","finger"),("tsume","nail"),
    ("mune","chest"),("senaka","back"),("onaka","stomach"),("hiza","knee"),("ashikubi","ankle"),("kakato","heel"),("tsumasaki","toe"),("ashi","leg")
    ]

general4=[
    ("megane","glasses"),("me","eye"),("haha","my mother"),("chichi","my father"),("shokudou","cafeteria / dining hall"),("kuruma","car"),
    ("kuni","country"),("kuchi","mouth"),("kazoku","family"),("onnanohito","woman"),("obaasan","grandmother"),("oneesan","older sister"),
    ("oniisan","elder brother"),("otokonohito","man"),("otouto","younger brother"),("ojiisan","grandfather"),("imouto","younger sister"),("uta","song"),
    ("ane","elder sister"),
    ("iiko","good child"),("iru","color"),("obentou","lunch box"),("kabuki","traditiona art"),("kyonen","last year"),("kusuri","medicine"),
    ("kusuri o nomu","drink medicine"),("kondo","near future"),("sakubun","essay / composition"),("shiken","exam"),("sengetsu","last month"),
    ("tango","vocabulary / word"),("byouki","illness"),
    ("kokuban","blackboard"),("kongetsu","this month"),("tenkiyobou","weather forecast"),("tokoro","place"),("nanika","something"),
    ("hashi","chopsticks"),("maishuu","every week"),("raigetsu","next month")
]

general5=[
    ("eki","station"),("okanemochi","rich person"),("kisetsu","season"),("gyuuniyuu","milk"),("kotoshi","this year"),("shinkansen","bullet train"),
    ("seikatsu","life / living"),("sekai","world"),("chikatetsu","subway"),("tebukura","gloves"),("tempura","tempura"),
    ("tokoya","barber shop"),("biyouin","beauty parlor"),("bin","flight"),("fune","ship / boat"),("yakyuu","baseball"),
    ("yuumejin","celebrity"),("yoyaku","reservation"),("raigakki","next semester"),("ringo","apple"),
    ("okashi","sweets"),("oshougatsu","new year's"),("otokonoko","boy"),("omatsuri","festival"),("omocha","toy"),("onsen","spa ; hot spring"),
    ("onnako","girl"),("gaikoku","foreign country"),("kashu","singer"),("kawa","river"),("kochira","this person"),("kongakki","this semester"),
    ("shachou","ceo/president of company"),("jugyou","class"),("shourai","future"),("jinja","shrine"),("tsuri","fishing"),
    ("bijuutsukan","art musuem"),("mizuumi","lake"),("yama", "mountain"),("yume","dream"),("sora","sky"),
    ("imi","meaning"),("otearai","restroom"),("kaje","cold"),("kanojo","girlfriend/she"),("kare","boyfriend/he"),
    ("kion","temperature"),("shiai","match"),("seiseki","grade"),("seki","cough"),("hana","flower"),("fuku","clothes"),
    ("futsukayoi","hangover"),("mono","thing"),("youji","business to take care of")
    ]
season=[
    ("shiki","four season"),("hairu","spring"),("natsu","summer"),("aki","fall / autumn"),("fuyu","winter"),("tenki","weather"),("hare","sunny"),("kumo","cloud"),("kumori","cloudy"),("rain","ame"),("taifuu","typhoon"),
    ("kiri","fog"),("yuki","snow"),("ondo","temperature"),("shitsudo","humidity"),("atsui","hot"),("atatakai","warm"),("samui","cold"),("sujushi","cold"),("kuuki","air")
]

adji=[
    ("ii","good"),("hayai","early"),("oishii","delicious"),("atarashii","new"),("atsui","hot"),("isogashii","busy"),("ookii","large"),
    ("omashiroi","interesting/funny"),("kakkoii","good-looking"),("kowai","frightening"),("samui","cold"),("tanoshii","fun"),
    ("chisai","small"),("tsumaranai","boring"),("furui","old"),("mujukashii","difficult"),("yasashi","easy/kind"),("yasui","cheap"),
    ("aoi","blue"),("akai","red"),("kurui","black"),("sabishii","lonely"),("shiroi","white"),("wakai","young"),
    ("atamagaii","bright"),("kawaii","cute"),("segatakaii","tall"),("segahikui","short"),("nagai","long"),("hayai","fast"),("mijikai","short"),
    ("amai","sweet"),("itai","hurt"),("ooi","there are many"),("semai","narrow"),("tsugougawarui","inconvenient / to have a schedule conflict"),
    ("warui","bad"),("atatakai","warm"),("osoi","slow;late"),("sujushii","cool (weather)"),("tsumetai","cold (things/people)"),
    ("nemui","sleepy")
]
adjna=[
    ("kirai","dislike/disgust"),("kirei","beautiful"),("genki","healthy"),("shijuka","quiet"),("suki","fond/like"),
    ("daikirai","very hate"),("daisuki","very fond/very love"),("nigiyaka","lively"),("hima","not busy"),("taihen","tough"),
    ("yuumei","famous"),("suteki","nice"),("kantan","easy"),("ijiwaru","mean spirited"),("jouzu","good at"),("heta","poor at"),
    ("shinsetsu","kind"),("benri","convenient")
]
negativeAdv=[
    ("amari","not much"),("jenjen","not at all")
]
positiveAdv=[
    ("taitei","usually"),("chotto","little"),("tokidoki","sometimes"),
    ("yoku","often/much")
]
verbs1=[
    {"go":["iku","u"]},{"return home":["kaeru","u"]},{"listen":["kiku","u"]},
    {"drink":["nomu","u"]},{"speak":["hanasu","u"]},{"read":["yomu","u"]},
    {"get up":["okiru","ru"]},{"eat":["taberu","ru"]},{"sleep":["neru","ru"]},
    {"see/watch":["miru","ru"]},{"come":["kuru","ire"]},{"do":["suru","ire"]},
    {"study":["benkyosuru","ire"]},

    {"meet":["au","u"]},{"there is":["aru","u"]},{"buy":["kau","u"]},{"sell":["uru","u"]},
    {"write":["kaku","u"]},{"wait":["matsu","u"]},{"to take a pic":["yoru","u"]},
    {"understand":["wakaru","u"]},{"is in/stays at":["iru","ru"]}
    ]
verbs2=[
    {"swim":["oyogu","u"]},{"ask":["miku","u"]},{"ride/board":["noru","u"]},
    {"do/perform":["yaru","u"]},{"to go out":["dekakeru","ru"]},
    {"play":["asobu","u"]},{"hurry":["isogu","u"]},{"take a bath":["ofuronihairu","u"]},
    {"return thing":["kaesu","u"]},{"turn off":["kesu","u"]},{"die":["shinu","u"]},
    {"sit down":["suwaru","u"]},{"stand up":["tatsu","u"]},{"smoke":["tabakoosuu","u"]},
    {"use":["tsukau","u"]},{"help":["tetsudau","u"]},{"enter":["hairu","u"]},
    {"carry/hold":["motsu","u"]},{"absent/rest":["yasumu","u"]},{"open":["okeru","ru"]},
    {"teach":["oshieru","ru"]},{"get off/leave":["oriru","ru"]},{"borrow":["kariru","ru"]},
    {"close":["shineru","ru"]},{"take shower":["shaawaoabiru","ru"]},{"turn on":["tsukeru","ru"]},
    {"phone call":["denwaokakeru","ru"]},{"forget":["wasureru","ru"]},
    {"bring person":["tsuretekuru","ire"]},{"bring thing":["mottekuru","ire"]}
    ]
verbs3=[
    {"make/produce/manufacture":["tsukuru","ru"]},
    {"to sing":["utau","u"]},
    {"wear hat":["kaburu","u"]},
    {"I know":["shiru","u"]},
    {"to live":["sumu","u"]},
    {"wear items below":["haku","u"]},
    {"to gain weight":["futeru","u"]},
    {"wear glass":["meganeokakeru","ru"]},
    {"wear items above":["kiru","ru"]},
    {"to work for":["tsutomeru","ru"]},
    {"to lose weight":["yaseru","ru"]},
    {"to get married":["kekkonsuru","ire"]},
    {"it rains":["amegafuru","u"]},
    {"to wash":["arau","u"]},
    {"to say":["iu","u"]},
    {"to need":["iru","u"]},
    {"to be late":["osokunaru","u"]},
    {"to think":["omou","u"]},
    {"to cut":["kiru","u"]},
    {"to make":["tsukuru","u"]},
    {"to take thing":["motteiku","u"]},
    {"to stare":["jirojiromiru","ru"]},
    {"to throw":["suteru","ru"]},
    {"to begin":["hajimeru","ru"]},
    {"to drive":["untensuru","ire"]},
    {"to do laundry":["sentakusuru","ire"]},
    {"to clean":["soujisuru","ire"]},
    {"to call":["denwasuru","ire"]},
    {"to cook":["ryourisuru","ire"]},
    {"to dance":["odoru","u"]},
    {"something ends":["owaru","u"]},
    {"to be popular":["ninkigaaru","u"]},
    {"something begins":["hajimaru","u"]},
    {"to play instrument":["hiku","u"]},
    {"to get":["morau","u"]},
    {"to memorize":["oboeru","ru"]},
    {"to attend, to exit":["deru","ru"]},
    {"to do physical exercise":["undosuru","ire"]},
    {"to take a walk":["sanposuru","ire"]}
]

verbs4=[
    {"to take (time/money)":["kakaru","u"]},
    {"to stay":["tomaru","u"]},
    {"to become":["naru","u"]},
    {"to pay":["harau","u"]},
    {"to decide":["kimeru","ru"]},
    {"to travel":["ryokousuru","ire"]},
    {"to practice":["renshuusuru","ire"]},
    {"to tell lie":["usootsuku","u"]},
    {"to become hungry":["onakagasuku","u"]},
    {"to own pet":["kau","u"]},
    {"to cut class":["saboru","u"]},
    {"to take class":["toru","u"]},
    {"to learn":["narau","u"]},
    {"to climb":["noboru","u"]},
    {"to work":["hataraku","u"]},
    {"to get tired":["tsukareru","ru"]},
    {"to quit":["yameru","ru"]},
    {"to fight":["kenkasuru","ire"]},
    {"to introduce":["shoukaisuru","ire"]},
    {"to go on diet":["dietosuru","ire"]},
    {"to be late":["chikokusuru","ire"]},
    {"to study abroad":["ryuugakusuru","ire"]},
    {"to walk":["aruku","u"]},
    {"to catch cold":["kajeohiku","u"]},
    {"to be interested":["kyoumigaaru","u"]},
    {"to loose":["nakusu","u"]},
    {"to have a fever":["netsugaaru","u"]},
    {"to become thirsty":["nodogakawaku","u"]},
    {"to cough":["sekigaderu","ru"]},
    {"to break up, to seperate":["wakareru","ru"]},
    {"to get nervous":["kinchousuru","ire"]},
    {"to worry":["shinpaisuru","ire"]},
    {"to turn":["magaru","ru"]},
    {"to cross":["wataru","ru"]},
    {"to sell":["uru","ru"]}
]

etc=[
    ("tomo","with"),("hitori","alone"),("futari","two people"),("takara","so"),("hito","man/people"),
    ("takusan","a lot"),("demo","but"),("goro","around"),("gurai","approximate"),("hitoride","alone"),
    ("isshoni","together"),("sugoku","extremely"),("sorekara","and then"),("daijoubu","it's okay"),
    ("totemo","very"),("donna","what kind of"),("atode","later on"),("osoku","do something late"),("kara","because"),
    ("kekkoudesu","that's not necessary"),("sugu","right away"),("hontoudesuka","Really?"),("yukkuri","slowly"),("kyoudai","siblings"),
    ("kesa","this morning"),("kazoku","family"),
    ("yokattara","if you like"),("mochiron","of course"),("moshimoshi","hello"),("betsuni (negative)","nothing in particular"),("nanimo (negative)","not anything"),

    ("kara","from"),("sehi","by all means"),("tokorode","by the way"),("minna","all"),("mou","already"),("itsumo","always"),
    ("uum","no"),("um","yes"),("kanpai","cheers"),("zannen","that's too bad"),("nitsuite","about / concerning"),("mada","not yet"),
    ("minnade","all of people together"),

    ("aruite","on foot"),("ichiban","best"),("ka","or"),("kagetsu","for ... months"),("go","in ...time; after..."),("konogoru","these days"),
    ("shuukan","for weeks"),("de","by ; with"),("douyatte","how; by what means"),("dochira / docchi","which"),("donogurai","how much ; how long"),
    ("nen","years"),("hayaku","early ; fast"),

    ("ato","after an event"),("shusshin","coming from"),("soshite","and then"),("dake","just ; only"),("ten","points"),("hisashiburi","it has been long time"),
    ("maamaa","okay ; so-so"),("motto","more"),

    ("odaijini","get well soon"),("genkiganai","don't look well"),("tabun","probably / maybe"),("dekirudake","as much as possible"),
    ("deshou","probably; ... right"),("do","temperature"),("nisannichi","for two to three days"),("node","because"),("hajimete","for the first time"),
    ("mousugu","very soon; in a few moments"),

    ("sukoshi","small quantity")
    ]
# pdb.set_trace()
verbs = {
    "verbs1":verbs1,"verbs2":verbs2,"verbs3":verbs3,"verbs4":verbs4
}
noun={
    "activities":activities,"peopleThings":peopleThings,"general1":general1,"countries":countries,"majors":majors,
    "occupations":occupations,"family":family,"things":things,"places":places,"fun":fun,"food1":food1,"food2":food2,
    "time":time,"location":location,"general2":general2,"general3":general3,"etc":etc,"bodyparts":bodyparts, "season":season, "general5":general5, "general4":general4
    }
adjective={
    "adji":adji,"adjna":adjna
    }

adverbs={
    "negativeAdv":negativeAdv,"positiveAdv":positiveAdv
    }

all_vocab=[noun,adjective,adverbs,verbs]