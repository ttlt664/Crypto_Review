from Crypto.Util.number import getPrime, isPrime, bytes_to_long
import os

def 0psu3_The_best(sz, d):
    while True:
        p = getPrime(sz)
        pp = sum([p**i for i in range(d)])
        if isPrime(pp):
            return p, pp


p, q = 0psu3_The_best(512, 5)
r = getPrime(512 * 5)
n = p * q * r
e = 65537
flag=open("flag.txt", "rb").read().strip()
flag1=flag+os.urandom(128)
m=bytes_to_long(flag1)

c = pow(m, e, n)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")


#n=43090231453250894711427929679917165532091051269639380881822679198388872373018031295429558758883298138388596507242928145888959963579111847255588834248367032580980272245414738073179172684104908272069503607376171584936239696444309039211273376010193165083254209608051430794825261116490356392215410064858020176711199543381037420111454942356936721487016187240237683725310306748046587503625096246489043270381153251813360521583717685413070481576320194446237522118380283335294528606720928637529817170809666802598938788405154468683850385277659812316577873886708164549255359514776884765904417881419804464020855420288884972204146588152412816874161445668955639456202226751519881834234916642218078966066353317917939418964763844067220460513388433020071277477619189495465483910271310025371745344364984826481983188861624474015117761898377237745775289039922285111681410319016537270412509750339539020876501534842403407208957382830000761065368861209033791387480377889838737241326116532852335478193204425626487166234964754732945953080086117315162916374952094149599597509405176646068341218684523765974759907645226607364627690026025662221036766148813918691578120023886400197652148214238256715089883892069133754778609710846757189987335827693169644541734443763194942694587436469448973201513131503797898892822373949177030567791519349220158287318717788746060997955057747930375117780320371517616412423571775682868481089431670802944047375824503353609019686495670630728618082254293585479431369645935654024149490741245953271830453426444847467908952699660750809490650479987
#e=65537
#c=30862228874892553476569860337345503267926249096036551213683005116620750680365154103242717714230966827288361499342464202425467642950081816675486231250411347472976482409360391136808439034217688010072648722396312121758844966972323513456884732046270240934002095706243044210312663525491282667971502534420245427643076262414036655243117610886157895994101178663474990136516153062956803591842233732498519246731337518545018734984319536536205092573418457928952414660837594265802406473201400259189950484841504227372735345451459452313825309333631615286962304963039625162366186574440146535361888708570569938418676320446653266676364765870547213167058713058609788316647593834008151805692510044158607162858906528913516242904419457446211348504248317409844426309455978985314882123424453618672960876022996245213882467954521212481418830104602302179759479012618982228223244131619557639469872139485197176384683400796204681045965981417650462297978265085323342772310690638049411549216990505001950512428646871875659468885490055363436412364532718888124906227240501145227269727887236864060558999336443165765870556727793253297515155026234234422303238380776900105115890363548589834345888430695886678231459920101695996112312269637459823479947618045447071359886515163416153117176539752947700226596291435270282598638974889205601333097978743387412651687356072223691445472690647184292120882095587563356691450107194982597794937293154289560470269606300576216128045797481404606810315677962659136641943747123985144899464108823536597185386155005111274476874957827391438859327653936
