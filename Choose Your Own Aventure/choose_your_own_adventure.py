#Created 3 iteration of the function that takes user input for the choice.
def choice3(page1, page2, page3):
    page1 = str(page1)
    page2 = str(page2)
    page3 = str(page3)
    while True:
        choice = input("Enter either page " + page1 + ", page " + page2 + ", or page ", page3, "\n")
        if choice == page1:
            return page1
        elif choice == page2:
            return page2
        elif choice == page3:
            return page3
        else:
            print("Sorry that is not an option.")
            continue

def choice(page1, page2):
    page1 = str(page1)
    page2 = str(page2)
    while True:
        choice = input("Enter either page " + page1 + " or page " + page2 + "\n")
        if choice == page1:
            return page1
        elif choice == page2:
            return page2
        else:
            print("Sorry that is not an option.")
            continue

def choiceEnd(page1):
    page1 = str(page1)
    end = ""
    while True:
        choice = input("Enter either page " + page1 + " or press enter to end. \n")
        if choice == page1:
            return page1
        elif choice == end:
            return end
        else:
            print("Sorry that is not an option.")
            continue

#Assigned every page of the book a function, when a player is sent to another page the function of that page is called.
def page1():
    print("""
       _                                     _    _           _            
      | |                                   | |  | |         | |           
      | | ___  _   _ _ __ _ __   ___ _   _  | |  | |_ __   __| | ___ _ __  
  _   | |/ _ \| | | | '__| '_ \ / _ \ | | | | |  | | '_ \ / _` |/ _ \ '__| 
 | |__| | (_) | |_| | |  | | | |  __/ |_| | | |__| | | | | (_| |  __/ |    
  \____/ \___/ \__,_|_|  |_| |_|\___|\__, |  \____/|_| |_|\__,_|\___|_|    
                                      __/ |                                
                                     |___/                                 
                 _______ _             _____                               
                |__   __| |           / ____|                              
                   | |  | |__   ___  | (___   ___  __ _                    
                   | |  | '_ \ / _ \  \___ \ / _ \/ _` |                   
                   | |  | | | |  __/  ____) |  __/ (_| |                   
                   |_|  |_| |_|\___| |_____/ \___|\__,_|                   
                                                                           
                                                                           
                 BY: R.A. MONTGOMERY
                 Adapted By: Hayden Whitney and Josh Bothell

                 Tip: To best view ascii art step back from the screen and look at it from a distance.
                 Tip: Always read the text before trying to understand the ascii art.
                """)
    input("...")
    page2()
def page2():
    print("""
                                                                                              `.`-/d
                                                                                             :/sNmdm
                                                                                            sNNmMyMm
                                                                                           +hmNMyomy
                                                                                          `o-- `   +
                                                                                          -        +
                                                                                                   +
                                                                                                `-oo
                                                                                                `+od
                                                                                                 ++y
                                                                                                -s+o
                                                                                              .yysod
....                        `+o+:.`.....-.`. `.`..`odm-`                                      -+.hdh
    ..`                     hs.so```..`-...-`...`./+/o `-.                                    .o`dNy
       ```                  o//:--:..-.-/yo-.-..`.---s`   `..                   `--       ./+.`+`yNy
          .`                hy: `      . .+o+/.``   -/--`    .``                +`.-      s:-:/..` +
            `.`             o:.:s-           `:o+::-`--./.     `.`             `s`.:      :`--`.   +
              .-            s .-:-               `.-/:hy- `.     /ho.           +-`-   `.`/:.:-:---o
                :`      .```y```                     ./ym/ -./ho+hhh-..`        s:./.-.:oyh++o:/-..+
         -`  `   -`    `/+s+/:o/.                        `/y: hMN`     .-.   ://y/:++:+s/omydNdo:::+
         ``ds`    -     :``/dd.-/`                         :: `+-        `-. `+mmMmymmmdyddmdho/-.-+
          dd/      :    .. -m/-:/.                         ss-sh+....       ./sss+soodhy+/+/:/yhhhdo
          o-.     `//``s+y++myhmhs+`..-/.                 -+. :dNdo+y      .-:+d.   .d- -/.   /yys++
           :/  ```.-.  `.o+os+//     `.`-.../:ds         `-.   `yNs/+o-  :yNdydhdNN+-o  +:y`  -+.s++
    `-----+:--.`           -s.              /+--        /d/      +do+oh:.NmmdmhsMMMNy+  +/.s+-/+o:o+
    +mmNNMMMMMNNNmdhyosoo++sssoooooooossshdhdds  .s:.-.:sh:-...``-+y:o/s.smdmmNsMMMm++:/oo/so+/o+so+
    -ooyhmNmddyho+-.```             ``....:ydNN:: +:       ``..`   `........--------...-.`.-.```   +
          `:hNNmNmNho-..-+/`  `-/+- `o+yoohNmm/:  /+`          `-                                  +
           `ydhhohNMMMNmNMNdohdNMMhoshMMNmMd:    `sNysshysyohhysyo+++//::-..---::-.-..--:o/---...--+
...``...`........--/+ymMNmmdddddmMNNNmho/:+--.    yMMMNmMNNmNMmmmNMMNmNNNmNmNmdmdddNNNNmmmNNmdddmmd+
                        ``.------..` `.....   -.`./MMMNNNdNmNmmNmNNNMmdmmmmmmNNNddmNNNmmmmNNNNmmmmh+
    .:o++oohoyshysoyyhhysyo:/+ooo+o++/o+/+:-  `//+sNMNNMMMNNNNdmmdmNmNmmdNNNNmNNmmNNNNMNmmMMNMMMNNy+
          `:/:-`.:////yy+ooyssohhhsyhso++:-..` ``     .-.::+oo+/:ooohhhmmmmNNmdmddhyoo:+ooos+//oy/-+
     ...-..`   `...-:-:/://+++/::--`...-.``` ```-.--.....-...::/::.----.```.:---/.`-/://--/oss+y///+
-`..``     `.-.:--....--.....:-..-.-//--/-:/::-.......-..```.. `.-::.  `--.-...:-::-:-.--::----`-:.+
                                            .....--..                                `..-...---..-.+
                                                                                                   +
                """)
    print("""
    You are an underwater explorer. You are leaving
to explore the deepest oceans. You must find
the lost city of Atlantis. This is your most challenging
assignment.
    It is morning and the sun pushes up on the
horizon. The sea is calm. You climb into the narrow
pilot's compartment of the underwater vessel
Seeker with your special gear. The crew of the
research vessel Maray screws down the hatch
clamps. Now begins the plunge into the depths of
the ocean. The Seeker crew begins lowering by a
strong, but thin cable. Within minutes, you are so
deep in the ocean that little light filters down to
you. The silence is eerie as the Seeker slips deeper
and deeper. You peer out the thick glass porthole
and see fish drifting past, sometimes stopping to
look at you—an intruder from another world.
                """)
    page3()
def page3():
    print("""
    Now the cable attaching you to Maray is extended
almost to its limit. You have come to rest on
a ledge near the canyon in the ocean floor that
supposedly leads to the lost city of Atlantis.
You have a special sea suit that will protect you
from the intense pressure of the deep if you choose
to walk about on the sea bottom. You can cut
loose from the cable if you wish because the
Seeker is self-propelled. You are now in another
world.
________________________________________

    If you decide to explore the ledge
where the Seeker has come to rest,
turn to page 6.

    If you decide to cut loose from
the Maray and dive with the Seeker
into the canyon in the ocean floor,
turn to page 5.
                """)
    choicex = choice(6, 5)
    if choicex == "6":
        page6()
    if choicex == "5":
        page5()
def page4():
    print("""
       `o-                               :+   +-                                       :`           
         +:                              -+  `+`                                    `-oo/----.``    
          s`                             -s` -s:                                    :sdyyshhs/:.  `.
          .s                             /y. -:.                                    sMMhsso+:.   `-`
           s.                            :y` +o                                   /mMMmmdh.     .:  
           .o-                          `//  o/                                .+dMMMNhsso/`  `-:.` 
            -s                          `+:  -/`                             ../NMMMMNhhs/+/.``-`   
             h+                         .//   /.                             -odMMMMMMmyyyddsyho:`..
             ym-                        `//  `y-                             -mMMMMMMmhosyyyddsh/-. 
             yNd//:-                    `:-  `+`                             sMMMMMMNmy:/ooddydy:-  
             oMmyys+:`                  `/`  `::                            `NMMMMMMMdyssyhysshy:   
            ++MMNNdsoo.                 `/.  `-+                           `:MMMMMMMMmysyhsyss+-    
.`         `yyNMMMNhos-`                ./-   -/`                         :+mMMMMMMMNhdmmso+-`    `.
-/         .hymMMMMmh+.                 -+`   +/-                         -+MMMMMMMMd+yo+o:      .-`
:h.        `yymMMMMNmo/:-.``            .+-   `/                        `.+dMMMMMMMN+s:./.     `:.  
:ss         osdMMMMMMyoosss/`           -s.   `-.                       .sNMMMNMMMM/ :.:`     ./.   
-oh.     ```oshMMMMMMds+/+:-            /+`   `:/`                   `./sNMMMMMMMNy/+:/`     -:`    
-sy/     +ssdddMMMMMMMs:                +/     ::-`                  `+NMMMMMMMMNyoyy+: `  `:-  `   
/hyh:+osymNNmNNMMMMMMMs-```            `//     .::.                   :MMMMMMMMM/.//./`   ./` `.  ..
-+:ys/sdNNNmmNMMMMMMMMdso-`             o/     :+/                    :NNMMMMMMh `-`-. ` `-` --  --`
-++sh.:os/-ymdMMMMMMMMMd+              -o.     .o/                    /MNMMMMMN:``` :   ..  :-  --..
-///ssy+`  `oydNMMMMMMMd-              :y:     `oo.              `   -yNNMMMMMy`` `:.` -:`.:.  :-.+ 
-oooddd:     odNmmMMMMMMm+/-.```       :o:     .-:.             o-  +MMMMMMMMM/`.//:`.-- -/-  /-`/` 
:yhhdmd.     `hhydMMMMMMMmhhdhs/-`    `:o-     ++//            /+`.-NMMMMMMMMh.`+. ..//`//`  --`/.  
:syshm+     . `yhmMMMMMMMNso+o:.`     `/+`     -//-           `o./+mMMMMMMNyo.`:`  `oo`.`   :-./.   
+dhhhN:     :.`/hNMMMMMMMNm/:-.       `+::     .---          `osoymMMMMMMd:.--+  `.:s`.    -:.:     
/hhhmN+      o` `yMMMMMMMMm/   `       :o.     `+ss          -+/ssNMMMMMd`..-/. ```s/     ./::      
:ysyyydo     -:  -sMMMMMMMNy   `      -oo`     `--/.        `o-+ooMMMMMMh+hss` `/`+y.    `oo.       
/ysyyyym:    .o`  /NMMMMMMMN-  -:  `  ::/       -//.   .   `/. .sdMMNMNhhyyy/``o:++o     /:o        
:yyhyyysy-    -+.-/mNMMMMMMho` `+     -+-       `:-.  --   /-  /yNMMdhshdhyo-`++/+s:    +-o-        
+mhyyssmmm     y++yNNMMMMMMmm+  +` `-`:/-        -/+` +`  :+` -/mMMNs+hddhNs`+//os+    -oy/         
/mNhssdhym: `` o`sdNmMMMMMMMMd+.-y `+//:.`` ` ` `:+o/+-.`-s+--.+mMMo+ddddNs+++h/o+-   `/so`         
:sdmyosyss+  ` :-+hmMMMMMMMMMMNyhmy+syos:-.` `.-.:oo/-..-so..-+hMMMsyy+sdm:/hsooso    +/..       .+-
/hhdddhdyhd` ` --:smNMMMMMMMMMMdhdmhh+::+-`.``-::-o-oy++oy:.-/mNMMdshysyd/+yodhoy`   /s         -ss:
/ydddmmhssh-   `s`oyNMMMMMMMMNMNddmmd/:+s+oo++oo+so::+::hy/::omMMMmdhyhmooysyyys/    /:       `:+oy:
:ydddmmdysd-    +::hmMMMMMMMMMMNdhmNdo::dhsosyyhdNd/ .ydhs+oomNMMmdhydmmhdysyhho`   .+     ` `oshhs-
:hdhyyddhyd-    -+/sdMMMMMMMMMMMNdmMy: smmmhdhyysyds--yNmsyhdNMMNhhdmmmyyhosshs`    s.      `+oodys-
/dsshhhddddo    `h.sdMMMMMMMMMMMNmNNs.+dsssosssydNmy+/oNdmNNMMMMddmNNNddddhddo-``` -/   ` `.ohhmho+-
/ydmmdhdNNdd`   `+./dMMMMMMMMMMMMNMh--+hsoo+oo++ymy+/`/hdNMMMMMNddmmNNdymydmhy``.` s`  ```/hyyyyhss:
/hdsyhsoyddd` `.:so-ymNMMMMMMMMMMMN- :oddoos/++sydho-`-hNMMMMMMmmNmddmmmdhhyo.``  //   ` +yhhhhhs+- 
/hyo+o+ossdm:`..-ydoohmMMMMMMMMMMMy`  /odos+/::sdohyo..+NMNMMMMNNMmmdmdyhyoo:    .+-  ``-sdsyydo.   
`sysyysssdhsd/`--/sdhmNMMMMMMMMMMMd.`/hhdh//s/+ydodhy+.:NMMMMMNNNmmmNdo:+o+/     +/. ` -hddssys  .:-
 .hhhhdyyhsmyh+`:oymmyNMMMMMMMMMMN: `sNmNmyhho+yhmdmm/ `dMMMMMMMNmNdhy++o/+ `   `o/  ``oohyoos` :/.`
  -ddyhyhhhNhsm/syddmmyNNMMMMMMMMm:` sMNmMmdddmMydmNN/` -NMMMMMMMNmhdyhsoo-    `+-: `.o+sodss. :o:+:
   /NdmdhhhhNdddshhmmNmmMMMMMMMMMy```hMMNNdhmyNNmmNMMh-  sMMMMMMMMdNmNNdd/   ``-o`...oo+yysy. /ooy- 
   .dshsyshyhydhyyshmNNNMMMMMMMMm.  -NMMMMMNNdMmMNhyMN/` `mMMMMMMNNmNNmNm.`````++-`-oooyddh- .s+o-  
  ` shyooooyhdhoohhNNNNMMMMMMMMMy  `yMMMMMMMdNNMmNmoNMh.  yMMMMMMmMMMNNNy` ``.+/-..ohoso:s:``s++-   
``` .yhdhhhdhmdhssmdmNNMMMMMMMms+  /MMMMMMhyso+++hMMMMm+..yMMMMMMMNMMMMds`.``s-.:`+hs+sy+:  +s//    
`````ydyyyhhmddhoodNmMMMMMMMMm:-  .yMMMMMM:.----`+MMMMy/.-.mMMMMMMMMNNNho:``-y...+syyo+o.``+yho     
`   `.dyshhNmmdhhhdNmMMMMMMMNo`   hMMMMMMm/ymmmh.`MMMMNh`  syMMMMMMNNNhsy:-./++./sh+sso.  +-.:      
  ````oyoohNmyddmdddmNMMMMMMd   .:mMMMMMMh-omdhs  dMMMMd.  .hMMMMMMMMmhho+ooyy.:sss/+s.``/:         
    ```ddhhdMNmNNmNmNmMMMMMMm   :hMMMMMMMo`o+/-d  +MMMMM/  ./yMMMMMMMNdmysooo:.ssyooo: .o:          
..-    /hhmNNNNNNNNNNMNMMMmyh. ..osyNMMNmo/yh:oho+/dmNhoo-.`.+oyNMNMNNMdhos-o`+oh+o++` /y           
  `-` `-NhddmMmmNMNMNNNNMy`     ````-/+::yddhydmdso/.o-  --.    :mNNNNMddos:o+yhsoso```h-           
   .::/+dysyhNdhNNMMNNMMd`  .```      ` ``:::o/::-`  `     .  `` -NMNMNhhhdydho/oyy`  -s            
   `.so:sdsyhmmMmNMMNMNN.               //`` //` `-.              +MMMMhsdhhdhs+od`   o.            
   ` `+..hyyyhmNMMNMMMmm`                `:-:---:``               -yMMMNhysdho+oy/   .o  `          
.:---:/s.:dshyhmMmNMMMNy`                  /dyss.`                `hMMNhdysmssmdo    h` `           
-o++/++ss:yddssyNmMMMMMMo                .os.`.:s/                +MMMNNmsydyyys  ` .o.             
.-:+/---hyomdyhhddNMMMMmMd/             .:y-    +y-`           `+mMMMMdNh/yysyh/ `  s.`` `          
        -s+sMhddhMMNMMMNhyNNhs/:-.`````:++..--:. /+.       `:+hNMNyNMMMNhhhhyyds/::/s.-`.`          
.:       o+hmhhhmmNNNMMMhs/+yNMMNddhyydmms  `-`   dhhyyooymNNNmhsoydMMMNyyhs+yho+:-h` `             
 o-      `s.s/h/syhMMNMNms/o+o//yhmMNMMMN-` `` `  -NMMMMMmNyysso/+hNNNNmNdy+os:--:/o                
 `o`      :://ssyhNMMNNMMNss/yo+o/:/sdNMo          yNMhsyhy:oys/+omNdmmoshy:-+`.-:y-. `             
  .o       yo+/NdmmMMNNNNNoo+ssshy::/yhd.`         `hdyyyhddyyy+odmdmmydyhoyy/ ``s/.--.             
./:y/-..`.-o-:sMNmmdMMNNMNd+o+dhhs/-+yy/`  `   `    -dhyhhhNhyssdddhmm-//ms/y:``.h`--:.`            
+hyymo:/+/-`s+shmy/+hyhmmNNdhshhy+::+ys    ``        +shyhhMdddysssy++:-:hhh+./-:+` ``.`..          
-yoosd`.-``.syods`-:sshhhdmNNNmhdsssdm-     ````     `sdmNyhNNmso++my::::hoys `:h` `   `..``        
 `os+os```.-shsh` `.++o+/+hNmNhyhsodMh.`.` `.`-``..```-NNMhmmNNdyyhdhyo-oyy+-/.::+.      ``..       
   :+-/:``./`+/s+s`./:``./+dmy++ooyNN.     `.::`       +mNNmmmmddymy:/s+ssy/`.o/ `::`      ``.`     
  `.-/`y.`...`////s- /` ``.+dysysydmo        .`        `ymNmNmdddydd+/hds+/--`o-/.`./.`.     `.`    
 ..  o::o  `  .+--so.--  :+ydhdsoyNd`                   .mNMNNdmNmy++hhhdo:.-// :.: `:sy:`    ``..` 
``  ..o`h```.-`-+:+/o..:.+odyhd/ydm+               `     /sddmhhNmh//yhmdy..:y.  +-:`-yy:..:`   `..`
  ``  //s: -:...s+::++.s`/o+sysodmh.                      +sosyodNmsoyydy+/.o/-  :+/``/-hyso-     ` 
 `. `  y.o:::-/:-+o--+h:/ooosy/ddm:                       :+/o+-ymmdhdosy:/s-.:..++ys/s-ddds+       
`` ``  :/:h::/:--:o/+hd/hssshosNmy  .`                    --//+/ddNmdd+ss/+h`.:+/-.ydyN+:-+hh:`     
  ``    yodsss+++/:hdNyyysyhysdmN:  `.           -.`     .  :++ymdhyy+ :/+o/: :h//.-:ydydh+-:o/.    
 .` `  .sddNdyyssoyddmymsddhydmhy`   -  `+`    `:s+-        `:ommdyod+.`:/s:/: +/y/`   ``    `s/-   
`     .:-dmNyoyhhhddmddmmmdyhmmm-`.  .`        `:::          .oyhosyhs+`.o+/-o`.ho:.           ::.  
  `  ::.:++:m+o-+oy+myNNMNNmmNNs  :   .        `  .    `      /o::.yoo/:`o://:: :o.:.           .-.`
`` `++./o/.-:d-::o-:/hydNMMMNmm.  .`  `               `    `` .//-o//++/::::/:--.+/`:. `      `  `-`
  `+/-:+/...+/yoo:..:hymmNNNmh+    `  `.              -  `.. ` .:o/.`++o+-:::/:/.:y/.o.`-   ` ```  `
 `o/./++:.-/-.:hs`..+NhddNNydy`    .   `---           .  :      :/:-``++o/:::/-:/`oy:-/..:. ``:---` 
`o+-/+/:`-//`.:-y+/sosdsddNyd/     -`  omdNs         -  ``     .----- -+oo.::-::---oo.:/:-/-``-::--.
:/-/++:`/-o`-`.+/m+:-++yydhmy      `- `odyhy+        ` ``     .- .:.-- /+o:---./:` /y/:/+:-::.`.---.
.-/+//`:-s`:`:-/-:y.-:.dhhyN/       - ./s:/+s`      `--`      -   ---`.`+oo.--..-` `/s:-/:--+:.`:::.
./++:.--s.-  `///-do:`:oy:yo/.      .` --:.`-:     ..`       `-   `.--  -+oo`-` ./- /o/:://:-+---::.
-/+:-/:o--`   `   -d.`-:.ss-...     `- .  -  `    ``       `.-`    .-..  :+o/``  //:-/:-:-+:/:+/-/:.
.+/:++//`-        -/+`. `/:  `-      :           `-      .`         --`   oos.    /:/:/.//:/:/://:--
                """)
def page5():
    page4()
    print("""
    You radio a status report to the Moray and tell
them that you are going to cast off from the line
and descend under your own power. Your plan is
approved and you cast off your line. Now you are
on your own. The Seeker slips noiselessly into the
undersea canyon.
    As you drop into the canyon, you turn on the
Seeker's powerful searchlight. Straight ahead is a
dark wall covered with a strange type of barnacle
growth. To the left (port) side you see what appears
to be a grotto. The entrance is perfectly
round, as if it had been cut by human hands.
Lantern fish give off a pale, greenish light. To the
right (starboard) side of the Seeker you see bubbles
rising steadily from the floor of the canyon.
_______________________________________

    If you decide to investigate
the bubbles, turn to page 8.

    If you decide to investigate the grotto
with the round entrance, turn to page 9.

                    """)
    choicex = choice(8, 9)
    if choicex == "8":
        page8()
    if choicex == "9":
        page9()
def page6():
    print("""
    Your sea suit will protect you from the intense
pressures of the deep. It is a tight fit and takes you
some time to put it on. Finally you slip from the
airlock of the Seeker and stand on the ocean floor.
It is a strange and marvelous world where your
every move is slowed down. You begin to explore
with your special hand-held searchlight. You
examine the ledge by the canyon.
    Suddenly, a school of bright yellow angel fish
dart by, almost brushing you. What made them
move so fast? Are they being chased?
    Then you see it. The Seeker is in the grips of a
huge sea monster. It is similar to a squid, but it is
enormous. The Seeker is just a toy in its long,
powerful tentacles. You seek shelter behind a rock
formation. You know the spear gun you carry will
be useless against this monster. It looks as though it
will destroy the Seeker. Fish of allsizes huddle with
you in an attempt to escape the monster.
______________________________________

    If you stay hidden close to
the Seeker, turn to page 10.

    If you try to escape in the
hope that rescuers will see
you, turn to page 12.
                """)
    choicex = choice(10, 12)
    if choicex == "10":
        page10()
    if choicex == "12":
        page12()
def page7():
    print("""
``````````````````yNNNNNdyysyyydmmNdhyhsydhdNdyhmmdhmmmhho`````````````````````````````````````````:
                  yMMMMMMMMMMMMMMhdhshdyhdhhNmmhymdddhmyy-                                         -
                 -NMMMMMMMMMMMMMMNhmydhhshNMMNNmsysyhNh:.                                          -
                -mMMMMMMMMMMMMMNMNMMNNNNMMNNNMMNNmhydMh.                                           -
               /NMMMMMMMMMMMMMMMMMMMMMMMNMNMMMNMmNmhmMo                                            -
             `sNMMMMMMMMMMMMMMMMMNMMMMMMNNNMNNNMNNmNNy                                             -
            -dMMMMNMMMMMMMMMMNMMMMMNNNhmmNMNmmmdmNNmm-                                             -
           /NMNmNdhNMMMMMMMMMMNNMMNMMNNmhmmmNmmmNmNMs                                              -
         `:ddo-/sydMMMMMMMMMMMMMMNMddyNMMMMMMMMMMMNm.                                              -
        .:sdmyhsdNMMMMMMMMMMMMMNMMNmmsossmNMMMMMMMd.                                               -
       :my/ommdmdNMNMMMMMMMMMMMNmNNNMdshsyooodMMms.                                                -
      /NNysoyhyysMNmMNMMMMMMMMMNNMhyNdy:/.   `:-.                                                  -
     /Nhymdyoys+ymdmMNMMMMMMMMMMMmhhdo` +`   `..-``                                                -
    :dyshyyy+soyNNNNNNMMMMMMMMMMMNdy-`. +. ` /h`s/```                                              -
   .soyoydsoo+:hMNNNddMMMMMMMMMMMNyho``.:+-``hNsmm-`.```       `-                              `.` -
  `symmhsdds++/hNNdddmmNMMMMMMMMMNydNo.y/s//hNMMMMd/+```/` ````                                 `  -
  :mNNdddhoo+++/ososssyyhNMMMMMMMNNhyhmNhhhdMMmydMNmy:/yy...`                                     `-
  `osyys::yoo++-/+/+y+yo+sms:mMMMNMmmNmNNNNNMy-..NMNhhy/:`` .-                                 -`..-
     `````.` ```..`.--....`  -dMMMMMMMMNMMMMMmsmdmhsd+/` ``. `.                                -.. -
                              -mMMMMMms/hMMMMMms::.:/+o/.`--  .:                                `  -
       `````````               oMMMMNo-./MMMMMs/--.``.-...-/:.`::` `...  .` ` `                    -
 ....-..----..-:..-............+mNmmmydNNMMMMMs-.--...`...-.-/:..``.........:----:::::...``   ` ``--
               `.`.`......````..-hmmNMNNMMMMMM/ `--:::`.--:`  /::-          ```` ```.`````...`-.+hs-
`.-...`..-.`...-..``.--..-.....`.sNmmmmdmysysso``.````.-:/+:/../-:....``.`````...````.-...:osyhy:..-
`...```  `        `  ```.--.:...`/mmNNNNNhmddNy:`  `-://--:::``.os-```.`````````.``...```.`-`` `   -
                        -`-  .-:  :NMMMMMNNhsyNs/:`  `` `  .-:o.++/.                 :mddh+`..-..  -
                        ..`+/`.-   -mMMMMNmmy+hmmdh:++::s:-.-`` -o/-.               :hmNho-        -
                        -`-:+.-.   -:dMMMMMMNmdhhdNNMmNNmNNNNysssoo+/`             :dMNN+`         -
                        `:-.:o:/.  + -NMMMMMMMMMMMMMMMMMMMMNMMNmhh/`.-            `yNmys`          -
                           -yo+ys+-:.o.sMMMMMMMNMMMMMMMMMMNNNNNdys/-/`            /mNhy.           -
                     ..::++ys+yyh`+:-.  -sNds/dNMdsMMMMmNMNNMMMdmmms-/           :ymhy:    `.`     -
                `-+oyhmmNdNNysmmyshNo/ooyh+:sNNdN`sMMMN+-mMNNMMsdmMMh+          /hhms/    .`.      -
             .//ymmdhoo/d+yymossmmdMdoho/:sddmNMs.dMMMN. -hhmNhoyssoo.`..``..`-oyhmdo     .``      -
            osyhy/:.`../dodohohyooysdyMddNmmMMMN-ohmho+.```````  `.           `.+/:-....```--      -
          .yddd/```-+ymyy+.oy:`.-:::odhNy+/mmNy.`:s+-                ```        `         `...-..``-
 `.````..`+hyy/--.:/:::......` `-oo+/--/- +hdd+`-++:`        `-.`.`           `             .--``..-
 ``````.-..//o//:....---:oyoysssh/.-o.s-/:+:::--yhs:..`..``.``.::-..    `` ` ` ``` ```.`.:-.``     -
 ...`   `  ````` `-/oyyyydmdNNmNo/-`sohddy/ `smNMN+.  .///:+:`.dmyo:o.``.`               -.`       -
               :sdy+:+oo/s+o/+ssyhmhhdhmd:.:+MNNNh...::-.`yNN+.:sydh:                    .:-       -
             `hhys:shNMMNm+-.:o/ooyhhNdhyo:omMMNdNs.:omh` :yhyhmNMMNo.              `.:/oo-.`      -
            -ddo:-+mMMMm+...-:.`   `.+mMMNmNhdNydMM+:/yy+sdNNMMm:hMNm--`           .:ossdhhs`      -
           -d+h:`+mmdmo-.+`+h+     .syNMMMMMNmdhNMMN++hNNMMMMMN: `oNMds-`   :/:  -//.  .---sy/.`   -
          -d+o: /hmhs/  -- :-      ymNmMMMMMNMMmymMMMMMMyNMMhNNm+` :dmNh-.  /+:/yh/`  `:`.``:+sssoo-
        `:doo/ -dddo+  .-       ..-sMNMmdNMMMMNMNmdMMMMy/dhyy+mMm+. .dmNs--  -+/-`    `- `   `.-///-
     .-/hmyo-  smNso` `:    ..:///--hNMhhNMdmMMMMMmNNMMmdmN+:osdNy+` -mNNs+`        `.-.         ` -
 -+oyhhyyo-.  :hNhs: .:``.:/::.:mm::.mmsNNdsMMMMMMMmodMMMNds++somds/  sdNh/.        -+/.```.``     -
.syoo/-.`    `sdmo:`::::/:/h+ `.osoydNNmmdmNMMMMMMMMMohMMo```  `ydyo- :hMNy/    `...oy+//+yso:::..`-
`.`/:-o`    `ohmos-+++oo. :hs:/ydNMMMMmmdsdMMMNMdNMMMNysh`      so:o: .shdmy    `.`./s:-shys+oo/::/-
      y+    ohhs+-o.:.dm/:/oymMMMMMMMMdmNomMMMhNNMMMMMNy+/`     //:s: ./sNNs  ``.---://:/+ssyyssyoo-
    `:h.  `+dmo/` `/-:/shmNMMMMMMMMMMMmNdhMMMMMMMMMMMmNMdo/:````+ssd/ /smho-:-:-..`` -o:/::/yyyyddh-
.s++s/`  .yhy+:`   `/-++////mNmMNMMMMMMNh+NmNMMMMMNMdo-yNNsh///sydNh..sos/o: `.-..``::```-/:ohhhhhs-
 ..`    :oyo+.           ::`ds/mMNMMmhdNMNNmNMMmNmhy:`  .+dNNmmmNdo-./hsNMy ``:oo+-./o-.  -osyhhdhs-
      `+o/+-             ./:-oydMMMh`  /dNNNmdyoo+-`       .//+/:` `/ymNMd...`./-:---o:..` ohydhdy+-
     `ss/+`         ``.`-/:` `yhNMd/    /+...`               `..-++odNMMh+/.  `o   .+++::.-shddso+:-
     hh//        `:/+++:o-    shmMy-    :o/`               -yhhddmNNMMNmos:.-.    .+ssh/- +yyhsyo//-
    /m:o        `oo+`         /NdMd:     .+o+:/.``       `omhNmMMNMNhhhsh+-:-.`:s/sNMdmd. -hhysyo:--
    dh+`        +s+            yhmhy.       .-shso:.     .yddMMMy:-` ydhyymNNyyhNddmMNNy` :hhyyyo. -
    mh:        /sy`            `ydhdy:`        `-sNh-    -dydNMs`    +hh:yNNMmNmhmhNMMN-`:yhhydso` -
    sN-:      -sy:               /ddooy.          yN.    -dydNm:      --sMmmNMNmhmmMMNs :+sydhosy: -
    `yMo:/.`-+yyo         ``      `smhos/         -My``  .yodMd-    `/ossshmmdyhNhNMNhy::/ohsssyos.-
      /hd++yyhy+      `.--.`        -myos+        `NM:-+:oyyNMh`    /+.`-o+mdy:odNhohyo``/:oyysoo+--
        `-/+/:.    `-//.             :Nyoh-        sMh+-sydMNd.    -ys/smhshy+smms/.mN+. -//syyso+--
                 `//:.`               dddy+   `..`  /hmNNmdoo/`  `sysyydyNdy/+ydhs-hMNsso+-/+ysy++--
             -oydyyy+/.               ydmd- .o.`+d+   ``.`   ./+/sshmmhmMms::m+Nh:ohmMNNhyso+oys/+--
          `-shhddhhs:`                dyNh` -y//dmy         `.::--/mmdNMds/.dhso/oMh:yNMd` .++oy+:.-
   `-::::/syyy+/--://:/:-.          .sdNd:  `y.ss:+`--.+++/soohyddy+dmdNhy+odNd++Nh`  -hysyyooso//:-
 -:++//+syys//:os+-.````:/so/-```-:ohmmh:   .s/o+   /.-oyhhdmdmNMMMyod+y+-shhhy/sd.    :hmNmNyhhs+/-
`://+osyy+-`.-ss`         `-+hdmmmNmds:`    .s/.hy+.://+///:::-.:hMhhs/-`/MMNh/hh.     `odmdMmdy+:.-
.yyhdhhy+//-:-sy. `          `.-:-..`        o.:dd+            +y:h/Nmmy+oNmyssN/       sdmmMmy+:. -
.yhhyoosoo/-:::-.`                           /shhh/         `..-odsoNMhymMMNhsyy:.--./+ +hNMMhs:-. -
.hhhhyyyys++++o/----:..` `        `/:..``.``` ```         `:....:/ymMMNdMMMs+Nohs+os/s. +shNms+-`  -
.mhddddmdhyyyhhhhhhyhyyoo//:.. `  //-:..`.--:           .-.://ohs-oMMMMMMMMmy/:s/Nmys/.`+-ydmo/.   -
`:/+sddddddddddhhddddydyhhoss+-`  +ysy+::-.:/-        .....:hmMMy+dMMMMMms+-` `::NMNms:/-/sdh++/`  -
 `.://ssddddhdhyysydmddhhhyhhs/`./sodyo++/sy/o+-.    +/+-+ydmmhhymNMMMNs`     -.`mN/++sso:shh//-   -
`::::::-:::++//::/+hddhhdmyhsyo-o+/./yhhymmmmd/.`   -y+:dNNs-.:/dNNMMd/      -` /d/ `-:/yh+oso/.   -
`--.`.::://+++++++ymdmhhsyhyys/.` .-:-./ohssd+-     :/-oNMm.`/sdMNNy:`      ././m+`  `-yhhmo:+/`   -
    :+o//+ooyhdhhhhhdmmmdydhhs//-`-::--...  -+.     /:-hNMm`:yNNMMm-        `:hmh-``:+sdhsoso` `.  -
    `:-..:/++o+syyddmNNmmhdyhs+/.`  `--.``.`       `s:smMN/ .:MMMmy//        `:--/+oo+o+:`` oho. .--
 ```.::::///o+:/oshhhdmdmNmNhhs//::`..-+/` `.`--   -h/ymNs   `hmds`.--     `.:/o/:..`.`      yMh+o:-
`-://///:///+/::::/osoysdhmNNNNmhho/o:` `.-.` `-`..+/oyNy`    `:+dy-.+/``.`.-.`              `yNd/ -
       ``    ``````````-::/ooosdddmhyyo+/:..-::...``..-/-...``  `:odhdho.`                     ohs -
  ``` ``                       `:/ohmoo//sdds+:-:/++-:.-.````-:/+. .hNdys+/-                    .+:-
  ...`..```.`..-.-...`` ``    -yhhdddso+/ohhyyddyosoyNd:::o+ooso:-`  sMNmNMN:                      -
                    ` ..--:::://+ooyhmmdmdhh/.-/ys//MMs.````.:``/-   `smMMMM+                      -
                              `.-::/oooohyhhhhshNNNNMMNMmdyyooo-.``   `dMMMM+                      -
                                   `.-:.-:/+++sdmmNNMMNMMNMNNNNMdyo/.``smMMMo                      -
                                       .::-.-:--./+/+osyhmNNmddyoyyyys:+odNMMs/:-.`                -
                                          ...---:.---`    `.--:/---:/oossmMMMmyyyoss+++:-`         -
---------------------------------------------:/:/::++///:-------------:/hNNNNNsooososysossy+o/-----/
                """)
def page8():
    print(""" 
    Carefully, you maneuver the Seeker between
the walls of the canyon.
    On the floor of the canyon, you discover a large
round hole out of which flow the large bubbles.
The Seeker is equipped with scientific equipment
to analyze the bubbles. It also has sonar equipment
that can measure the depth of any hole.
______________________________________

    If you decide to analyze the bubbles,
turn to page 11.

    If you decide to take sonar readings,
turn to page 15.
                """)
    choicex = choice(11, 15)
    if choicex == "11":
        page11()
    if choicex == "15":
        page15()
def page9():
    print("""
    You pilot the Seeker through the rounded entrance
to the grotto. Once inside, your searchlight
picks up what appear to be docks and piers along
the grotto walls. The Seeker's searchlight is not
very powerful. However, you do have a special
laser light which would light up the grotto like
daylight. Unfortunately, the laser light can only be
used twice for very short periods before it must be
recharged aboard the Maray, now more than
2,000 feet above you on the surface.
______________________________________

    If you decide to use the laser light,
turn to page 16.

    If you decide to cruise further into
the grotto, turn to page 14.
            """)
    choicex = choice(16, 14)
    if choicex == "16":
        page16()
    if choicex == "14":
        page14()
def page10():
    print("""
    The giant squid tosses and turnsthe Seeker, but
finally the creature growstired of its new game and
jets off with an enormous squirt of water. You now
are free to leave your hiding place and examine
the Seeker for damage.
    To your dismay, the airlock entrance has been
jammed shut. You are locked out of the Seeker.
The crew of the Maray, however, suspected trouble
when you did not respond to a routine radio
check and they are now lowering an escape platform
to you. Once on the platform, you radio them
to start the slow pull to the surface. To avoid the
bends—rapid expansion of nitrogen bubbles in
your blood—they will have to bring you up very
slowly.
    Just as the platform begins to move, the giant
squid suddenly returns as if from nowhere. It is
headed directly at you.
______________________________________

    If you decide to fight the squid
with yourspear gun, hoping to scare
it off, turn to page 17.

    If you decide to signal Maray to pull
you up at top speed, knowing you will
get the bends, turn to page 18.
            """)    
    choicex = choice(17, 18)
    if choicex == "17":
        page17()
    if choicex == "18":
        page18()
def page11():
    print("""
    You squeeze into your sea suit and, outside the
Seeker, you use special equipment to analyze the
bubbles. As you work, you clumsily knock against
the valve that dumps the compressed air necessary
to make the Seeker rise to the surface. There is
nothing to be done about it; so you continue to
analyze the bubbles. They contain a high percentage
of oxygen and no poisonous gases. Perhaps
they are coming from some area below the sea
where human-type beings can live and breathe.
Perhaps they are coming from Atlantis.
    You wonder whether you should try the
Seeker's drilling arm to enlarge the source of the
bubbles so you can explore it with the Seeker. But
you are also very worried about the Seeker's loss
of rising capability. You might also be able to trap
the bubbles and use them to raise the Seeker.
______________________________________

    If you try to collect the bubbles
coming from the hole to fill the tanks
of the Seeker, turn to page 24.

    If you decide to drill, turn to page 22.
         """)
    choicex = choice(24, 22)
    if choicex == "24":
        page24()
    if choicex == "22":
        page22()
def page12():
    print("""
    Moving cautiously, you climb up the sides of the
canyon hoping to reach the ocean floor. You leave
the Seekerin the grips of the giantsquid. Your plan
is to signal for help with a dye marker that will float
to the surface and make a bright yellow patch in
the water. The crewmen above have been instructed
to watch for such emergency signals.
They will send help.
    Once you reach the ledge above the canyon
and feel slightiy safer, you see the most feared of all
sea creatures— a huge shark. It begins to circle
towards you and you know that you are its target.
You wonder whether you should fire your
emergency propulsion charge that will send you
rapidly to the surface. The shark is fast; he might
catch you anyway. You also know that you will get
the bends from the rapid rise to the surface.
______________________________________

    If you decide to fire the special
propulsion charge to get to the surface,
turn to page 21.

    If you decide to wait quietly
hoping that the shark will go away,
turn to page 19.
         """)
    page13()
    choicex = choice(21, 19)
    if choicex == "21":
        page21()
    if choicex == "19":
        page19()
def page13():
    print("""
                                                                                                                                                                                                                                                             
       `/                                                                                           
      ./h.`:                                                                                        
     `do--::-                                                                                       
     .soy/ssy.                                                                                      
     -mshs+msdso:::--``                                                                             
   `:hdsdysyoNhNydddd/:-                                                                            
 `/hhyNmdddmddds/+/+mdd-                                                                            
-ydshmNMNhyy+yho``  sNo`                                                                            
-hyy/.:NMNdy//NN/:  oo/                                                                             
:h:`   -mMNo-mmdoo -+o:                                                                             
:+     `sshoydyooN++d-/-                                      ``                                    
-:      :sdmdo/soos-:://                                  .+:+o/                                    
:o`     `dMMMNNMhyNs-+:`      `   `  `` `..``````````   .osy+++/                                    
:yyysossyMMMMhMMM: -so+o+o+osssso/o+++/////:-.`--....``+shos++/o` ``                                
+oyhooosdMMNoyssmN/ +myhysooooooo+//////::------.....-hhhssy+++:`````-:-.`` ``....`..-.`...`.`      
.:/o++++yds+:+/+oos+-//:::-..---:..-----`...`.------::-...`   ``               `..``.`` ....`..-.`` 
/o./:```sMN+d/...` -mdo+oyso::..                .:oooo/syhhhsss:.....   .....` `                    
`  `h`  oMmhM/      .dNs++s/-      ``.`-``.--.-:/+o+ss+yhhshyoso                  ::-::-``:o/-`-:.. 
``.-:o. .:syo: ` .` `.syo+s:-:.-`..```               `.:/++osyhN:                 :-`.--.`/+.::.:-:`
`.--.-s/--yyy-..-``..``:ho:.               ````    ``````.----/+o/...``````.``````````````.-.:-``.. 
      `o`:NNM-      `.-`             `-`` `                   `  ` `.--..``  ``.`--........--.`-..` 
       `-oNdNo    .-`          `:/ohdshyyyy+s+/-`                      `..`..```                    
         ..`.`  ```           ``..`.--...```````                              ``.``.``       ```-.. 
               `.`.-/+oysshhdshmmhhdddhy+ys+++-:--:::-.-.```   `                      ``.-/ossyysoh.
               .+hmmmmNNhhhdmhNNdhhhmddhydNmddymhdhhhydyyhhsoo/+///:./....`` `  `         `--oys+hN`
`:./:     `     `:yNNNMNmmmydyNNmhyhNdhyymdhdmhMdmdddymyhmdhdhysooyososossososyyssss+++/---....-.-:`
`-..-` :-.:..      .+hNMMNNNdmmNNNmmNmddsmdddmhNNmNmhsmddmdhdys+s+osyoysossyddmNNNNNNNNNmmmmdmhmdhd.
       o.:+/.        `-+hmNMMMMMNMMMMMMMmMNNNNmMMMMNNmdhss//:-......-.::--:/oyNNNNMNMNMMMMMMMMMMMMM-
       ./o```            .:sdMNNNMMMMMMMMMMMMMMMMMMMMMmmmmmmhys+-.`         /NMMMMMMMMMMMMNNMMMMMMo`
         .               `-odMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdo:`      /NMNNmddhss++:--:hNMMM/ 
                      `:ydNMMMMmmmNNMMMMNMNNNMMMMMMMMMMMMMMMMMMMMMMMNdy/.    -+/-.`          `-odNh`
                   `-odMMMMMMMNNMNNmdhso/:---:+osshhdmmmmmNmmmmmdhmMMMMMh-.``   `...``           .:`
                 .odNMMMMMNmmho/:-.`                 ````...````  .omMNo`  ```..``  ```...`````     
              `:yNMMMMNmy+-``                                       -y-         ```.`.````````..... 
             .hMMMMNh+-`                                                             ``.`.--......- 
            +NMMNd+.                                                                                
           .NNd+.                                                                                   
            .`                                                                                      
                                                                                                                                                              
        """)
def page14():
    print("""
                                                                                        
                              .//-:::/.                            `hhhdhhhddddddddhhhysyyhyyhhhyssh
                `.`            `:::-:+ho-                           .+hydNNNMMMNNMMMMmmNMMNmmmmdmhhm
                -:-::`           -/-:/ohy/.``                        `-ydNNMNMNNNMMMhdMNMMNh+ossssyy
                ::/-s:....`````.::+-:::::/::-:.......```````````     :yNNmdMNMMNNNNNhymMMMMdsssshyyd
                :.:.:+:  ```..-:..-:/:-/-:-::-:oys/--.--......``   `-:shNNMMMMMMmhdN+`/NNNNNhoohhhdd
                -:+/`s:.   `----` ..--`----``+smoh/:`    ``..:+////+o+sohMMMNNdyd+my  `yNMmdsshyshdy
                 :/y+:o:.-oo.`.--.:---.--``-./mNohs:-.---:///o+-:++osmNNMMMMmyyNs+h:   .NNMNsyo+shss
 `.````          -+yo//ssmN+--.--`/-.:..--`-``/s+/-./-+sssso+oo++++hNMNNMMNh+yd+/hy     +NMNdyooyosy
 -syhy++++`  `.../+s++/yMMmo:/-`:.-o-++:/-:--:+``/-::`os+++/-::-./yddmhNNdy/ho-`+//     .mmNmoohhhhh
 omNN/ .:/.``:++/odhNNdNMMMmhsoo+osoossyoo+syy+/+ssso+++///::.. `s:.`..++h:ys- .:-/     `NNMNyssyydy
 yMMh .:o+y///--::s+yhohsdhdo++o:+o+s/o+oo+sy//+soyoh/--` `     ``     `hohhs/ /yh+     -dNMh+/yyhhd
 yNNy:  -..`     `--:://-.yh/s+s++ss+-o-`--/o .o:.h.   ``.-.-..`......:oyoh+`s+/sdo `   :dNm+ho+/sss
 yM/+:- .. :    `.::o/oo../hy+yddhdhhoy-:osyhsy:s+y/. -/.o/:hys+oo+++/+so+y/ /hyo+o..   `hNydd//ys+s
 sh`.:/``` .`   .::o-+/``-+oyshmmhhyyy/odNmmdd+:o+:.` ++os+/+sysyyyssoohh///`sh``oo`    .mmmhy+yy/+s
 .   -:`    :````:.-:/   +o++ohydo/:/-+dhdhhss+/-.----:+::+oys+yddmmdmy+:+-/oy` `yy-    /NNNNodmhoy+
  --  `- `  :ysooyo///-.-o///--+/-.--:soydNhh/`..`.-.-::-.-:/+/++hyhhh+.  //o:   o/:    /NNdhyhmyo+/
 -/s/  -.`  `yosss///++o+oss+syoso+o+:-:ddh/-...` `          ``-+oyhyy-    :+/-  o/+`  `oyyh+oyo+hNM
 :/o/.---`/:`/mdhhysssoo++++syss+ooo++++yyo+o+//+++o++//++so+:::/+dddho-    `/o+:/od/   shmdyydNNNNN
 :/+.   -oys `mmmmmdhdyss+//-/+++/+osooo//o/:::/+o++/:-+o+/oo+s++oys:+hho-     :/osso: /mmNNMMMNhdNh
 /++/+/:++o+.-oNMNNmmmdmmmmmdmdmddmNmNNs++sssyssosssooooo+oysoysss+dmy+/dho:      ./+syNdNNMMNmmmdhd
 `.....--.....-/syddmNNNmmmNNmdhhdhmhmsso///yhsys::::.-:-++-./://oyyhmNmsshhy:`   `:shhhmMMNNNMNdmmN
     `` ``           `.-:+yshmddyhhhyhshyohyooshmhhymh+yyso++++s+/hyoodMMMyoohs/smmmdoydNhNNmNMMmdmM
 /:--+.:+:.                 `.-:/+os/+dmmmddysdmmhyhddhmhysso+yyosmmmmdmNMMNymddddho+++yNmNMNmNdmNmd
 o+:-+-://-                     ``...-+oydmNmmmmddNNMMMMNdssdydhsomNmMNNNdhhMMNmNmsyyooyohNmNmmNmmhm
 ` ` `                                 `.--:+yhdmmNMMMMMMNNmdo+oshy///+++o+sNMMdd/ysmmdhoshdddhossyy
                                             .::/oshmMNdydhhoyommmysso+///+dNNNd+mmyhyssohys+/++ys+:
    ```   ``   ```````    `` ``      `` ````   `````.:yydhyhhyysssymhh/-soyNdddmNNhhhhhssyysoooss//:
             ```.`....   `.``` ``````````....` .---.-:--/ohsso+osssyddyoooyhhydMNsyhyo++oyyhyyyhs+oo
                    ` ```.```` ``````    `   `` ````...```...--.``:so:.`.`.+mmMy.`./:--:/++++sssooos
   `` ```.....-```.````..`.``````````                 ```.`..``:ssd+.```..+sNMm////+-/+ssyymmddyssos
 -....`.-...`.`.`.-....-``......`.......`-.-..-`..   `--:..   ``.:+/+:-/+oyNmh+oyyo++o//:/hdmmmh+shh
                                      ``.``....`.    `.-..`         .:+ssyNmy++/+/://ossydhmmhhhyhdh
                                                 `````...---:.:://:++shydMmhosso//+oshyddNmmmNmmNmmm
`ssysoo+++++++++o++/::/+++/++/++////o+so/+sysyhyyyyyhydhhmdmmhmdmdmmdddo+dy+soo:/+++++ssoohmMmNmNmNN
`dmNdmmhhhmmNNdmNNdddhhdmmdmmdmmdmdhdddmhddmmmNhdddddddNdmmmdhNdmdhddhdNy:/syssssyys++syddmdmdhhhdNm
 :::-:---:::::::::::-.-----:::::::-::://///+oossyddhddmddmddmhNdmhhNmdNmdy.ydhhsyhssssossyoo+o++ooo+
 ````````````....````````````````````..-..........--://oyhddmmmdmdhNmNdmddy++://+++----..--.---::---
                                                `````......-:+shhdmNddhmdmmo:  `.....-://++o+/+//::-
                         `                               ``...-`.:+hdhhhdddd/        `````-::--::.  
                         -.-..                        ```...``.--.-.-+hmdmNN+`                      
                      :`.: ..```-`-:.`                +/+/:/::sy+:-::-yNmso+//+o/+o+:/:-.           
                        `  ```-. -:.--`               /dmmNMNMmdyyyhhhNNmhhyshhdyydhso+/:`          
                                    -:`. .:``.`        .:+syhys+:-.```.:..dd`  `   `                
                                     `-.`  -:. :: ..`-``./+-:`:-:-`     : +`                        
                                     .--:` `.--:` .`.`-:.. :--. `       .:`                         
                                                                                                    
            """)
    print("""
    You cruise silently into the grotto. Its roof seems
to slope upward and you follow the slope. The
depth finder shows that you are rising quite
rapidly. Perhaps you will reach the surface and
open air. Then the roof of the grotto stops sloping
upward. Before you is a perfectly round metallic
hatch made of a metal that you have never seen
before. With the mechanical arm of the Seeker
you try to open the hatch. It will not open. You
begin to send radio signals at the door hoping to
make contact on the other side.
_____________________________________

    If you decide to blow the hatch open
with an explosive charge,
turn to page 26.

    If you decide to continue
transmitting radio communications through
the hatch, turn to page 28.
            """)
    choicex = choice(26, 28)
    if choicex == "26":
        page26()
    if choicex == "28":
        page28()
def page15():
    print("""
    You maneuver the Seeker next to the hole and
begin to take sonar readings to determine the
depth of the hole. To your amazement, the sonar
readings indicate that the hole is extraordinarily
deep— it might reach the center of the earth!
    What lies down there? Where are the bubbles
coming from? Is Atlantis beneath you?
    Then you notice a disturbing reading on your
instruments; a mild earthquake has occurred. The
Seeker is not damaged, but the earthquake could
set up a tsunami wave on the surface causing the
Moray to leave forsafer areas. It might be dangerous
not to get back to the surface and leave with
the Moray. On the other hand, you are perhaps on
the verge of one of the world's greatest discoveries.
________________________________________

    If you decide to descend into the hole,
turn to page 23.

    If you decide to return to the surface,
turn to page 27.
            """)
    choicex = choice(23, 27)
    if choicex == "23":
        page23()
    if choicex == "27":
        page27()
def page16():
    print("""
The beam from the laser light illuminates the
entire grotto. Far back on the floor of the grotto is a
submarine! Cautiously, you maneuver the Seeker
closer. You identify it asthe submarine that mysteriously
disappeared in the Bermuda Triangle almost
a year before. The Bermuda Triangle is more
than 2000 miles away.
The submarine is apparently not damaged, but
it is covered with a slimy algae. Beautiful fish swim
around it as though it is their own special prize.
Then you notice that the main hatch is free of
algae!
_________________________________________

    If you decide to try
to enter the submarine,
turn to page 29.

    If you decide to cruise on through
the grotto, turn to page 31.
            """)
    choicex = choice(29, 31)
    if choicex == "29":
        page29()
    if choicex == "31":
        page31()
def page17():
    print("""
    With a rush of water, the giant squid attacks you.
Two 20 foot tentacles with their pulsing suction
cups reach out trying to ensnare you. You dive off
the platform and rapidly fire two of your spears.
They strike the squid close to its two monstrous
eyes. But the squid keeps on coming.
    One of the tentacles wraps around your diving
helmet and ruptures the seal to your suit. You fire
your last spear hoping to hit the monster in a
vulnerable spot. Water is beginning to trickle into
your suit. You signal the Maray to haul you up
fast— "Emergency Hoist." You must have hit the
squid. It floats away writhing and thrashing. You
think you're about to black out.
    You wake up on the deck of the Moray and are
quickly rushed to the decompression chambers to
ward off the effect of the bends. In a few days you
are better and start to worry about diving into the
abyss again.
_______________________________________

    If you decide to quit the
expedition now, turn to page 32.

    If you decide to go back down to
the deep, turn to page 33.
            """)
    choicex = choice(32, 33)
    if choicex == "32":
        page32()
    if choicex == "33":
        page33()
def page18():
    print("""
    As they begin the rapid hauling, you lose your
ability to function in the deep. You start to get dizzy
and your arms and legs feel weak. You lose your
hold on the platform and drift in the water
exhausted. Then you see a dolphin heading toward
you. You know that these marvelous
mammalssometimes help people in trouble. Will it
help you?
______________________________________

    If you try to get help from
the dolphin, turn to page 34.

    If you decide to carry
on alone swimming to the
surface, turn to page 37.
            """)
    choicex = choice(34, 37)
    if choicex == "34":
        page34()
    if choicex == "37":
        page37()
def page19():
    print("""                                                                                                
                                                    `                                               
                                                 .+/o+:`                                            
                                                `ssyd/:/-                                           
                                                odmNmy/dm.                                          
                                            ``.....:hmdNNhh/.``                                     
                                          ..``      `sNmy/:` ``.-`             `                    
                                     `-...`          `sh.       -o/o+         `:``                  
                                     /mdy-            .-       `-yyh-         -..-`                 
                                     `/syh-                    -/hdh/         `...      `..         
                                    `/      ```````..-...`.:--:osmmmh`         ```     :sd:         
                                    /+``` `:/+sosooyssoo+ssyhhmdmMNNMy-       `-:    `+mhy ``  ./`  
                                    +-.-.-.:::/+/+syyhhydhhmmmNmNNMNNNmo.     .+. `.``:----yo.ohy   
                         `.`.`.``.``/+dhyysososyhyhyosshddmdhysyymmddhhhy---- .-`..  `  -/o+sdys.   
                    `..-`.-..`..-:/+:oyhysydmddmdhhhddhddhdddhymddmhhhdddoo-` :`-y  //-.-yosNNd`    
                   `::`-/syy/:+:/:-//ohyhhyysysssyhdNmMmmmmNNmmmmmdhhhhdm/o/. .`/+``ds-:doomMNy`    
                   `...:-.:.....`-+//smNmmmNNMNdhNMMMMMMMMMNNdmMMMMhyoo+h`      ::-..` syohmhdm+    
                                 /+ :dyNmdNMMmomNMNMMMMMMms-dMmdMMMmhshhh`      -:-s.`/hodms`sdd`   
                                 +o`:mmMMMNMNdNm/ohdmsy+/--/mMMddMMNmhmmm-`    `:ydsosydo:+-` -y.   
                                `sd//ssyddhddddhodhshysyhyyhhmddsdmhyhyydo-    --`       `-:/-      
                                .sds+NdmNMNMNMMo.s- ++  +:`:sMMN-NMMNNNNm                           
                                -odhyNyhmdNNmMMs.+-- +  --+.:MMmoNMdssyhd`                          
                                :+hyyNsymmmNdMMo:++: :  /+/-`NMdyMMmdmmhh`                          
                                :+shhmydydNMyMM/ -+-`:  -:.  sMMoMMdhhmdd.                          
  -:.`       `                  .+hhmmhdhdNMNNso   ./.`-+`   `hNdNMmNmmNm-                          
`.::-::-..`..-sh-`---..-`       `/ohdshddyddhdyh+sooshhyss+ooyshyhdhhhyhys-                         
.`.````-/-:/` ..`.....:-.        :hdNNymmmmMMmo+:o/++o+o/+++.`dMdMMMddddd.                          
//ys+hydddyoso/:::-``            `/mmMmmMNNMNNNoshhdhyoshddh+-MmmMMmhyddm`                          
:o+:-:++:.```                     `NydhhmdNMMMMso:ooo+--.:+o:oNdMMMho+osd`                          
``   ```                           d:yhhhdNMMNhs+: .``    ``-hMNMMMhhyooh`                          
                                  `s sss++dMMM+o+y-         /oMMMMMmNmdhh`                          
                                   o sds++dMMM+/s:/        -+/MMMMMhos+os`                          
                                  `+ +ddyshMMM:o/h.`````...y+-NMMMMhssssh`                          
                                `../ omNmmdNNNhhhdhysyyyysoysyddNmdddsyym-                          
                              `/osys oddhdNNmmhyyyhhyyyhyyyyyddddmddhyyymNh-                        
                              osmyshy+NNNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNMMMh                        
                             `sdmdhdNNmhMMMMMMMNMMMNMMMMMMMMMMMMMdNMMMMmmMMNo.                      
                           `/dNMdm+omMMNdyyddmNNNNNNMNmmNNNNmNmmmmmmmNNmmNMMmm+                     
                          .yhyNMmMyymMMy` .--:/+::+++:..----...`.....mNdNNMmomN+                    
                         .dhsydNNNmodMMd```    `                     dNmNMMdshNN:                   
                         ydh++odmmNshMMM-   `.`--:-:/:--...``    `-. dNNNMNys+mMh                   
                        /ms+:oshMmdddMNmo          ```.-:++::`   smy dNNMMh//+mNN.                  
                        ohso:+oyNMmmNMMMy               .-.      .s/ mMMMNy+:+dMN/                  
                        shys////omMdNMMy`    ``. ``     `.`   ``````.mNMMMyohNMMM:                  
                        :mmhhhysshmmdMMo ` ``.::/:+:-`  ````-:-+syhhymNMMMNNNNNdd`                  
                        .////////:///::.          `` ..``.`...   ..-.///:::::::::                                                                              
            """)
    print("""
    You wait for the shark to go away. But then you
notice other sharks coming to join in the hunt.
They circle you, coming closer and faster each
time. It is too late. There is no escape!


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
                                                       
            """)
def page20():
    print("""                                   
                                                       `....`.:`-.-:-..`````                        
                                                         `````....oo::/+ooo+:.                      
                                                       `.:///+/o/+hs+-:-.-.`                        
                                                        ``.+s+/:-o/.`                               
                                                         `.:+o//yh+/----`                           
                                                                o:`.-+oyy/`                         
                                                               -s ``.:///-.                         
                                                 ```..```.-/+oshs/:`..``                            
                                  .-+o+oo++++++oyyhyyhysyshysymd+/-                                 
                                   `.-//ooosyhyhhhyyyyoo///:`.s/`.`                                 
                                      ``--:+ossyhyoso+/-..   //.                                    
                                          .-/+hhhsdhdyhhyh++oos+-.                                  
                                       `--. .+ssoooosyyydhdmhsy+..                                  
                                  ..:+--:.`.hd. -y````:hmmdm-o+/-.                                  
                              `.-/+:.` `:/shmN/./+...:dyhdoo+s/`                                    
                             `:/+++/.` :o+smMNo--:-`  ydhdy.sy/`                                    
                               `.:oyso-.`-oNMNdsdmdy:`/dhhy:dy-                                     
                                   `...:- `sNmhyNNNN+/`ddd/hm:                                      
                                `:/+shy:-oddNNmyydhy+//+moodMh:                                     
                            --:/+/-`/shdmNdydmdNNhy+`-d.dsdh+/-                                     
                               `. -osshyh::/hNdNmsdy::-.+dMhs+.                                     
                                  .:+odMNhmsydysy:-om+hh+hyhs:..`                                   
                                 `  -:MMMdysoossmN+/dNmooo:hdysyy:                                  
                            .---::/osoyhsoyhdNmmmNMNmNdhy:.-/oossyo.`                               
                             ` :sysy/  -omhyssyNNhMNNm+yddso+s:-.-y:/`                              
                                `+dMmoyhhddyydmmNMMN++:yhmmmMMMMNmN+y+                              
                                  sNMMMMMNdhyysoo//-  `dyoss/--+sdNmh:                              
                                  /./sysNMMMMMNmhyyo-.+ymNsos/+so::/:`                              
                                  -`  `:hMMMNddNMMMNysmMMMmdhooso/.::.                              
                                `.::.:shdNMMmyyhMMmNy+mhhhhshss/`   .`                              
                                  `- ``.:yNMNsosmNm/yymyNyh+doo/..  /`                              
                            ```   `-     .NMMysyyNs`yhhmmhNhsyso+:. :/                              
                            `.-:::++:---``sMMNyhNM/.oyoMMMN+oh/o/:. ``                              
                                  `-./+o::/dMMMMMMsosy+NMMho:hso.-yoyoo:.--                         
                             `-::::+-:-.````/sMMMMhohssyMmmddydss+yoy/+o.-/-                        
                             ./ooosd.   ./+/+sdNhmhNMNdsMMmhMd/yy+oNhosmdmmo                        
                              ``..-yo:-``./ooy+N:hMMMMMmNMo`sNh+omNNMMMMMMMd                        
                                   +o+o-   .sssy:hNNodNmNMMs.:mNs/ymNmhdmdds                        
                            `....//oh:.`   -+oy: +dh+/+sMMMMm+-yNm++h+-````                         
                          `ooo++//:-y`  `  `oyss /hyo.+yMMMMMMd//mNo++/:                            
                           ```.---::s/--+:`./hhs``shmydhNMMMMMMMs-sNy++/-.`                         
                           .`./--::+oy:-`:yyysy+..`ohds-oMMMMMMMMm+sM/sdyo.                         
                           :://////o:y`  -soosy-:---/dh:.hMMMMMMmNh/NNoy+-`                         
                             `-/yyyysd+.` -++s+/o:+/:hs:-+mMMmmNNdddNNh/`.`                         
                               -/+yyhyy+: /ysoooy+-:+hd+//NNhhshNNmy+-//`-                          
                              `:/+o/:-+   ./+++s-/--oyyshMNhhhmNMd++:++...                          
                            `osysyo+/+s:`` :o+oo/-++yshddNMNNMMNs.///oyo`                           
                          .yyhyyhhyyhmhdyo:./ss:o+/shydyNmNMMMNy/:/:-//:                            
                          `oyoooyyyhyd/s` -osss.+/o/hhysmMMMMMh+:::+/:                              
                           .-:::::::oshyo:+hys.-:yMMNmMMMMMMMhho+/--` ```                           
                           ..``     `.+:o-+sshdo+mMdMMMmoMMMNyy+-..```-//+-                         
                           -+so///:-.`-.-:+osssoyh-o/dmooMMMdhso+++o::.  +:                         
                           .```    .-+sdyyshdyoohssds-yysNNMyh//+/+:.``-::`                         
                               `.//://ohshshhsy/ss:MMNmdNNhmdh++/-. .-::.                           
                             .///+o+/++oyyhdhos:-NNMd+hMMMMNNy:/. :/ss/`                            
                              `-+ossmNmymdmhosyhdMMMhsdMMMMMNh+/: -.-:.                             
                               .++osyo++syyhsyydMMMmmNmhMMMMMsoo: `+ss-`                            
                           /+ossyss+ososodsdo sNm:Nys-/yhhNMMN-+/  ``/oo.                           
                           yhyssyyyssdsshmh/dhNMNmMoys+shyshMNh-ohs+``+o+                           
                           :syhhyyssooy+oydossdNmNM+Ns:`ysssmMys-/yy:`oo`                           
                           :syysso+///o++sdsodmhyNM:dsshdydosmmss.:ss.-+`                           
                           -ysss+++ossy/+syyoyshymM/ds+dhyhdNNmd/o-`+ds:.                           
                           `.`.-:/++//++:./y+yo+/yhhh+:mhsyhhhdmh.-` `:yh.                          
                                  `.::/o///o:-:-osshs-yddmhmdNmNdo   :sh:                           
                           ``...```````:.::++//:`+ss+/dyooso+syhhh+./+::                            
                           :soo++///--``::::o::.`/soyyy++:soo:/+++hy+.:/                            
                           /so+//.``    `.::o:- //ooyy+:oo/oo/ss++yy+ ..                            
                           `--`      `.-///--- .s+sssds/+yossooo+shy+`.`                            
                                 `..:+++o///-+`-+oo::-dhyhms:-s/.yhh+```                            
                                 `````.+-:/++s/:.o:`-sys++sys+s++/::`  `                            
                              ``.-:::- .--..-/:--/o+o+oo/---+.:-   -   `                            
                            .::+:..----:o+/+ooo/++o+:-``::     ``..:                                
                            +oso+++/+--./.::+sso:+//.`` -.   .::::`.                                
                            .-::/+ooo+/:+--`--s/os++s.-.``--:--/-...`                               
                                `.-//://ooo:--/sooyooo+-::-``  :/-.:.                               
                                   .---:/sos/::y:++y--+o++s::-. ...`.                               
                                    `:-:/s+s/++y/+/s/:.::osss+:``o+/-                               
                                     `.:/s+s+:/+:::/+///:::o++/:-..`.`                              
                             ```..///+ooyo//o::::.-.`.-:oo++/o+.:.                                  
                            :///+::::::::/+-+--//://:+ys://:--++/``--:                              
                            :/-``` `..---/+-/:/++/sy+:ohs+/-..``  ::`:-                             
                             .:/+oo+/:::-:o://-::/:+oo++o:+:-.`    :-.`                             
                                 ``.-+/++sdsyhooo+/`..-:::-::-.``                                   
                            `.-...-/+ssoooy++s:.-.-`--:+--...::.      `.`                           
                            +ssooooo///:+os//s:.-/-o/:```/o//+/-     -``-.                          
                            :oo+ooooo+++++os/oo+/+- `.  `:::--`     `/  .-                          
                            /yy++++///oo//oy++/.``   `--.        `.` .--:.                          
                            -++////:.`:/+++y++o//+...``.``      .`  .  / :`                         
            """)
def page21():
    page20()
    print("""
    You fire the special propulsion charge and zoom
upward through the water, frightening schools of
fish as you go. You become dizzy and lose track of
where you are. The world seems upside down.
The shark is nowhere around, you hope. Then
you break through to the surface floating about a
half mile from the Maray.
    The lookouts spot you in the water and quickly
rescue you. Unfortunately, the rapid ascent has
given you a bad case of the bends. It takes a long
time to decompress. And when you are finally all
right, the ship's doctor informs you that your
underwater days are over. Someone else will have
to find Atlantis.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 

                                                                                                       
            """)
def page22():
    print("""
    As you begin to drill, the stream of bubbles
increases.
    The stream of bubbles is strong enough now to
ruffle the surface of the sea. You could try to
surface now and locate the exact position of the
bubble area. Then you could make plans with the
scientists aboard the Moray about what to do next.
But also, you could simply explore the hole with
the Seeker to determine the source of the bubbles
now! There is great risk in entering the hole, but it
could lead to the source of the bubbles and maybe
to Atlantis.
_______________________________________

    If you explore, turn to page 38.
    
    If you try to surface, turn to page 35.
            """)
    choicex = choice(38, 35)
    if choicex == "38":
        page38()
    if choicex == "35":
        page35()
def page23():
    print("""
    Now is the time for decision. You check all the
controls of the Seeker, grit your teeth, and push
the control column into the deep dive position.
Down, down you go where no person has ever
ventured. The Seeker is built for deep, deep dives,
but you are descending rapidly mile after mile into
the deep. The pressure is intense, the darkness is
complete, and the depth guage indicates an incredible
15 miles. You quickly reverse the control
column. Warning lights flare up on your control
panel; they show that gravitational forces are now
stronger than the Seeker's propulsion motors. You
have passed the point of no return and your journey
downward will continue in utter darkness until
the water pressure is too great for the Seeker. This
is the final voyage.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page24():
    print("""
    You are able to capture the bubbling gases and
fill the tanks of the Seeker, enough to allow it to
rise. Slowly, the Seeker rises out of the canyon,
scattering schools of brightly colored fish, and
brushing past underwater plants that wave like
palm trees in a wind. Just as you reach the ledge at
the top of the canyon, you see what appears to be
an old road! Rocks along its side seem to be guard
rails. Could this be a path that leads to the lost city
of Atlantis? You anchor the Seeker and prepare to
investigate more closely.

        """)
    page25()
    page6()
def page25():
    print("""
:mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
./NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
:NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMMMMMMMMMMMMMMMMMMMdMMMMMMMMMMMmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMMMMMMMMMMMMMMMMNs- `yNMMMMNNs-:+yoNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
+MMMMMMMMMMMMMMMMMMMMMMMMMh-    `/-:+/`  -:/.yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMMMMMMMMMMyMMMNd:.-:+. -   `..`:   /NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMMMMMMMMMMMMMMNy` /+m  -` `/hssh-` yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
.+yhmmNMMMMMMMMMMMMMMMMMMm-`N+/  -`  -+:dy`-:NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
+hy++::oyhdMMMMMMMMMMMMMMMh`o-+  :``.++/y++/`+ohMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmmMMdhyyhy
`/ssmhsho+//syhdmNMMMMMdds+  .+:.:.``:o/+s/://--:dMMNmmmdddddhhhhyyyoooo++++/::-.....``````omy.  /o`
/o/+-::/syyhmNmysssshho-s++//--`    ``      ```/hs/..````````                            .ohm/  :ddy
/oymmmyssoy---//ydmyo/`/hmdmddhhyyssyhoo///////+yos+-`                                  `+oss.  `oyh
:NsyyMssyNm+hyhyo:----..:ommNds++++/+/++sydmNMMMMMMyNms:`                          `  :yo+oo/`  -hhh
/mydsdohoNNmNdsMMh:os.```+mmNdNMMNNmmmdhyoo/+oydNNmhMMMMmy/.                     .+o.-shdddmd..++hdd
/hdhdyysyyhoydNMMMmmmy+/::-+o.:ohmNNMMMNMMMNmNNdNhmNMMMMMMMNd+-                  :yhshmNmmmmdoddhddN
:ymmNmhoy+y/MMMMMmmMNMMMMNmNNddh++osyyhhhyyysydyymMMMMMMMMMMMMNdo-`        :y:..-osoooooo//ooosyhhdN
+hhmdsymhhshMMMMN+-++ohNMMMMMMNMMNNNNNNNmmmmmmm:MMMMMMMMMMMMMMMMMNms:.    .sys+osyyhhddhssyyyymNNmMM
+dhmysdyh:yNNNmMd:+:.:NdmNMMMMMMMMMMMMMMMMMMMMh.MMMMMMMMMMMMMMMMMMMMMmy/..:+syssydyyydddmdyyhdNMMMMM
/mNhyhNyyhdso/:soyyo--:-sNMMMMMMMMMMMMMMMMMMMM+`mMMMMMMMMMMMMMMMNhdNMMMMmmhhhhddmNNmNNNMMMMMMMMMMMMM
+hmyhmNddMh.+osoyoysoy:`+MMNmMMMMMMMMMMMMMMMMM-`sMMMMMMMMMMMMNNNNddydmNNhdNNNmdmNNNmddmNMMMMMMMNMMMN
oMNNNdmmmNs-ohmhy-ssy+-ohmmdhNMMMMMMMMNMMMMMMN``:MMMMMMMMMMMNmdhyhyyymmhssmMMMMMNdyhhmNMMMNMMMMMMMMM
oMMMMNNmdNdo:hmys++odoydo:symNmmmMMNMNNMMMMMMd ``NMMMMMMNyyhymyhyNMMMMMNMNMMMMMMMMMNNNmNmNMMMMMMMMNN
oMMMMMMNdNN+oyyhhy/oyohhd+/hmhyNNNmNMNmhNMMNdy`/-dMMMmMNdddmMMNdmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMNdNNMNNmNMms:sdhdyddhmmMNdyMyhhyNo::mohmNN+NNdNMMNNMMmhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMMMMNMMMMMMMMMN+oMMMmNN/dNMNmhddymsdsohdyhohhsNhhNMhNMMM+dMMMMMMdNMMMMMMMMMMMMMMMMMMMMMMMMMM
oMMMMMMMMddhmMMMMMMMMMMd/MMMMMM+yMMMMd:mhMm+Nmsoss+//yNyNNMyMMMMoMMMMMMmoMMMMMNdhMMMMMMMMMMMMMMMMMMM
oMMMMMMMNmMmssMMMMMMMMMm.MMMMMMysMMNMysNNMN++++o+++//oysNhNdMNMm-MMNMMMyhMMMMMyhmMMMMMMMMNNMMMMMMMMM
oMMMMMMMNMMMN:NMMMMMMMMd`MMMMMMh+MMNMm//MMd/``-/-`::` ./ymmhMMMm+MNMMMNomMNMMM+mMMMMMMMMdsNMMMMMMNMM
oMMMMMMNMMMMM+mMMMMMMMMd/MMMNNdd:MMMMm-sMNd:.`./:`.`-/::`-omNNMNsMMMMMsmMMNNMmoMMMMMMMMN+hMMMMMMydNM
oMMMMMMNNMMMMsyMMMMMMMMmoMMMMyNh/MNNMh-dNho:- .+oyyhso/. `.:/+hmhMMMMM/MMMmMMdmMMMMMMMMoyMMMMMMm/MMM
oMMMMMMMMMMMmh:MMMMMMMMh+MMMNdMNsNNmNs-o/::-...---+hhhho:`.+s-+o+yohNNoMMMNMMdyMMMNMMMM/NMNmNMMyyMMN
oMMMMMMMMMMMNd.MMMMMMMMs-NMNmmMMyydyo.-`   ``   ```````.+ddmNNdNmdydss+mMMMMMsmNMMMMMMh+NMMMMMMdMMMM
oMMMMMMMMMMMMN:NMNMMMMMNohMy+hMMM+``  `                 --+yNNNNdhyo--..oohdm/NMMMMMMM:yNMMMMMdhMMNM
oMMMMMMMMMMMMM+dMMNNmmmh+:dh-:MMMN/       `.       `       .:-::. `       `-o/mNMNNMMN:ydMMMMMosNMMM
/MMMMMMMMMMMMM+/o+/:```    `  dMMMMs`      sy/`           /-             `..`-/yNMMMMh.mmMNNMN.:+hMM
`mMMMMMMMMMMMMs:`---:-`       yMMMMMmo-`   `mMm/`         -Nh/`       ` ```. ./yddymNh`+NMMMMy hMMMM
+mMMMMMMMMMMMMh+-hss/:`      `dNNNNNNMNds/::dMMMd-         :NMh:          ` `.-///+--+smMNMMMs:NMMMM
oMMNMMMMMMMMMMNNdyy+:`   `.-.--::/::---:/+syhdmNMMs-`       /MMMh`          ./o+::.-:::/++hNMsdMMMNN
+Nmhhhyyyyyyoo:--:--`  `-.`..``    ``..`       .+ymNNdyo:-`  yMMMh.        :dmMMNo`````.-:+yhsmMMh/o
:o+yo:-``/o- yhoyssy/+-              `-:-`         `:odNMMNmdmMNMMm:`      `:oymNMNmh/`    `./hMy/dN
oMd-+:o+++--:``::/oo:-`       -/. `-:```.:--..-`    `.-:odNMMMMMNMMNo:--.`.`    .:++o+.     :shd.hmd
/d/-ohMMMyo+//       `      .omNdhdd+:/sd/++.  `..` ` ```.:/+ymMMMMMMo/.`..````.:/+++//:/::---/osNMM
+h++`..-+oss/`    `  `` `   :hymssmNhhdmNhhmhs:  .-..         `/hMMMMN:dd+`                 :+hshMMM
+dmo:/ ``.    `..-os:+:.-.:://+sssyodNmmmddmdy+/:-:+/+s:-:////+++omMMMNyNMMy+:--``.-.:/::`-///+/hdMM
+mNohoyo:`.     `-/:/-`     .:::-:odNNMNy/+:-/ssym`    .-`         +MMMModMMMd- `  ``.`.-...`/-:yhhN
:os++s+y+:                   `.:/sosydNNy//-:+smmNy.     `.`        oMMMN-NMMMMh`            .:/yhdM
                                       ` `  -sMMdy:`        .       .MMMMooMMMMMm:      ```  ``/mNMM
                                            .:.oo/:`  `......-       mMMMd/MMMMMMN/  .--./////:/dhNM
                                                     .---`` `./      yMMMo+MMMMMMMM/ `..`-`///osdhmM
                                                     /-://--+:y     :MMMm-mMMMMMMMMN` `` ` -:/sdhyyM
``.` `..```  ```.`.``````                             `:+//dmho    -mMMd/dMMMMMMMMMM+ o`  .+++:hmshs
            ``.--.`.-/:::-`..--/--/:-:-`...`            -osdmN:   :mMMs/dMMMMMMMMMMMs/+/-`.:ohyohhss
                      `````.  ``..-..-.--..```````       :ydN+   +NMd+sNMMMMMMMMMMMMNs///.`+hhdoohNN
                       ```        ` ..`...-.````.`.      `ys:  .hNh:/dMMMMMMMMMMMMMMMm////`.ssoydmNN
       ```..`     .  ` `..`` ..``  ..```` ``           `.//-`-sy+..sNMMMMMMMMMMMMMMMNNo+//+--:ohNNNm
`````  ` ```                                        `..//:-//-. `+mMMMMMMMMMMMMMMMMMMMsssooo`:hmmmNN
```                                               ``-/ss-``` `:smMMMMNmMMMMMMMMMMMMMMMyss+/.`-hhdmNm
      ``               ``.`.`                   `-/yhys+:`./ymNNmhyo:/sMMMMMMMMMMNNmds+-.`o+syosNMMM
       `.``.`` `       `````.`.. .-//:/:...`-`.:+hmmmyyhyyhys////::sdNMMMMMMMMmhy/-.`` `-:yodyshmNMM
                    ` `            ``:-....-+yhdNmmmddNNMddyyyssoohMMMMMNdyo/-``--`:/:-ymymNNNmyNMMM
````.``.```                        ``--/+osdddyooo++o+o++o+/ooshmNMNdyo:.`     `-s+:+//+hdmNMMo`hMMM
 `.--:://--://.:/..` ``   ```  .--/+osyhhhyhyyyyyyhhhdddmmdddddss+/-....-.` `  .:-++oyhdNdMMMM/:mMMM
      `.--:/+//.:-:. `..`.+//o+++yhyyhdhydyyy/::-::-/:---:-....`` `..`      .--:.`..:-+dMMMMMMy-oMMM
        .`..--.``.`....-+++oossshhhhhh++so:/.-----`.````          .`.`    `.`````.--.:/+yNMMMmys`ohm
        ```..`...+//::++oshyyhysy+oooo++o+:+-/:::/---.`-..` `  ``-//-:  -:.`-.++/sy-yss:-dMMNo-y: ``
        `..-::::+++ooo+:+:::::/::-:-:-/:::-::.-``...``-``.` `````.+-++` /-/-.:oyysdhooyoo:hMMNoy-`s-
    `--.:/+//+oo++-:``` ``.`.`.`.```  ``````..`-.`.-::/:-/:-::-.:+os/+/o-:o+dNNmNNMMyhdh//+hMNMmh`sd
    -:-/+++/--`                  `:-.`.:...``.``       `````...:+/:.--::-yhmMMMMMMMMo+y+:s+:mMMd+ -:
     ...``                        ``.-:::///:o:-//./:`..``.```.:-. ::.:/ysymMMMMMMMmd++yddoyNMMMm`.:
                                         ````-:::::-/:/----:::--.-//-+:dhMMMMMMMMMdmsyodshhdmoyd/`hM
                             `-//``       ``-:/o/:o/o//:` ..-/:-+/+o+yo+sMNNNNNMMNommhhMMmhmh./+oh+s
    ``` ``              `.-...-://o/o+-.--.--+/.`-:-yo-`     `  ...-:smNMNNNmmddMMmdmMMMMmhmdsms/+:y
     ```.--:--.``````   ::/.+-:::::::/-`:    `.--`-` .-..-.-/:..--` /::oNNdsmmyhNMMMMMMMMMNmd/o-`ys/
    `````...``.`..--::/-:-:-::/-:/-::--:+-..-`  ` ``    --:-.:-./---o -:://:ymmNNmNMMMMMMMMNd+``:dmm
`/--..-/:::o:-+/://:++++-``..:::-ososydhNNNddd+:--..`  :-:/.-/---:.-/.:`.:yNhNMMMmdNMNMMMMMMy:./mdys
.s:+///ys/::/-oy-///so/s`        ./s+syhhhyssyso+o++/::++o+o-++---///:/../NNMNNMMMMNNmMMMMMMNdo-`:-.
``..:o+--.                     ```   `.:.      `...::-:.:::/os+oo:oss/yy:++oNddMMNMMNMMMMMMMMMMMy-`+
                         ...`.::-+-.--` `  ```   `.-:-`    ` ..:/`-:dhmmyhdmdmmmNdhNMMNMMMMNMMMMMd``
                     -::+/:./::://:/:o/:++:-`.-.:+osyyo+-::  -::.-`-yoyys+oy/ysshydNMMMMMMMMMMMMhd/+
        .`.`.```     ./-::o/yyyosysyshs+/:---:-`-sssss+-:/-`.-:-:/:/+:/hssy.yh+hmo+//oshmdsoymMm.-`o
              ``..`.``  `:s::+:.:::-..`     `.           .-``.-+/:-+:///shyshmo::-o-+o-`.s.``+mN/+s:
                      ``` `````                        `.:..  -::-s/o/yo/ohdhyo.-./sys- -/.`/`-++o+/
                    `.-      `.`..-..-.:-:/`         `-+:/++-`..  oosohsyodhhyhhhNNh/`-y./ `-:++:sso
         `:::s/::+/-//::/+:/://:/+o+:`-+/..:++..`.``::.shddhd+.   o+oyyoooymhdNmyddmm-:yh+./:oo/+.``
          `-:///:::-+/:://+yhddy+++:--``..-` `      `osyMhys+:/-``s:y/hhymymmysmhmmssdNssso+://+o--`
                 .   `                               -  +o`       o:o//:s/.os/-shsssdmmoomMMNo:/:`- 
                                                          ``      +:-+ys+hd/oo+h:`oy+hmmMMNs+-`.-.-s
                                                                  :o/s:-:ss/+dy/`sdysdMdNh/+y/hMs`.N
    """)
def page26():
    print("""
                               .:/oosooo+shsdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdoMMMd -mMN/.`/mMdh
                            :yyhyshhNMMMMdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhNMmMMMM++NMM:.smso/yh
                            ````-smNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmMMMMMNhssMy/Ndo+dMd/
                                 .ymmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdNdMMMMMMMhhNohMMMNsNMMMmmMMdosy
                                  :NNMNMMMMMMMMMMMMMMMMMMMMMMMMMMMNy`+MMMMMMMMNM/`dNNMMMMMMMhmMNdNMs
                       `          .NMNMMMMMMMMMMMMMMMMMMMMMMMMMMmdMNmNNNNMMyoMMM/mMNNMMdo/+MdNMMMy--
                       :.    ` `  `dNMNMmNMMMMMMMMMMMMMMMMMMMMmdmMdo:.```-omNMMMNMMMMm/`  .MMMMd/+y+
..                     ..      :   `-ss:.oMMMMMMMMMMMMMMMMMMMMMmNs.        .oNMMNsmMd.  `/mMMmy//:++
+o-`              ``   `.` `  -. `       oyhy+dMMNMMMMMMMMMMMMMMNo-.sdmds:   oMM/`md` -+omMNh/.:++//
/d+/-      ``.     `` ...  :``--- `        ` `ohsNMMMMMMMMMMMMMMMM-yMmmdhNo  .Mm`ym.`so.:ms.`:so+//:
+Mo:-/    ``` ` ` ``..--```+..-:```.``         `:oNMMMMMMMMMMMMMMMNh/oh+-:y` -MdhM: `-:os++ss+::/+` 
oMMN/:    ```` ```.``..`- `.-`:.``` .`         .ymMMMMMMMMMMMMMMMmy++ohds`+. odmMy `/hdhddo-`/yyys..
oMMNo`         ``..``        `...`             yMMMMMMMMMMMMMMNs//:-.sNmhy. `mdyN.-dMMNh++/`.:: `.+y
oMMmy     ``` ````..   `       `` ``.``        yMMMMMMMMMMMMMM/.dMNNdMMNMN  sMho/+NMMd:.syo+/--osso/
oMMm:          `````        .. ``  ``          .oMMMMMmsMMMMMd-+MMMMMMMMMo +MMh+/NMNo.-oyms++ooysys/
oMMms.     ` `````.````...-``-.```   ```         :mMmo:mNsMMMd+oMMMMMMMMy`oMMNo/NMh:/ydhyo++/oosys+:
oMMMNo     `   `...-.-`.... ```-` ..  ````        -:. yMhodhMMMMMMMMMMm+-ydhm//Nmssdmmhys//s/shhddds
oMMMM:     `.. `..  -..`. . `   ..                   .MMm/::sNMMMMMMm+./hhmy:odyosys+yo//osyyydddyy+
oMMMMo `-::.`  `     `    ``.  ` `.` `..``` ```````.``os+:-o.odNNms:`-yNNd++hyyo.ydh:+/+o:-/yso/odho
oMMMm-:yNNdho.             `-```` ``   `                .///: .-.  `odds:/oyymN/.oo++o/-`..-`  .oss+
oMMMMNmMMMMMd:`    . .`  . `..`---:..-..-..-.` ` `      `/:.+.--...-++ooydNmhs/:-/ody: `. ``.:+ys+-`
oMMMMMMMNMNMNdo.```` `` ``  `   .`   ````       `````````   o`-:://///:/---...-:-`+:``-:/ossoo/:-.-.
oMMMMMMMNMMMMNd-.--`.```..`                                `s:`-:`-.:-:``` `-.`.:/ssysossssosshs+/..
oMMMMMMNmMyoMMNys//:-//:..-.-..`        `oo-....`        `-/yy/shds++/:../oyy+syohdmmdmdhmMmhmdhhdhs
oMMMMMNhMMd:+mMMN/-...````-.:-.-----.` ``.+y+/.``...``- :/:/+++dhsyys  +y/:-. .:ohyNmdNMMsdyhmho-.-.
oMMMMMN-/hMm:NMmMNmdmhdys+:-....-.`.:::.` `+hss+.```./s :``   -hNMys/ `-`     .` `.:dhNNs- -.` `.---
oMMMMN+` `:s.syhMMNMNyyhyyy:--:-  .`   ...  -oddo/.:+oo.-o   `+:mMm+.::+sho+:.-`...+oo/``/osshddysyo
oMMMMmo-     .dhMNMMMMMMMMmNs.``:` `..       `y/+//+sho:/-  `-.`yMm- +:` .:+ssy++/-.  :dNmMdsdNNmNho
oMMMMMMNo    smsMMMMMMMMMMMMMy  `/  ``-.     `.--:/o: --:s/`--/ymh---oyys//:-.`       -:-oys+:+hssyo
oMMMMMMMdy+` /hNNsm+/NMMMNdMMM/  .`    .+-    /o/::-`/:ohhhsysshmMNmdhdyyss/+y+/-      /+hNy+/::``-/
oMMMMMMMMMM-  :y-`+dNdNomNmMMMd  .  :+-``/+...`         :::.+/:s:y:-//+///shhNssy`   `.oo+sssoo/+:  
oMMMMMMMMMMy     oMNMNMMMMMMMMN` ``-shyy.-.             ``. -.`-`.`       `-/ooyh-` .dmmy+:``:hhyo+`
omss+dMNNMmyo    syMmMMMMdoyMMm   `:mmm+`                              `-.`  `.:-:--.`/mdhss+::ssy++
oNmdmdho-/hdy    :MMmNMMyohNMM: `.. `:.                                .--..--`  `-.-../:oo+osoosys/
oMNm+oyd/`.`   ``:NmhyMMNMdoNy-.-/:`:++////:-....````    +so/.`          `        -`````  ```.-sydho
/yhmNMMNmdh:`.:.-:hNNmMMMNdsyd:shdhy+NMMNmmdhhhhhyyyyhhhdmmNNNmmmmmmmmmdhhhhhhhhhhhhhhhhdmmyyoyhhmmy
+mddhhddmNm+//.::/odddmhddo.o: :ymd+os/-..`````````.------:::/++oyyyhdmmmNNMMMMMMMMMMNdMMNmsmmhNdsNy
...```.-..//://+/::hmdhho+- .  -ydm-``  ````  --:..-----`.-:-..-.````.---:://++oyhddmmNMMMNdNNhdhhdo
  ./o/:` `.-    `:oyy/.`.:` `-:/oso--..`    ..--///-:sss//syo-`-o+o+so+o++sssyhdmmmmNNMMMMMMMMNNNNNh
.smy/`-/yyo-    .-:ossoooo.``---.:/ydyos`  `.:/o`y/.+yo+/.o/`.+yysdhyhmNNMMMMMMMMMMMMMMMMMMMMMNdys+-
oMy-/dNNo` ```    `-ooo/.+:```-`  .:yNNd++sssydy`/`/ddo:`-:+yyyyshNMMMNNMMMhydmmMMMMMMMMMMMMh:.` .+:
oMhdMMNd//yddh:o+   :dNm`-:-.-:/-::` /dMNNNNNNNs -ymds-/shhhNNNMMMMMMMNNMMMMNNNNMNMMMMNMMMMh:   `/hy
oMMMMmhdNMMMMNNh:::-NMm::.`/:--:osso++/sdNNNMMh` yms.-yy+/odMMMMMMMMMMMMMMMNMMMMMmmds/://:/:`.:sdNh/
oMNNMNMMMNNMMN+-hd-hMh.-Nyshds+++oyhdmNNmMNmho.:ss/.:+shmNMNMMMMMMMMMMMMMMMmhs+++:.``` `. ```:/+/:.-
+y+mMMNh+yMMN+omy.:Md--ddoNoNd...  `.-/yyys/.`:osyddmdhddNNdmdmMMMMMMMMMMNNmmdhyyso++o//+/:///:.``` 
.+mNd/..yMMMMMMd`+NMy`yMmNy/Mm``:- .--.``-//+sNdNmNMNMMMNNNNNmNmddmdmmmNNmmNmddhdyoso/+:-:/:+oyso/` 
oMNy-`-yMNMNNMM/sNMNsyNMMMymMh/`./   `-.:-s+ydmmmNmmNmmmhhyhdmmNdhNNmmmmmNmmdyohyyhhyhhs-...:+//-`  
:y/:.``-mmNNMMMNMMMMNMomMmhMMo..+o/  .:``.-+syyddho+::+yysss+--/+oo+o++++yo/---sdhhdhddhyss+//+:/::`
 `-```. `:s+hmNNMNNmso.dy.-ds.-:hys:--.-:++oyysyhyosso:..-/osos-o:.-::--.-:-.`.-::ohyhddhsydyysoy+. 
`-- `:.    ``.::+::`  `:. :     `.:o::+o++/++sossssyyysooo--/:``.`           `-:::+o+/://:--..      
`` .--                 /+ :                  ```..`..--:-//.`                                       
 `.`:                  .:.-                                                                         
 -`-                                                                                                
 .`                                                                                                 
        """)
    print("""
The only way to get beyond the door isto blast it
away, or so you believe. The Seeker's laser cannon
is powerful and you position the Seeker to fire.
Pushing the fire button, you send a powerful beam
at the hatch. Nothing happens. Then you advance
the cannon control to full emergency force. Again
you push the button and the beam dissolves the
hatch instantly. A flood ofsea water rushesinto the
giant hole, carrying you with it into an air-filled
cavern beyond. The water fills the cavern with
speed and explosive force. You see several people
scurrying towards escape hatches. IT IS TOO
LATE! You did the wrong thing


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page27():
    print("""
    Deciding to return to the surface, you direct the
Seeker cautiously back along the side of the canyon
in the ocean floor. Without warning, the
Seekeris gripped in a powerful current thatsweeps
it toward a grotto. Once in the grotto, the current
carries you to what appears to be a large metal
door. It swings open and the Seeker is swept inside.
The door closes, the water in the grotto drains
away, and you step out into a chamber that you
decide must be made by human hands.
    A door opens in the wall, two people dressed in
simple clothes come towards you. One of them
says, "Welcome to Atlantis. We have been expecting
you."
    What a discovery! You have found the lost continent
and its civilization. The two people tell you
that although citizens of Atlantis occasionally journey
to the upper world, anyone who happens
upon Atlantis is never permitted to leave. The
Atlanteans are not cruel but fear discovery of their
world.
    They want you to follow them and you agree.
But you have another thought. Perhaps you could
blast your way out of the chamber with the
Seeker's laser cannon.
______________________________________

    If you decide to follow the people and
join the Atlantean society, turn to page 39.

    If you decide to make a dash for
the Seeker and try to blast through the closed
door with the laser cannon, turn to page 40.
        """)
    choicex = choice(39, 40)
    if choicex == "39":
        page39()
    if choicex == "40":
        page40()
def page28():
    print("""
    The radio transmissions seem to be failing, and
you grow tired of sending signals through the
closed door. You are just about to give up when
the doorsuddenly swings open revealing behind it
a cavern with another door. You enter the cavern
cautiously and receive a radio signal in English. It
tells you that you are welcome here, but that once
you enter this place, you may never return to the
world above. It is up to you to decide.
______________________________________

    If you decide to go on
and investigate what might be Atlantis,
turn to page 41.

    If you decide to retreat, turn to page 42.
        """)
    choicex = choice(41, 42)
    if choicex == "41":
        page41()
    if choicex == "42":
        page42()
def page29():
    print("""
    The submarine is indeed mysterious. You now
have on your sea suit and you open the hatch on
the conning tower and enter the sub. It is amazingly
clean and in order. There are no signs of life,
but there are also no signs ofstruggle or trouble. In
the control room, you see a piece of mystifying
equipment that just doesn't belong on this sub.
    A voice begins telling you that, thousands of
years ago, the leaders of Atlantis realized that their
continent was slipping into the sea. They discovered
a large underground cavern and built new
forms of living quarters for their people. Later
when Atlantis was deep beneath the ocean, some
of their scientists discovered and perfected an operation
enabling them to breathe under water.
    The voice, which sounds friendly, also tells you
that there are two groups in Atlantis. One group is
good and the other is evil. The voice invites you to
enter the world of Atlantis and gives directions and
instructions to a secret passageway to the underwater
city.
    As you follow directions, you spy an unbelievable
underwater craft with several people in it. It
must be an Atlantean ship, but are the people
good or evil? Do they know of the secret passageway?
_________________________________________

    If you hurry in, trying to reach
the secret passageway without being seen,
turn to page 43.

    If you rush back to the Seeker
trying to escape danger, turn to page 44.
        """)
    choicex = choice(43, 44)
    if choicex == "43":
        page43()
    if choicex == "44":
        page44()
def page30():
    print("""
                ``  `   ``` `.`   ...`                     `/..//.:/sy-..`   //:/-- `  :sooss. -:::`
                                `` ```.-:--::++:-:-.-     .+o+-:+yo:-   ..`          /ssooso      .`
                                           .`...:-/:.`-:o///::/:/.        --       `:s/oy+-       +.
                                               ` ``.`::--///s/:.``.-     /-:.     -+-+o+.      `-./`
             `.:``./+/::-:../.                 `.:`:..  `/o-:  `    `    ++-   `-/.-oo::.      `ysy.
    ..--..`.--/s:///+oy/:/-`:-               `-//-:.`-..+/`             ./o-:-+s+-.ohs:.``    `/yss.
    ```..`    ``  -.....::-`                .-`  `--.-` `             `-/+.  `+:-+ss.``.-. `y+/dho+.
     `-`                               ...  `  ..```        `     `.-:+y/-``--``./-`     `-:dhsodh/`
                                    .` `   `/::`             `..ohdoh+..``:...`oo- `.   ./:yo:o/syy.
                                ``````/-.../`        `..-/:--:`-so:.`  `..- .:`.`      ` -/:``` -+-`
                             ``.` ``./+.```   `.-+oy/:./dNh//:.``     `.--s-.--       /oo/.  `-./s:`
                        `` `.`` `.+o:``  .:/-::./ddd/h+//:``        ``   -:`           /s:    ``.-` 
                ``....--.`` `.////-..-+yh:sosdd-:--.`.`           `.`   ..          `/-+/  -.:.-.`  
              .`/++:.. ``-:-:--..--:-mMmdooss////.`  `          `.`` ``..           ./.`   -`o+.``  
            ``.-..``  .-...  `:so.``.osoyyy/::/oso.``         `--.``-.              :-   `-.`.`-.:  
       ```..``  ``.`:.-    .+dNNs`os--os:-..`:/+sdo``       `:.` `--:         `.-`-..   `-.`` `-``.`
  ```..``` ...-.``` `    -/-/oy+:-/-` .-y+.  `-:syo        ..`  `oso:`        .-:::     -`:``-:  `- 
`..``  ```-://.        -yNmohho./.    `/smdhyshhhyy/`   ```. `....` `  ``     ``-/      --`  .. -:. 
    `.-.``` .`  `.-` `+NMMMdmmo.     `// -smNNNmh:+o.  `::```:/                `+             ``/.  
`-``` ``:././..-o+. .ymNMMMNs/      `+-`.`.://y-+.``  -```.//`.  `.-:++/.......:`         `   `/`   
        ----.--/::..mNMMMMMm-     `.o+ `..ss:s-     ..`  -:. `.-+hmMMMN/`:shhy/. `-     -/o/ .:     
    ..-:.`.. `...--ooyMNymN+``.+/shh-``:` -+//   `:.-...-``-o-` :shhyo/:+MMNy-` ./o.`   ` `.-.      
-/.-    .:`..-//o/`  -+/oyo/++o:://--+: ..+o:  ``-..o:-`.-/dMh`  .-:dMmmmMMNy:    .`      -//.`     
` `---`   ```.`:.-`.`:+:/:.-/++s+:./-.`  :ho/`-.`./:-.-:.:NMMh:+o+dNNMNMMMMy             :Ndo.hs-`  
/o:-.``.`.. `.: `-   ```      `++.-:` ` `+-+s.  .+:`-yM-.NMMddmMMMMNys++/+s.        `/  :NMMN--oo/:`
:hhhs/`:..-`:--      -..`  ```:s:-` .+- /-/yy. `:.`oNMm-+NNNMNMMmy/.  `  +-      `-.+s-+mmdhy.`  oM-
/hdyhysys+:` `-.`.  `++.`..yys/:. `    :. `.y:-+/`odmdoymNNNMNh/     .++-.          `odmNmMMMMm` .+.
`-/yyyddhyss:------`  `-.: :o:.`    `.:/ `  o+` .-/:/dMMMMMMs+::`    `//-`.        :+so:oymNNMNs/mh.
.`   .oyhdmyhdhss/` `.`. .:-`-..- /:-:+h.`--o/:`-/.. `++ydNs/:-`     -.. /-`      -smy`  `/ymNMNMMM-
:o+/`. `.+yhsydhds.. `  ``-. `` `.`-:o-o+o. ::-` --.`.`   `-.-:-`  `:..+..-/-.    `o/.      -hMMMNm-
`++o+o/:   `:sdyyhss+//`. ..-/-`    `  `   `-.:`      .`      `+/`-:. `:.         :-          .yNMM-
  -`./-:/+:  -/o+shyyhoyo/oo`:o:..`` ..``.. `.     --.     ./.  --++.  .`        `/.            .sN-
 ``  ``-yds:   .`-//ssyyhdsss+y::-/+so:/+s//sy/o///s/::+:`.`..-`````:/-`        `-`               .`
  `   `smho` ` `````./+oos+hs:/::sommmhydhddhdyhmyhymhyshyyhmyoohs/+:/o.       `.                   
`    `-dy.   ```--```.``.:/o.-.-````--:-.ysoho-/+++oo++:-+shmshmmdmdddo/      `.                    
`.  :ssy+.-``:+./:o+  `-`  `..-`         .``. `-++++++//+/``..o--/.--:-..````-`                     
.. `+dh/-`.`.-/:ydmmso``:.  `..`            `:dNNNdso+sy::    -/` .:::::` `.:/`                     
 ``.oy/` .` :   `./:ooo. -``:``           `:+dNhdh:-..`-+:   //:  /hdyo.:---:..`                    
` `sys```-`+`     ``.`:`.``-`            -mhmNmmh.`   `../  `:.` `+NMNNhy//+...-`.`             `.. 
:/oyo` .` -s`````  ``   ``++`         :oosmNdymh:`   ``.`:  ---:.  :oyNMMmo:``.::`..`             . 
:hhh/ `-  .++s/:-  `:: `-.-:-      ``ohysNNNhhy:.` .o/oo-:`.: -/:   `.:yNMMo`--/:-  `.-.```     ``` 
-hs/.`/`   `/osos+/s+/:/:/+//+o+ossood++Nmmhdy--+++myhhy/:..:..-+`    -/yMMN.-.o/::-` ``.---:-..`   
:o` `--      `/o++//:sh--yy+osyohyhdhy+ysNNmd/. :yNN+s:+`-`:./:-/+    `//NMM/-+d+:+s+-/:-``......-o.
.:  `/    ``-.``   :mhy+/hmmmmmNdmdss/+osNysss./y//-`y:-:  .ss+-+:    -:--+o+hds+shoh/ohy/.-ydd+``:`
`  -..    :s+`    /NNyNh+oshyyyhd+/syyshNd:syy+so:/+:o .-   /yo/s    :`  ./+osmhhNs+hs+:  /:.-./.sh.
  `//-     `     /NNsdso/.````:dd:/+:+smd+++:/:/+--//+`    -ds:+-  `-../++yosyyymmmhhdd...sy`-o:-//.
.`.-`        .` :Nmsyo-`     /hsos.hhs+::++/o+os.  `:+`   `yysd+   -:+//o/.` ``-/ymmhyyhdyss/:-ohmh-
 .`    ` `   ` .mmsmo-`     omooos//hNhhs/-:hmdy../oos+- `hNmds-   `-:+/-..--:---.-:oyhhdNNNMmsmNom-
``    ``      ./:-dy-...-::yNdyshyhodhoso++dMMmNhsmdsooo++NMhmo    `  ```   `  ````...`---:/sh-os/+`
            `-+///+.  ..`-y++shhhsNy+mys+:dMMMd//hydhmhy+--yNy.` `:.           .o.`-/../+.`.-s/:::+`
  ``..```  `./o+od+.``  .hdos:+syhdy:shhsmMMMh-   :+ydNN.  `h+   /+`       ``:.hs/+ss:+y+..`.s/:y/+.
       ```:/sysms+:h/:- dmoyo:/oy+/oy.syNNmyo/...`  `-yNy---: :/.``  ```.``-so.so:+os/:o+:.//----++`
     -/oo/./---hs-`os:/ dMmhyhhNNho++:oNNd+--.-::-..` `-:/:.```.`.`.```` ` .+/-+-+:/+/:::`:o:oo::+:`
    /hyyhdh---::/:/hdy-.sdNmmNMMmo+++s++yo ``-+/-`.-::.--::-/:/-.``````   -//+--:-/:/:-:-..+:s+``-.`
   `sydNNNM:`:dmmyo/.`/hosMMMMMMNmhddo.y+. `...     ```` `...``             -:.//-:-/-+:`:+-+s+o:   
    smmhmNd//+h+:    .smyNMMMMNhoNNMMNh+:`             ````                   :o+/./-:++:.-`.:---.:`
     /+o+:`            -MMMMMmh+hMMMMMmNm+----.`     . ````                    .`:./``o/:+:.::`..   
       --`     `  ...:` hMMMMNMdMMMMMMMNdhss/-`...` .-`                 ./:- ::--/:/    .:././.`    
`+://-`/:.`: -`-..```:` omMMMMMMMMMMMMMhs/+so++/-`.:-`                 `/o.o++o+hdhs`  `/.-..   -   
`- -/+::+-+o..``       :Nmm:NMMMMMMMMNMMMMNddys//+-.`..`                .:-:+o/.`./    :/`    --+:.`
                       hmN- yMMMMMMMMo/:+ydMMMMMMNs:-+.-                 +mdo+:--.+/+:+y::-...:.... 
                       os-  -MMMMNMMNy/ ```-:/::yNNdoo-`            ```.-/yd:``.-+-` .-.`-`     `.- 
                             yMMMMMMmd:....    .yhdyo+:           `.     ``.+:--``.  /-:.::``++/++` 
           --``             `-NMMMNMmy.`       hhdmNy/-        ```    ```-+:```  --:.`-.` -`-+++    
           //::. .      `` `  :NMMNMNy`        MNNNo+:       `.     ``  :/`     ` ..`.`  `-:-.o+    
        `:-://:/+:...`         -mMMMmy``       mNNN+.-     `` `  `     +o/:.``.         `:h.. `     
        .+o+++++oos+/           oMMMN/.`       ymNN`-   ```     `     `-+hy/yo+/-`` `-/sy://+-      
       :+o/:+o-++o+//          omMNNM:--       dNNy-. ``  `  ``        `/mNmmhssoss-/s/+s``.`       
      .+o++/s:::///+.:..     `smdNMMNo:`      `NMy/o` ``````            /dMMNNNmdhhsso.``           
     -o+o/++:/-:o+++:++o-   ..oydhmMMs.   ````/yN-.---..`             -:/shdhmNNso-h::`             
 `/-/:o//+:o.+-//+////:/.` -.-./mmmMs....-----+hdy::/-...````.```-:  ./----s-oyy. `-` `             
-+o+s+//++/::-../:/++++-//:-:`.hddM+     ````/+o/:``   ````.-::.../..-. `..``-+`                    
-os/+++o+-++::--:::/+:-:/o/.` oddy:          //o.  ``...``...::---.::`  ``   /:                     
`-:o/o+///://+/-//+//..:/+:.`/dmo.        .``-.:---.`.````.......-o:`      ``+/                     
`++s/o+/::/++/+///o:/:--/s/:omy.          `-```` ```            `/sy+.`   ./.:                      
`:ooo/++:-y++:oo:/o-:+--os/hNh`            `   `` ``           `o-::`   `///`                       
  ` `/+/+-+:o++/:-/`----/omMd.                                `.+:-.   -/+.`                        
   ``..:+::/yy/:+/s. `s-` oh+                               `--``     `-                            
  ./o.-:-`:`s:.--+y..ydhy+  /                              -.```                                    
  `/o+--ho` +`  /+o.-yNhNm: /                            `.`  `                                     
   ``.`.-o-.:.``.-/-..yyydy`:`                        .:.-`                                         
    ..`  /+//syo.  .` .yshyo`:                        -.`                                           
   +yo/:--/h:/:ys  ..  .ddsh::`                   ````  `                                           
   ./+`./+oho+/o+  ```  +y//d:/                 `.-`                                                
  ---  :-:-  ``     `.  .so+ooo-            ``.:-.```                                               
    -+:`.          ..+`  y++o/s+:       -.+-:-`                                                     
     /`.  `   ``  .+oy`  /o:+/-/s/  ``-. `                                                          
     :`- -/. :o++`/:`    :s//s.::+o                                                                 
     ...:.   yo/h/:      `y::s++::o+`                                                               
        """)
def page31():
    page30()
    print("""
    You cruise through the grotto past the wreck of
the submarine and then you spot another ship
wreck. And then another. They, too, are covered
with algae, but they appear undamaged. Maybe
people from Atlantis capture ships in the Bermuda
Triangle and bring them here. Then you see
another ship, but this one is a three-masted
schooner of the type used in the early 1800s. Its
rigging isfestooned with algae, and fish swim lazily
around its mast.
    Your curiosity captures you and you put on your
sea suit. Leaving the Seeker, you move towards
the old sailing ship. Suddenly a thirteen-foot long
deadly poisonous sea snake strikes from behind
the forward cabin and bites you in the soft flesh
between the fingers of your right hand. There is no
antidote to the deadly poison.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page32():
    print("""
    With great sorrow, you decide that it is wisest to
leave the expedition now. You can't risk returning
to the great depths below. So, you reluctantly
return to the United States.
    You are invited to tell of your adventures on
several major television shows. While on one such
show, a special news flash announces to the world
the discovery of Atlantis. You regret your decision,
but you didn't really have a choice. Did you?


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page33():
    print("""
    You can't resist the adventure beneath the sea.
You must go down again, and after several weeks
of rest, you enter the Seeker and slip quickly into
the deep. You bring the Seeker to rest by the great
canyon in the ocean bottom and, wearing your
special suit, you venture out into the depths. There
are no signs of the giant squid and you feel safe.
    Rounding a rock formation, you come upon the
wreck of an ancient Greek ship. How strange to
find this ship, intact, so far below the surface. What
brought it here? Was it visiting Atlantis before the
lost continent slipped beneath the sea?
    You take pictures and make notes in your special
undersea book. Maybe this ancient ship hides
the secret to Atlantis.
_______________________________________

    If you go aboard
the Greek ship, turn to page 45.

    If you return to the surface to
report your findings, turn to page 46.
        """)
    choicex = choice(45, 46)
    if choicex == "45":
        page45()
    if choicex == "46":
        page46()
def page34():
    print("""
    The dolphin looks at you, and you even imagine
that he is smiling at you. You grab one of his
flippers and with a powerfulswitch of his body, the
dolphin swims upward. In a short time, you break
through to the surface. You blink in the brightsun.
The Maray is nowhere in sight. You are lost far at
sea.
    The dolphin dives beneath the surface with you
still clinging to him. He speeds off and within 20
minutes you are next to the Moray. The dolphin
must have heard the Moray's engine noises underneath
the water.
    Once aboard, everyone congratulates you on
your escape. You will go down again, but the
thought keeps haunting you: What if your luck has
run out?
______________________________________

    If you decide to dive again
the next day, turn to page 48.

    If you decide to give up
the expedition, turn to page 47.
        """)
    choicex = choice(48, 47)
    if choicex == "48":
        page48()
    if choicex == "47":
        page47()
def page35():
    print("""
    You suddenly realize the stream of bubbles is
powerful enough to raise the Seeker. You guide
the Seeker into the bubble stream and it heads
towards the surface. As you swirl upward, you
begin to notice increasing amounts of brown
kelp— seaweed. Near the surface, you become
entangled in the seaweed. The instruments in the
Seeker indicate that the propellers and the steering
mechanisms will not work.
    You put on your sea suit and go out to see what
can be done. Once outside in the kelp, you realize
that you can't free the Seeker. You start to swim
for the surface but then you are soon completely
stuck in the clinging seaweed. You are trapped and
unable to go forward or return to the Seeker.
______________________________________

    If you decide to keep struggling
towards the surface, turn to page 50.

    If you decide to rest quietly,
gain strength, and work out a plan,
turn to page 53.
        """)
    choicex = choice(50, 53)
    if choicex == "50":
        page50()
    if choicex == "53":
        page53()
def page36():
    print("""
                                     -ysss/`  .:o+-.-:/:-++.-::/++yhooys/+o/--.`                   -
                                    .s:-+ooo:  .ohh/:ys   .  .oy:.-.```                            -
                                   ``/mo:+osyysdmds:::ososoydmdNNhyysoooyyyyysooooo+++++///+///+oso-
        `````.:-.:::/::/+++os+/oyssyymMNmdhmNNMmdsydhhyhddyssmNhymdyyysoooos+:....````             -
 `.::::/::-:-:ooos+++/o/:+/--.---+.:hhhymddNNdho+-/-.-``-:+:.-+s/+os/+++osyhysysysoyhhssysoyhhhho::-
              `              .`--:++yNmdmmNmhddNho++sh///sdho/+/o+hhhsysyyys++osyys++++++/:/:--.`` -
                                 ...//s+/::o+so+//shhhooo++osososyhmdysysyo+osso:-.`               -
                             `...`-::::-.`/ssyosyssyssyshdNmyosyyhho+oo+:////:..`                  -
                         ./oss::.+o/.-:o/./doos+.:+oso.```..../`.```--.-/`                         -
  ``.........-..:-.....:odmh/:/.//y+-`-+:.++o/+:`.::/- --`:.-.`-.` :`/:`-/-.                       -
.syhyysssddhshmdhssoosdNddho+os+s/sdmm//`++oo/so/`--`` `.`./o:-`o. /.+y-:::/+-                     -
 `--/yo++yyhossoo+/:syyhsdyyoydsoddmmdyso+-:--oyys-.-//..  ::`.-//.:ymsdo: `oos+o+oo////+o+///:-`` -
  `:osoyysyyosooooshdds+sdsssdydmmmNNNMNy/-::syhys.:-`-``   ` +o:soo-osNy:o/-so/oyhhhyhhhysyssoooo+-
     `.///sdhhyyhdhhssssyo+osmmMNMmmddds+o+///:--....`..---.` `.-s-  ./hmmNN:o:  `.-///ossoossssssy-
         `+shdysssosoyddhhmmmNNMmdy+:-+symdmmmdhssdyhyoo+/.``--:oo/`:/shhhddhh.   ``.---:-:-:/oooos-
.+-`        `+ysysoosyyddhdNmdhs/:+ohdmNmNMNmNmmdNNmNmdmNmdsoo+o+:/:--odhmddNNo                    -
-mms-.      +mmmhs..shydyoo+//+yhmNMMMMNNmNNmMMMNNNmmMNMNmNmNmmNNNmh/..:shohNNM:    ``````....`    -
-NNNd+-   `sNhmh`::..--:/osdhNMMMNMMMMMMMMMMMMMMMMMMMMMMMNMMNNMNNNNNmy:` ./+ydmh`  ``.:..-/sssyoooo-
-MNMMNy:  sMhyh.-oos/:+ymNNMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMNmdsoo-+yyd/          `.:/+syy-
.ydMMMMd-+Nmhdyoyhso/yhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmNMNMMNd+.:ssyo:            `-+s-
-myhNMMMmmNNmMNNmMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMNho`:++yd/   ``````.::+sy-
-mmdhNMMMNmNdNhmmNshNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMNmy+/hhhNdy++ssssyssyymdy-
.mMMNdNMNmmdhh+.+s:hmNmdhmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmMMNNdhMmMNNdyydhyhdyo++/--
.hdMMMdMhNmNhd/`o:dNMMMMNNddhyssyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMNmhMNMNNMyoh+/::--``  -
-dNMNMNMmMmdd/:`/sMNMMMMMMMMMMMmdyyysyhdddmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdodymNhMd`.          -
-MMMMNMNmNhdh+o:+NMNMMMMMMMMMMMMMMMNmmmmdyyyoyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmsyhyNhdM:        `-:-
-MMMMMddNMmhyhmodMmNMMMMMMMMMMMMMMMMNmmNNmdmhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyooymNhh+     `-/sdm-
-MMMMMNmNMNNhdNhmNNMMMMMMMMMMMMMMmmNMMNNNNmNmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmoymmdhs   `/oymNmd-
-NNMMMMNMMNMmdyNMMMMMMMMMMMMMMMMMMNhhmMNMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNssdNdNy .+hNdmmyhs-
-MMMNNMMMMMMNhhMMMMMMMMMMMMMMMMMMMMMmdmsdhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyhMmM+/mNNNmhhdhy-
-NMMMMMMMMMMd./NMMMMMMMMMMMMMMMMMMMMMMh-://dMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMhsNdMdMhNMNmmNNNmmm-
-MMMMMMNMMMMMh.yMMMMMMMMMMMMMMMMMMMMMMdNmmhhNMMMMMMmmNMMMMMMMMMMMMMMMMMMMMMMMMMMsmmdMmMNMMMMNMNMMdh-
-NNNNNNNNMMMMMm-MMMMMMMMMMMMMMMMMMMMMm:Nds`s/mMMMMMNNmMMMMMMMMMMMMMMMMMMMMMMMMMMdMhdmdMMMMNNNmdddhy-
-dMMMMNNMMMMMMM-dMMMMMMMMMMMMMMMMMMMM/oMhh.sy/yMMMMMMdMdmMMMMMMMMMMMNNNMMMMMMMMMNmdhydNMMMNmmhmmmmm-
-mdmmNNMMNMMMMMo+mMMMMMMMMMMMMMMMMMMd`dMhh.sMm++mMMMMMMhNMMMMMMMMMMMMMMMMMMMNMMMNymNNmMMNNNNNNNdNNN-
-ddmNMMNdMMMMMMos-dMMMMMMMMMMMMMMMMM/oNNhN/hMMNh/odNMMMdMMMMMMMNMMMMMMMNMMMMNNMMdmmNdMMMNNMNNMMMMMN-
-NMMMMddMMMMMMm/d/`dMMNMMMMMMMMMMMMm-mNyhMyMMNsmds//NMMNMhNMMMMMMMMMMMNNMMNNMMMdNMMNNMMmNmNNmmhmNhh-
-NNNdymMMMMMMMmsdy:.NMMMMMMMMMNoMMNmsMMmNMNMMMmm/sshNMMMMMMMMMMMMMMMMmMMMMNMMMNNMMMMMMMMMMMMMMmdhys-
-NmhdMMMMMMMMMNsmdd:+MMMMMMMMMMMMMmsdMNhNMmhhmMMdNMMMMMMMMMMNNoNMMmdNNMMNMMMMNNMMMMMMMMNNMNMMMNMMNm-
.+:NMMMMMMMMMMMhsmmho:dMMMMMMMNhmNh`/MdmMhssmydMMMMMMMMMNNMNNhmmMmmmmMMMMmhmMNMMMMMNmMMMMNNNNNMNNMN-
  .MMMMMMMMMMMMMNddNdo-:dMMMMMMMmNMmMMh-hmyhmmMMMMMMMMMMMNNMMMNoNNNNMMNs+hNNdMMMMMMMNmmMMMMMNNNNmdd-
 `.NMMMMMMMMMMMMMMdshNmo./sNMMMMMMMMMMMs`yMm/+mMMNMMNMMMMMMMMMMMmNNMmosdNNNdMMNydMmMNMmmNMMMMMMMMMm-
 - /MMMMMMMMMMMMMMMmhs+yyo..:hNMMMMdodMMh`sMMh-+NMMMNMMMMMMMMMMMymho/NMMNMMMMh.+yMNmMMMMNmmNNMNMMMN-
`:- -mMMMMMMMNMMMmNMdsho+yys/oyhdNN:+msMMd.:dMMs-dMMMMMMMMMMMMNdy+/hdmdMMMMm:  shMMmmMMMMMMmhddNNNN-
 o-`  NMMMMMMMMMNNmMM/ddhsoooymNMd-yMMmymmm- sMMN+NMMMMMdhsds.+oydhm/NMMMMM-   /dMMMmNMMNMMMMMNhhyh-
 +.-  NMMMMMMMMNNNNMMNNsyhyNmdNNs-dNMMMmyMdm+ /MNmdddNN+.yo+mNmmmNMMNmhdMMy    sdMMMMNhNmmMMMMMmmss-
 :.-` dMMMMMMMMmMNmMNMMMNhssmMh::hMMMMMMNhmsMs-mNNMMNyssoMNdhMmmMMMMMNNNmm`    odMNMMNNdmmMMNMMNNNm-
 ..-. -mMMMMMMMNMMMMmmNMMMMMMN/ohmNmMMMMMMNMNmNNNMMMNNNmddoo+mmyhmNMMMMMd-:+-  ++MMNNMMNmdmNMMMMNMN-
 ./-//:/dMMMMMNMmMMMNdmNMMMMMMmNmmNNMMNNMNMmNNMMhydMMMMMMdmNmmmMdhhdhNNy`:--   .oNNmmmNNmNdNMMMNdmm-
-hyyshhdyymMMMMMmMMMMMNNNNMMMMMMNNNNNMmNmMmNNNNNdydhMdNMymhydmmdhosdNdhd:/-`-.  +dNNdmNNNMNNNNMNMNm-
.hyyhyhhhydNMMMMNNNMMMMMMNNNmNMMMMMMMMMMNNNMNMmmMNmNMhdy++ddhdyohNMNNN+mNd/`/.` +yNNNNNMNMmNhdmNms--
`.:o+soyyhoydNMMmmNNMMMMMMMmmmNMMMMMMMMMMMMMMMMNNMMh:/+m++odyyhhyyyyhmoydmMd:   :sNNMNNmdNmdsdo:`  -
  ....++hdymddNMMNNmMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMd++m/+ddNdyossyyhdddhsyyhdy+..:+oydNMdhyo:-`     -
       ...-`-///+dMMNNMMMMMMMMMMMMMNNMMMMMMMMMMMMMmmhyyNmNyMdo-/o+oshmNoNmmhhhNs..+:-o+.`          -
        `.`.. `` `-sdNMMMMMMMMNNMMMMMNMNMMMMMMMMMMMNNNMMNyNNyMm+.:+ossdydNdNdyymm+--+:./-          -
          ```.` ``` `.odNNMMMNNmMMMMMMNNMMMMMMMMMMMMMNmM+dNNNmyMy/.:+oydsNhysdhsdNh::+-.o/-`       -
 ........  `.``.` ..`  `-/+sNNNmMmys+:.-odmNMMMMMMMMMmmy-MMMMMNMymh/./oh+/sdNmmmsyddsmmy:`-::      -
 ``.-:///+oo///---..`.``   sNNMNMs       ``.:dNMNMs+:.+/oNNMMMMMNNdms-o-+yohdNNdN/.o`:dM:/-//.     -
      `.-:/+ossooosso:-.-./mNNMMM:          -dhmNM.    -ohhdNMNho++o:+///+ohNdyod//.-odN.` `-.     -
           ```.--:+ssyyssyNMMMMMm..`        .dhmNMo     .+yhNy.     `-/-://dsNo/syhhs+shhs/`.`     -
                   `-:+++hMMMMMMdo+osso:---`-mmNmMm.     -/yh.  ``.-/+ys:/mMydy//:/-+oyo/-.``..``  -
                        .hNMMMMMs/+shdhyssyhhNNMNMMh///syoyyhs/osoosyymNooMMNmmNNNNho//++o+-. .-:+`-
                        +NMMMMMM/....:://sossyNNNNNmdhddmdmNNNNmhdNMMMMMmNMMMMNMMNNMmddoooyyy:.  +s-
                       `dMMNMMMM/`.-....:----.so/-//sydNmNmmddhmmMMMMMNNdNMMmdMmNmmNmNmdddhdyoo+o:d-
                       -MMNMMMMM-   ```---...+oo:.-yhmdddddsso:..--/sdmMMMMMMNNmmNdNMNNdsos```-:soy-
.o++/:--/:-.``         /MMdMMMMM.     .-.`.``ossohdMNdsys/:.`        `./sdNMMMMNMNNNNNMMmh`     ``+-
.soooo+ooooo+//:+:..`` +MMNMMMMm      /.  `  .hmNNMNNMs:..`              `.NMMMNmNNNNNMMM: /y: -:sd-
 --:://///////+///+o+::sMMMMMMMs      +   `   `sNMMssNMh::...`            `NMMMMMMMMMMMMm:-dNdsyhNd-
 ```-://+//+++oo+o+osssyyNNMMMM+-...` /`  `     /MMMh+dMm:-----.`          -+hdMMMMMMMMMMNmmmmmsmmy-
 `.:++//s//++++++sssos++hhmMMMdosooo//o/-..`    `NmNMNooNm- `----..`         `yydMMmNMMMMMMMNNNmmys-
   ```````..--/+/++//+osddmMMmsysys/ossyss+o//:--ddydMMh/yd+`  `.---..`       ```/mhMMMMMNNMMMN//y:-
                     ``-oyNMN:-/+//++oososooo+oosdNmyhyNN-/:-.    `--...`         .yNMNNMNo+:/- `` -
                        .omM/      `.-/+ssso+ss+oodyshymmyo+/y/..````--.`.`         :mMNmMy`       -
                         hMs            `::://++o+yhodyyyhmmds-:ooyoo+o+o::--..```   .yMmmNh-      -
                         oy               `.`.`.--.-y/-/+osymh:`  `.yoyssyyysyysooo++/-oNhyhd-     -
         `````.--//.-`                      `.``.....`     `--/o:`.:oos/yyods+sssossssyydmdddys++/--
         `.....-:::/os/---/////.`             `..`..-..`        .++:::/-:..o:::+sydsddhdhmd+`//+sds-
            `-.-+++++ooo++s/:-:///.-.``          `.`...-:..`     ./`.//:   `- .``.--//+/ooo `:-.-oy-
            //:::/o+++oooossso+oos++syy+++/:.-`      .`..-.--:-...` `.``    `. `.         `-/`.-.//-
                 .:--//++/++ossoooo+oooo++/so+///:::`    `..`..:-.-```        .` .`       `+/     .-
                     ```-:---++osss++//oss/:///+////:..`                       `. `.`  `.  -       -
                             ...::++++/+oo+oo+///o/o:-:-.``                      `` `.`  `..       -
                               `...//+ooo//os+/+o+oy++so++:--.``                   `.` `...`.-----.-
                                    ``.-::::-:+-:+//:/:/:++o/o+++/..                  `...`-:--..``-
                                         .:+++:---::::::::::-/::-://-:::-..                        -
                                                   -//+/:-:/+/:--:+++o+///+//--:-.`                -
                                             `..-.....-.---://///++oso+os++:/oossoooooo++/-.:...   -
                                             `.-...-.-//:/+o+/::::/:/::::::::/++oo//+o+://++//+:-.`-
        """)
def page37():
    page36()
    print("""
    The dolphin might help and might not. You
decide to chance it alone. So, up you head, swimming
towards the surface. The dolphin follows for
some time, and then swims off. You rest for awhile
about 300 feet below the surface before your final
ascent.
    Then a large fish— ugly, lumpy, puffed up, and
covered with black and white markings swims towards
you. Its bulging eyes fasten on you. It is a
big-mouthed grouper, a fish which does not
bother to bite its victims, butsimply swallowsthem
whole.
    It looks as though you are its next meal.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page38():
    print("""
    You decide to guide the Seeker into the new
passageway to the bubble source. Suddenly the
Seeker is swept downward as if pulled by a giant
magnet. You lose consciousness. When you
awake, you are in a well-lighted and comfortable
room. Three people are standing close to you.
They look normal and appear to be friendly.
    The middle one speaks. "You are in the nether
region of Atlantis. Thisis a visitors'reception room.
If you wish to come into the city of Atlantis, then
follow us; but you may never return to your world.
If you wish to leave now, we will escort you safely
to the surface. It is your choice. We do not wish to
harm you."
_____________________________________

    If you follow them into
the city of Atlantis, turn to page 55.

    If you decide to return
to the surface, turn to page 51.
        """)
    choicex = choice(55, 51)
    if choicex == "55":
        page55()
    if choicex == "51":
        page51()
def page39():
    print("""
    You are led to a room. The floors are a rich
marble. The walls glow. The ceiling is like being
inside a diamond looking through the many facets.
    A person who immediately commands respect
beckons you with firmness and kindness to come
to her.
    "Welcome to Atlantis. Thousands of years ago
we learned that we were about to slip into the sea.
Our people prepared for the calamity by building a
new city inside an extinct volcano. We have lived
here in peace and harmony ever since. We have
no sunlight, nor stars to gaze at, but we have other
spaces to meditate upon."
    She tells you about a group of people called the
Nodoors. If you wish, you can live with them, but
you cannot leave Atlantis.
    A bearded man is to be your escort. Atlantis is a
beautiful city. Buildings merge one into another,
colors radiate light, and coral branches fill courtyards.
There is a sense of well-being and peace.
    It would be pleasant here, but you don't want to
be a prisoner. Maybe there would be a better
chance to escape if you join the Nodoors. You ask
your guide about them.
    "Oh, we believe they are dangerous, but we
don't really know. They live in the center of the old
volcano. If you wish, I can take you there."
______________________________________

    If you decide to join the Nodoors,
turn to page 56.

    If you decide to remain with
the Atlanteans and perhaps get a
chance to escape, turn to page 57.
        """)
    choicex = choice(56, 57)
    if choicex == "56":
        page56()
    if choicex == "57":
        page57()
def page40():
    print("""
    The Atlanteans have lived in peace for thousands
of years. They have no love of warfare. Their
civilization is technologically very advanced and a
sensing mechanism tells them that you are about
to use your laser cannon. They quickly fire a special
beam at the Seeker that makes all its functions
stop. You are now powerlessto escape. They walk
up calmly to the Seeker and tell you to come with
them to Atlantis.
    "You are now part of Atlantis. We understand
your fear, but do not be frightened. No harm will
come to you and your life will be full. Follow us."
    As you walk with them, into a new world, you
wonder if you will ever see the sky again.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
    print("""                                                                                       
                   .--..                .::::-.                                                    
                `oNdMmMo             `+mMMMMMNMNhs/`                                               
               /NNdmMMMNNNMNmds+.   `dMMMMMMMMM+.:sddo`                                            
              :MmdMMMmyddMMMMMMMMd- oMMMMMMMMMM:   .`       ``-:--:-``                             
              dNmMMN+`-::/MMMMMMMMN-NMMMMMMMMMh`:o/::     `-`o+so+:/o-..                           
              odddMN-:/s++NMMMNNmym:dMMMMMMMMh` ./.`-   `: .`..+omsy//:-o                          
              `-`+MMmyoodNMMN/ /y:. /MMMMNs+: `.  .:.-  +..`.  +o.:/`./os                          
                `/MMMMMMMMmo.  `..-  NMMN-`:/  .`-./   `o../- -.  -/-//+.                          
               ss/MMMMMNo+`     ./.  dMMd/::y      :    ./NNs+`    `.:-:.                          
               .sdyyhd+`/o-    /o`   `+hsy+syy.    ..    :NM+..    ``.:-                           
                    `./ .:`...`/`.-/.:-:sdh::+s+`   :`    -//      ``:-`                           
                  :y:.+/-:`:```-o+-+/+:/dyo:.:-o+/:::`     .y/+.-    /.                            
               `:`hyo/.--.s-  o+:    `/-ydyoso/sos+/:      md+`  .-+:`                             
              -s. .oo+ys+hN+:-h:-    .-/om:`.    :h+y    .-hMNmd+` md                              
            .:.``.. `:+ommy/-yhyyo. .::yMmo-. .:o+ssoo/+yNN/.+hdMmhNs--                            
           /-.    -      +y/-mhho:/:-:yNNdm:/oo/+/++oshNmo.     .oo/  .+`                          
         `shys+-  /`      /.oddddhyshNMMMMNy:``.o/    `/.   -..`.-``/...o                          
        `++ohy/do--.        /ddms++oNMMMNN+o++:---.-.``.::---:: `` `- ::o.                         
       `sho:/ssms+.`         syo:+oNMMMMmhsso/   .`-/-/osyy+ -          -/                         
       /+shyyhyss--/-.`   `-/yhso+dMMMMMMh/ss+.  :`/y+shmmdo`+/.      .///                         
      -hys/:+dss/```:o++o++hs+yo+yMMMMMMM/dmN+o``+.+d`/dMMm/ /         `-+                         
      dmddhh/+yo+/.  `.`   /sso+-`yMMMMMN:hmm/y`-y..m-:sMMy: -`.       `.::                        
     .oy//so .yoy:.`      .+ho/ -.oNdymMMo+soh- od:-mo/dmds+`:--      -:+/+:--.                    
     `s+s-:/` ys+++/.    / hy/:/+oshdNdhhshyh-  os+-+//hdNo. :         `+s.    /hs/:`              
      +++.  : .y/s://` .+`.::osyNMMMmdhhhhdys-..s+. `.-`.:/:`:::     `:+o.  :dNMMNdyds....`        
       /o+  :` :yys+s/:+-+/:    `osoyydmNMMNo--/ ``.:. `+:-`-`         /+/-` +MMMMo..`  -+-/-      
       `+sy:-:  +MNNMMNNMNy/     :dhysoossdhdMNNNh/``--o-   :``       `-  ./+yMMMNy.   `+s+//.`    
        -/+o`:  omMNdymmooo-    .mMmdNNMNoydMMMMMMo:-  o`  `-::     ./:       `/yh/``.-.-:-:-`-`   
         ::+:/::-+NNo.yh  .-   .mMNNNMMMyyyMMMMMMMh:   o`..-.-.-.--..-.               `.``         
          ods:+s-dMMNshNs `/   dMmNMmMMMhddMNhhdMyy::.`y`         - .-                             
          `+:.`:+doh:+hsy `:  /MMNMMMMMMdmmMdosmNsh+` `N:         : /`                             
           `:   /mNMyyNNh .o  hMMNMMMMMMMMMMdyhdNddy:.`Mh    :    :-o:                             
            ::`:--ddhhhdm .-:  sMMMMNyhMNNMNMMMMMdsyoyhMN.  -:    ss-.                             
            -dy:::+ddoshd`  :` `dMMMh +NmdNNMMMNNh/s:-. `:````.  `h`+.                             
            `hyysody///:.    /  yMNNh`oNmmmNMMMMMddo    `++` `  `o:-+s`                            
             oy+++o/         -..NMMMhoNNyyhNNNMmmo++`    ++::  `:.`. `:`                           
             :ys+s..          /oMMMm`.hmNdNMNmNdN/-+./-/::s:` `-`-:-   /                           
             :hsoo`-          /mMMM+ oNdhdMMNmNmdo`/  .-//:.` +.:.``   `-                          
             +syo/:+          .MMMM/ mdhh-hMMdmNMd:/`  ````  +//:.-...  :                          
        """)
def page41():
    print("""
    You are greeted by a group of people who look
like ordinary human beings except that there are
gill-like slits on their necks. Their bare feet have
skin between the toes forming a web. They order
you to put on your sea suit, pull you quickly from
the Seeker, and lead you towards their city. On the
way they show you the zoo where there are animals
from the world above the sea. There is a
glass-like cage surrounding them filled with air,
allowing them to live below the sea.
    The leader of the group explains that if you wish
you may either submit to an operation to have gills
inserted so that you may breathe underwater, or
you may join the other animals in the zoo.
_____________________________________

    If you agree to the operation,
turn to page 58.

    If you go to the zoo, turn to page 59.
        """)
    choicex = choice(58, 59)
    if choicex == "58":
        page58()
    if choicex == "59":
        page59()
def page42():
    print("""
    Back aboard the Seeker, you radio the Maray
that you are surfacing to make a plan. While rising
out of the giant crevice-like canyon, you spot what
appears to be a road running along the top of the
ledge. What is this? The scientists aboard the
Maray had mentioned the possibilities of finding
signs of the ancient civilization, such asroads. You
must investigate.


        """)
    page6()
def page43():
    print("""
    You escape being seen by the submarine craft.
Following the instructions you enter a passageway.
At the end of the passageway is an airlock
door and beyond it an incredibly large air-filled
cavern. Perhaps it is the inside of an extinct volcano.
    The land is pleasant, although strange to your
experience. A softsubstance covers the ground. It
seems to be alive. You can't tell. A gentle light
comes from the sides of this huge cavern. It reminds
you of early morning light just before the
sun rises.
    A group of people approach you with friendly
gestures. They are wearing simple clothes much
like the clothes people wore in ancient Greece.
They are kind and generous. You remove your
diving suit to find that the air is good to breathe.
    These people speak a language that is unknown
to you, but one of them acts as an interpreter. You
find out that this is Atlantis. They tell you it is
governed by a man who is greedy, selfish, and
dangerous. The people are like slaves. Everyone is
unhappy except a few who serve the ruler as his
lieutenants. These new friends ask for your help.
Perhaps you can help them escape.
______________________________________

    If you decide to leave
your new friends and search for
the ruler, turn to page 60.

    If you decide to help your
new friends escape, turn to page 61.
        """)
    choicex = choice(60, 61)
    if choicex == "60":
        page60()
    if choicex == "61":
        page61()
def page44():
    print("""
    Quickly you get into the Seeker in an attempt to
escape the strange submarine. You notice that the
sub is chasing you so you put on full emergency
ascent power. You could use your laser cannon to
blast the sub, but you do not wish to hurt anyone.
    The ascent towards the surface is swift, but a few
fathoms from the surface all systems on the Seeker
fail. You are suspended in the water in a helpless
position. It seems that a mysterious force has disabled
you.

                                           ````                            ```     `  `  `---:::.   
                                    ` .``.````.:-  `              `.:-.   :s.:/-..`:/:.-y+++symM+   
                               `````   `-  -/::o`//     ` .`.```.` oo.-:. :/-`--:-hddNd+.  -mMMd    
                          ```.``         .`-:.:/+:-    `` ---/....-:-``--:soooyso:yo:o.  `` -Mm`    
                     `--..`              - `..- ` ```..`-++/  -/--/-.` -..-/+-ymds/-` ./syy.`d.     
                 `/+/.`                  -     ````:o`y/:```.-+h//-:--./.++:-oo+-`-.-+++:`  :.      
            .`... .                     .``.``    .:+:`.-/+/++ss-::.`:-`hds/-..`.:hm/`    `.        
         ``:+.`                       `./-.       .-/o/sdo-`./-`.-o/+/ss:.`:/-:/+oh`     -.         
        `.                        .`...`      `-+ydNNhsoo   ::yo:oy-+..    -hmy//-`-..`--`          
                              `..-...`       -sNd:``:mN//oyo/./::-`         -+`-/+-.`  ``` `.`      
                           `..:-+::`        -sMMs ```/sMhoho/-`   /os//      `./             `-     
                        `-.-+/.--          -//--yh/:`-hy/.`   -  :sysh:     .+//:-.....` ``...`     
                      .--/--`.-`           /mNmNdss//-. --`  :md/++yo:      ``./:.`.```.-``-`       
                  `--.o-+.o`-              +hhy+:-     +NNmh sNms:          `-.`--`  `-../.         
               .--.    /s /.               .`         .ydhd- :.           --.``-`  `..--.           
            ``.`       :s+                   .``  ``     --            .--``.`   ...--:             
        ---`         `.+-..          `.``.---.    ```-`            `-/:  `.`    :...`               
`//--..-.`        `...ommo`-`  `.----.``       .-/++-...`...    `:o/-        `:.`/-                 
::- -y..-.     ``.-yy. `/`-.+///:``           ./::-:`-..``.:-/-++.`        `.` :`.                  
.`  .-:.-y     do:. :o- -shdos`        .:::::.`-.:-:....-::::/.           `.`o:                     
      -y:-. `-.//+/  -sh/.hMoy `--/++++//+so:. `.:------``-.` ``       -- `..`                      
`    `.-- :-/```:.:/-/.No-+yhosyysosossso:-::.-.`..   ...````        -.  `--                        
-`    /-     .```.`:s..s+--`   `-..    `      :/.` .:/` .-.        -. `--`                          
 :`  `:.        ---yd..    .-`..  `.-.`  `+:--  `-.`  ..`        `.    `                            
.`      :`      `/.      ..`   `-.:`  :-.:-   `-` `.``                                              
      .:.   `` . ../        --/`  ``:.`        `...`                                                
      -. -   `/. `.- `.  .-``    ..          `.:.                                                   
   .. ``.   .:...- `.:`` `:.              `:-.                                                      
   /.::.  `        -.+-:/:..           .-:--                                                        
   ..:..  -` `..`:.`+-`.-`           `.:`                                                           
`         ` ../+`  ..`.`           .``                                                              
                   .``-.                                                                            
 `...`     `::  ` ` `:                                                                              
.--`.:   `..+...:---                                                                                
.. .      -./.`--                                                                                   
:        -    `                                                                                     
:..-`-s+.`                                                                                          
`-/:o+/-                                                                                            
--:..-                                                                                              
  ```
    If you decide to wait on board
the Seeker for help from the Maray,
turn to page 64.

    If you try to escape from
the Seeker and try for the surface on
your own, tum to page 63.
        """)
    choicex = choice(64, 63)
    if choicex == "64":
        page64()
    if choicex == "63":
        page63()
def page45():
    print("""
    Cautiously you enter the ship's cabin. Clay jugs
called amphorae, once filled with oils and wines, are
strewn about. There are no remains of the crew.
You do have a sense of being in ancient Greece
and it is a strange feeling.
    A door leads to a smaller cabin. On a table near
the rear of this cabin is a golden box. You open it
and find the remains of a map. It does not show
Atlantis. It shows that the ship was searching for a
hole that leads to the center of the earth!
    You return to the Seeker and use the map to
locate this incredible shaft to the center of the
earth. Using some guesswork to interpret the map,
you discover the tunnel opening, which appears to
be roughly 100 feet in diameter. The sonar
readings indicate the hole has no bottom.
_____________________________________

    If you decide to descend into the hole,
turn to page 65.

    If you decide it is time to go
back up to the surface, turn to page 66.
        """)
    choicex = choice(65, 66)
    if choicex == "65":
        page65()
    if choicex == "66":
        page66()
def page46():
    print("""
    The trip back to the surface is smooth, and
finally the Seekeris hauled aboard the Maray. You
climb out and are greeted by the scientists and
crew. The Seeker is prepared for the second dive,
but suddenly the wind rises and the sea kicks up
into furious waves that crash over the deck of the
Maray. All hands rush to prepare for hurricane
force winds. There is no chance for the second
dive to begin. All day and all night the Maray
pitches on the stormy sea.
    The next morning the wind has died and the sky
clear. You are now ready to dive again.

        """)
    page48()
def page47():
    print("""
    A helicopter is sent to pick you up and return
you to an air base for a flight back to the United
States. Newspaper reports indicate that the search
for Atlantis has been given up. Several months
later, however, a group of scientists get in touch
with you because they believe that Atlantis can be
found. They have put together another expedition
and want you to join it. You are tempted. Adventure
into the unknown is what you like.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page48():
    print("""
    Again the Seeker is lowered over the side of the
Maray and slipsinto the ocean. Fish swim by peering
cautiously at you in your metal shell. The sunlight
fades as you descend into the abyss.
    You are headed for the giant canyon below that
might lead to Atlantis. When you reach the canyon
you switch on the Seeker's searchlight. Immediately
you spot the round hole that appears to
be made by intelligent beings. Perhaps it leads to
Atlantis.

        """)
    page49()
    page9()
def page49():
    print("""
                                                                                                    
                                                                                                    
                         `:/``.`                                                                    
                      `..-mm+-``..`...`.-`                                                          
                   `..`   -+:+/-......-m++h                                                         
                `..`   `.oo/-``:hy:...-:.sy                                                         
             ...`    ...`-/-:os+:.-`    .yy                                                         
          `.hNs `. .-.s-/yys+-           +/                                                         
        `.``:+oydy-/. .//.`              :-                                                         
      `.`     ym++`+-.`                  -`                                                         
.  `..`       /sys`..                    /                                                          
``.`    `..  -:so.y:      `-`            +                                                          
``      /yo-.`sd:`-h`     /s+            /                                                          
.:-`   `/s/-`.:-   h+`  `-+o`            -                                                          
.`//   /sm/:--`    -s:  /-ss`            -                                                          
--/o``..:s.om:````..o/..os+--`           -                                                          
.::::///:::+o:::::////::::/:+.           -                                                          
                         `s-:            :                                                          
.:-------....-s/.....``.`+y:-            +                                                          
oMNNMMMMMNNNNNNNNNNmmmmmmNNh`            :                                                          
oMMMMMMMMMMMMMMMMMMMMMMMMMM/             -                                                          
oMMMMMMMMMMMMMMMMMMMMMMMMMm             `-                                                          
+NmNMMMNMMMMMMMMMMMMMMMNMM/             .:                                                          
:s/osyo+o+ssshhysssoo++++s::.-..````    -:                                                          
-o-:+shho++/:/osys+/+/sysyos/..  ``..   .-                                                          
:soo/++o/++/oysoyyssoos+o.```           .`                                                          
`:--.-..``..```.-/:/oydd+`              :`                                                          
      `:/+oo+oso::///+so+.              :`                                                          
``...`.---//++yho--:---//-              -                                                           
  -:+sys::.    .:+yhys ``               /                                                           
--             `-.--.-:                 +                                                           
-:`          `   `///.:-                +                                                           
::         `.oy/:/`                     :                                                           
`:-          `-o+/                      -                                                           
              .s:`                      +                                                           
               ``                       +                                                           
                                        /                                                           
                                        -                                                           
                                        :                                                           
                                       `-                                                           
                                       `.                                                           
                                       ..                                                           
                                       :.                                                           
                                       :.                                                           
                                       -                                                            
                                       -                                                            
                                       /                                                            
                                       +                                                            
                                       /                                                            
                                       -                                                            
                                       -                                                            
                                       :                                                            
                                       -                                                            
                                       :                                                            
         .`                           `/                                                            
         `...`                        `:                                                            
             ...                      `.                                                            
                .- ``                 `.                                                            
              . ..o/.-..`             --                                                            
                  `.:`--.`...`   ``   --                                                            
                    `:`       ` ``//::++`                                                           
                      :`    .-://.    -`  ``                                                        
                       /       `.-:-  /  -::                                                        
                       .-            `o :/o:                                                        
               .    ``  /            /+ /-::                                                        
           `-../+dNs:-``+`       ```:./-/ .`                                                        
               .-NM+``..+:.`..:.+yssy/`os`                                                          
               smhm.    :       :yhdooydm+:                                                         
               hM/:     +       /o+/oymN://                                                         
            ```sN+/.``.`o       os-.NMmd:so::+-...`                                                 
               `:h/--:+:h..-:--+h/`.mN/+`/:o.`````                                                  
               `+o./.-:.y.`-.-+ydsosmMd/syy+-                                            ```````    
  -o+/:--:--:hdd+o.::..`.``` `/oo++ssss+/+/:..-..o/.`....`.-.````  `````.....`---....`.```  `       
  /dmNNmmmhsoo+/-`            :/.:`:--+`      ``./:oo:so/+:-::::::-/---....````     .           ``  
  /mmNMmMmMNMMNNmmdhso/:-..``+s.                  `..`++mso/:````       `           .`              
  `--/+sdNNNMNNNNNNMMMMNNmmmmNdh++//:---...```        .o/+h+`           `     `            `--.-.:/-
     ``.-/dNMNmddhhdhdyydhmNmNNNNMNMMNNNNmmmdddhhyyysoossosyy+:.`       .`    ..          ./+-+/o+s:
       `:sshmMMMNmddym+ssyshyhmyhmmdhmmNNmNNMMMMMMMMMMMMMMMMMhsyso/:.` `-`                 -+ysddhN+
        +shoydmmmhNMNNhmydydhhdsydyhhhmmhyhddmMmNmMMMMMMMMMMMs/hdyyss+//-.`                  /+-..- 
        /dddmy::+dNMMMMNNNNMMMNhyhdNNmmmhyyhmdmmMdMMMMMMMMMMdyysso/o/..:+os+:.``        ``    `     
          ```. ``.+sdmNMMMMMMMMMNMMMMMMMmmdmNNMNMNNMMMMMMmdh///`         `-:++oos:.```           `  
               `.``..-/shmmNNMNMMMMMMMNMNMMMMMMMMMMMMMMs:`      ....`...` :/ooosddhyyo/.`           
                         ..::::+ssyyyyyhhhhyyyyso//++yo                       `-.-:+ooys+++-``   -:/
                                          `....   ` . -                             ```.:+yso++:.```
                           ..-::-::-.`        ````... .-``      ``` .:--.`..`              ```-:/-.`
                                ..-:--//--.-..``   .   -              `.-.:::-:.`                   
                                        `-..:///--`.   :/-`                 `.....-:.`..`           
                                       `://+s///ooo  ` .o+:...`                         ``.```      
                                            ./osss/`` ` hhs/+.```.                                  
                                              `-:s`-o.  +s+:`                                       
                                                 - . `.-.``                                         
                                                .`       .                                          
        """)
def page50():
    print("""
    You are dizzy from lack of oxygen and fatigue.
With your knife you slash away at the heavy brown
kelp thatsurrounds you. Bit by bit, you seem to be
getting free. Then suddenly you shoot up through
the last clinging pieces of seaweed and reach the
surface. You fire the special signal flare and the
crew of the Maray quickly spot you. Within a few
moments you are safely aboard, surrounded by
your friends. What a relief to be out of that nightmare
world!
_______________________________________

    If you dive again the next day,
turn to page 67.

    If you want to rest a few days and
make emergency plans, turn to page 68
        """)
    choicex = choice(67, 68)
    if choicex == "67":
        page67()
    if choicex == "68":
        page68()
def page51():
    print("""
    The three people of Atlantis sense your wish to
return to the surface. Instantly, they produce a
bubble-shaped capsule and put you inside.
"Farewell, earth person. May you live a long
and prosperous life."
    You shoot up swiftly through the sea and break
out onto the surface near the Maray. The capsule
that protected you disintegrates upon reaching the
surface. Once aboard the Maray, you tell the crew
and the scientists about your adventure. They are
kind to you, but no one believes you. They think
you have imagined the world of Atlantis as a result
of being so deep for so long.
    Back in the United States, you begin a television
tour telling about Atlantis. You write articles and a
book. You are paid a great deal of money for this
work. You are tempted to use this money for
another expedition.
______________________________________

    If you use your money for
another expedition, turn to page 72.

    If you decide to retire and
lead a life of ease, turn to page 74.
        """)
    choicex = choice(72, 74)
    if choicex == "72":
        page72()
    if choicex == "74":
        page74()
def page52():
    print("""
mhmdddyddhmNmdmNy:/-.-:-:.``..///::/++/----.--..--:sshh+``...``````````------```````````````````````
yhdhhssyddmmmmMh/:::-.......-:-....```..`---.-.-hmddhs:.``  ``               `.                     
yyhhsdhdhddmNMNN+.`                          .sNMNdo.  ``...`     `` `..`                           
yhdhhhysydNmNNMMNNNh:.                    `:sys--`            .-`...``.```    `                     
hydyhhhmmdmdmMNMMNs```.`.`..`` ```.....:+hh:-..-.`..``.``` .  `` ````  ```   -+                     
yysyhdhdyhhhdmmmNm/````        /:`      .-`            ``..`.`.```..........`+..-                   
yhhdhhhdyhydmdmNNm+:.-....`.-:/:s+-.`                                ``````.//.:-.``                
dyhyhdmdyshhmNNNh.-          ``.//++++:-``..`.` `                          -y:o-`.`.`.`             
ooysyohmmmmmNNNmh:.....---..````` ..+/o/+...                        `     .-/-.     ``````          
syyoosohdmNNNNNNMs::                  .oss/.:...`.```          `    `````::-h:           `.  `      
hossso+ydNNMNNNmNd:.```                 -hNmmh/+.  ```.``````         `-:``:/.`               `.``  
yyyddysyydmNNMNNmmo` ``.`.```.`````.`    .mMdh:-         `` `` `` ``-+-:+-::`  `````              `.
hhhhhmhhmddmmmNNNNh:......```` `   ``.``  hMdo`       ```:-/:/..:/:..+:+o:s-       ````             
hhyyhddddhmdmdNNNyo-:.--.-++:-.- ``` ``  `dMms    .-.:/-//:+++/o//----:+yy+.          ..```         
hhhddmmdmdddNNNMN:.``    +o+`    ...````.+mdd+``.:.//:-/::--:+/--``` ````.-.````  `       `.``   `  
dhhdNmmmddmmNMNNN:..`.```/+/.` `..`..`.`:ddmN-``:+++o/....``-``         .```  ````:so.       `.`--.:
ysdNddmyhddmNNNmmy-``````:`---/......``/mNmmm-..:/y/o-....``````                  `o:`` `      .-:dN
yddmhhhdyhdmmmmmmd:`     -`.-``    `` odyshNh..:/os/+.````` ```.-...````  `       -o- ````  ````:/MM
mNmdmmhhdhddhNNmm/      `/./.        :NNhdNd: `://++o/..`     `   `.`.---..`` ` `-//      `...`.yNNN
hmmmmmdNmmmmmNNNNh-     //`/`       .mNNmms-  .://ooo:``.```       ```````--...://:`       .:dhyNNmm
/ohysdmdhddymmNNNNs    `dhod`       `oNN+:/y/-.. .::///   ``..`         ````.-o//:..``      :MMMNmdm
/oyyyddmmmmdmNmNmh-    :Nsdm`         -hds:/ohhyo:/s/::`     ```.``         `.-.``...``     :NMNdddd
+yysymmdmmmmmmmdy:...``sd/dh.     .`.` .omNd+:ohddyyo+++.```      `.``          `.`.``-.-:/sNNMmmdmd
yhyoshdmddmmmdmo`     .MN/MM`     `    ...oydhs/:+osy///  `...``     `..`          `..omNNMMNNmdddmd
syshdddmNmmmmmh+-.`   `mh/ys-`    `.` `   `odhys/..+yyds-.`   `..``     `.`         .dMMNNNNNNdmdmmd
+++ddddmmmmmN+ `.-.`  .+--/oss.       ``.``mMMNNNdy-::sss` ````  ``.`     ``.` ``  ./NMNNdmdyhddmdNd
//shdmmdmmNdy`    `..-.+dNho/os+.     ` `-+yMMMMMMMmoo+:/`    ``.`  `..      .. -yhmMmNNmhdddddymhdd
shmmmddmNNd-`.`      ``--+mdysssy+.` .+/+o+odNMMMMMMMMNyh/``     ```  `-      - :mMNNmNmmNmmddhhdhmh
ydmdhhyNN+: ``.. ```   .``-yddssyyshso/hmmmddyyNdmNMMms+:` ```     ```  - +s+/+omNmddddmdmdmdmddddhy
ydhhmmhmo-.``       .` :--oyshmy+s.oo/-:-yMMNmh+s+ymhso:      -`     `---:mNNNmmddys++o/osydddddmhdh
shmmmNdd.``.-......::-.-.`+ooyhdsdh.-``.:.yMMMdyydho+o/`      `     :+hdhmddmdhh+s-`       -sddhmmmm
mmdmNmhd..`       `o-:`..`:/s+s//+s:./..+:/yhdmhhm++//-..`  `:.````-yddyoo/++--:.`          `-/yhhhd
mmmNdhh+.`.....`  .:oh`  -+sohydoyyys:+shmMMmhhhys+. `...-:..odddyohsoo-                       .:/os
syhyyd/..   `````  /oh   `yyyhhhys+o+ysssdNNmmmy+`  `.`` :mmddhh+/.`````                           `
yshydm:```         .oy.:-`:`-/--//:+odo` `/ydh+-``.`-.-:syh/:::.                                    
yysymNd.`````       `-/::+:ssyhdmooNMdh-` -mo. ```   `:s+.`                                         
sssdmNN+    ``` `       -:-:-oshdymMdo+/sos:`     ...`.                                             
yddmdNNy`      `.`.`           .:yMNsys/o`` `    .--`                                               
NMmmdMMy       `:. ``..```      `dNhso/s````.   .--                                                 
mmmmmNNs``:-. ./-.-..:..ymhyhsoo-`.-:/s:     -.                                                     
mmmmNNNNs+/os:+:-::.:-/oyyhddmmddo:` -:   ...`                                                      
mmmmmMNNh`--/:/..        .:/osyhdNmh:.    -/.-`                                                     
yhddhmmNd`    `..`..`----.....`...-`      -`                                                        
ddhmmmNNNo..:--`.`....``.--:::.-`  `.`.-+-`                                                         
ddhhNMMNNh---.`.``.` ``..` `.-.:`...```.s.-`                                                        
dyoshNMNNh.``..```.```-```       ````:.-```.                                                        
doydmdmMMd-.`         od+`          `sy:`                                                           
hhmNNdmMNNm:`-` ` ```/o/.` .---``.`:Nmh:````                                                        
shNNmmNNMm:...`..../://:`       `.:oMNh-`````                                                       
ymNNmmmNMh...`..  `+///`          .mN/`                                                             
hNmNmydMMho-`  ```--:.` `:-::..`.-hNh.                                                              
mNdyhNNNMMmh:`    :.   ``` `` ``-/hMMy-...`                                                         
yshmNMNmmdmm/``` ``   ```` . ```  `dNdo:/:-                                                         
//odmNmddmdNm/` `...--`     :+    oMNdyyso+:-                                                       
/oddmmmmNmNMNms-..         -/+.   .mNNdddo/:`                                                       
yhmhyddhyddmmo-...```  ````+-..   /NNhho-                                                           
dhhdyhymhmmNms:` ..-`...``:+-:/`./mmyy:..                                                           
hhyyyoshdmNmmy/      `````//.//   sm+---/:`                                                         
hhhdhyysmdMNNh` `.     .../oo:.  -hhsoo://-..                                                       
/+ssyyydmmMMMy`           `++..```hdso///:.                                                         
::oosoyhmNNNNm-           :+-  ``-hys--:+-.                                                         
.`/ooyddNNmNNN.   ```  ` -y/..` `dNmyo:-``                                                          
//oyyhmmdmNNMN+...`.``.`-+:``-.`.dms//.`                                                            
oo+syhyyymNNNy.````    -:+```.--/h+.                                                                
/+//shydmmmNN:`` `       ` .  .sy-                                                                  
/+//ohmNNNmNM:````         ``:ymd.                                                                  
/+//omNmdmNNmo.     ``       oMMNh+-                                                                
osoyhdhmmNNNNN+``  .``   `..-/NMmho:--.                                                             
ooshdhhmmmNmNN-` .----.--.```/mNyy+//:-.                                                            
s+oyyhdhdNmmmd/.``...``.....:+my..`                                                                 
/+ydddmdhmNNNh-``..--.--..`-sNh-                                                                    
oyhhddhdmNMMh-```..-....`../dm/                                                                     
oshhyhmNNNNNo` ` `````..`:hNm:                                                                      
oyhhmmNMMNmNo`..`--.`.```:Ndy:..```                                                                 
+symmNMNNMNNm:.`.--:-.```/Ndyso++soo.``                                                             
/oyhmdNmNNNNy.` `--..----sNddyyo//--.-.                                                             
+/+yddNmNNmNs-...```..`:hNNNds+-`` ` `                                                              
+osshdmmNNNN/```..`````/mdhh:.``                                                                    
ddddhymMMNNNo-  `.--./oys:-.`                                                                       
mNmNNNmNNNNo` ``` `./my.                                                                            
hmNNNNNNNNs--.:..--.oNy                                                                             
mNNmNNNMms:-.``.-/+hNy:                                                                             
NmmNmmNN/`` ``.:hmmh+-`                                                                             
mNNNNNm/--:-:./hNmo-`                                                                               
NNMMNm/::::-+dMMmo-                                                                                 
MNMMm. .//+smNNNh/-                                                                                 
NMNy.-..`yNNMNmhs/:-.                                                                               
NN--.`.omNmNhs+:`                                                                                   
d/-:`oNNMNm+`                                                                                       
        """)
def page53():
    page52()
    print("""
    The worst thing you could do would be to panic.
You relax and drift with the current which suddenly
takes you upward. With your knife, you cut
through the kelp and are free. What a relief.
    But no sooner do you get out of the kelp, than
you are caught in the vortex of a giant whirlpool!
_______________________________________

    If you try to swim out
of the whirlpool, turn to page 69.

    If you dive into the vortex of
the whirlpool hoping to reach the bottom
and get out, turn to page 70.
        """)
    choicex = choice(69, 70)
    if choicex == "69":
        page69()
    if choicex == "70":
        page70()
def page54():
    print("""                                            
                                                     `..-:                                          
                                                    :- ..---                                        
                                             `..-..+/:-.``                                          
                                     .:--:/:++/.`./``+----:-::-.                                    
                                  .-:....---////o/`  s:       `.:-.                                 
                               `:-`..:+oo++//oo+.   .dd`         `-/`                               
                             `-/.-+ysyyyoo+so/.    /ydhy.          `:-                              
                           `-:/ooss+:/o+/o:``+o  .+ysysos/` `.       -o-                            
                         `/o+ossoo++shss+::+yh--+yy/++/:ods:.+     `-`-/:-                          
                        :yssshys+syho/+syhshmoyyooso/++syysy/o+      -:/..:`                        
                      `+yssyyosshhshohmdhsydmmmhdo+osshsoydhysoo+``   .:/ `/`                       
                     -ydhhhhhmmhdhyhhyyhddmmdmmhyyys+ydysyydmhhdhsyo-  `s  `/                       
                   `/hddddydhhyssyhhoymmmdsyhhydmh-. oyhdssyhyyhyysyss. :-  -:                      
                  `ydhymhydhsshhydhyydNNds++oydmy+`  /hhyshhmmMmmhyydmo  :``:o`                     
                 .yddmmdddyysyy+hs/hNNdy/::-+osmmo`  .hyhmMNNmy++sddNdd` `//`+o                     
                .yso+yhyhy+oohssddmNNy-      `yyhy-   ohmMNms.    :dddy+  //. ::                    
               -hsoohhyods+//ho/oyhmd.       `ydhyooo:/yyhdh`      osh+y  `+/  -:                   
              :mdddymdyyNh+oyoyssyhsmy+----:+shoydmmo` `ssyyh/.``./hdmod-  so   ::                  
             -hdhhymds+ssd/+y+oyhyhdddNdNMMmmmhhdyNMMh:+o-++mMdhdmmshmyh-  do``  :-                 
            `yydyyymsyyddNmhhosysddddhddMmhhyyhmdyNNdhdmNhs `sddmy- `doyy  o/`/   /`                
            sodmhhmhhssdymmhhososyhhdhhhhdddhdddds/.   .:o-   --.   -ddyd` s/ +   `+                
           /hyNssyNs+/+ssdyss+++ssyssssyss+::::.   `+:-`   `-.`.`  `yhs+y+`o/ / `  +`               
          .ho/dyyddsos++odyd//////++//sssso/yo+/:+++y/+:-oss+odh- -ysydyysss` s y` .:               
         `+: oyossdo++o++d/yyo++/++++hhsssssdMmNNmo`.-/:::o+   .-/ssoodsyymy  / +o `+               
         `   +sy/oh/oh///dydsydsoooooo++//syhhhdyydsoss/:o/`   `/hssssmhhhdms`+`-s: o               
             +d-yom+sy+/:h+h/++yhsosyddysyso/` /mh:-.:+      `:ysys+//y//shdoyo` +-:o               
             +-s+odsdyoohyoh+sooo+oohssssyho//ys/`        :/oyo+/+d::oN+ssosoom: +`:/               
              ooosdsdyoymyddydydyysodyyyhmdNmso.   /s-  :ymhddyoyhds+ys+//-:s+oh`/.                 
             /o+y`dsdhyhsh-hysohsyhymoshdhyNmNms++smo-:odydmddho+y/s/s.hoy` sos-+./                 
            .y+y.`hoy.ydy+.hdyydoyhdhdmdhydNmNNMdy+-` -Nmsyyy/shh:-dd. oyd- +y/ -++                 
            -yh- `ho+ sdN+/hdhdysydhhdmyoommdNNh/`    /mNho`::.oo`/s-  `yh. -h.  +s                 
            -d:   sh` yyy/yyddhyydmdhdNmhhmNdyyh.    :mNMdo--s- `-oo    .y: -s   `:                 
            `o    os `d:-/yoh:yyNmmmNmMMhds:do:-:/-:-dNMMsy+:/+..` o/-`  .. ``                      
             .    ::  s`-..::`shy++osssshh: .+-//+//:dMMd.:-::///` / `::                            
                  ``  .     .oooysys/::sy+   `+-.+o++ymNo   :s//o: /   .:.                          
                            o:+ssyhhdo//+s/-  `:o+/++oyo   /s: `+s:+`/-  --                         
                           /+:s//oyyso//-.+++/-`./+//ds  ./+-`  .sh:so:  `::                        
                          .s+s:/s/:o/-----.`..oo:.-sdh.-/+-+:y-  odhss+   o:-                       
                         `oo+:/ds/::y-`./.`:-  ./+o+d/++.`:yoNy-ommdos/`  +.+`                      
                         +s:.-os````/+./..oy`    -dms+.  ./+/MMmdmd+y+/-  +../-                     
                        -h/:-:hs`.. -//:+ys/     -mhs//` .o++NNNohh+ys+/``s:  /.                    
                        o:-.`:+s+//-++:/yo-`      s-++o. .dmsdymymdhsyso/so:   /.                   
                       /s:---/:oy/ss+/s+:-`       ::     .-y--y++yydhsmhdmy--` `o                   
                      -h++/o+/oo:ydhos/-`    `/`  -/`-:-  .s. s--o`+//Nmdhhso/` :-                  
                      s-/+o+++/+yNddo:.     `+o:  .+-///` `:`      -sdmmNNho/`  `:                  
                     -h+:/+s+/-:oNms+/`     -/:.   o ``            /smdddho+s/. --                  
                     -yyy+::+os/-dh:::.     --`    s               +Ndhh::///+y:/                   
                     `hhy+ooss/-+++s++:.  `-:`     o ```          .hys+::    `+/                    
                      -y+sooooss:/.`soo+`-+o:      y oo+-        :y++/-`  `.:y:                     
                        :+//+shy+//--/+m+s/.`      s .-.        `mmdhy:../:.-+                      
                         `/+shs/s/oos:-/yyss       o            :NmdhdyyMN+`y`                      
                           `yyydsyy++syso. +       +`          oydhss:-oyNNy-                       
                             .oymsysso+/`:`s     :./``o-:-    .y+:...``  sy.                        
                               odso+//. /+.o    /y`+.         `sh:-     `s                          
                               yhm///: `+/`o       /+  ..      :h::     /h                          
                               +oys:-:`.+-`o     - os //o+`     oo:    `sm`                         
                               +oyoos+:`o -:    /` yo `:-       `s`    `s+.                         
                               .s:y::+./-`+   `/. `yy`           :o    h-/-                         
                                s:+yo-:-`o`  .+: `yyd`            /:-`:: +-                         
                                s/:/y+://. .:o:  -dsd/             `./+` /.                         
                                :o-:://:. /+/:` `ssyho             .yyh- o                          
                                `h::://---::.  `+mdhyo         `.--/o+s:.-                          
                                 oo++ooo::-..:odmdddNs:--://oso.``                                  
                                 ``..--:/+shyhyhhysymhyhsy+shos                                     
                                         .mhyyhhhhdhNdhyo:```-/                                     
                                         `hymhydhsyhNh++.  ./o`                                     
                                          y+s+sssy++sy//`:yhmh+                                     
                                         `y+o+yyo. `sso+ohyhdy:                                     
                                          yhhodmdo`:hs/++s:-/+/:                                    
                                       ```:dmhdmd/:h-:ddhmsyyssm/::`                                
                                     `.ohhhmMMMMNysd//NmNmyhmNMNhdh:                                
                              `../oshddhmNMNNdhyyhNM+/NMMymNMyMms//:-```                            
                        ``../ohmNNmddhosdmhdyhsdoymMMMMMMMMNMsMNh+/...::-:/`                        
                      ./yhmMMNmmmyyo+:..ddhyyNMmddmmmmNNmmmMmhNNhyhdo::-:sd+:.                      
                   `.:+yhmdNmy+---/+yo/sNh--:+oo+/  ` ./:ososhdhNNdsy+//yhmy.::`                    
                .-oysyossmNdhdho-:/o/:. :.                 .--//++oddhdhddyhy+:+o:                  
                -:::---:-//://+o/-.                                   .-::/+os+o:-                  
                                                                                        
        """)
def page55():
    page54()
    print("""
    The three people lead you into an enormous
cavern. In the center of the cavern is a huge,
silver-colored machine. It isshaped like a long tube
with several round panels attached to one end.
    They lead you inside. It is the most advanced
control room that you have everseen. Computers,
sensing devices, recording devices, monitors, and
a host of dials and panels fill the room. A strangely
shaped figure with a very large head and totally
blank eyes faces you.
    "So, now you are in the control room of Atlantis.
You see our secret. We landed on this planet
3000 years ago. We used our anti-matter device to
sink this continent beneath the sea so we could
escape from your people. You can have a most
pleasant and useful life here with us if you wish. All
you need to do is allow us to inject you with a
special serum to enable you to live down here. It is
up to you. On the other hand, if you do not wish to
be one of us, you will be held prisoner."
_____________________________________

    If you submit to the injection,
turn to page 71.

    If you decline, turn to page 73.
        """)
    choicex = choice(71, 73)
    if choicex == "71":
        page71()
    if choicex == "73":
        page73()
def page56():
    print("""
    "I wish to join the Nodoors," you tell your
guide. He leads you to the outskirts of the city.
    "I must leave you now. Good luck." The
Nodoors send a greeting party that is heavily
armed. They are suspicious of you and believe that
you are a spy sent by the Atlanteans. They look
exactly like the Atlanteans, but they rarely smile.
    "Come with us. You must be questioned.
Perhaps you will work for us."
    For 3 days you are questioned and kept in a
small room without windows. These people are
not kind and you believe that you have made a
mistake. They ask you to help them spy on the
Atlanteans. They suggest that, as a spy, you could
pass freely between both groups.
_____________________________________

    If you decide to escape, turn to page 75.
    
    If you decide to accept their offer,
turn to page 76.
        """)
    choicex = choice(75, 76)
    if choicex == "75":
        page75()
    if choicex == "76":
        page76()
def page57():
    print("""
    You decide to remain with the Atlanteans. Their
approach to life seemsideal. Time isspent in creating
things to help life and not to destroy it. You
believe their leader is speaking the truth when she
tells of avoiding war and of not hating.
    You are fascinated by this apparently ideal
world. You would like to stay and search out the
history of how Atlantis became what it is and what
caused the split between the Atlanteans and the
Nodoors. Yet, in your mind remains the hope of
escape so that you can go back to your own world.
_________________________________________

    If you decide to stay and spend
your life searching out the history and
secrets of Atlantis, turn to page 77.

    If you decide to escape, turn to page 79.
        """)
    choicex = choice(77, 79)
    if choicex == "77":
        page77()
    if choicex == "79":
        page79()
def page58():
    print("""
    A large white lightshines down on you as you lie
on the operating table. Then you become unconscious.
Pleasant thoughts, sounds, and pictures
occupy your mind. When you awake, you feel no
pain nor any real change. But, now you can
breathe underwater and join the Atlanteans in
their world.
    For several weeks you explore the world under
the sea as you never have seen it before. Without
the heavy oxygen equipment on your back, you
feel a marvelous sense of energy and you glide
through a world of beauty. Your two guides have
become very good friends and they take you on
adventures in the deep, exploring the ocean bottom
and getting to know the fish and other sea
creatures. It is a very exciting life indeed. You like
it, but you regret that you will never again know
the world above the sea.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


        """)
def page59():
    print("""
    "No, I refuse to have this insane operation. I
don't want to become a fish!"
    The Atlanteans try to convince you that life with
them will be happy, useful, and long. Yet, you still
refuse. Sadly they give up their arguments and
spray you with a special mist that immediately
knocks you out. Several hours later you gain your
senses only to find that you are in an underwater
air tank where you breathe naturally. Your closest
neighbor is a horse who looks at you with sorrow
and understanding. The Atlanteans have built a
small apartment very much like the ones in the
world above the sea. People come by and look at
you and talk with you.
    Maybe you have made a real mistake. They no
longer want you to join them in their world and
way of life. You refused their offer and now you
are a prisoner in a zoo.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 


                                     `--///+/::.`.`:/``.:`                                          
          `.`...-...-``       ./ooyhdNNNMNMNdNmo++Nmh//+:  `.                                       
       `.` ` `..``...../-+ydhhmMMNNNNMMMMMMNm/   /ddhNNNNNmy-                                       
    :sm/.--`..  ..    `-hmMMMNNNMNMMMMmMNNNmy  .+hddmMMMMNN:                                        
  -hNMy:/-     -`      -NMMMMMMMMMmMMMmNMN+m+ :dNMMNNNdmMMMNo`                                      
 -dMMMsy`   `  :        sMmMMMNMMMNMmMsmMy`d++NMMMmNmmhNmMMMy+-.``                                  
`mMMMMh``     `. ```    +MNMMMNyMMMssd.NM+sNmMMMNhyNsys+yNN+oyy/``.-                                
+MMNNN-``   ` ..        odMMMM/sMNM+.yhNMNNmddNMMdmdso/ssohsoyNh+/`y.                               
NMMdMm:`.   : .`.       +mmNMM+.mNmhhmsoM:.```.omMMmyyssosyhyhNMmmyds`.`                            
MMMmMh/ `.`/:./         o-syNN-`oMMm+s/`m.      `.--:--/:+osysNMMNmm+      -/ssys+`                 
NmMMmd-``--:so.         ..s+oN+ymNMy`:s y/                 `-ommdys-    `+dNMMMmhmo                 
MNMMMN/ .:+sy/            .+yNhs+-yo -: .                     ..``     /dNMMMMMMNMN-                
MMMMMMh:shmdo`       `   /dy/s``+ +/                                  /N/dMMMMMNMMMo                
mMMMMMMyddym/.          `./- ` `+ ./                                  os/sMMMMMMMMMm:               
oMMMMMMMmsdNho/ `.`  `   `` `` -`  -                                   `o:oNmshNMNMM+               
:hMMMMMMMmoshhh-`.``:ss+//--/:-.                             ` `-.```   +/`-/+ssshm+``              
`:NMMMMMMMh`-dd+`   shhoo:/`.:`                            `-+o++so+/:/```/ :mhs//oos:...           
 /+MMMMMMMm`hMhd:` //.::/o.`-`                            -smmhhhsodhy+///+/o/.```.-:+/`.-          
 `:NMMMMMMs sMNhy` o- :-h+`.:                             :/ommdyhyhhdoyy/-:--.      .y/ `-         
  :yMMNhMN` `hMMh/ :/ ./s-`:`                              `hhy++yysy++yhy+:-`/       ./- --        
  .yMNyhMm   `dMd+../  ss`-.                               :mMdhhhhyhyo+yyos-`-`        /` -.       
  /NNy./Mh    :MMy/`: `y:`/                               -mMMMMNMMNNNNmNdhhs/+`        `/  /       
  -s+` /m/`    yMd:++.+s/o+                              .sNNMMMMMMMMMMNMMMNmmh:`        .  :`      
  `    sd..    .mMsNm+/oyh.                             -:mmMMMMMNMMMMMMMNMMdmm/          . --      
      `dN:-     oMmms:::/-                            `-`oNMMMMMh-NMMMMMMNMMMdds+..       ``-:      
      .MMh:     -ymo/o:`:                            `-  /NMMNNs`.mMMMMMMMMMMNosyy:`        .`      
````  .NMd-       :-+My./                           ..   omMMm+ -mMMMMMMMMMMMMs/oo/o:`      :`      
ssssoydMMdsso+o++-`s/N/`s`                         -.   :dmNs. `hNMMMMMMMMMMMMmmmdso++-     /`      
yhyyyhNNNmsdy+:-`  soo//:`                        :-`` :sdN+````./dMMMMMMMMMMMMMNMNhoo:     :       
--.```.-..``       h.-sd+:                        `:ydsdyhh:--+o+oNNMMMMMMMMMMMMNNNNdo+`    :       
hmmdddhhsos+//+/:::d+--sh.-+:              .-:/:o+/--hMNN/::++sdmmmNNNomMMMMMMMMMddmNNNs::///       
:////+++/+sosssshhyyydm+dNNMmo+/+/+/:---..+/---/ohmydMNNMhosysoooydNmdshNMMMMMMMMMNNNMNs//o.        
yysshysso++osssoyhhsomMMmmhoo+++++/syyhhhhsyddhhdhhhdNMMmhhyshssssyhhyyysddNMMMMMMMMMMMNd:          
 `..:-....-//+yhydmNNNMMMMhs`                  `.-:--::/:-..-:::::::-...-::-:/+ooooooo/.            
                   ` .----.                                                                         
                                                                                                    
        """)
def page60():
    print("""
    It doesn't take you long to find the king. One of
his countless agents leads you to him. He is in a
small simple room with a strange light glowing
from the rounded ceiling.
    "So, you have found your way here after all. Put
your mind at rest. I won't hurt you." The king's
booming voice startles you. He invites you to sit
down.
    After several hours with the king, you find him to
be bright, friendly, and interesting. Maybe the Atlanteans
are wrong about this person.
He offers you a chance to join his government.
He tells you that most people are lazy and selfish
and deserve to be ruled with power and command.
He has been king for almost 1000 years
and he has survived because he is not afraid to be
tough. He wants you to be an advisor on his staff.
________________________________________

    If you decide to accept the king's
offer and work for him, turn to page 80.

    If you decide to refuse and
go back to join the other people,
turn to page 82.
             """)
    choicex = choice(80, 82)
    if choicex == "80":
        page80()
    if choicex == "82":
        page82()

def page61():
    print("""
    The problem is where do they escape to? The
king is in charge. He rules the world below the sea
and his spies are everywhere. The only answer is
to devise a plan to capture the king and put him in
prison.
    The people are frightened. Some citizens tried
to revolt years before and are still in prison. The
king is smart and suspicious of everyone.
You suggest a plan to put on a festival with a
play. On a given signal the actors and the people in
the audience will rise up and seize the king. The
actors will be carrying real weapons, but no one
will suspect them because they are in the play.
The people like the plan. They ask you to become
their leader.
______________________________________

    If you accept their wish to
become their leader, turn to page 81.

    If you decide to help them in
the planning, but also to escape from
this sad world, turn to page 86.
    """)
    choicex = choice(81, 86)
    if choicex == "81":
        page81()
    if choicex == "86":
        page86()
def page62():
    print("""
                                                                     -//                                
                                                                :./.`                               
                                                               -. :/-                               
                                                              /y/.``                                
                                                            .-`.-                                   
                                                           .- `                                     
                                                  `-sdhs/`:` .`                                     
                                                `/dNMMNy+-.`-`                                      
                                                sMMMMMMm/.`-                                        
                                                :NMMMMMs-+.                                      `` 
                                                 yMMMmy.`/`     ` `  `` ```` ..```.``-` `` `.   `..`
                                                 :d++.`.-`.``  .```  `` ``````.`..` ..` ``````      
                                        ``` `..-:.-   -/.-`            ``-.:--.                     
                          `.`..```..`.``.`.```  :-  `+`` -````.``````````                       `:` 
           ```.``.`.```````                 ```-:: `+y/  .-  ....--   `-                     `:///` 
 .``  ```  `                      ` ....---..-./-/ `  `-` :-``.`     `.`             ` ``:-/++/:-`.`
                                  ` ``.` ```.`.:+`     .:` -.      -:`            `-::....-..-` ...`
                           ``.`-...` `.```     +.     `..-  s``` ``/--.       ``..`.    ```  .--+:-`
             ` `..``````.````                 .+    ::`.::- .+-/``-:/.`    `---`:`     ```       `` 
   .   .   .`                               :hdN:-+::.``.--:`-:. .` ``   `/o/.`.`     `...:-:`   `:`
                              ```         :hMMN:sMMh-`-:ssdhm: -+ss/-  -ohso/:::`   `.-/.--:o-      
                          `-::s+s/.-`    yMMMd-dMMM/+s+oo/dMMNo:.-```:ohy/+s/+os+` ``       `:....  
                          ..:md:-`..:.-.-mMMh:dMMMNydyysdNMmy+:/++s+`y+/ohddNy+-.--`..`:- `      .-`
           .+`            .`ym:`:ydd+:`-+MMMsNMMMMMdhMMmy+::yyydms+`//+yss+-`-//:+-.       ..     .`
       `-.`/. `           s:+NmdydNMd.-yMMh/mMMMMNdds/..:osdhyyso+oddhy-``.:/-`                `.--`
      ..`  `.--:     ----:od/mMMmyyho -dMy.dMNys+:.//ssdmmNmmhh-.:+:-``.--`        .-/`    ..::.    
   ` ``..:-.   `.:-./+ --/ymyhhhhdhsdhoMh.oo/--./yymmmNNmmdo/:-``--..-:``      `/+s/`..-o+:..```  .`
  ```.`````   `-.-:+/:+++soyhddssyyyo+//.-/oydddmddNddNmy/` `.-../::..       .+hds:/sdhhy:.   -  `` 
       `-`   -/:ooo+++oyho/shyyysNyd+:osyhyooyyyssoo//:::--..`---.        `-ooyymhhs+/-..``  `:..`  
        `   .dhmNh/:-`.omds/so:-+MddhdN+-``./:----..--.```.:.`          .+so//os+-.```..`-.`.`. ``  
      `     /hmMNdyysosdNyds-:/sNMoymh:..:::+oooso///o..`            .:shhoss/:-`   ``--/+:.``..--- 
 `...-.    `:sNNNNMNMNNMhmhyddNMNs+oo.../:/:/++++o+/-.           `.:sydmmmdhy:.```.:/o+/.``-:os+-`..
 /::.``....-:.hdNMMMMMMdmyMMMmds-`-+:.-//::-:-:oss:.          .-odddddmmmhhssoso+/+::/o+/ssy+-`   ``
  `.:--/:-.-++yosyNNdyNsmmmdo.-.:/:/:/:::+o:::-.`` .:oo---++sdmmmmmmddyyy+o+o/o+yos+/yyhsdy/.-.-:/o:
`ooo++/:..:ooys+++hy:yo/s/::/:::/+ssso/:--..`  `-:yyhhhhhddmhddds/:++//-.``-/oo+o++oyyhyy+/+/oys++o:
.s++/.`.:+yhhysoo/::+/-///:/++ooss+/-````:://+sysyhhdsysos/::.``        ``.//.. :+osssyyyo//::-.`-:.
`...-+shhdhyyo+/---.``..../o+/:-.`   `-++/oyysss/:.....`          ` `.:.`.`-/+oyhyss/+++:..`.-::-:.`
`oysshyo///:-:````.`....--``     `.:/ss+//::-.`   `.-///:/+/:://--:-::/::::+hssho+/..```         ```
`++//+/---:/.``.-+y-```     `.-/osso/:.`       ./++++///:::---.-` ``-.--::+ss:-.``....-:....`-.--:-`
`++-:---//::--+o+/.       `-oso+-.`         `.:/::```  `````````..``````.....--:::.-..:--.::-.`.`   
 ...---.``-.::-`      `.//::-`         `.-//+/-///+++/:s+osohhydhmyyyhyoysoo::.             `.::-   
`..`    `..      ``.//:.`          `--+oysssyysshdhho/o/:/o/hyossh+/+/:-.`       `.-  ``...--.`     
             `.-...          `.://+oo+o-..`  :++/:-.   .---...``         `:...:://yooosoo/`         
        ....``     ``--/+/+sssyys:-..                              `.:+sosso+sy+o+ys/:.`        .-.`
 `---..:/:`..-//oyyyyyyhdys+:-.`             `.`::. .`   `         `:--/..``.://+: `       `.`.```.`
`../shdmmmdhyo+/::-...`       ``...``````..-:``-+: `:.`--:               -+so+o/.  .-/-:---- `` .:. 
.hhys+:.`              `....:/:-.``   ` `` `` `..-.-:.`.              `-sso+o/`   `-+:-.`        /` 
 `                    `..../-``         `.`:oso/::.`            `-://+osoo+.                        
                    `````        .:-`   ..-.`                -/++/::+++s/.                          
               `` ``   `.::.`.-.-:::--`.                .-/:+o////+++:.                             
          `...:..`.`.``+oo:.```    .:`         `-/syds///+---o+hys-`                  `.-::         
 ```` ` `` ````..``....`                  `-:+shoo+/:::/--:::s+/.`               `..`.::-`          
`.`-` ``...```                      `-:oshoso/-` .:/so::////:-`             `..--.:-.`              
 ``````                     `..-//++/:--.``      .-oyo++--.             `.-.::::-`                  
 ``                   `.:/+/--.```           .-/oo/://+//+:-       `...::.//..`                  `  
               `.-//o++/:.`              `.://++++::+s+/-.      `...`  `/-`                 `````   
        `..-/oooo+/-.`                 `//-:-``.:+ssyo.     `.-.`````-..`             `.-:://:-.``.`
   -:::::-:-..``                            `-+oyys+-`   `.----:.--::-            `-:+/s+oo///+/-+/-
                                       `.-:+ooo++/.`   `..----::-.`             `.:::://::-.:/+/::.`
                                    .-:ossoss+:.`   ..-`....`-.`             ``.-.`` .```  ./--.`.` 
        `.`                      -:/yh/ooso-`    `.--.:-...:-              `. `        `....```     
  `--/+:..                   `-+os+:+-..``    `..---:--. .yo-            `.`      ``.--``           
 --+//:`                 `-/osy++++-       ``.``.-------://.                  ``.```                
`o+-..              `.:/oooo+/.```      `.-.```...///+o/::`                ``-``                  ``
`/-`           `.-/osso:o/-.`       ``.---```.---:///--.                  ``                   `---`
          ``-/++ss+-` `-.        `.......:--::.````..`            `--..               ```     `.://.
       `.-:osy/-.`           ``..`.--...:--``://:::.    `.---.---:-/:+o+/.`   `` `````::-   `--::-. 
   `.../++//.``          `....-/:-:+o/..``.``.--/--` `-+hmhhhdhhhhhyo+.   `` `.``   `...` .-/:--`   
 ``.:/::.``            ....::::------/:///oyyo+-   ./yyo/shs/++:::/:/o:`   `.:+/.-... ``.-/:-`      
 `...``            `.-:://:://:/++/+oyosssoyso:` `-o:`   ````        ``` `  -+++:. ``.---.`         
 `               `-/////++o+/o/sy+oo++/+so+/:``--:-    ```                 `.-` ```  ....           
              ...--/+/osoo/o+oo++/++/-----.`.-::-.  `.`                 ````..`   `.:.`             
          `...-/+/+so/+++o+//+//::-:..:.` -.  -:````             ``:/:/o+/---` `-:::-     .-`.:o.   
       .-//--::/+/+os+s+/:://///:::/-`        ```. .`    `.....-::-..`    ``.--.``o` `.--`..-:-.  ``
 `---:oosoyo/+o+o+:/++soyyoooshy:-`       ``.:...`````.`-:-.--.-`       `..`-`  `.-::-`   `--:-.-.` 
.ho+soooos+soyyysymmhhhmyhdso:-        `.--.-..:-::.---//.``       `.:-...`    `.`      .---`       
    """)

def page63():
    page62()
    print("""
    There is one way out, you decide. Leave the
Seeker and try to reach the surface on your own.
You enter the airlock chamber which gives you
access to the ocean. With a quick push off, you
leave the Seeker and swim towards the surface. A
small, yellow life raft is part of your escape equipment.
The surface of the sea is calm, but the Maray
is nowhere in sight.
    For 2 days and nights you drift in the life raft
under hot sun and sharp starlight. At last a search
helicopter spots you. Finally you are safe.
    The exploration of Atlantis will have to depend
on a new diver. Your eyesight has been damaged
by the strange force that immobilized the Seeker.
You career as an underwater adventurer is over.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    
def page64():
    print("""
    The best plan is to wait until the Maray locates
you with sonar equipment. You can't signal the
ship because none of the Seeker's electronic
equipment is working. There is no sign of the
mysterious submarine. Perhaps it has left, now
that you have been chased away from the world of
Atlantis.
    Looking out of the thick glass porthole, you see
a giant blue whale heading for you. It looks as
though the whale is going to ram you. Maybe the
other submarine has angered the whale and it is
seeking revenge on any craft near it.
    Suddenly the whale hits you full force. The
Seeker is badly damaged. Water begins to trickle
in through the hatch cover. You must abandon the
Seeker. The whale now remains close to the
Seeker watching and waiting.
______________________________________

    If you decide to try and escape,
turn to page 63.

    If you try to hitch a ride on the whale,
turn to page 85.

    If you don't know what to do,
turn to page 87.
    """)
    choicex = choice3(63, 85, 87)
    if choicex == "63":
        page63()
    if choicex == "85":
        page85()
    if choice == "87":
        page87()

def page65():
    print("""
    Why not go? Who would believe it? The center
of the earth! You push the control column forward
and dive deep. Soon there is no more water, just a
heavy gas that acts like water. You look at a world
of colors and drifting forms. You pass by layers of
rock and sand. Suddenly you sail into a gooey
mass which almost fouls the Seeker's propellers.
Then the Seeker's engine stops and you are pulled
along through the semi-liquid material by something
like gravity or magnetism. You burst through
a thick elastic membrane and enter an area of giant
atoms. Electrons whirl around you at high speed,
but there is plenty of room to maneuver between
these fast-moving particles. The electrons are revolving
around a small mass you know is called the
nucleus. You are able to avoid collisions with the
electrons. What a world! Maybe you are having
hallucinations.
________________________________________

    If you continue on in this trip
to the center of the earth, turn to page 88.

    If you try to turn back, turn to page 89.
    """)
    choicex = choice(88, 89)
    if choicex == "88":
        page88()
    if choicex == "89":
        page89()

def page66():
    print("""
                                                                                       ``.-+y/          
                                                                                `-:--://+/`         
                                                                                                    
                                                                                   `                
                          `-`/+`.                                                  -/:              
                          -` +:-/                                           `.`-   .://`            
                           .` `-/                      .-`..              `````-      `.            
             ``.. ``           :--`                -:.//-`:-`           `.````-`                    
             ` ```..-`---.:-..` -`..    -+hyy+-    /-.::``.`           --.--:-:                     
                          `..:---:os/::./hMMMN-  `:/o`                 :.-..`-.                     
                                 .sh+-`:-yMMNd.-``/`                   `.``..                       
        `                         .yyhoohdNy:/od///--...``` `            ..                         
       -.`  `                      -dmyyds+:yoy/-           ` `  ``.` `./-.```  .....```            
      .//+/::  `../-               `o/-:+/. o/.    .:                .-````     ````` `. `         `
      so://+ -o:..-//              :`.-+y+`..   `-smy              .o-:                             
     /ddoh+` ymmo. :-`            .-./o++`.`  `:smd+`        -+/--o+.:`  `                          
-+s/oysss/:` `:+yh+++` ``.....`.`.s:+hy/..` `/+mdy/`       `-`-dmddo+:  -:.:.                       
:ymmddmNmy.  :/:-o+::-.````--//oshy/+h:-+-`:/yy+:/.`     ``  ```:hNNhs/..:ss--`                     
+::/sysoo+:///-``            `.````..``./:-/:-.``     ```         .omNdss/soo/.-.```.--..``       ``
::/.`----//sddyhy+-.                          ```..`.:.:+-`..``     `/ymms/--/sy/-` `.-`.`-:-/:-.:o/
 ./+:../+sydhddddmdhy+-`                          -:--:/y- ````..      .+/y+  `/s/-   ``../+yhyy::-`
` `:+hdyhNNNNNmMNmNNNNmys/.                     ``-``.-/o:.   `       `-/.-`..:.--.```..---:syyy-.``
-.`-+Nmy/hNNNNMMmmmNMNMNmNmy/.      `.:         `-/--/.-.--/-..    ` `-:-.   `.``-:--:+++sssyso+` ..
/.``/MNNho+hNNMMNNNMMMNNMNNMNds/`  `-.`            ..://-...-::.`  `.//:-````.`.-..``````.```  `:-` 
+yo-+NNmhs+//hoossyyhdmNNNNNNNMNh+--- `              ```//::...-..``:/:.```....`.....`.....```:/-   
-hNmd+-```.+ho.--....--:osdmNMMMNho/-+`                  `../+- `.--/:.                 `-`-/-...-/.
::/dm/`./:/::+++/o::-`.`....:+sdo` `sms-``::/-              `-     .-o`                  .:-``  ````
``/ys+.----:::sNd.  ./o--.```--`  .omMNNddy-:d:                      -.-``.-.---.`  ```-/:```       
-::///+-`o+.::.hdy+:.-s-/.//``   --`-/shmNNdhy-````...`                 ...`-/:+/o/:+o+/-/oos+:.``  
`---/:::-/o:-/+s+yyds++..`` `.`.-````-..-:/+oss+:-----.                   .:/.--.`:ss: ``-/hd+o++/:-
         ````.---..  ``  `   `          `:``:sdNdo-`         `             `:/. .+o-     `....`` ```
          ``-.`        `` `. `          ..:.```-odNd+.`...:.-:.:.        ```-//sy-      ``````  ````
      `  `-```.``          ` `            ..`.-:--+so+/:-...:/-`:    ``:o--..  `-.`.-:-:---.//:--.:/
 `.```.`...`    ```````-..``........`.`` `    `-..--.:odmhoo-..--``.-sodds/:+-    .`    ```    ```-/
./::-::::---.`````.-`     ``` `.`             -   ``.``.+sdmh/.````  .//shhs-+`    `.....:.``.:/odm:
::........-.`.`.....------:/`  `.``/-.````````.`````.   .-./s+:..o:`    .:+:`:-````.--::-:/:--+osd: 
.``` ```       `        ````. ``.` :++:--::::-::-....           `s/...`.`.-````  ``-/////- `/ys-s:  
                        `    ..--      ```     .-     ..... ``                   `.::-``/-oyy-`s:  `
             ` ``.. `` ```.-::.`  `.:-:://-` -//+-``   `  `..``-.-...` .-:::-:.-.-.`     .::::++.-::
      ``......````.-``..::/-` `....--.`./-.-.-//+++/::+-.` `         ``     `-.```.-:.       `/+o/:.
.-.--.-.`` `  `.--+/:-:-``:/o+ss+/oo:-.``  ........--.` ``   `.`````         `.--```           .o/-`
 .`.`````...---.:://oo:-  `:oshshsyhss:--..`...:------`.---:--./::++/-.   `.:-:.`::`       `:...-..-
                ./oos//`` ./ooso/:-. ``-:-:////--:::/+///::::::/::///++-.. ``.:`     :-`..` `..-.-. 
             `---..-`.-:/:/..`     `-:/.`  ````   ````-:://:/::----..`   `...-.    `-.`.` `:-.-..`  
...`..`..----.```.-:-.``        -.--. ```                   ``` ``..```````    .-:.`    ...`     `.`
                              --.`                                           `.:-`     ..- `:-:....`
                          ````                                              ..    ...`..-:. `       
               `.-.`.:...``                                             `...   ---/`                
            ````                                                  ``-....    ` ./+`                 
       `` ``                                       ``.---`` .`...`` `  ``..-..``                    
-.-...`                                           ..-.-....-...---::-..`                            
                                               ..``                                                 
    """)
    print("""
    You face the fact that it is too dangerous to dive
into a deep hole that might lead to the center of the
earth. It is better judgment to return to the surface
and work out a plan of action.
    You give one last look at the opening, check the
Seeker's instruments and head up to the surface.
Finally the Seeker breaks through into fresh air
and sunlight and you wait to be picked up by the
Maray.
_________________________________________

    Turn to page 32.
    """)
    page32()

def page67():
    print("""
    You insist that you are all right and will dive
again the next day. The scientists try to convince
you that it is foolhardy to go down again so soon.
The captain of the Maray reportsthat a large storm
system is coming and the next day will probably be
the last day of diving for some time.
    Against advice, you enter the Seeker, wave
farewell to all your friends and descend into the
deep. You feel tired but excited.
    When you reach the bottom, you decide to
explore the ledge along the deep canyon.
_____________________________________

    Turn to page 6.
    """)
    page6()

def page68():
    print("""
    A violent storm is reported heading your way.
The captain decides to move the Maray to the
shelter of a nearby island harbor. It is too dangerous
to remain where you are. Deckhands lash the
Seeker securely to the deck of the Moray and you
get underway.
    The storm breaks before you can reach the
island harbor. The Seeker is torn loose and lost
overboard. The monitors aboard the Maray are
damaged by a frightful electric storm discharge.
You are all alive but there are no funds to replace
the damaged equipment. The expedition to Atlantis
is over.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
def page69():
    print("""
    It is no use. The whirlpool has you in its grip.
You feel your arms and legs being torn in every
direction. There is no way out. Round and round
you go.
_______________________________________

    If you use your laser pistol to
blast a hole in the whirlpool wall,
turn to page 97.

    If you continue to struggle,
turn to page 98.
    """)
    choicex = choice(97, 98)
    if choicex == "97":
        page97()
    if choicex == "98":
        page98()

def page70():
    print("""
    You decide that you can't swim out of the
whirlpool. There is only one thing to do. Dive deep
into the center.
    You kick several times and hurl yourself into the
center of the whirlpool. Lights and colors dance
before your eyes. You lose all track of where you
are. You find yourself standing on the ocean floor.
You can look up through the center of the
whirlpool and see the sky more than 2000 feet
above you. It is a tiny patch of blue.
______________________________________

    If you try to return to
the surface, turn to page 99.

    If you set out to explore
this strange area, turn to page 100.
    """)
    choicex = choice(99, 100)
    if choicex == "99":
        page99()
    if choicex == "100":
        page100()

def page71():
    print("""
    Perhaps you are being foolish, but you decide to
join them. The injection is painless and you feel no
different than before. They lead you to a comfortable
room where you all share a special tea in
celebration of your decision.
    "You see, all living beings are basically the
same. Everything is connected in life. We have
come from a different planet in search of other
living beings. We have to be very careful about
taking new people to our planet. Some of your
people seek us out, just like you. We choose carefully."
    You are amazed at what they say. A choice is
given to you. You can either journey with them
through time and space to their planet, or you can
remain in underwater Atlantis as a worker recording
information about life on earth.
_______________________________________

    If you decide to travel
with them in space and time,
turn to page 90.

    If you decide to stay in Atlantis
as a worker, turn to page 91.
    """)
    choicex = choice(90, 91)
    if choicex == "90":
        page90()
    if choicex == "91":
        page91()

def page72():
    print("""
    The only way to prove that you are not crazy is
to lead another expedition back to Atlantis. You
take all the money from the TV appearances and
articles and outfit a boat, hire a crew, rent the
Seeker, and set sail. Most people think that you are
out of your mind. You will show them.
    Poised over the spot you so carefully marked on
the charts, you dive down in the Seeker. Again you
find the hidden grotto and the round metal panel.
    The panel seems to seal off a passageway. It is
locked. You try to open it with the Seeker's drilling
arm, but it will not budge. It is frustrating to be so
close to the secret and yet so far from it.
_______________________________________

    Should you blast the panel with
the laser beam? If so, turn to page 93.

    If you wait patiently to be
observed and asked in, turn to page 94.
    """)
    choicex = choice(93, 94)
    if choicex == "93":
        page93()
    if choicex == "94":
        page94()

def page73():
    print("""
    The idea of being injected with a serum and
joining them for the rest of your life is awful. You
must plan an escape.
    When your captors are not looking, you slip
away and dash for the door of the space craft. You
fail to notice a laser beam guarding the exit hatch.
Stepping into the laser beam, you freeze in midstep.
The Atlanteans gather round you sadly and tell you
that you will have to remain this way for the earth
equivalent of 23 years and 61 days until the effects
wear off. Then you will be given a second chance.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
 
    """)
    print("""                                                                      
                                       ``-..-::+///:-.`                                             
                                 `-+ooyyoshssyhsshhhyyhs+o+::.                                      
                             `:oyyyo+/++/:-/::++//+soosyoooshooo+:`                                 
                          .-:--``                     ``.:::/+oooosy+-`                             
                        ..`                                   `:/soss+o/-.                          
                      ..                                          ..:-.`--:.                        
                    .-                                               `.`..``-.                      
                  `:`               ./oshddhys/                         `-.`  -.                    
                 .-                 /o-sMMMMMMN.                          `.`` `-.                  
                .-    ` `.          `/:NMMMMMMM/                            `.-.-:-`                
               `-    -.: -`        .-`-sNMMMMMm`                             `ysoo -.               
              `-     -.:--.        `:. `-odMMM/                            .:/..:-  .-              
              :     `.::`````-.    -`   `-smMd`                         `-:/.`   .-  `:`            
             -.      `-`    -`    `-  .-:+/s/`                         -:/.`      --  `/`           
            `-         ``   -     -`` --+//:.`.` ` `                `.::.          `:  `:`          
            :         ..`:`./...  `.` --:``  `.:.`...--..`.`      `-:-`             `:. `/          
           `:         `---+::/-.:     ::`      .-/` :.`  `-:-.` `./.`                `:  `:         
           :.          `.-/:-.-:/.    +:...    `/---s+o::::.`::--.`                   `-  .-        
           /            `.:+. -:/: `...````` ...:`-::---::.  `-:.                      `-  :.       
           +              -+:.``.-``` `.`./:-/.-- `+:--.:`-``-:``.                      .. `+       
          `:              `-.-. ./     -o:s++::`-....:-`. `.++:+```                      /  +`      
          :-               `-.:`// `````+`::-.` -....:  `````-----:-                     -. .:      
          :`                `-.--.``.-.`./:--     .`.```..` `--.-//.                      :  /      
          -`                        ``.::-..`       `````.```/-.` .:-                     :  /      
          -                     `.-...`-..`          `.:/oyo:/.:.`./:.                    `- ..     
          -`                        ``.---`          `sdNNMMNm:---.-.`                     - `:     
          :.                      `--.:..--.. `  :`.-`:NMMMMMMd:.-:.`                      .  :     
          .-                     ./syddhso/:+.y+`Ndhmh/oNMMMMMN```                         `  -     
          `/                    oNMMMMNh++hNsdNN:MMMNMMNmmMMMMd                               -     
           o                   `NMMMNy++hMMMmMMMhMMMMMMMMMMMMM/                              `/     
           /.                   /mmyoodMMMdhhdddshhys+NMMMMMMM+                              `-     
           .+                   .//+dMMMMMNh- ``      yMMMMMMMm.`                            ``     
            +                 .::.`.+dMMMMMMN+        `mMMMMMMM/-                            -      
            --              .:::`     :yNMMMMMy-       -NMMMMMMo-`                                  
             /           `-/:.`         -sNMMMMNy:`     /MMMMMMy:-                                  
             --        .-+/-`             .oNMMMMMdo-` `.oMMMMMN//-`                                
              :`     .://.                  .sNMMNmo.:: ..yMMMMMNys/-`                              
               :`` .:++.                      :ho/o`.:`  .:yNMMMMMMMms:`                            
               `/-.y+`                          /-`:-`     -+ymMMMMMMMNo:`                          
                .//o`                           - ./        `.-sdMMMMMMMdo:.                        
                 ./                            -..:..         ``./hNMMMMMMds:.                      
                  .:                           :-:.             ``-:sNMMMMMMmy.                     
                   `/`                          ..`               ``-:oNMMMMMy+.:-`                 
                    `/`                                               `-hMMMmss.-:                  
                      -.                                               `-+Nys:--/-                  
                       .-                                                 ./+/  /.                  
                         -.                                               -:::`-+````               
                          .-                                             `/+o/++//:.`               
                            --                                                                      
                             `-:                                                                    
                               `-`                                                                  
    """)

def page74():
    print("""
    You argue with yourself for several weeks about
setting out on a new expedition. Money is not the
issue. You fear that finding Atlantis will ruin it for
the Atlanteans. You believe that their civilization
must be protected. You decide to use the money
you have made to carry on research on space and
life on planets in other galaxies. Someday perhaps
you will meet the Atlanteans in space.
_______________________________________

    If you don't like this ending,
turn to page 107.


    """)
    choicex = choiceEnd(107)
    if choicex == "107":
        page107()
    if choicex == "":
        print("""
           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
        """)

def page75():
    print("""
    Escape will be difficult, but you decide that you
must get away from these people. The best plan is
to tell them that you want to accept their offer to
spy on the Atlanteans. They are of course happy
when you tell them that you will work for them.
    "You see, the Atlanteans are jealous of us. We
must be on our guard or else they will invade our
area and capture us."
    You don't believe the Atlanteans are at all jealous
of the Nodoors, but you won't argue. They
take you back to the outskirts of their area, and you
leave to join the Atlanteans. Once back with the
Atlanteans, you ask them to allow you to live with
them. You know that you will never be allowed to
leave their underwater world, but there is always
the hope for escape. It could be a good life.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page76():
    print("""
    "Ok, I'll do it," you say. "I'll join you and spy on
the Atlanteans for you. Who knows, maybe they
aren't as bad as you think."
    The Nodoors are delighted that you will help
them. They give you a room in a large building
where most of them live. It is grey and forbidding,
more like a prison than anything else. That night
when all are asleep, you sit sleepless and realize
that you are caught in a trap of your own making. It
comes to you that the Nodoors are from a different
planet and are unhappy outcasts. The Atlanteans
want nothing to do with them. You chose the
wrong side.

_______________________________________

    If you don't like this ending,
turn to page 108.


    """)
    choicex = choiceEnd(108)
    if choicex == "108":
        page108()
    if choicex == "":
        print("""
           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
        """)

def page77():
    print("""
    Maybe you can learn from the Atlanteans how
they achieve such happinessin their lives. You will
seek out their history.
    When you announce your decision to stay, you
are treated with kindness and friendship. You explain
that you would like to help in their underwater
food production.
    Atlantis was an advanced civilization thousands
of years ago. The citizens nourished their peaceful
thoughts and plucked out their hateful thoughts as
one would tend a garden. Their minds became a
rich and dazzling universe, clear and unbounded.
    You have so much to do, helping with sea plants
and studying their history that you soon forget the
Seeker.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page78():
    print("""
                             `.````::.. . `` ` -.    ` ` `. ```-`        `--:-----.                     
                         /hyh.`yydd:`-`/ : --   :`:.....oo:y`       .ymmNmo`                        
                         +ymh  oydyN. ::-: -.  `- /`+o../s/`        yMMMs.                          
                         -yy/  :dMNN.-//++     / .::.` `so         .mNMm                            
                         `hh-  `dMMMms:/y-`-/`.:+s`  `+d:           mMM+                            
                          od-   +NMMMN/+y`-..`::sd .+ys.            hMN.                            
                          /d- /  yNNMNso+-.:-::+odyy+.  `.`         sMN.                            
                          `d- -:.`hMMNN/ +.+:`:dmNy`    .:`         sMM:                            
                           o::`.:`/hNMMs`:-.+dsssos` .--            :NMo                            
                           .h`---:.`/dMd.-:yNm..+`//` .`            sMM/                            
                            o/ ``. `:/Nh-.mMMs  :.  -`              oMN-                            
                            `d/  . :`-Ny`:dNms .`:`  -.            `oyh`                            
                             /N/ ``/-/M+-/yddm/----`  .-          -oo+.                             
                    `--./--   hN+-`- sm++-yyhhdy:/.`:` `:`      /dms-                               
                    `.-.``:.``:Mds . mh-.`.ysyyys/- `-.  -`   .yyo:`                                
                      .-` ..`.`hmN/ -NM-/-.o./++osyy+.`-` `.`:y+.                                   
                       `   `.: +NNm +NM:+odms:```-/syhs-..  /y:                                     
                           :.:.-MNm--mM/mmNNmyy+   ``-oy/--./-.                                     
                           `-.--mMd::/NMMNNsyhh.  ``  ``++-/. -`                                    
                            ``./mNh-ys:mMMM//:o:   .- :`.-o`-.`-                                    
                               yMNy.sMd+yMM+.//y/``.:-:...y. -`--                                   
                              .shmd -dNNs+Nd.--ydo:`-s+: .d`  :`+                                   
                              :hdd/ :o/oNo+Mm+.-y+:.//h+`o:   `:-`                                  
                             `/+sh`.m+`-mM+sMyohmNh+s:+/:-.+s/ :..                                  
                             -/sm-.hMyo:dMm/ddMMMMhNh/:syhyhmN::-`                                  
                            `/+h+.yMNyyssssyhhMNNdsNsh-dsymNmy+o:`                                  
                            .-::.ohmNNy-y/ys:`yyodMMMd`+mNhMNysd/                                   
                           `.  . :////-./+s-`/+hmMNNs+o.yssmNdm/                                    
                           -  -    .-./`:`+` ssmMMNmdMMhydmmmdo:-`                                  
                           `  :   `+.-+-` -` -osMNdyymNdoydNNh/ `-.                                 
                           . `.  `-` :`: -/`  :mN/.  ./``yMMmss  `:-                                
                           - `   :  -. :`-/-  `mm. ..-`.--+NmMNo. :..                               
                           .:-   /:.+` /://:  `hy.. -o/-   :MMNdh/- -                               
                           `h/   :dhho -s. :  `o:/..-ys    `mMMhs/`.:                               
                            -+.  `smmm` /--:   ohms+/-o     sMMN:.`hNo.                             
                             o+   .hmM- `: /`  -yNd+:oy`    .mMM:.-.sys/                            
                            `-+     .ss  -`/`   +dy/+dy/`  `.-NMy.                                  
                            - -`      o/. -+`   `so-/+s`..`:  oNy/`                                 
                           `- `:       --./+` `+d/:yoo -.`:+`.+NMh:.                                
                           :o/.-        `:os:.-`.++s+o  ./`./`-ydmmhso+:.`                          
                           /MNd`          +do+y:. /:--  -hy``/    `.:sdNMd/                         
                           `NNy         ./yyysMN-`- `-  -dhs``-        .+d-                         
                           `MN+       .dmhyy`sNMmo `-   -hm`: `-                                    
                            /M+      .sNmo.+  .hh `o.   `hy `/ .-                                   
                             dy      h//o :-   .:-sos.   ds  -. --                                  
                             `d-    ymdo--./   /.:-yhs`  oo   /` /                                  
                              `s`  ohmy..-:`  -.:-+ho.-/.//   .- +                                  
                               `o  odhd.:`:  .+ +-:. + //od+- `: ./                                 
                                ++`mNMm+`+`.. o`+    -` --d-oh`:  +                                 
                                -N:dMMm-:::..-y+/`    :` -oh:hso `+                                 
                                :My-dN:.dss+. ++o:     -`./`-/-/` +                                 
                                sNN` / +Mmms  -h/+.     oo:`  :.``/                                 
                               `mMM/..`hhhMMs` o++:.    /d++  /  /                                  
                               yMMMs- :s /MMMN+`y++//   -+hs-:` -.                                  
                              /MMNMo+ /: `m+hMm+.oo/++   /dd+` .-                                   
                             -mdmdh-- +.  m/.NMh/-o++ss` :s- `-`                                    
                            .mysoss : +` +Ny +MN+ :oosy+-``:+.                                      
                           `hdohdd- : /.`mMm.`mN:  :s+.  .yyh                                       
                          `yNh+ydo  :`--`NNN+.mh  `.- `-+//.+                                       
                          omhs+hs   .-`:/dmNy ho .-``/oo/y--`                                       
                         /shhdd+`    / s:/oNs`d: yh.::s+oo.:                                        
                        `hshhy/      -`-:--o.ys  sNo: os/:o                                         
                        oNyds-        + +.::/y`  .ydy .+-ys                                         
                        dmds`        :y-:/.+o.    -dm-/-ysd                                         
                       .yNs`        `dNo`::s`      :dh/:+yd                                         
                       .Nd`         :d+ --o-        -yho.mh                                         
                       `N/         -ym` `/+:        /o/d/dd                                         
                        s/         ymm` .yo:`       //s-/dh                                         
                        -+`        ymNh-/sm/:      `+ :. yh-`                                       
                         /.`       -NMMmmho-/-      +  - yh.yo-`                                    
                         : ..      `dMMNNsy :+-.`   /` - sh :ms-..                                  
                         .. `.      -NMMN`m//Nyo--  :  `-dh +dNNs:                                  
                          -` `.`     /NMM-mh/NMm:: ./-``:Nh `+smm/                                  
                           .   .`     :mMsyh`-sNo`  /.  oMy`   +d-`                                 
                           `.   `.     -NmoM` :yd/` :`  sd/.:  -d:-`                                
                            ..   --     dMsm`  `h:: -.  hNm:/   sso.                                
                             `-.`.`.`  `mmms`   :y+` / .oMN+.   yss.                                
                              `.::. -` /hmm+:    yd+-- :-Nm+    o-y/`                               
                                -://:/+hdds+::.` -Nh: `:`mms   `+:-                                 
                                 ..:+++mN+.dh-./ `y/  -` mdy.  ::-                                  
                                  ..`../+ :NMNy+ oh:./`  oh./ .o--                                  
                                   `+`  -` :odNo-`.`ys   :d:o`sy+o/                                 
                                   /Mh.  :  `oNd/  /Mo   `yyoyhh. `                                 
                                 `:NM+`:-.-   h+.`-Nm+    -ddh.:                                    
                                /dNs+d-`-+-``/oo` :moo     oo:+`                                    
                               -NMh:/+.  .`::y+ `osh`:     y+:y.                                    
                               -mMMNd/   `:-+  `-omd/:    /y-dh/`                                   
                                 sMd`     `-/ `- .m++.   `hh+/m++`                                  
                                 sm+:     .+o.-  :s`+    +ds: o/./                                  
                                .mMs.    -.-d+  `d+:o.   sN:: .h/h.                                 
                                 /ds+    o/:my` /N.yo:   sN::  -/do                                 
                                  sho.   :m+dys`hh/`y+:  dN/:   sh:-                                
                                  `d:/  .:+:NN/oNy: o:+  mM+-   .o+:`                               
                                   `oos .:-+dmhydy` /h/  NMs-    +s.:                               
    """)

def page79():
    page78()
    print("""
    When you get a chance and everyone is doing
other things, you dash for the tunnel exit and make
it out into the water. No alarms sound. No one
chases you. It is strange; they said they wouldn't
allow you to return to the world above the sea.
Why are they letting you escape?
    You swim toward the surface; then you black
out. It is too deep. No one could survive the pressure
and lack of oxygen. But a miracle has happened
because you suddenly find yourself hacking
away at brown seaweed that surrounds you and
you are just a short way from the surface.
______________________________________

    Turn to page 50.
    """)
    page50()
    
def page80():
    print("""
    An advisor to a king! What a chance. Maybe the
king has ruled so long that he is out of touch with
the people. Perhaps as his advisor you can help
the people get what they want. You don't believe
that people are lazy and selfish. The king just needs
a new point of view.
    You are appointed the king's special advisor on
problems of research on food and shelter. You
immediately call general meetings of all the people
to discuss the food program and the work
schedules. The king is so glad to have someone
else take over the problemsthat he leavesit in your
hands entirely. He gives you land and a large
salary. You set up new programs and schedules.
The people are involved in the planning and the
work. You listen to their complaints and their
ideas. Life under the sea is rich and full. The
people are hard working and good. It was a wise
decision to remain.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page81():
    print("""
    You do not wish to lead a revolt but the people
need you. You organize the play, and the king is
pleased to have his people involved in a project
that keeps them busy and happy. The people can't
wait for the day when they can put the king in
prison and make their own decisions.
    The night of the play, the theater is filled, and
everyone waits for the king to appear. But there is
a delay. The crowd grows nervous. Then a messenger
from the king runs into the theater and
announcesthat the king has had a serious attack of
brain fever. He may not live.
    You wonder whether the king is really ill or
whether he has found out about the plot against
him. The people are confused and do not know
what to do. They turn to you and you tell them to
go on with the play.Just then, a squad of the king's
soldiers enter the theater. They are headed for
you.
_______________________________________

    If you allow them to capture you,
turn to page 116.

    If you try to escape, turn to page 117.
    """)
    choicex = choice(116, 117)
    if choicex == "116":
        page116()
    if choicex == "117":
        page117()

def page82():
    print("""
    Advisor to a mean king? Not a chance! You tell
him that you want nothing to do with a tyrant who
doesn't believe in people. You tell him to his face
that the people are unhappy and angry. He laughs
and tells you to go back to them if you wish. He
warns you that the people are complainers, not
workers.
    Once back with your new friends, you discuss
how to overthrow the king and his henchmen. You
hold secret meetings and work out a plan. But on
the day of the overthrow, someone discovers a
leak in the volcano wall of the underwater world.
The entire civilization is in danger. All thoughts of
revolt are forgotten. The Atlanteans must stop the
sea from crashing in on them. Everyone works for
a common purpose. Survival is the goal.
______________________________________

    If you decide to work with them
in this time of disaster, turn to page 112.

    If you decide to take advantage of
this emergency to escape, turn to page 114.
    """)
    page83()
    choicex = choice(112, 114)
    if choicex == "112":
        page112()
    if choicex == "114":
        page114()

def page83():
    print("""
                                               `.                                                   
                                              ./::                                                  
                                          /.:` -//                                                  
                                          :-://`/o.                                                 
                                            `:+:+/////.                                             
                                              -+..-/.:-:+/                                          
                                            -:/:-/:o+///`-/:                                        
                                            ::+syo -``ys:-./.                                       
                                       .+.   -:...  `+hm+---+. .h:      `                           
                                      .mmo   ::`::/+hydh+---+/.yNmo    +o+                          
                                     `ymhs-.-:`/`:hdsohy+----dhyyhm   /dyy                          
                                  :o.+dhy-o-/:://:.:+ohd--..`ydyhhd` -mmoy`                         
                              `../mmsdmdo-y:-+sh:.`-+oh/``.`/Ndhdhh.:dNNs+yh.                       
                            `so/+yo+/+yNs/d+sosoyhsoss+.-..:hNso/o///oyd/-://-::..`                 
                         ```.--sdds+sdNhmymmMNmdsosyd/---.-osdhm+:/-:osmshhyydhmyh+                 
                        +hdmmmmNNhyNMNs-Md++dosh/ohdo.`  :osoydy+/hsdssNo:dmMs/:..                  
                         .-+hNdo/ohMNo:oNmh/so/syyds.`.:s+/s/sy++yyhy-hNm/dMMmyyooo//.              
                           .hshys+mmo:+d+oNm+s:/ydo..-/::so++`+ssdho+oomMmyydMMMNNmdy:              
                          .hssdys+d/+:+s:odNmho/y+-..+so :h+s `ommyo/:yodNhsshmN-.`                 
                         .dm/s/:+-+/sddsyssyNNsyo. -os+s+/dyy/.+hhy.+oooohh/syyo                    
                       :+hNh::osss--sNNdmy/yNNhss..ssMm+ymdoy/+Nd:os::ods+/-:.y++                   
                      /NhNdyyyoyyo/:/NmdhMmhmNdds::s.shosMd/hhNNdhydy+hs+++/:.-oyoo.                
                      .:/mMMNmyhmsosmMmhmMNdhhy++/-/o..ody+smMmsmmdmd/mdyhshhs+o+yNy`               
                        `dmdmydyyNdNNNMNmmmMhdmddd::/os++/++MNydhmNds`:dhdhdmdms-s:`                
                       :sy.+.:dysmhdhyMyo:syosso+sosy/s:/yhshyys++myso:ydyoo+oh+s.                  
                     `sho-+-:yhomhmysdms:oss+++.+`oo.s.  s/o/-+++ooo`o`:+s-:` :.h/                  
                    .yy+/hsymdmmhsh+hmyyddyy/- ../: o:   y.-++/+++sh.y--syy:/ /./mo.                
                   .my+shsdmdmd/-s+hyssymys/. ./:`` +    /. .s-+o/yddh:-+yhs:-hd+/sh-               
                  `hhsdhhdhdhh+.+o+h+ooo+/..+/-  :: .:+   .  `/--:/shm/--yhs+/ydsosoh`              
                  /M+NmNdhdyos://+o++/.s:dNmydd/-y/` +o:  .`/+/.  .:omd:-yyso+yhhsh+m/              
                  sMNmhyhy+y+:::smhyshmmMMMMMNydss- :s::oommMNho+/-  .dh/syyy/y+sy//ss              
                  -NNdhyoh/+:-/ymh+sdsdNMMMMMMNm/o. y+omMNMMMNMNdh/   :yyoyoy-o/sh:/:h              
                  -hMd+sss+::shomysdNmmNMMMmmMMMys` :+hMNmNNNmMNdMm+- +h:hh/y/:ooo:/`h              
                   `ymy:ssoohm+yy+sNdhmMMNo.yMMMNh//`oMMMyoddNNydyho`-hhoomyoo.s:oo-:y              
                   `hmoosomdNy`mhyysshNmMmyyhNMMM/   sMMMs++mMMddyyo ymmm+ydhs /ods`s.              
                  `sodyosyhNd/ ym+`.-oNNMMMMMMMMN`   /MMMMMMMMNd/ss`.hhhdm/myy//+d`-+               
                  sysNsyshhmms.dm-   /mdMMMMNNmmm`   -NMMMMMMMss+ `` shhmd/hh:`s./: :.              
                 `mhh/y:hymNh::Ms`   ```syhyhhhm+:-   -dMmmmy+        omMy +so .h`+``/              
                  hMhosshhNmh.`Ns:```   ::`.oyyssmmy.  :+//-`         .Nho +sy` d/`o :              
                  /My/ohhdyhy`:dmys/--//::osdmsdMMNo`:.-y`            oNsh.:o/o dh +-/              
                 `+My:hdhy:o+ s-Nsyhhh+syoodMNmNNds- -y.:-           .Ndhh-:y+y.dd /y`              
                  -dd//Nmhddo o:hNmdNmdmhymMMMMMNy   :ho:--        ``oMmhdosdhhsyy`/o               
                   .Ndodhydy:-y:+NmmmNNmNmMMMMMMMNh+ohMmy-.+:-`   `o`+MdosydmdhMyd.y-               
                    -Nysh/h:.s:omNdNNMmNmmNNNNMMMMNMMMMmmyommy+`  oo:`mddydmydyNyd:h                
                   .ohydmhdo/ysmmNNNNMNmmddhhhNmNNmmmh:::./yNmd. -dd/ ddddNhdhyNhy/+                
                   .hdyhmmN+ohsmmNNNNdmhshsdddhhh/-h:`    `:Nmy` -mNy`dNymNoNosNmos-                
                   .NdhhddMNh+smmNdmooyodddhdo/:/``s`       omy: `ymd.yNoNsoh-shd+:y`               
                  `omdmymsNmdsmmmdNhmmNNMMmmo/:-:  `        /ody:.:ym+/mhmssy.myd+`h-               
                 :yddNhsyydmmdmmNNmmMNMMNds+++oso-..--.``  .+dMMMNmmdNmmMmm/+`dsd//+-               
                ooyhmNdNsddNNhdmMNmNmNMmhhyhmdysyssymNNdhdyoo+hMMMMNNMNNMMm+/:y+o/-s`               
                ohdhmddNssyNdsmMmdmmNNh.::/oNNmyo/``-:+osyd:dhyhmMMmNMMMNNd-+s.y::.s                
                 hmyhydmsshNohyNmddymh/.-::+dNMNMNosh/+:.`os:/`.sMMNMMNMmmmos..h/`o`                
                 yhmsdhhhdmsyoyhmyhyshoydy:sdmdNNs+///oyyyh:.``ohhMMMMNMNdNm+ +d./:                 
                :/oymh+yyhmoo/dmmhmmdsdydddmNddmh/.`  ````` .o:hysNmdNmMNdMmo`d+.+                  
                -/+-NdmNoNyy` +ddydmdyh+hymdmNNNNmho/// `.``:yymdsdNyNdddddhhom-+`                  
                `s+ oddMhNyo :oy++yddddsydhydmdmdhhNdmh+h+soh+:syymsdds-myyshmhh`   `.`             
                 oo .dhNmNM- ho:  .:yhmdhyhdmyhydyhNmmhmmhmm+d/oddNyys. odhymyso   -:-/             
                 `s/`d+smNM.:m:    `../dddhddymdhdhoymhmhyhy`doomyd++:.`+ddsNyh/   o                
                 ``yodhsyyM/:m.       -/hsomhNhdoyh+Ndyyyhmm/N+sd+o/-  /sydhMmds   -:               
                 :::y+dyysNd`dd`      .:y:.hoysoo./.ysd+yNNmod/:y:/-` -+-dyhMN/y.   .:`             
                 `. -hs/smmM::Ns`      /.:/o+/oo. ` ./::/d+yho-:s.   `y`-M/dhh`os    `.             
                    -oo.so:My :mo      ` .-y-/+`       .-::+d/ /.`   `+/+M/dsd/:y-./. /.            
                   ://oy-+:Mm  oy         .y/+`          ./-ho.`.      /dN`ohsNo/o-:+ :-            
                   s/+:s +yM+  :s         .o./            - /::       `++N  oodo`o//o:-             
                  `hy h..dMs  `y.         `o`               ::/      `+..N- +/N--syd:               
                  `od.h:yMs   o:           /                `-`     -s`  y+ -.hy:/+y.               
                   +s+No/m``  s`                                    o/   :o   .-- :h                
                    +/my`/`o` .-                                     y  `y      -`/.                
                    `-/+::`:.                                       .o  /o     :.                   
                       s. ..                                        `-  `+:-/  /`                   
                       `/- `+                                               :/  .                   
                         ::--                                                -:-                    
    """)

def page84():
    print("""
                                                                                              ``.-.
                                                                                   ````.```.--+oooo 
                                                                              `..-.```..-`.yddsohNd 
                                                                          `..-.`` `...`:/odmo+hNMMm 
                                                                       ..:.`   `.-.-:-oNNNo-sNNMMMm 
                                                                   `.-:.`   `..``..+/oNNy-+hNNMMMMN 
                                                                 .-:.`   ``.`-` .:symNh-:yNMdNMNMd: 
                                                               `..`    .-.` `-`+dmMNy:-/hNNmmNMMh-` 
                                                             `..    `.-.   -/+hmMNy//hdmmmmNMMN+``. 
                                                          `.-```  `-.`    `:hNNdo//hNmNNNNMMMN+  -` 
                                                       ``.-```` .-`     `-yNNy/:ommNMMNMMMMMy-  .`` 
                                                      `.-.``  `-`      .yNNs:+ydhMNNNMNMMMNs`  -`.` 
                                                    `.-.``  .-`      `/mNy-/sddmdMMMmMNMMM+   -`.`  
                                                   `..`.` .-`       -hMd/:ommhmNNMMMMMMMMh   -`.. ` 
                                                  .` `` `-.        :mMd.-mmNNmMNNNMMMMMMN-  ..`. `- 
                                                .. `. `..         .dMN.:mdNdMNMNNMMMMMMMm  `.`- `-  
                                              `.` .` .:`         /dMMy.mmdMMNNMMMMMMMMMMo  - - `-   
                                             .` `.  -.          +NMMMoomhMMmNNMNMMMMMMMM- `... :    
                                           `.` `` .:           +NMMMNNdNdMNMMNNNMMMMMMMd  : - -`    
                                          .. `.  :-           :NMMMMMMmNmMNMMMMMMMNMMMM+ ...`.`     
                                       ``-` ..  :`           :dMMNMMMMMMMNMMMMNMMMNMMN/  - . -      
`````           ``                    ``-  .`  .`           -hNMNdNMNNMMNNNNMNMNMMMMNy  -` `.`      
                  ``...`.`. ```     `...  :. `-`           +hNMMdhmdNMMMMMMMMMMMMMNm/` `-   -       
```.-.`` `-..`.`            ``` `` ..-.  -`  -````..` `-.`.syhdmmmNNNNMMMMMMMMNmmdh``  :   ``       
`````      ``..                   .`-`  -   :             ```     ``````.``````  ``   -`   .     `` 
         -`                      -`-`  -   -                               ```...-```.-``  .    .:. 
         `-..--..-.............-/::.`.:.  .. `        `:o++++ooooooshhydmhdNNMMNd:  `-`.:`-:.--.    
                               -.-`  ..  `-           .NMMMMMMMMMMMMMMMMMMMMMMMMd`  .  -`..`--..... 
                              -`-`  `:  `:           `oMMMMNMMMNNMMMNh.yMMMMMMMNo   - -`- -         
                             -`-`   :   /            +NMMMMMMMMMMMMMNs`dMMMMNMMy+  .` - : -         
                            ....   ..  :.           omMMMMMMMMMMMMMNds+/MMMMMMMd-  : -``. -         
     ` .-.                 `-`-    :  `:           :NdMMMNNNNMmMMMMs:do`/NMMMMMd`  - - .` `         
     .sddo+               `-`:    .`  +            oMNMMMMMNNMNNMMm//dd+ :NMMMN+   - - -  .         
      hNMNs               : -`   `.  :.          .:hMMMMmNNNMNMMMMmohhym: +NMMN-   -`: -  -         
     `/:+::/             :``.    -   +           /sdNNNMmMMNNNMMMMMmyohdN::ddN+    :`/ -  .         
                        -``-    .   /-          .+dmNMNmMNNMNNMMMMMMdohsmh-::+:`   / . -  -         
                       -` :`   -`   y           :smdNMNNMNNMMNMMMMMMMmyo/h/   ./  .. : -  :         
                      .` ..   .`   :h           yhhddMMNmNNMMMMMMMMMMNh+::s-   y+..  : -  +         
                     .` `-   .`    y+    `     /dmmddMMNMMMNMMMMMMMMMMs+-:s:`  +ys`  - -  :         
                    ..  /   ..    +m`         /dmhMmNMNNMMMMMMMMMMMMMMy/:://. -hhys. - `  -         
                   ..  -`  ..   .yNd.        `mmMmmmNNMMMMMMMMMMMMMMNNd++--:..ohdhdd.` .  -         
                  `.  ..  .`  .omMN/         :mmMMdddMMMMMMMMMMMMMMMNmsy+::.:shmmsy+/` :  -         
                 `.  .- `-` `/mMMMd`     `  `oNmNNmmhMMMMMMMMMMNMMMNd::/+//oNNhs:`. // -  -         
                `-  .- ..  .hMMMMM/     `   :sNmNNNNmMMMMNMMMMMNMMmo.`::`-oMMm/`:.` :::`  :         
               `-  .-  `  -dNmyoNd`    ``   sNNNMMNNMNMMMNMMMMMMms-``.-`.:mdNy://.`:-.-.  /         
              `-  ``     `hs:` +d.         .MMMMMMMNMmMMMMNMMMms..```+soo+shh:++--:/`` -` -         
             `-  .       .`   :m:         `hMMMMMMMMNNMmMNNMdo.``  .sd-`/ys:. `-/:-.`- ....         
            .. ``            -d:         `yMMMMMMMMMMNMNMNd/````  `.+. +d-       +/:.:``..          
           -. .`            -y.    `    `sMMMNNMMMMMMMMdo-   ` `` `   :h-       `-o+:///.:          
         `-``-`            -+`    ``   `oMMMMMMMMMMNms:              -:`       `.`.++sy: :          
.`      `- `-             ::    `     `sMMMMMMMMMmy:`    ``` `      -.         ````.o/o/ :          
 `...` -. -.             :.   `::    .yNMMMMMMMMs.  ....`  `.`    `.             `.`.oy.`.          
`   `-:./s-`           `:.  `.:.    :hmMMMMMMMh-`...`  `...      .`              .``..+ :`          
-`  ..`. ..+-.        -:  `.:.    -ydMMMMMNMN+..`   ...`       `.                  --.- :           
 -:.  ..   ``:--    `:``:+.     -yNMMMMMMMm+..    ``          .`                   ``: `-           
 ..-      :+`   `..:--//-   `:smMMMMMMMMho`.`               ..                      -` -`           
    :`    .` ``` --`...-.++hmMMMMMMMNy:` ..    `          `-                       ..  :            
   -:-`   ```  .:``:+yNNMMMMMNMMNh+-    .`    .`        `.`                       ..  `-            
 `-.  .   :. .-:/ymmdMMMMMMmds/.`     ..    `.        ..`                        ..   :             
.`     -   .:ydds/.`oMmyo/.`        `.`   `.`       ...                         .`   `-             
        /-smh+-``  ::.`           ..`   `.`      `..`                          .`    :              
       .mmo-` `   -`          ....   ...`      ...                            -`    -`              
       hh`    ``---      `....   `...`      ...                             `-     ..               
      `/`     ++:+   `````  ``..```     ``..`                    ..```     ..     .:                
   ``.`     ..:-.. ```   ``.`        ``.`                                 .`     .-                 
`  ```     `//--.-`   `..`         ``                                   `.      .:`                 
`... .`  ``..+.-`  `..`                                `..````.-  ``` `.`      .-.. `               
 `---`   `-o-/.  ``.``     ``                 `.....-... ```...`` ``.`.`      -+.```    `  `.`..-.. 
 ./--. `:+/``` `.`      `                             ``  ```     ``-        -..`      -o:/++...`:+ 
-o-.``-+:.`   .`                                 ``` ``..`.-.`` ``.`       `+::...--/syyhsyhhyosyh+ 
:/- `/m:  ` `.                                   ````.:://oo//:-`         -+-.-...` ...`.......:+/- 
.-/ `s-    ``                                         `  `.---`         .:/::-::::-./:-..  `.````-. 
``+`+.   `-`                                            `.``          ``````` ` `.-:os:.`.`  `.--.` 
 -./.  .`-`  `                                       ````           ``.```    .-/+o//::/+os+ohso:.` 
 +/.   `.  ``                                    ``.``           `.`  .-+y+- `o/++yyyossyhmmdmy/.`` 
.:` ` ``  .`                                  `..``           `.`      `...` .:-:oydNhooo/+.`-+ss/+ 
`  ``.  ``                                 `.``            ````                    .::`             
  ..`  .`                                ```            ```                                         
`.`                                     `            ```                                            
.                                                 ``                                                
                                             ````                                                   
                                         `.``                                                       
                                      ````                                                          
                                   .``                                                              
                                ..`                                                                 
                             `..                                                                    
                           ..`                                                                      
    """)

def page85():
    page84()
    print("""
    People ride dolphins, and you have met scuba
divers who reported they held onto the flukes of
whales for short rides. It sounds crazy, but this may
be your only way of escape. You leave the Seeker,
swim to the whale, and grab its fluke. With a
smooth powerful movement, the giant mammal
begins to swim to the surface. You have trouble
holding on. Then the whale breaksthe surface and
lies there filling its lungs with air. You quietly swim
away.
    You drift for 2 or 3 days, dozing and waking
comfortably. You stay warm in your insulated sea
suit and its special air packs keep you afloat. You
are hungry and thirsty, but unharmed by the time
the search helicopter spots you bobbing in the
waves.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page86():
    print("""
    It is their world, but you are willing to help them
with the planning for the overthrow of the king.
You want no real part in the revolt.
    The planning requires choosing new leaders
and setting goals for the people. You almost decide
to join them in the actual revolt, but you really
want to get back to your own world. Once the
revolt is underway, you hope to slip away and
return to the Seeker for a quick escape to the
surface of the ocean.
    The day of the revolt, you can't resist the excitement
of the Atlanteans' bold enterprise, and
you decide to stay with them and help in any way
that you can. The endless planning and training
pays off. The carefully selected band of men and
women easily capture the king and his guards. The
revolt has succeeded without shedding a drop of
blood and the people celebrate for days.
    The Atlanteans treat you as if you are one of
them, and, for the first time, you feel that you are.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    
def page87():
    print("""
    You admit that you just don't know what to do.
The whale is frightening looking and you don't
have any escape plans. So you wait and watch and
listen.
    After what seems a long time, but is probably
just a few minutes, the mysterious submarine returns,
attaches a cable to the Seeker, and pulls you
up to the surface. Then the submarine vanishes
under the wavesleaving you to wait for the Maray.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                                                                         ` -.                       
                                                                        -:- `/.                     
                                                                      `-  :/:                       
                                                                      `.   ````                     
                  `                                                     .` -:``-.                   
                   .`                                                  ++/-....`                    
                    ``                                                 ----:.` `                    
                      .`                                               `.-:-```..`                  
                       .                         `:.`            ``` ` `:/` `.`o:-                  
                    ``  .        `.              :: .           .:.... `:.  .o/-:/`                 
             -`     :s/-..````   `-             `::-.           .`-`   . ..  ``                     
             :.-`  ```  .:`/`-.` .`              ....       `` `:  `.-`  ` ``                       
             `::.+o/:.   .`` .....              ` ``       `s-.  `:o+/. .::-:                       
              s-/ssdmhd://-:+++-`               -          `//```//o .--`/:+.:                      
              s.-` .:o//dm/osdy                 -         `o+``.-`s:+dy/`--::-                      
             --`     :- ```` `:                `:        .hN/ `o+/m-/oy/ ...--                      
                           `       ./+o+/+:o.:`-y-      `hhmsoyy/ymo::o` `.-..   `./`               
 .-`--::::-......`.```     +`      `:::ysssyss+yho:-.`  `sshdmNyddymo.o+:..-+///-...                
  ` ``````````-hs-::-.-:`-:os-.---.`` -o+syysssso++o::  `````yNhhymMdydmd+ydmho.                    
 ```  `` ``` ``...-mh`.:`` -h+--:::-.`.` :/        .+://:/. `mdyhdNMNy-+s:o:/-..                    
..--:--.......`..`-Nm-..-..-++--..:`` . `+`         +:---oo.:Nsymhdmd:`.  --/```                    
.``-//+-         ++ss        +``      : /s          .o`os-h/-NmNMMmds..:--+/--                      
``.`--//`        sh.-        .-       :`so           /./o-:+dNMMNMMm- --//.:-.  `...`     ````      
.` `:/`:  `.`    yh-.        `s       /:s/..--/:::/-/hh.-s..dMMMMNhy `+-``         `` `./-:----`-/  
`...:` -.::-:    -:o:        `+.```./:shmhsmmNNmo+hssoy+//--dMMMMmms-//--              /hhsshyhyo`  
::-:/`--`:+./....--/.````` `./+/.`  `..:++o++/+//:+--.```  `/hmMMhMmo+:-.`..``          .-/s//.`/.  
-..`.`.:.+hyo+-  .`:`--...`.`           -`o`+./`::+`          .:+/hdhdo-.   ``..`         `         
-.`````-.-/++/:.--.-.`````                  ` ` ` `                  `-.        .-.` ``::-`         
dhhsoo//:-::/:-. ````.``                                                        ./:/:/-o:.-         
hhhNNMNNMNNNNddyyys+/:-..``                                                      .:./+ys/`.`        
o//ssmyhhhddmmNNNNMNMNMNmddhyso/:-.````-/++.                                     `://sNNy.-  ``` ```
NNNMNMNMNNNNNNNNNNMMMMMMMMMMMMMMNMNmdhhNdsyy:-.```                                .-:-s::.` `-/+-:/-
///osyddNyydmdyddNdNddNdmmmdNmNNMMNNNMNMMMMMMNNmmdhyyso+/::::-....``````````...-/oydNs+````:-`:-.:`-
ys`  .-./sdmmmsssmyy+so/o+h++/:ohyhysdsyhyhyhyddNmmNNNMMNMMNMMNNNNmmmdmmmmNmNNNNMMMMN:hhdy+oyo+:::::
mm: /` .+sshMMMmmmyo/so:+/s//::syhdsso.-+/:/:.:o/o+hyoyhsshddNNMMMMNMMMMNMMMMMMMMNMMd/:::+oyoo+o/:.-
NN/`:. :NNddmMMNMMMNhsyo+oy+/+yNMMMMNs-/:::--`/yshhho////-/+/ooshsyhmmmNMMNMMMMMMNMNo`  .-.+++s/s++-
mMs.` `oMMMNMNMNNNMMMMmdyys++:ohmNmdhs:+::/:.-hMMMMMdh-::..::-/::/.:-oosyhhdNNMMMNy-`/.-/yyyos/:-:++
NNNoo. :NMNNNNm++mNMMNdNNNhsooyysh//o/o+/+/-./symdmmhy//--:////::-`..-/:s+shhydNM-   `/yyNmNmydooo++
NNNy/--.:+--::`.`./hNNMMNMMNmdmddh+++:y+/o+:-o+/+ooos++/-/dhyhhdyhsshhydmddNmddyo  `++yomMNmmyNyoy/o
y/++sydyy/.`.--``.`./yNNdhddNNNMMNNmmdhsyddsshohoshymoys/:mNNMMMNNmdmdhydNNmdmdyo- `hddNNdmNNhNhho .
oyhydddmmhs:``.`.oyshdmNMNmhyssyddddmmmdmNmdNNdNmMdmNNMmdmdmNNmmmNmNMMdydhysosooo+/:/+ymMNNmhddhy+:.
mMNNMMMMM+-. - ``:mNNMMMMNMNMMNmmhysyyssyhsohoo+shymNMMNMMMMmNMMMMMMMNMMMNNMMMMMMMMNmdy+oyyso/:---:.
.-:::::++/ ..``  .-/---:-.-.:+//hydmNMNNNNNmNNNNNNNmmdhhyso+////////+/:/:---///:-://+/::-+//:://::: 
       /:.` ...``-` -             `/+:--:```````.``              `.--::oo++:/.                      
     `.`:`.+-/+/+/-.--...       ://-```..      -/s+--                                               
     -/-/--::::--//-`````                                                                           
    """)
    
def page88():
    print("""
    The electrons whirl about at dizzy speeds and
you continue until you get to a spot where your
instruments indicate that there is no time. The
clocks stop, the speed indicator stops, your heart
stops, and yet you are alive. Every sense in your
body seems more alive than ever before. You hear
beautiful music and see lights that you feel and
taste as well. Peace and well-being fill you.
    You become aware of other beings close to you.
No one has entered through the only hatch and yet
there are other presences in the Seeker. Turning
around, you see three Atlanteans. Then you feel
that the Seeker has become just a thought and that
the people from Atlantis have entered your mind
and are aboard the Seeker. You try to enter their
thoughts, but they tell you that you have not journeyed
far enough yet to be able to become a
thought-traveler.
_______________________________________

    If you try to turn back from
this strange world, turn to page 95.

    If you decide to travel in
thought-time-space, turn to page 96.
    """)
    choicex = choice(95, 96)
    if choicex == "95":
        page95()
    if choicex == "96":
        page96()

def page89():
    print("""
    No, you will not dive down toward the center of
the earth. Once through the thin outer layer of the
earth, you know that the regions beneath change
from solid to molten and then to a hard core. At
least that is the theory given by the scientists. You
couldn't possibly survive such a journey. Anyway,
you think that your sonar gear is probably not
working correctly. The hole is deep, but you don't
believe that it really goes all the way to the center of
the earth. Caution is your approach. You go back
to the surface to consult with the scientists aboard
the Moray.
    The scientists tell you that their instruments have
been damaged, perhaps by an approaching storm,
and they too, are cautious. They decide to move
the Maray away from the site of the mysterious
hole. The expedition retreats and you know your
chance to discover Atlantis has slipped away.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page90():
    print("""
    "I will go with you. I want to see other parts of
the universe."
"Congratulations. You will not regret this. We
are ready to depart."
They take you to a small room and three of them
stand with you under a beam of intense light. You
feel a rush of speed, and yet you are not moving.
You feel as though you have traveled hundreds of
thousands of milesin space. You rush past the sun,
past and through the Milky Way, and on into other
galaxies. Yet, you feel asthough you are stillstanding
in the same spot.
Then you are on the planet Aygr where the
Atlanteans came from. It is a world of fantastic
shapes and strange plants. The city gleams like a
thousand search lights. The shapes that must be
their buildings are pure light pulsing with energy.
Nothing is hard or sharp. Everything is light. You
see no people, just forms of brighter light that
move. Suddenly, some of the moving forms
change into Atlanteans.
"Our bodies are not important. It is our energy
that isimportant. You can see usin our body forms
if you wish, but we only use them to communicate
with people like you. You may choose to remain as
you are or accept transformation."
______________________________________

    If you decide to stay in
your body form, turn to page 101.

    If you decide to
be transformed into an energy shape,
turn to page 102.
    """)
    choicex = choice(101, 102)
    if choicex == "101":
        page101()
    if choicex == "102":
        page102()

def page91():
    print("""
    You have had enough adventure for now.
Travel to another planet in a different galaxy
sounds like more risk than you wish to take. Besides,
you can always go later.
    You tell the people that you wish to stay and
work in their society. Perhaps your knowledge of
the sea can help them. They discuss your case very
seriously for several days. When they are through
talking, they offer you a choice of jobs in Atlantis.
You may become a farmer or a musician.
______________________________________

    If you decide to become an
underwater farmer, turn to page 103.

    If you decide to become
a musician, turn to page 104.
    """)
    choicex = choice(103, 104)
    if choicex == "103":
        page103()
    if choicex == "104":
        page104()

def page92():
    print("""
:.-`/-`.s--/.-./o.``-Ny++:`/./:++s/---./.``+y:o-s:````--.hsh:``-::/.``````.-.:`````.````````/o-`.`
.-/o-  .+ -o+-./-  -y./hh+/ydydsoyos`.-. .odyMhh/./.`  :Nhd-  ./.:    .-.: :              /yos.`  
 :-`    :o--`:--/.  -::+/- +m/+-/h`y-.`- `ooso:hN::-/  `.sy-  `:.-  -ss..:`-            `:..o:    
 `--` ` `yo  .-`::      .: :+--/.o+/:.`:  --y`.yNdsoo  .- -.   +`. --.do/`:            .:. ``  `-`
   ..`    :-  .``--      :  ..-:-/o:+ .:  .:o.:`omhoy./-: .`   - -    /d-`.           -:` .   .:. 
`   .-    `:. :hs..`    -.-  /.o::o/so/`- .-/:/-/-+hm/-+- -`   .`-` `-o: :    .-./   -`     `:-   
     ``    `.`s+d/ .    +`:  --o- /``os-: `-:+.  `ssNmys` -    -.+. +./ .`   `//.:  -      -/.    
   `:/-      `/ /y.   `./:o::`:` `-` -.`-  `-+.   /:s/`:       -..   .. -  `/.:-` ..      ::`     
   -oo+          :+`:---/``/+..  ``- `  -   `/    . ///+      ``-    ` .   .-oo+ ..    `.-.       
     ` .          .s-  /-` :.--  ` .    .   `o `  ` oho+      ..`     `.   --:+```  `/.-.         
   ..   .`         s: .:   `--h  `        .  s/`    /.`+ ``.: .`      .    ``-.  ``.+:-`          
./ss/-   .`        -ds+:.`  :-h.         -` `-`     `` - `-.. -      `    .`--``-./.:   -y.       
`:/:``.   ` ``    s+y:o../+/o:-:         `  /-.        `      .      .`   -:/..`-`-    :sh- `     
    -  .`   `/.   +-./:+  `.-/ :              -         ` `   .`  .  ::+. ---` -`   .:y+d/.`   `.`
  `./   `    `/    ` `/s---.`- .`             .        .+`/` ``:  `.``.-` `-/`-- `:++-.`--   ..`.`
.- ./`        :-    :- ```   .```             ` -/     `` o/-.:-.``../.  `-/+---//:.   `` `...:/:.
`--`          .:.:.  :/``     .     `           :o-      `/+o.-+::/-`.`   `-:.-+/`    `  ...--.   
..`..          ` ::-``.++     ` :``-             :o/   .-//```-: `:-  .-:/ooy. `.`      `-/:. `-:.
  ```.`            ````ho.    .:yso-.   ` `-`.    //:   :-.`-:-.-`  .//++ddss/.-/::. `.:/..```..` 
   ``./-`      /.-`   `y+-   -:.../o--`:/yo/+y/`   :-/.`-` -+N/..: ./shhds/--:/-:.``.//:::-```    
  `.-:-`.`     ::ysso`.:-. ./.    `..:.+sso::os:   `/+so/- .oN/ /--.hhs+:`  `:.-..-::/-...`       
   ``     ``  `:///-/o:..-//` . .  `.-/+o-++/ +o-   +::-o/` :hNoo:: -:.     -` .`.-++:`           
``      `..-`  :`    `++::.  ..`:   -:/:/oo/.`.o/`  -.  --   -+ds./.     .-:- ```:/:`-//-.`      .
`--`    sy+/`` -`            :..-`-``.:oooo/+/.--:.`.o-:/-.   `-shsys+-:-.`  `://:`     `.-:-` ./.
`.````  +y+/-             ````--/:.::/:+yoo+:o   `.://:+/:-`..-ohs..s://:-` `.--.   .  ``  `.o/// 
 `..``  oo+.:```       `-`++`.` `````--+o-.:.::````-:-.-.  /::+s`  `--..``````     :::/.  ``..s:+ 
    ``` -o/`o:+/+o-``  ./+`-./.-/o+- .`-+/ ..`o--oo+:`   .oyshy. ``:hs+: `..-/o+``.s://-.`    :`+`
``      `ss:o    -s+:``-.-`:ooydh/`..`  `-    s/:///.  ./y+.     .-:m:`     ``-.`...`/++:``   -:d:
         :o::    `-.s/:::+oyhys:....````  -` `+`.  ``.+o/`   ````../s-`````````.`-````` -//.-/shm:
           `   ``````.:osyho:-.-::```-.``` .--  ` `-:o+. ```````   /+```.        ```....``-:::+ss-
              ./-`.` ./yh:. -.-:::/-` -:``.`     .:/+:```         `o:-/-.`     `       .-` `-+sys`
      .-`..`..-..    ://`  /y/s-` -:/+` -:-..``..`-./:-.          -yyy`  ````        `--`.-`:ohy-`
           `--:./-`  ` `.  +ysy+` -o+o:`:/oy.-.-.   `--//.       `:hhs-/``     ``  .::` ```//d+-` 
`...`      `  `..--`     .   ..-:.``  `/:-..          `::.        .::+//.`-`-:`-.` :+ ``   /hy:.-.
  `.``.``     `-:-` ``    - `/.-:////::+:-`                    `.:++++/-.::-/:--...+ `.    `s/---.
         `.-:/-:.` ``/.    -`-```+-:+/--`.`           :`     ./o+oyo++++//-/o//:-:+. -      +-:-:.
.:-----``  `` `.---``-.     -    :o:-. -`+/.         :+   ./o+o+sohss++/:+sss/+-o:: -      `- `   
 :-..-.-.-.`..``   -/+-      .` -:-.``.+`.-.         s.`:+s++os/smmso++///+++/o/++- :      -`   ` 
  ` `````.```` ` `----+//     /-..`..+/--           .h/+ysssyoo//:d.  `.```        :       : `.```
-+-    `.....-...::.`..+:/`  `+..`.:+-            ./hNy-hdy+:`````-o-.-/-.`.++``.`./       :.::--`
/ds/--/s:::::::::-.-/+:d-`s:`.:.-:/``           -smyNMms+.`.``     `oyydh-`::           ` ----...`
`` `.-+:.      .:/o:-/+:  `:   oo.` `````` --`/shydyy+-.-.        `hdymNm+-`        -ys-/`---.---.
-soss/:/+o-      `os/`.   -       :+--+/-  ./ysddy:`..`/h/.`    `. oydhmo+:`       :dy:--- .:.--/`
/+:-..---`     ``.s.:+.  -        -:-..-d:yoyso+...`  .+so:/:`:: --::  .:+o+--`    +/+y.---.-:-::`
             `::-.s` .s/-             .yNymdo:...    :oshmsyo.     /:   ...:o:s   .sdy/:`.---`-.-`
`...``       .-.` +/. -d.          `/oydMd/-.- ./`  `.-syy/::-    :/----`.  .:s/   :/sdho-.-.-:.  
`.---...`   ````..+-  `:         .:ssoysd--`  .-`:- `..`         `:/y.s..  `.--.:. -+ o+.```.` .-`
./-..    .-/:`  `+:   s.      `/yo++oo--.``::so/:-   ::        `-//.----/    `..`.:/:-s:. ` ``.. .
     .-::..`    y.   :d     :ssydss/.--  .+mmd+:.               -/-:-//::..  `.+oo.:o+-.s- ..`````
`-.```..:```    `  `.-+  .+ymdhyh+.:.    `:os/:.             ....--:yho/so+yo+:::..odh`  /+`  ``` 
        `.--..    `- s./ssmmNdh:`-. `  ``-.:/            `....-/s+/.::+m++mo--. `..-:```  ./.   ``
 `.`.``.`-:`     `.`syymhmNMm+.--``.` ..`` .`     ```---.`-+s++//++ohhoss ./ -`   `::-  ````:-`   
.--.`-::.--.   `.:omMmhhmMmo.-:..:/+oydmmds+....:/:-..:oshddhhhhsoss+:..:s-`-`-`   :/.`   `  -:.  
`---..//-.   `:odNmmy+hdds.`+shdNmNMMMMmmy++yo/:--/+ydNmhyso+o/:---`     `oo/o+.   `-.``   `  `/.`
 .``.-::`  -omMNmhosdmNo:+odMMMMMdyyhNmdddhdhmmddhysoo+/--::.``      `   ``-+hmss-.  -:--.. `   -`
./+oo/:`   yMmddy+hmMhssdNNNmmmysohhdmmdhhyysy++//-`````             `.  ``-.-odso+o-:o/-/:/:/-   
.:-`..     `+yosdNNdy++/....-:+ydho-`..```-`                          .` ` `-.-+:  `-  .- `` ``   
``.--```     .smNmy-. -..`+ooymh/. .     `-                            -.`. `:./+      `. ```     
.+/::---:.  . `os.`-.  `-ssshy/`.--.     :                 .          ` ``/- `:-+.`     ..  `     
`..:--:::+--`    :.. `--:++``` -.-`     -`    `    ``      .      `   `   .`  `/::.`.    ``       
  ``..-::-.`.   .+:` ++.`/+   .`-`      - :`. /`  :`-      ``        `     `   +: -`.`  ``.`      
`````:+.--:-`   :/.. ``  .+  .`.  .    - `+`  o```-.--      .                  o.  - .  ``.-.`    
```.+y-:-.o-` `-./- ``` .-- ``. `.`   `. -.. `+/o: .`-      .                  +-     `` -``--`   
 .o:+:.` -/``.:--oys+::+s-  `.`-:`    - `.-. :-`-` `-:      `        `     `.  -/        `::`-..  
 `.-.-/.`oo.-`+:oshyydds`  ..`-+.    `. . :` -` -``..-                      .   .         ++ `::. 
  +./Ny-yys/` /:+msoyss`  :-./o--   `. ``-/ ...    ```                       `            /s  `.-.
 `o`mMmydy+:  `--ooo:/`  ./.:/::   `.... /- :``                             ` `           `.   `.`
 `sshMNs:/`./+-  `-.   `.`::h/o.  .::.-. . ..                  .            ` `        `          
   /+MNd`   -/o. +h:     .-omh:-osh+/-.    `                   -             ` `  ```  ``         
   :dhs.   `:-//`y/``   ```:+/+hh+/-`                          .             `.``  ..+`.:.        
  .+-`     .:..` `/+.` `  :-``-/.-.                   `         .      .      . .   /o++o+        
`::. `           `sy.`` `:-`   ---`                             .     `+`      . `   ..`.`        
.:```     ``      /o`` `:.`  .-/:.                              `     `:y.-    .```               
````     `` `       ` `:.``.`:/--`                     `        ``     .o.-     - `               
`.    ``.``          .:.. ..:./`.                              . .    `.:+-     `. .              
`    ..`--``` `     .-`.`.`-`:```                              /oo    ``.:       .```             
    .--:h:o+-`     --`.``-..                                   `:y-      -`       - .             
  `:-./-.ss+-     -.`.` .`:            `               `         `.       -       .. `            
`--.             -````  `:             -:`:  ` `            .     `       -`       - ``           
.-`            `:````   :`            .++`-  . `       -    :`     `     `.-        - .     `     
           `` `. ``.   :`           .:``     - .  `    - `. -/`.`-+:      `-  .`    .` .          
``  ``   ``  .. ``.   -.            -  :     - ```/`   - -.  -oNmmdm`     ``. /+.    -```         
  `.`  `:-``     -   .-    ` `      .     `  - /:oh:     ..   .:.-yms      .: .yo-    -``       ` 
 ..   :yoos/    .   `-       `    -`.        - oydy.     :`    -  .s:      .-. `oo-- ::o``      ``
..    :s-      .`  `- `     -.    o/   ` `   - -`        --    `.  :+       `-   +yss-+y:`        
 ```          ``   - .``   `: `    o::`.-.`  . - `       --        :s`      ..    -:-/+o+-        
``           ``   . `. `   :. .   ..  `.-.- .. .`-.      -/`     omdo.      `        /+/          
                    :`.   `+ .`       .`/`-..`  ---      ::`    :+mh/       `         ./o.            
    """)

def page93():
    page92()
    print("""
    You'll try to blast the hatch right off its hinges.
You have the power. Your finger presses the red
button that fires the laser cannon. A blinding flash
erupts immediately. But the hatch remains firm.
You fire again and again and again. Each time the
Seeker is rocked by the force of the laser cannon.
The reflected energy is damaging to your craft.
You continue to fire the cannon, holding your
finger on the button.
    Then there is a blinding flash inside the Seeker
itself. The laser cannon has exploded. You and the
Seeker are destroyed instantly. The hatch remains
closed.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page94():
    print("""
    It is never good to use force unless you are
attacked and must defend yourself. You refuse
even to consider using the laser cannon; it might
kill people and would certainly destroy any chance
for friendship. You decide to wait patiently and
hope that you will be noticed and invited in.
    For six hours you sit quietly and wait for some
sign. A green glow comes from the area ahead of
you. It bathes the Seeker in a gentle light. The
hatch door opens. Three figures emerge and
beckon to you to follow them.
______________________________________

    If you follow, turn to page 105.

    If you refuse to follow them,
turn to page 106
    """)
    choicex = choice(105, 106)
    if choicex == "105":
        page105()
    if choicex == "106":
        page106()

def page95():
    print("""
    This is too much for you. It is like a nightmare
and you decide to turn back. But going back is
much harder than you expected. The electrons
whirl closer and closer to you as though they were
guards keeping you from leaving. It is difficult to
guide the Seeker in this maze of atoms. The instruments
are useless now. The figures of the Atlanteans
disappear. Suddenly, you are caught in
the elastic membrane that almost stopped you
before. It sticks to the Seeker, holding you back.
You want to be free and return to the world you
have known all your life.
    You lose consciousness and wake up several
hours later in your sea suit floating above the hole
in the ocean floor. The Seeker is gone. You're
dazed: did you dream the whole thing? Slowly you
return to the surface, but the Maray has disappeared.
You can't decide how much time has
elapsed. You realize that your crew must think you
are lost forever and you know they are right. The
waves rock your unresisting body back and forth
as you float alone in the vast sea. You feel your
strength slowly draining away.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       

    """)

def page96():
    print("""
    A thought traveler! You realize that people do it
all the time in day dreams. Of course, you want to
be a thought traveler, but how?
    The Atlanteans speak softly and tell you that all
things are the same— past, present, future are all
the same. It simply requires you to concentrate
and put your thoughts where you wish them to be.
    You try, and amazingly you are rapidly rushed
through time to the day you were born, then to the
day you made your first deep-sea dive. Your mind
flies from one time in your life to another. But
when it comesto the future, you meet a blank wall.
You can't seem to travel into the future.
"Why can't I travel ahead in time," you ask the
Atlanteans.
    "Be patient," they reply. "All in good time."
    Suddenly you whirl through time into the outer
reaches of the universe where you can actually feel
the light going through you. You cast no shadow.
A sense of peace fills you.
______________________________________

    If you decide to drop out of
thought travel and return to earth
life, turn to page 110.

    If not, The End.
    """)
    choicex = choiceEnd(110)
    if choicex == "110":
        page110()
    if choicex == "":
        print("""
           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
        """)

def page97():
    print("""
    You have a laser pistol that you carry for
emergencies. You blast a hole in the whirlpool wall
and dive through it. Facing you is a school of fish
who are puzzled by this strange intruder. Behind
them lurks the form of a shark. You swim toward
the surface slowly and the shark vanishes into the
deep.
    The Maray is nowhere in sight. You are wondering
how long you'll be waiting when a loud splashing
sighing sound startles you. A huge whale has
surfaced and lies nearby spouting and sucking in
great noisy draughts of air. It take you a good half
hour to swim to the enormous creature. It pays no
attention to you. You climb onto its tail and crawl
on hands and knees toward the highest point of its
back. It's like creeping up a gigantic grey rock.
    From your vantage point on top, sure enough,
you can see the Moray and the tiny glint of binocular
lenses reflecting in the sun. The Maray crew is
watching the whale. You wave, feeling certain they
have seen you. It won't be long before they come
to collect you.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                        `        `..                                                                
                   `  `          `:.`                                                               
                  `               ``                                                                
               ````       ``                                                                        
               `` `     ``..                                                                        
             ````     .. .:...`` `` ``                                                              
          .`.```    `.::.-:..`    -  .`                                                             
            .`      `.-/oss--`   ``.                                                                
            `.` `    ```://+:.-.` ``.                                                               
            .` `-       .--.  .-`` `-                                                               
               `. `...`  `  `` `   `                                                                
               ...```        `.`.``                                                                 
               /.              ```                                                                  
               s`                                           -/                                      
               s`                                  ``````` `yNo..`                                  
               .                          `   ``..--:oo+/-:somymmh.                                 
   ` `...` .``--``````````````   `````-.....-:++sydmNMMMMNhdossdmd`                                 
``.:+hdmhyhhyo+/+:/:--......--..--:-:++osydmNMMMMMMMMMMMMMMMMMMMmmo`                                
.:hNMMMMMMMMMMMMMMMNNNdmdhddmmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho+::-.`````                     
:NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmdssydy/-..-://:::::----:-::
+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdysoo/::-//oyoooodo
sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhhyyo:---//:+s/
sMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhosmNNNNmdo://-:/:-`` `:-//:
mNNNNNmddhoyysymMMMMMNNmmmNMNNNmmMMMMMMMMMMMMMNmdmNMmNMMMMMMMMNNmhhys+:-..---:..```.-:.-:.::/:----  
.:-::./o/:...``.+yhhdyoo+/:/:.` `shdhmNdyodyhsyoosss/+sosssysss/::-/++////ossyyyy+++++/:.         ``
-.-:/.--..+o+syso/ssooso+:-         ..///:-/-/////syss:o/-/::.  ...`..-:oo:++://:.`          `-.-`.`
++ss//--.    `.```````/::-:::/+/.:/:+- ````..-``` `  ``        `--..-`-..:::+s+o/-.`-+:-....-`.`:```
`..::-.`.`` `-:/:/:-..-.-:-.```.     .-+oosyos+ss+::::::--.`    `..`             `---.-::/.-.-/.-.-.
:::.:.        `.--........`.--..-:-.-::.:o:///+/+/+:-`  ``...--`   `.``````.        `.--:..`..-/:`` 
              `                                                                                         
    """)

def page98():
    print("""
    You faint, and when you come to, you are
floating on the surface of the ocean. There is a
heavy ocean swell and the sun beats down on you.
The whirlpool must have stopped as quickly and
mysteriously as it began. You feel dizzy and
exhausted and you move gently to make sure you
haven't broken any bones. As you move your
head slowly inside your helmet, you feel an intense
pain shooting across your right temple. You have
to lie very still then and gradually your ears pick up
the thrum of the search helicopter. You don't dare
move to look, but as the minutes go by, the thrum
gets louder and slowly disappears. The helicopter
has passed over you. It won't return this way. The
pain in your temple increases. You begin to lose
consciousness.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page99():
    print("""
    The walls of the whirlpool look like solid ridges
sloping upwards to the surface. The water is rushing
so fast that the center looks absolutely calm.
You wonder if perhaps you could swim up through
that calm. It's worth a try, and you set off. Before
you can tell if you're making any progress, the
whirlpool reverses and instead of whirling down, it
whirls up and catapults you out of the ocean and
into the air. You fall back onto the surface of the
ocean close to the Maray. Although you are
stunned by the fall, you quickly gain your senses
and are picked up by the ship. Of course no one
believes your story, but then even you think it is
almost too fantastic to have happened.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page100():
    print("""
    The ocean floor has a small metal hatch on it.
You pull with all your strength but it will not open.
You rest for a moment and look through the wall of
watersurrounding you. Two fish stare back at you!
It's asthough you are in an aquarium for the fish to
look at.
    You don't hear the hatch open. A voice commands
you to enter. With fear and caution you
walk down a corridor that leads to a small room.
Three people meet you.
_____________________________________

    Turn to page 55.
    """)
    page55()

def page101():
    print("""
    You just can't give up your body. It might be all
right for the Atlanteans to move about as pure
energy, but you have not reached a point where
you are willing to risk what you are for what they
are.
    It is strange wandering about with bright glowing
blobs of energy moving with you. They ask you to
give talks about life on earth as you know it, and
you agree. For two years you meet with the Atlanteans
in their energy forms and talk about earth
and how people live and what they do. The Atlanteans
are interested in all aspects of earth life: the
technology, politics, wars, and religion.
    You ask them why, but they never give you a
direct answer. Then one day you look down at
yourself and you only see bright, glowing energy.
With horror you realize you have become one of
them.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page102():
    print("""
                                                                 .ohmMMMNo`                             
                                                        -/osdMMMMMMMNMm.                            
                                              -//-:`  `hMMMMMMMMMMMMMNmd                            
                                           `/oyy/o/-:.-Ns+syhMMMMMMMMMoM/                           
                                     `-//ossoymh-`.+:o`+`  `/sMNMMMMNyyms                           
                                `:/o+s++///+++ys:  s++mNd-.` `-`..:://mMd                           
                            .-::oy+//+oooohsyos// .o/mmNNh`   ``..:++ysNy                           
                           .:-.  ./yhhyso+s+shs+++yymmMNm/` ``:../--`` ``                           
                           ./++:-` -yosymNNNMMMNNNNMNNMMs.  :o-   `                                 
                            `sNddysdds+hMMMMMMMMMMMmNMMM: -ydhs.                                    
                             -odMNmhdmdNNMMMMMMMMMMmmMMMmydms/+s-                                   
                              .:ohNMmddNNNMMMMMMMMMNNNNMssyhds+oss-                                 
                                .:+sdNmyydsdNMMMMMMNmddy` -yshhy+yy+``                              
                                 `--:/mmy/-::ohdmMMNNNd.   .+yosooo/.-/                             
                                   ``-y/+s+`   `+yNMMh`      -ooso.`.+y.`                           
                                      oho:--  `.+oyhM:         osooh/Mdy:                           
                                      :Ndso/---+osooNo-        `/+NMshdss.`                         
                                     -:hMds/+---hohhm++         `.+NMoNmho.                         
                                    ./:+NMmmhyo+hyhsho..        .-:sMmsMhs:-                        
                                    /::oNNmNNMMyoymooo--`       `:-.sMhdms-:`                       
                                   -/.+hMMMMMNmoydh+:+o::`       :/:-hMods:./                       
                                  -/`/sMMMMNMMNyos+s+:ss-:       .s///N+`+s.+                       
                                 `/`:+dMMMMMMMMNNNddyyyy/o.       +/:-yo-oo:+`                      
                                 -:-+odNMMMMMMMMMMMMMNms+/-.`     /.:-.` :+/+`                      
                                 `o-+/soMMMMMMMMMMMMMMmms++://`  :`-/`:o+`.+-:                      
                                  -/./osNMNMMMMMMMMMMMNdhyo+o/o`-`:/+////: ::-:                     
                                   o`/:odMMMMMMMNMMMMMmy+/://+o:+`....++.:/`o::-                    
                                  `/`/:+hMMNMdNhssdMMMNhh+-..:+/-`   -o::/:.y+-`                    
                                   -.`//:mNNmyNhso+omNdddy:` .//:. .  .:/-/+o::                     
                                    - ::+yMNd/dooo://ydmddd/`...-/: - `:----::`                     
                                   `/-./-ohmy:yos:---:+ss+so/-`` :y-.-  .--``                       
                                    :s ::s+.-.+s/::`:.-:/:/:+y-+..h:-/                              
                                    `+`oo+.`.`-+/-:` `::::/--o--``o+`/.                             
                                    -/./o/`  `:o/`:`  `//++-.-. `::/.+.                             
                                   ./`::o: `  /s+.-    .+/+- ` ``:/:`+-                             
                                  .:`--os` `.`so-:     -/:o- ` ``-+:`+                              
                                  /: :-h/  .`/s/-`     /-:o: ` ` -+o`/                              
                                 `/:`:+y.   ./o::      -:+:/.`   -o/`-                              
                                 -+`:/+/   ``s+-:      `o/-/.``  .-:`-                              
                                 .: -++:   `/o/:`       +-:/- `  `-+`:`                             
                                 `+ /+s.   .o/--        /-://`.  `/+ /.                             
                                 .- /os.  `/+:/.        s/:/:-`  .+/.-/```                          
                                `-` .oh`  `s/--.        /-/:/.``` ::/./:.```                        
                              `` /``.ss.  `s+.-`      `-:.:/+`     .---::-....``                    
                            `````/`:/+.`  :s/.-..`.````.-`:y/  `.``  .-:/:-./:.`-.`                 
                            `.```//.s+:`  -+/./+/+/-` `-+.`::``.`.```  ``-: :y/.:.-                 
                          .` `-.-/o.o+``  `o+-`-/:/:`:-o/:--.-:...```..`````:++--.`                 
                      `````..--::+::s-     so:  ///+/+....`` ``` ```::..``` ``                      
                     ` ----/:::.-+/.//```  :s  .://-.`                                              
                        . ````:: .+++:-.-` ``-.``                                                   
                                   `````                                                            
    """)
    print("""
    You are in the Atlantean world; why not become
like an Atlantean? Looking down at your
hands, you see them gradually begin to glow with
a warm, yellow light. Little by little, the glow travels
up your arms and legs until suddenly you have no
body left. You are a glowing energy form. You feel
a sense of freedom and happiness that you have
never known before. You can float, or fly, or zoom
anywhere you want to. No wallsstop you; you just
melt through them. You don't need food or rest.
You can travel through time, and you can travel
instantly back to earth in your energy form.
    You feel that this is the way you want to be.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page103():
    print("""
    Farming under the sea is a job that you enjoy.
Outside Atlantis, there are fields of sea plants that
are worked on just like gardens above the sea.
Atlanteans go out each day and harvest the plants,
take care of the fields, and chase away the fish that
love to nibble on the growing plants. Then there
are fish pens to work on. There you feed and tend
the fish until they are needed for food. Farming
under the sea is beautiful and it is much easier than
you had imagined. Danger lurks, though, in the
form of sting rays, slender sea snakes, and occasional
sharks. You have to be on your guard at all
times.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page104():
    print("""
    A musician in the world of Atlantis. Who would
believe it? You are asked to choose an instrument
to play. You examine water lutes,sea drums,shark
bone flutes, and a wide range of electronic instruments.
You choose one of the electronic instruments,
but it makes no sound at all. You are told
that it plays music that people feel rather than hear.
What a world you're living in! Who would believe
in music that is not heard? Gradually you learn to
feel the different notes with parts of your body:
your thighs, chest, temples, and fingertips. Your
interest in this new way of sensing music grows
with each day. You master this new art form. You
become their greatest musician.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page105():
    print("""
    These people lead you to a control room. There
you meet the commander of an underwater scientific
center that is conducting secret research into
life underneath the sea. They inform you that it
was a good thing that you did not use your laser
cannon, because they have anti-laser devices that
would have blown you and the Seeker to pieces.
    After a pleasant meal and a tour of the deepwater
lab, you are sent back to the Seeker for a
return journey to the surface. You are told never to
return again; if you do, you will be kept a prisoner
for the rest of your life.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                                                           ``                                       
                                                         ....-.                                     
                                                `.-.....:/--.``                                     
                                           `.---...` `-: .:  `.--.-                                 
                                         .``..--:.-/++.  +m`      `..                               
                                       .///oyhy++yo+-  `+oos`       `:`                             
                                     /oosyssooss/.:s+`/y:`-oy/`.    ``/:`                           
                                   /dNmNmmNd++shydmhshs::--:oho+/    ../..                          
                                 .osydNmddmmdmNNmmmMMMdsyhdhyNhddo:`  `:.`:                         
                                :ddhmNmMmoohhymMNmdmmmd+-/mmmyhmNmydy- .+ .:                        
                              `ymNmNMmhhhsh++mMMmdhhdmo` -hhdydNMmydhm+ :` /.                       
                             `shhmmNNh+sydhdNNy/::/oyd+` -hydMMNs+yNMmd  -::+                       
                            -ymddhohs/:hohhmm-     `dy+...smNMy.   -hhy: -/ --                      
                           :mmmNNdhNhsyydmMNmy/:::/yNmmdy.`sdmy-` `:hmdo -+  .-                     
                          .dNddNdhmdmdhshdmmmNMNNNNmddhMMhoo//yNddmhydms `y.` -.                    
                         .smmhNydmmmNNdyddmNNNMMMmNMNdhy+:+hh: /yy/``hNm``+.:  /                    
                        `yhNmNMNNmmNNNddmmdhhhdysso//.``:.` ` ````  omdm:-+ -  `/                   
                        :::dydMNmyshydyoo++::ohyy+ysooo+s++:s+//s/`ohmsoso.`//. /                   
                        ` :Nshmsd+/ydmhNoydoohdhhymNNdd///::s+` `-hNyhdhhm:`/.s :                   
                          :sohdhm++hhy+osysoshhhyy/-+ds//o-``  .+sddhysoyNy/:`o:/                   
                          `oyhNdNdddhyosyydyyssoss+yo-` `  `-/oss+ys+hyoysdms /.+                   
                          :ss+NNmdmmsNmmmddddyhdNMmd:.-y/.:hNmmNhddmhydo/.mNm.+``                   
                         `ys:.hy-hdo/mdNhdmmdmNhmMMMNhyo..mNNhmsdh:Nd.+so yy://`                    
                         -d: .ho mNsshNmydhsdNsomNNMy.   +MNs`/-+/-d: .d+ +y `s`                    
                         `+  `h.`y/+shyddMMNNMhdhddo+.  :mMNs/os `/o`  -+ ::  :                     
                          `   o  /..-:.ydyysyhhd-.o:/+/:sMM+o:-/-- +--` `                           
                                 `   -oshsds-.ss  `/::s+ymh` `oo+: : `-.                            
                                    ./os+ymho`.+/-.`/-//ss. -/: .s+::- .-                           
                                    +s+:+-o+-.`.-:/+--osd.-/+//` ohhy:  :-                          
                                   ++//h/``+``.`.: `-/sy+:--/om+/hmmy.  ::.                         
                                  /s-`oy`` /---+s    +m+-` :.oMMdmhh+`  :`.-                        
                                 .o-.`os/-:++/y:.    :o/+: /yhmmmhdsh+::+` :.                       
                                `y+/:-/oyoyoy+`      `/ .  .h:+hshhhdmdNo.` /                       
                                +/oo/-ooyNdo.`    ..  +./:` o-`:--.+sMMNdo:``-                      
                               `h//o/:::hNs.      .`  y..`        `yNNmds+-  /                      
                               `hdy+oss/oh+/.     `   s`          .mds+-/os+:.                      
                                -s+//::o:`:s+: -:`    +`.-.      .sy+:.``.:/.                       
                                 `///sds:..:+h/+:`    s./-`     `yyo:.`.-:/`                        
                                   ./dhy+oo+/oy++     +        `/NNmhhmy-+`                         
                                    `:hmydsoh//.o   ` +``--    +ysy+-/sNy-                          
                                      `dyo/:``:-/  `+.+````    +o.    -/`                           
                                      `hho-. -:-.   ` o``..    :y.    s-                            
                                      `hys/-`:--.   -`h-:+:     s-   `h:                            
                                       o/o.-.-`:`  :`.m:        ./   +-.                            
                                       +.+o-../` ./.`yy:         -.``: :                            
                                       /+:o/-``::+` :ds+          `/: -.                            
                                       `s/:--`-/-. .dmyo       ``./ys`-`                            
                                        so+ooo:-:/smNmMy/://+o/.....`                               
                                           ``.+yMmhdmNMhssys/:+                                     
                                              -dNNmdhdNh+:` `:`                                     
                                              `s/ydhs++mo./yNm-                                     
                                              -hsyyy- ss+ohshh.                                     
                                             ``hNdNNsssohymooss:.`                                  
                                        `.--odhNMMMmym:yNNNNNNMNms`                                 
                                  ``:+shNNNmmNNMNsyshMhhMMmMMyMh/-.-..                              
                               `+hmNMNmdys/--NhddMNmmmNNNMMMNmMdsy/-:-o+.                           
                           `-+yhmdMNo+--:sy+om/.:+//. `.::oshhhNNdh+/smd-:`                         
                          `+oooooosshdh//-`                  .--/+syhmdys:/y:                       
                                                                     `.-:/-`                        
    """)

def page106():
    print("""
    When you refuse to follow them, they take out
small hand-held hypnotizers that put you into a
deep trance. You are led through a long tunnel
into a large underwater lab. Three military technicians
come up to you and break the trance.
    "You have stumbled into a secret military base.
We're developing too many secret plans to risk
being discovered. You will remain our prisoner."
    There is no escape.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                       .-.-`.-...                                                                       
                .omN/ /` + /`..`                                                                    
              `/Nmm/o+::-:+o.:---                                                                   
             :odhdhsss+--/s//:/`/o                                                                  
             `ommmds/:o+oo:/++:---                                                                  
              `sMMMNhhyo++ooooooo                                                                   
              `sdmNMMNdomNooo+o/+                                                                   
            -+oy+--ymddsddmh-`  /+-`                                                                
           `hNh/`   `y: `..`    `h+-                                    -:.---...``                 
            .-y`    :d` `.       /`            ```.````               -ymy`./.:`:`.-                
             `y`    hNs/+o:      :          `/y+--:`/`.:.`          .ohdmoo+-.-s+./`--`             
             `y-    .:ss+.`     .-        `-ymmdo-:.:o+:/--.       `+dhNNoo+++/o++/..o`             
              dds-`  -/:/`    ``++        :yyddd++/+:o+//`//        .ymNdo+hysy++/+++.              
             `dmNy+/:/--`.`..-.+.+         sNmNMys++s//-:/+`         .NMMMMNmho/:/+++`              
          ..+odyyo+:--+yo.....-:.ho:-``    `NMmNNdsysooosy/         -yhNMMmNdmysss+://`             
       ./:y/+:+syy+:-/`y--:....:sdNo::+-` .-dMNMMNdmo+oo++/-`      -mNddm+.+h+//-.  .h:             
     `++/-` ````--:/:::+-:.--.:+hd-   `++`mNdMddyhhmhyyo+:o//      .hNshh- +dys.    -+.             
     /s. s`                  -./y.     `//hdNms-:sd:o/+/-/ds.       `:ym/`:.syo``.  -`              
    :+.//s    :::::-.--.:::::``+-   ``-:../dNh.`.hy /```.+m/          .yh/:.::``.:-/`               
   /s`-`/-    s++/-.:+/`-+:/`-+:o.  :::   ./dm-ohhh./.:-`oy-           /MMyyd/`-.sys                
  .y+/`:/.    o//.  -:. :o:`-y:-o:  o//    -yN:ssdy::..:/o:           `NNmhsod+-///o                
  s/++:.//   .s`.`      /o--.`..y:  :o`    `yd:ohNo-o+:/so.        `/:ommdy+/--/--:o+-:``           
 -Mysssyoh`  :/o/:    `oh/-` o+:o.   :.    `+:+o/sy:`+/oh`      `-++//::--------.`:sh+/o+-`         
 sMmo++soo   ++ `    /+ys/   `` +.   `/    :y:d+y..` /-sd:      /s`   `........-.::oo`  .+:         
 hNNhoosh:   +os:-  -mNd/.   -::+-    +    -oyMhmo:-.s++s/     ++//.  +++o--/+:ys::os+   -o:        
.hhdy+o+d:   o:--  -:yd/     :/.o:    o  -/ohNMNh+:o:/://shoo++dh:.o: ::o:`:o--s/:+-o:   s`./       
`hoo+oyoho   +-`` -- .-         -:    +sh+//:-//-:.:...`-md+`:shhys:o -//:-  `-`-`--y:   /` -:      
`dy+yhNNm:` `++o:/..:.       +:-.:   -yNy  :+/:////::/:/hoyoyy+/dyyo+ -o::  /+--  o/+/   `/  +`     
 yddhNMdy:. :: .:/::`        ./. -  /yddo  -++/`:-:`o+.+o:+y:m:`/mhhh :/o/`:hd+.  ::y:    /  -/     
 /mhmdsyh:` :+ -:-:`            .:  .y+:o/ -so- -/  /:/:+o/d-+o- ymdd +//:/hs.    /+/:    :..:/     
 `mmdsydo-  //:so+`           .`-+  sso.`y./os:     `:`+/-:/ +/  .mmm+y-s/./`     o/+/    /:s::     
  /hhyoh/:. +ohm:/           o:+-o :hs+-`/++/..    :+./.s-/o-d`   dmh:h:`.-         ::    hNo+s     
   `/ydd:/-`sdym:`           :- .h dms` -:y+ys/`  /so:- /:ho+s    mNmhy.::.       -.::   -mms.+`    
      `h+/+sy+s:`             `.-s.Nh`   :s//-`  :dNo.  ://ss+`   sNmhh+so- `.-.` +:/o-`/mNMm-o.    
       sssdmssh-:            /+/:+-Mm-    :os+: +o/+   `/:+NMs:` --ho````+-.` -hdsysyNyhNmNMm/s     
       /NmNMMhyo:------.-----:o/+osmNy+`   /+/:sNy: `..-ss/hNso::./Ny+o+--     `:yNNmmddmNmdho`     
       sNMmNNMmdNNmdo/--/+oddhhds:ymmNdo````h+//o+-+:-o+hs/mdyo/-`+MNmddNs.`   ./syhhs+/sNy-`       
       mMMMMNNNNNMNo:.o/y/:hhmNNNdNmNMNh--++shsh++/::-+/:-/hmM+` //dMMMhhdsyooh:.```-.--./:         
      `ddmdo/+sooyNs+:-.-+sshyhso:dmNNNd/``:+ddhhyoyoohh/-` `/d.-/`+hyy/.````-N`    o````.::        
      ss+os/:.--.:-/oosys+:.````..yNMNNMmy-y+ohdmmNNNdNNy/+- -ss+..hhys+     -N`    +-.-.ysy        
     :ysoyo/-   .:   `+ms     .-.`.dNMMMMMmh+/yNNmddmNMMNdhy+/+o+/dyy+o.     :d`    /.  `::/.       
     smdy+s+.```+`   `+Mh     ..   dMNNMMMMNNMMmh/+/yyNMMmmNmhyyyhd/+::      +m/    :.     `:       
     +mddys/```+.    -dMm`    -:.`.dMmmNhhdNNNMd++/oyodNddhyss++//ho++:    `+dMd:   `/     `:       
     s+//-.`   +     +dMm/    `+``/mmdhy+-..--/hs+++:-::--....`.`.:dsh/..-:/+oNdds:.`.-...`/.       
    `y///.`   `:    .ydNdh`    +  ohyso.--     `-+d+        +:--..-NNmdooo-  -dyyyysoooossys`       
     hss/-`  `/`    +++msdo    / -myyho`-:        d:        /      dd-.      :h+oo+-``-...s         
     mdh++..--`  `./+` mhyd+.` .:.smhdhos-        h+        +`````.y- ` ``   +sos+.   ``. :         
     hyysssoo////oo.   dyoooyy+::::y+/+oy`       .d+        +:....+h.```.:   os/.   ``..`.-         
     --:yyoooo+-`     `Nhyyosoooo+ohossos.       /ho.        +    /:os/-.`   o/:    ```.-.          
        yo.+s+o.      -moooo:`  ``-y++/os`      .hNms`       /    +  `.+do/+`+s+.:-o+.``            
        -y/-----`     -myss:  `.::-o+osh+`    .++/ddds-      :.   +    /dyoo/+dyshhd.               
         .++/-:oss/.` -Nys:```````-shdhy+.`./o/.  +yshho:``   -..-o    ommmdsshds::y-               
              `odyyhs--dy/:/++/--. `yysddyy/:.    +ysyyyydys+++++s:    yMMNyodMMdy:/.               
               -dmdd/y:Ndy-`:y.        y+````.`   +yoo+:..--/+/y.      dMMdo:oMMs///.               
               .mhmMd:-MNms::o`        y+--:.-..  -yso`   ``.` +       hMMho/+MNo/`+                
               oMMMMN/+MNmhy+y`        :h/..``..` :dy/``.-:--`:-       sMMs+.sMm/. +                
               hMMNdd.sMMNss.o          -:::dyyo:-+mh/.:o/.--.`        hMNyy.hMdh+--                
               hMMmys`hMMmyo`s              s///+-sh.-//+.             sMMhs.mMho++`                
               sMMMmh.hMMMMh`o              hhhs`-oms//.o              .MMhs/NMdo:+                 
    """)

def page107():
    print("""
    You argue with yourself for weeks. Then you
decide to go back to Atlantis. You are in such a
hurry to return that you hire a small, fast hydrofoil
craft to take you to the spot in the ocean where
Atlantis is. Once reaching the spot, you intend to
make a dive with just scuba gear! You know a
2000 foot dive is impossible. But you don't care;
you feel you must make the attempt.
    A storm rips the sea for six days and when it
clears you prepare to dive. Just as you slip into the
water, you look up into the sky and high above the
clouds you see the sparkling city of Atlantis. No
dive is necessary.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page108():
    print("""
    During the night, you are awakened by the
sound of voices talking quietly. Listening, you
realize that a group of Nodoors is planning an
escape. They want to join the Atlanteans. They
believe that life in Atlantis can be better for them.
You join them and listen to the stories of fear and
darkness. They seek light and friendship. It sounds
simple, but nothing is easy.
    """)
    print("""
                                                                              ```                   
                          `...                                        `    .``  ..                  
                         `.  ..`                                -`.:.`.. ``.`   -.-                 
                         `:    -    ` .`                     ``.-` --. `-o+-   .``-                 
                        `.-    :` ``- .:.`                   :`..  ./``.-:/.   .+`..````            
                  `` `  ...    `- :  `+``-                   -`    :``. ``     .. `    :            
                 .````.`...`   `: ..  ``:-`     ``            .:`  .```           `. `..            
            `-..`/-    ``  ```.`.::`   .+` . `.   .          -`       `         . ` .-`             
           -`-`  `        .```....` ``....``...` `.`         ..` . ``.-`       ..-.`-               
           -.      `.`--../    `.-``.  -`.o-``./`  ``  -:` ..``.  `-..-    ` ..:-.``-               
           `-      -`    .:   ..-.``:-.-.`.-``..-``````/: `-.-. `++-` ..  .///``/--`                
           -.`     .-.-.    -ss//``  ..`- `.`...:..`       ````  ---`.`.`.--.-. ``..``              
           ``...-````:`     `-`:s:+`  -:.``.:-/...-              `-`  ```..`....````-.:.            
              ```.-`.:`` `--.` /-`:.  `.-:  -.`-.`: `` `.`.     `-    -....-.``.::/-.```            
             `.`-::..-`.-:/./.   ``.    -/`  .-`.`.````..-.  ..::    `-....`-```.``.-.-..` .`       
              `````.---`-.``.....`   ``.`-   :`````````` .`- .`+:    `` -.`:-:..-`...-/:-.` -       
          .--..`` ..`.-..``````````----:--```::::-::/+:::-+:--+s..`` `. `    - .` .--:--.```        
         `----://+/:+::/:/:::://///o/::::/:://:/+::::o:--:::-/+///+/++:-..-://:/:/+//o/ooo///::::-..
          ```.`  `.-:    .`  ``          -``-:`  `` ``- .-:..+/o-`   :-----/.-:-....-.-/--`-/--.---.
      `.-```  ....-`.    .`   .` `` `.`.-.`.:---.-.` .   `  -:-+:..      .-:.-`  `..`.`-```-`       
     -. -     .`-  `    `/`   -`.`.-.   `.--.` ` ``:.-.-.-``.  :`-.-   ``/o--/      `-..`..-        
    `:    `. ` .-      .:-` ..```..``.`-.``..`.    .`-...    `..:`-` ``...:```..`  `.-.` --. ` ./   
  ..`   .```/. `/```.-/o+o/++//+//++++o+/:///::-.-:/s:../...::-/::/-.`````:.----/-.-/-...-`    :--  
  /.-:`.:   ` `//o:::y+.``  `.--  ``   `````-:.````.-:--/::/:::-.-.::::///:+..-/++o++/ooos://o+ooo+:
  .::` :......` ..` .+/:....`  .:-` ..        .:.`    .  ..---  ``        `.  -`...::....- `:/...`  
 --    -+:--. :/-  `./:``  `..   `-  -      .-  .:--:```---...----....``-.:`-`.   ``    ` ``..      
.+:://:yyyo//:--.````-::/:.---.   -`-./-:.-  `.o--..:..-.:.`` ``  .`.`  .......  `.`/.    `-.       
-/+-.-+soos/:::://///:--/::/ohs+/://:++ssso+.  ````-::.:/--//s/://++//++:-:++++++//++++//++o++/::..`
   ..```:/h/             .`  ``.` `````````.o+++o+++///::---/sso/://::+--.``.:.---```.-::-`.```-:::.
  ``.:/` .:```:           ..`.-   `-`    :   .`.     `. ` -./-:::-.-/:.`-.:..-./+:--``  .`-.`  ``   
 `-   - ..   /`....``` ``.....---  .`  -.`:```   .--//.    `:.        .``     `/o:.    `-``-.`.`` ` 
  /-`  ``   ...` .:/-.-:.       .. `.--.. .   `...``-...` ...` .`.--...`.  `  -.`  ``:-`.-       `- 
-.:/ `.`  `.` `:`..  `+:`     .  :---    `:..``.``` --`-``.  `...:/::::`.:/--..-``.`.`..`.`   .`  : 
:  `.`  ./...:o:::..`.:-`     .  .-   ``..:..` ``.. `..-:.:: ```.--:::+:-...-/::::`-..````.`./+-:.` 
-.:/.`   ` --.`  :``.`       `.  --:.``  ..``    `::.``.`` `````  `-++.`     ```  ````..``..`..``-` 
 .-``:..`  ...  `/..      ``.` `..:+/-` -.``````:` `-/++:`/:. .     ::/        -`.-``...`  `     `  
..`.  .` .`-`:.`/:` ``--.:.`..`+````:``.:` ..`.--``..  `.:/+:.-.    -./:      `.  -. `.-:-`:`.-.````
///    `....``-:.`` ``.:::`-..-/:--..```   -`  `.`    `.-..-.``-    - -.`.`   .`-::---+//-```-` ` `.
+-/ `.....`    `-:``-..``:`.` -/``..`   ``.//`.`    ``-:-`  `.:`  `::::- `     `:o+:/.:.`..:...-.`..
` `----::-. -/:`   ` `--.:-`.-:`.-...`..///::.    `.-``````-`..   .+  `   `````..`:-` :...```:--:`` 
 --.`     ```:.`     `    `..://-` ` ` ..````  ````     `..:`:    `..-` `-``-` -  `` `. `      ``   
      `.. .`:-...`-.```       ``.``..`.`  `.:``` `        ```-    .    ```  `--. `...               
      /     `.`   :.``-...`    `  ``.:` `-. -`   `-    ` .  .:   . `.`    .`.-:::-....--`` ` `.``-  
      :-   `.:-`.`:/   .  ``.....-`--` -.--      `.-.`.o+::``:   -  `.``. `.-.++:+-::-/+:-`.``  `-.`
     -..`.``` `   `:.  -     ```--.o://` ....`..````--s///o.`    ` `  `-.-.-` ``....---:.-...` `.`  
     -.` .`.`  ../.::   -  ` `:.--`.`-:.-.  -/`    `.`-o+:.-`    ` `.`..` `.                  `     
       ..`:/-`` .:-..    -..``-.`.    `   ..:o:::--`````--./`.   .                                  
           ```:.` ``` ``-/.--...::-.   ```  -/:-``..-..``` ` .    `                                 
                ``  .-:::...:---:-:-.```-::-.`.`            ..-......- .:-                          
                     ``        .`  .```    `                          `./-..                        
    """)
    page109()

def page109():
    print("""
    Suddenly the door bursts open. Three guards
armed with special weapons rush in. They fire the
weapons and in a flash of brilliant light you and
your companions are vaporized.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                          -                                                                         
                          o                                                                         
                          o-                                                                        
                         -`+                                                                        
                         /.o`                                                                       
                        .-//--`                                               .`                    
                     `+dNsoosdNh-                                             /.                    
                   .:ohddhhNNNNmd.                                            :-                    
                :///s+oo+/:::///+/                                            ::                    
                ``./hooydhhdhyymm-                     `                      :/                    
                  --/o+/o+ooh+sNd-.`                   /                     .os...                 
                   ` -/:++++s+osmmhs+:/-.              o`                `/sdsooohNh:               
                      `/:+:--..-odMMNNNh+/.            +-              .omMMNNNMMMMMN/              
                         +`    ``-NMNyymMh--          -.+         `.--::/+osoyooo+:--/              
                  `      /+.o:-+:oMMmssNMM--.         +/o.        `-::+yo+yyhhhhydhhh`              
            .     o:     `yoy:.o/oMMMMMMMh/./-      -o/::/o+-       `-/ho/+/moyd+yhN-               
   `.-y-`..:s/y/+/s+::-   /y+://oyMMMMMMh:```/.   -yNMNNmNMMNy`     .:/s.`//MohoohNM:               
/+++/dNossymdhNyhsoosoo   `hdsmhy:.----y.     /..:ohhdmdddhhs+/        `-/-:d+o/+shy+               
   ``-+````.s+sh/.:-+o+.---+s:hho    .s-    -:/+---oo+oyysssoyh          `/-/--.oNNss-              
             ``.oymdyys/```.o-ohm+.-/dd+    `--so+/o+mhshhsshmh           ``s//yNNdmNNo`            
                `+smmyo+/+soyhhmdhoymddd-   +ssoo/.+`hoomoo/od-            ///mMM+:/yMMs.           
                  `om/   `-:+ddmhhyhysosy`  ....o/`+ ssodyshd-            -//dMMMdysmMN:-.          
:////+////:/::-:---:/:-..----yhhsoooo+ysm+```..:/+ss./oo+/++o             s+yNMMMMMMMMo  -:         
..``````.......-------.-:---.+dmhdmNNhshmhsssshddhsyssys+s:yo.` ``.-```.://. .omMMMNmy:---:-        
                     /        hds:hy+.`:y/-.--:oso+sss.`-::sh//-./.o+.`.sy...../dNh+`      /        
       -- ` ``/.:-/.-y---.``.-hhs/hy-.`-.-+-:/.-.-`.:/:.odhmh-`  //oo   /h.-oshdo++o       -:       
://-/o/sh+ssy+ysy/shhhssy:.` .y+``..````:/os:+:` :-   .sdNNdMNdo::hdh--.:./ohdhs:/:/.      ./       
``...::hs:/::+dhh+ymh/y../:---/o:.//:--.--:/-:`   +  :-osmNhNMh:sdMNo-....+sys/://:+o.     -/       
       .`     `/o++yhoho./o..``./.+s.::``/s:``.--./ -++/`/y+oNMmhdNms     `ys++//::-.+- `---.-      
                `hyhy+/ysyhsyohyhsyy.///`:+/-::osos::/://:///sdNdo-./-     ss----:-:-+s/o+:+-::     
                 ymhs:+os``.-:+ysyoy+ss++/+/:---.-/hssydhoso++o/:-.:`.-.   .s+-:////hddhsss:.`./    
                 sy-o::os  .:.` `..-...-://://:-` `syhmdhyo/+/s:.y/o..-::   .yoshmNMNmdy:./    -/   
                 +s:sms/o  mmo./://+o+o/::.`       `yhmNyso+o+h+-oodhhh++   `hNyNNmhyso./`-+-:-`o   
                 -yshmmoo  hhh+yys:::.              `hddhhdNNddoy`+:/+/:-    -oys/-:/osoyhhsy+:`+   
                  yyyhhy+  yhy/.//`                  /hhdyyysoyo+os/osh/       /o-:/smhhhddoy` `/   
                  syNNmN+  /hy:-.-/-soo``.........```:``-.    +:oysshys`       `//shhsssoo-:/`.+`   
                  /yNNMN+  .yso/`//-mdd-.`.``````..-/o:..   ``o-h/.hddd/        .smd+/+o/``//+-     
                  +mMNNdo   hmdsys/:+oy+..:+oo/-:-.:/o+:`  .::++:.-dNmo        :+shs-oos`./:s.      
                  /NNMMNy   +dhdddy:`hmh:/oydNMmmddddmso  --/yhd.:syy:        /y+sh++oo..shh/       
                `-smmNNNd.  `dhdmNd+`:dmy/++y+yhmmmNMMNd.:-.hmyoydmdosooss/``+/++s:/oy.`hsyo        
         `-:///oymNMNMNMMs```sddmMmd..hNNdhhhsosyyhhdmNNys`+d///hhNMNNmmmmdysyoysh-sh/ ohhy-///+//-.
         :dhyso+syoo+sooo/-::/mhMMNy/+/hsohyhd..........//:sdo/+smMMMMMMMNdydyshsosdo ohmNNNMMNNNMNy
                              NMMMMy   +dyddds-         /`/odhddNMNdmmhsssydddhddhMN`.mmmMNNNNmsss+.
                             `mMMMms`  -mhddhso       .s+ /sy-shMMNNNmdo/`-MMNhmmmmM:oN/::/:::-`    
                          ``:omMdmmds/  +mNNMNh```.-shNM-`-+o`hmNNmhydy++:/dMNmNmdhNdym:            
                     `/ss+/sdddMNMMmy:://NNMMMdoossyyhyh/:/o.+sosho-ymNdNNNNNMNNmNhNy.mh            
                     `+oo/+++/:/:::---` `yMMMMy        :+/y+hds+oo+`sMNNNNmhhNMNMdhNh.hm/           
                                      `.smMMMMd-`      -yhNddhoydhhymhy/:.  /mhhyyNNdNMdd`    ````  
                                 `..-+omMNNMMMMy.`   ..:dNNddmhyo+:-``````+yNmhyymMhmhdNNo++sshhhhh+
                               `ymNdhssssosssoo/-::--/soooo+/::::::::::/:/yddNhNNMmsshhhmNmdhdmmmNds
                                ````                                         oMMMMNydNNmm.`     ````
                                                                             :NMMMNNNmmmy`          
                                                                             .MMNMmhNMNdh`          
                                                                            `+MMMMNsmNNMh`          
                                                                         `:yNMMMMNhhNNMNN-          
                                                                     +yhmNMMMNdmNNdmmNMNNhhyyyhhdhds
                                                                     ``.....`` .+dNNmmmmmd+-...`````
                                                                          `+ssdmNmNNNhMNdmdddhyyhhy+
                                                                           .:-::-..```              
    """)

def page110():
    print("""
    Over 1000 years of thought travel later, you are
called into the main thinking room. You are told
that you may now return to earth life. You have
doubts about going back, but you are curious to
see what changes have occurred while you were
living in Atlantis.
    What a sight greets you as you circle earth at an
altitude of 1000 feet! The great cities of the world,
New York, London, Paris, and Hong Kong are
overgrown with vegetation. The roadsleading into
the cities are barely visible. But you see signs of
new settlements. There are clusters of buildings
spread out in the countryside. You don't see any
smokestacks. There are few roads and no cars.
The people live a simple life providing themselves
with food, shelter, and clothing. You wish to join
them.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
                              `....`                                                                
                            -dNMMMMMNdso:`                                                          
                           +NMMMMMMMy.:+shy/                                                        
                          -MMMMMMMMMM- `-..                                                         
                          +MMMMMMMMMM/ +s.o                        `` ` .-..                        
                          oMMMMMMMMMM.  :-`/                     .-:/://+:o:-/..                    
                          -MMMMMMyso.  `-/                      .-+hhm/ +oyNd+:-:                   
                           +MMMMo./-   -`:`                  ``` .yhss./..-/+/-/o`                  
                            yMMm:-/o     :.                   :.`-   -/--``/ ` :+:                  
                            `sNmo:-so`    :                  .:..o  /:y++:+. . /`:                  
                               -- .:sy+`  /`                 -` `` `yo+o:/-./:-o.:                  
                               /ss++/:s.-..                `.-o`y/-.+.y/+-.++`+-+.                  
                            `./o/`` `-o-                  `.`/..:/-.-o.:..+s..o:/                   
                           .:..` :-    ..-                .. `  /.o-:dms:/+o`-`:+`                  
                          :.    `.```..:ss++--`           o-  .--/s/sNN+/:d:  .o//`                 
                         :.      ``  `sso+ssoos:...`      -+.+-syo+y+ssos+oh.  :/-+`                
                        `+        `.` `:oysysyh+   `--:+.`.--::-.`     .`:: ..``./++                
                        `/       :-:     `:y+s. `      `.-.  ````---..`.-.--/. `--++                
                         o      -s-        :-.`./--     `` //+/ys/:..`:../o+:-  .ss-                
                         s-     //-         /   `/+/:``   `:y-+so+://+.:/`+:     /h`                
                         +  `   s:          +      :oo/:/` `/s+/./oyso:-::-   .+o:/`                
                         o   .::d:-.        +   ``.:--:NNNhho//:.`.o+:-:---:--/o:.                  
                         y`/o/:.-//::---/+//so..:--//+-yhyshdddysy+/+osoyo:-.` /                    
                        `hy+--``   `-.- +-.-.s---``   `s+ss+:+`        .--.   /                     
                         s/+o/+++osy+o/ooo::-so:/:+/+:/hso+.-`               -.                     
                         `//shdmhhmyoyyoo+:/s` --.+/o/`/-              :.--:+`                      
                            -dhhhdhh+o+/.   +          .-              +   `-                       
                            yoyhyyso+o+.   --           o`             -...:/`                      
                           -o++ooyys+-::--.o            s:::`                -`                     
                           o/:-:.-://+ss``.o            s+--```..` `` `.  ```.-.                    
                           /yoyoooo++://`-+.           :y::-`  /:-````+/-.`./.-/`                   
                           +.    `+`::.--oo           `ss+o``....-.``.......::--+                   
                           :o`    / ::   /:           :oh/.--`/:-`/:-+:-::-::..+s                   
                           `y.  `.: -:   /.           /y++os-.--::::/::/:.-.`.-.o                   
                            `ys+-.. /.   -.           :-:mmNyoshhhhhsho+//ooy-.`                    
                             /Nhs:  +`   /`             ommm+/+/-.+-./    --                        
                             .N+-:`-s`   /`            -mdhyo/-`  /-./`  +-                         
                             `do    o`   /             hNNmhs::  `/:-/.  o                          
                             :mo``  +.   o            /mNmdyd+/.  /:.:.  o                              
    """)

def page111():
    print("""
    One day your friendstell you that you can return
to earth if you wish. You consider it carefully and
decide that because of your thought traveling ability,
the life you now lead is what you want. You
decide to stay where you are forever.



           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page112():
    print("""
    Years ago the Atlanteans had worked out
emergency procedures, but most people had forgotten
them. One old person remembers where
the emergency instructions and equipment were
kept.
    You and the Atlanteans work without stop for
72 hours pumping out the flooding waters and
building a special retaining wall around the volcanic
crack. Finally the last pump is shut off. You
are all exhausted, but you've won in your battle
against the sea.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       

    """)
    print("""
                                                                                             ```:   
                                                                                            .::-+   
                                                                                           -//.:-   
                                                                                          `.:- :-.  
                                                                                          ..: `+-   
                                                                                          `./ :-`   
                                                                                       `.-`//.+     
                                                                                      :o+-/h++:.-   
                                                 `.`-.:-                             -dmd++ho+-./.` 
                                                .s``  /h-                           `+oshNmmNyo-.-/`
                                                `/-` `::.                           .+``.sMNmy+o/`/-
                                                 `.:/+:-``                           /   -MNhs-.`-. 
                                              ..-/:----.-/--.`                       : . .Ny.`.:`   
                                           `---:.` .-:+--`` `.-                      ..o :h-```     
                                          -:-..-  `:``--+...-.-.:``         ``        ./ .```.      
                                        `:-:--:-`/o:..++-...o:+o///.`     .`.`.`    `././: .:`      
                                        /+:/+/:--shhyso/` `:`.:`:s-.--`    `-::-.   `-s y` -/       
                                      ./o+:-:o/-sdhy:..-/-`--ho//y:.:..`   :  -o/  `-hMsd:-+y/      
                                    .-+s+`/yy/:o+/y--o.:oNh/-::/o+yms:-..  --` :/``/`hMNdds/--      
                                   :/sso+.++d+/dyoy::h-/smmyo/. .odo+++/--`   `-- `+ yMmd+:--:      
                                 .oyh+oo.::s/s-sssh::++/+:/shds: -do+::`.:o+:-:.  .:`mMyy.-h./.     
                          `    `/dsooo/o-:+dh//soohs.:-:  :s-/yy+./so/s.        .---:MN/.-y/-:`     
                      `-```  `:+os-/++:oy//ydy.+o+ys-`   `.s.`-+oy-`o:--..     `-..`dMd::::`--      
                     -os   .:/-.o. oo+.`/oh+-/-:oyyhdh+o-..o/+oosh: -`://-/.   `..:dMNd- `: --      
                     +++/oo+///hs/+yo/::--`+``+/dhsy/soNNdys+o/:-s/.-- :+: o-   ..ymmhs:  o`-/      
               `...` `.`../:/so-..`  -.    .s-//hh/o/+-MMmyMd- :mo.  o .:o :yosohhydm+-:  h-..      
            `/:/://+////+yoys/`             ./o/:/+oy-`s/y/+s  os/` `o/o-/ /:doy/mhmy` :  hy/-      
           /-`    .`.:++o+-.:++..   .:  `/-   /::  +y/ .-`: +` :    .///--`+ ohh-y+Ns  .` dM/       
          .+/      `++.`      so/`  +:  .y:.--:-.   sd.  `-:+ ./    y-s/- s--yhmyy+ms. ` .NMd--     
                  .ys/.       `.y.  o.`  ```    s   `do    .` `:    y:d``oo+mydhmy/od/   +hymo.`    
                 .y+o/`         +/ /y`y     `. `o    `s`   .   :  `-sm::++/dMNMMho::+/` :Nmyhm-.`   
                 o/oh:          :ssd-/o     `: `s.    `/-` -`` :  :hd++soymMMMMMoh// .+/:.--+yh `   
                ///od-          ohNy.y//    -/ `os`     `-:y` -``:shyydmNmNNNmodhy+:- `/:   ``o.    
                o+/sso         `mmdddo//.   s.  `y/       `-..`--omNmNNmNNNdh/:oN/-/-`  y-    .s    
               -hh++::-`       oMNMNooos`   o/   `s/+:`..:.  .//yhNddyooooyddsoym:-:-.  h/    `y    
              `odso+o/.`....``/dMMMNs/ho    /s.   `-ohso:` `+o-sys:.`      .-oddNs-:/-` h:    +:    
            `:sysho:o/:--.-//osdmmNy+oy:     ++.     `   `:s-`om/             --:++oo+- :s:.-::     
           `.hhdo+s+y:--:+o+--:dhmmNhoy:``` `.-+/-`   `-:/.` :+/                   ``-:--/:-`       
          -.dys+ohhhshdmh+. ` ...++sdhhs+.://.:-+oyys:/-`   :/.                                     
         `-/m++hNmoymNdo. ./-    :o-///o+`s/h+o-: `..``.` `:/`                                      
      ` `-`+dsdNNydmd+:/+/-`   .+my+o+sdm/-o:/s/+`   -+``.-/`                                       
     .`. : :d:ymMhsohs/:-``.`-y:mmNMMMmNNdomysdmms:://`.::-                                         
     : +`:-hNohNh:ods/`/-`-:/d+oMMMMMMNM+oNMMMo:oyys-`--:.                                          
     -.--:dNmNNmy..ymo.---/hmo-hMMMMMMMM:`NMMNhsso:-.-:-                                            
     -.`:dyyNmNmmh-shyoyydNmy++dMMMMMMMM+:NMMhy:-:+--so                                             
    ....+myyyhdyhNhs-Mhmdmmys+sNhdmNMMMNdmMMmhoooy/yoho                                             
    :`--dsyhhooooohdshyhyo+os+omhhhddMd-::dMhmy++o+/y-y                                             
    /`./dyyhdoso++ohdyhy:s+++/-shyydNMo   oMss-    `+ /-                                            
    ...:dyoodo/+//+o+odd+::---./hddNNM:   dM+//`  .s. `o`                                           
    ..-:dyyyddso+/ooooo+hhs-:..-mhymNm`   dN/oo``/y.   .o                                           
    `.::yhsyhhyoososso//sosy/:.:mo+syh``.+NMhh-/ys. `:  -/                                          
     ---ohs+ohs+/+o+/ysoo::/syo+so+ddooo+sMMhdhs.   o.   /:                                         
     ...+hoosyhhhsso+++syysosys+oyyo////+oNmmNh`   /o  :  /:                                        
      .--:hoyyhssoo::////+syshsoyyyhhydmdddNMM-  `os` --   -+`                                      
        -:/yhssmdysosssyo+ss++shmmdmh+o+..-MNN-`+hy` .s`    -s`                                     
        -..-hNhhddddyh+osoo+++ys+:.+`     +Ms/syy-` -h-      `+:                                    
         `.``smo/sshso+++-:--.:--..-     `hm/+s:`  +mo         +s`                                  
           -  +o:::+oys/://oo//-//--..::ohNN:+`  -ymh`          .y-                                     
    """)

def page113():
    print("""
`/.:+--o+`:-.s./:  /`  .`::. .+:`o+-. -`/o+:.+    `:-..``.`   .-: /+o-.`/ ..+/--../`   ../`:``-`.`-.
 ```  :` :.-  .-   o.:::/+hh/ :hyydy `--:- `.--```-```.::+-.   -:///`:. .`//-`    `-```:`-.-``:/.---
 -:+/++o/+++  /+yshdddhohoddy/+hyy/.: `/+:s/:.  `/`+-- `...     `./:---..::.`--`:/+soodhhy+ -:-:  : 
 /odhssdhsys  .dhhdohhs/yyym+::hdy` `sh-`yhddyo:`- . -+-..-```.-.-` //:/::`/+:ommdoyhhdMM+   .hNshy+
`syhoooydshN: :Noy+ooys+oNd/`  -:`  om.:dyhhdssyy  `y/   .:  ```/ .:`-:.-- .yoodhsooodmMN..+ :yhsNmo
-ohysoydm.hy. .dh//hh/osoMmNy``/ .---/ :.-+omy+s` -yhso/:+/.-...s-+:--ohy `hyohhdh-odhMd/ /-- /mhNNy
-/hssoyoh/-`:- `ohdsddo+sMMyo+ `.`:.    -.-.-//` .+ys+yossysysyyhhdy+ /+: sNsmNsm+:yhyy`   `+hmMdNNs
-+Nydyy:`-` /  syN/+hN:+oMMmy-`.- : -`` ./-    `oNNh/dNho/+oyshs/sshm-   `o.dmmyN-`--`    +mNdNsosNo
-hdmoym/ `` . `s+yhmhmdydMMNd.-`-//: -/--- `-.-/dmmomNd-/dh+yhhs+yh/N:  .`y-sNd/`       `hNo.-/ohhmo
 syNddMy` ```+:`sdddNMN:mNNNh` `sso+`.... -`-:.-:+`-./ymmhhosho+hds://- ``os:-.         -s:-odhddoys
 :omMdhmo-s/.ys :dMNm+-ymNNNy.:+s:+:.``.- :.:`.:..`::-o+sydosmy+:sdm::- `/-:   `  . .`   -yNmhohohhs
`-hNysmy::yy.+:  -mh- ``-++.`..   .:-.``../:+`:/:://-:.-:sNdhmdyhhMNo-:``.     `` ..`   sNMNdhydsyMy
`d// `---ymo y::``+ho/:  `/. .. .`..`:``----.:+o/.//:/s//smhmmMmhmMd``/ss:  ```.  -..   oMMNmmys-myo
.N- :` .:y+`-.`/+yo/osyo+od/-- `/---/-`.-:` -`.--+hdmmhdmdmyNmNmMNd--:+..``: -`` -..+ ./NMNMNmh-`-oy
 -.:o/ -yd+.` `+yo`.oyhhoho/..  `-o/+-::  -+s`  +/+oososmsmh:-:Ny/:o:` .``-`.  :-:/-/:/+s::my+-   ds
  /:// +hy-:.   `   -..` .`  -:///o/::o`   ` `-o+-:-osss+`.`  .. .-.  `:..+//:`/..:///-`  `. .`  `::
 -:-::--////..`.-.---...```````.``-//-``   .``:/:--/hmy/-- `` /   `` .`-.:-: /-:``/o/oss+:  `-./:.``
 `` `` `..````````::...---/:+:/-.`  ``.   ---.::..-o:/.`-. .`::+...:/:..`-   ` :-.`/o/-///----..`-:+
     ` `:        ..     `   ``.-..---:-   .-`:/`:yy/+o -``-::/::```--`.`   .. :``` `/s+shy+. ``-/+yo
 ..`...+......../:...` ````.`    `  `..::..--/-./sy/so-:-.s::+/.`+-.``` :.-`` .```-:yo+s/.`.`/+/.`+-
 ..`..:/.--::+syhysydhyhhyo+-.  ````.-.``.+-.`.::o:/`- -. :-`+/-...  -::s+::--/:-.`````.--..```...-.
      :o/-/+oshdhyssyhhNNdmNNmhs:.`` ``   `/` ` `- `-  /- :` ````+/-++y/:.``  ``::-.``    ``..`     
      -+-`-::+ddhsshysyhmmdhmmNNd.```      o.``  -.-- `::.: ` .-/s++-.`.``       `.:++--.....-.::.` 
      -:`..-/oydhhssoshdmddddNNms``..`..-.+s-//::--:.`.+./:---/ys:`    ``..`.--::...-s-`......``.+..
 :---.:+-/sy+shhhhhyyymdNmdmhy+.   ```` `:o/-/os::+so++-:`://+/.`       `.:/y:-.     +           /  
 +` `.-.`-+s:sdysosdyohdhy/:....```` `.::`-/- :/+//+ooo.` -s+...`    `.---.`y`   `   /           /` 
 /` `.-.`.:o-/hyhsoyy/:-  `` `  `---os-.` ./- `.--:.sy:..:-`   `..`.--`     o    ``  :           :. 
 /`   `  .++ .oyydh+` ```` ``.``.:--sy.   .+-` .:.sy-..-.   `   `-:+        / ``  ```o`..---..---o:`
 :`   ` `-/o.:yyod`   ```` ```-o`   -o: ``.+s/:osodh+/-      `.-.``/        +  `..:-.-..` -:     ```
`/.-../`.://:/yhhh`  .`     ``o+    :o::-` :Nshyhho-` .`   `-:`    /        o.:-o.        .:     `  
      o`  `.`/+mym/`    ``.````:..`/yyss/`./hy+-.      -.`-.`      /     `---.  o         .:    ``  
 .    : `.```+sdymsyo:.``        `-:-----``` /`   `` ``-o.         :  `--.`` `  o         .:     `` 
`:`   /`.+:..oymdmoddNho:``      .`     `.   /  ``.--.. +          /.-.:.  ` .  o-.`      --  ````` 
      +```.`-ssmmd+yhNMNNdho--`.-`    ``.```./-.-.`     +       `.--   --    `.`o``/   ``.//--.../-`
 `..../.`.++yhmdNmymNNNNNNNNddmmhhyo/----...-/          +    `-..`     :.  `.`  o``+.--..`       /  
 o`      `+ssdNNNNydmmmmmmNmss/dyho/``      `.    `     / `--.:        :-   `  `o-..`-           /  
 +       .+soyhmmd/hNNmNNmhhooohso+:`       ..         .+..   :    `   +`   `:--.    /           -  
 s       `+sshdmmh:yhmNmNmmmyhodsoo/.       :.    `-..``      /        +`--.-/`````` /           :  
 o        :hsmdmyh.shmmmmNmdhdhNhdy+:-...-..+--....:   `      /       .:.`  `- `.:+. :    `.---.--..
 +      `-/sohmdhm/hhmNmmhyossshyho:-/`           ..          +  `.:-`      `:`````- /....:`        
`+...-:--.``--+yymsmdNmmmhys+osso//. /            ..     `   .o--. /`       .- `.`--::    -/        
     `:    `./+yymhddmdNMmhyhyyso//. /            .-    `.....     /`       ./:--`   .:`  -:        
      - ` .`/+ohodshhmmmNmdyhys+/+ys.+            -/...-o          /`      .:yh.       -. :-      ``
      : ``.:/ssh/hsdyhdmddddhodsds/.:/..-..:::...-`     /          /`   --:.-mho/      ``:-:-:--::-`
      + ..--//+s/hsmmNhmdhooyhmyo/.-`      `/.          :          /---`:   sho//+.   `   //     -. 
 ``..-+..:+/:/+yymsmhmNddhhhysh/++o/.   `   -           -       .-:.    / `-yNs+-:-:     -/:-`   `. 
 s.    `-./.-:+o+mydNMNNNmmhhydyyo/:` `.-   /`          +  `..//`       +`./dms++o.`-:.-.    -.  `. 
 +   ``..`/+ossoomddmMMm:``.-/+ohhy/.       +        `.:+---  -:       `/.:hNNs-:/oo/o-       .: `.`
 /     -.-+:+so++dmmmNo-`     `:ysso:+.---.-o--.../.-..`      -:     `--+:shdNs/:o/++y:-` `     :+-`
 :   `--.:o//+ys+dMNy.  `--..-- y+o:.:            +           -: ..---` .oommmys/so-++:-+:       .:.
 :-.:+++++//oo+yodm/       .::  y:+:.+            +          ./:-`  -  -ohdNmhoo/s+::/::+:/.     .-o
 ..--o-::::-++shsy.       .. :  hoso`+            +    `--:/:.`     -  /ydmNNmy/:h/://+:s--/+--..  +
 .```/.::-.:sssd+`      .-   :.-mddy/h-`  ` `.`..`+-..-`+.``        -  /ymNmmhh+oy:o/:::y:-`o.     +
`...`/:`.:--:hs:..``  `-..--..`-mdyhh+:.``../-          o           -..sdddmmhy//++++/:-y:-.s.     +
`-:--+-/+++/++`    `.//.``/.   :hhyyo/.    `+           o`       ...:`-sdhdmhds::://+s++h:--s    `.o
.::...`.--s+.      .:/  ` o-   +ysos/.     `/           +    .`-..`   -ydyNddmh/::-:+s:/oo++y..--``+
-` ``  -:/+.`.` ` :- : .  +`   +hsso+.     `.          `s..-.` -      /dddNdNmhooy/:/s--::/+h``    +
-:-.` .:+- `.`..:/.  :-`  :``..ommmdy+...`.::``..`-.-:::.`     :     `:ydNhmddd++hssoy::..-/s`     +
--`   ./.  ``  -//   /`...:.-: :mdhyo/.`` ````````:`           /    .-symmhdhhN+/y:+/o+ys:--s   ..-o
-`  `:o`     `:- o``//:`.   -: /Nhso++            /            o...-:`oymhddmhmsoy///+//h+/+d...```/
...`.ysoo/-..o:..-` s-`     -: -hssoso            :       `.`..-`` .:`/dhhmmNmMhhdooo/:/h//+y      :
     y+//+++d-` .`  +:      `-`:dhyhho-`         `+....-:-.``      `/ /mdmddhmNsyyooso++s:::y   `  :
  :-omoso//:h   `   +-   `..--`:hhhyyh+:.--:.....--```` -.         .+-yhdhdyhdmo+/+/+o/od//+s      /
`omymN+oo+/:h       +-`..-+`   /hsys+/`    :            -.      `...``sshydhhmNo+//++s:/s+oos ``...+
-mhhmd/::/:/h    ``.:-` ``+    oyyyoo:``   /            -.  ``:-``   .yhmNmdmmmss+//+s/:+++oy-```  +
.s.-sh////-:h`.--:.`     `:    shhhyy+-`   /           `--.-``-`   `-:hmNNhddhdosdsoys//:o:o+      +
.y/+`h//--..s`` `:       `-   `syhdddy+-```/`````....-````    -`  `-+/yhdddmdhd+/msshy++/+//+      +
.Nh++ds+:/--s    -       `/.--.yhdyhds-.`````````/-`          -..-.-/`yyddhdydd++d+ooyyhso+os   ``.+
 sd+Ndo+/o/:y   `:   `..-..`+` oyyosd+-``        ::.       ``..`   -/ syNdmddmNhsdhs/+oomhyyo.--.``-
 +ymMdoy/-.-s   -/.--/.`    :` ysyssh+-          `/`  ``.:```      -+-hdNdmdmdNdmmoo//o+h/ohs`     -
`ssdNms+++/oh`....` `:`     /` yddhhmy-.`    ````//--.``-:      `.`::/hdmmdmmNddmdddyo++y//o+  ``.-:
`ooyyh///://h.      `/     `+:-dhdhhhy/-...-`.``..      .:  .`...` ` .ydNmddmMNmssosmhsoy+:+s::``:. 
`yyyNy/+o+-+s`      `: ``--..  yyyso+/+````:         ..-.:`.os-.    `:ymmNNMNNMdyhyodyoyhs+/s-.`..::
`++ydo:/:y-:h.     `.+.``.`    soyyyso/.  .:        -/-/++.`.y+:  `--/+ymNhdmMNMydy+:yyh:oysoy:+/``-
 ..-oh+/+o//y``+---`.    :-``  oyhhsos/.` `/`.`` ``:+s-:o/  +s/:::-`  /-oh+ohmdhhd++-yy+/yosyy`/.  .
`:-.oysoooooh+/s+/       ..`.--ddhhddso:---:..-``:.sdd++No. sm+ss` :y:   --oo+yNhNNNdh+-::yhs/`-./:.
.osdM++/+///h--:/:      `::./  yhdhmmhs.`-/-    `-`/hshoyo/ sh+os- +s+.`   `.:smdmyyho`-/sshs/`.sds:
-hhhMyso/+/+o-/++/  `.-.-`  -  ydyyddhmsymddo   +/-hsy-.s:/ -hoo``:oo  -      /yhhhyys+/os+so/o///y-
-hdhdsos+oohy:-oy+::::+o::/`:  hddddmdm+/+hy+:` ss.yyh+.-/-``--``+mNm:./       .+yyyossysy+++yhNo/++
-ms+hso+os+os+  :oys-sy+s//so `sdhhmNMhh+./:+yo-yo:/hdm:/--. `o//+oss+.`````    `.:--+-+/oosysyNm:yh
-Nsoy////+syss+.-//ssN-/...o+:-..-:sNMddNdhodmNohyo--sdh/+++-`so//:/--`     `.`.`        ` :y:sdN/oy
-m/:y+////s/:/h+./:ohm-y-:::+oo- -..//shMNsmyhm-.`-/o-...    .y-/:o+o/.``   `..-.-`            .h/ho
-Ns/-:-o/oo///h. -:o:mosN+.-ooyo:./--`:ohhymos:-` .`.///+oo  `h:+:++oy+so`.``     `             +y.`
.Nys++/y//-::/m:-//mN+o/:sdy+:/://:.`.`..  `./+:.:::.-:--s:`..soy::/+s+dy      .- -      ` `..://oy-
.ddmso/s/y//:/h` -+:o::``-::/sys+` .+:--:`--+sy:-..::---.-. ```-+hys+o+hm `      `- .+:/:so//::yhdNs
.hmNmNmdoy/::/m-.-: ` -oy-/+//ss/.`...   syd+/-``.          sNs/+//:+sdms  `.-/+o...+Ndo.`.-omy+-`::
.mNssdhsymms/:m.:/:`.::..-. `o..-.--+h+-.:s:` :/.        +-.:+s+o:ssssyo/-.`..:+:  `-dMd+-:.-:..`-:-
`oo//:/+/o++syh//... -.+: `.-+/     :++/:.   oos+.`   -./yyymss/y+osd/ho/ohh. ``-..  `smdy/./:/:.-..
        `-+.   :Myy--yos+:-` .+:      ``     `  .::+:ooshmdmmdy/s:sod.y+o+od.   :do-    :::..```        
    """)

def page114():
    page113()
    print("""
    With everyone worried about the sea crashing
in, no one will notice you if you try to escape. You
run down a long, little-used corridor that leads to
the sea. The exit door is heavy and rusty from not
being used. You push with all your might, and
finally it swings open into an airlock to the open
water. You push the emergency release button
and shoot out into the water. The Seeker is where
you left it, and once inside, you head for the surface
where the Maray waits for you.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)

def page115():
    print("""
``  .      ``----`..    ..      -..:.. .--::--/: `..--.`` .--/-.``                                 
 ...```   ```   -.--: .```.--:` /-+. `-.   ``    `   .`-```......-.`                               
  `:-.-:.  .---..-..`  `.`-.:-.  --     ``           .....``                                       
.-..``.`.```-.. `...`.`.`...    `+`        ``                                                      
  `....`-.``.` `--..:-/:--   /yshd+/-`       ``.                                                   
`..`....-.  .-:/:--.``      `+/yydyhdyo.        `.                                                 
`...--.  --:-s/.+..`/--     -  -hmyhyNmd/         `.``           `                                 
` -o:----`.``so+shs:+yo/:-:/-`.//NMNdyhy`     ..     ..`          ```                              
` .:-`  :-:- `.```.` ``-.`+s++:.oNMMs`.:    `.-/`                   ```                            
            :-            :/+s+ydNNhhh+/```.-  +d+s-                  `.`                          
           .++           `:-/ooysNymNdd+` -/.` ym/`..``                 `. `                       
      .`   /mN:            `.::/+sooyo/.``+  `.odo   ````                 `:.                      
      :+/. omNNs.            ```:```--` .o+   ./m.      ````                --`                    
       `:-`:-:oyhy////`              ``` ``  .o-- ```       `.`               `-``                 
         ``+:.- .:+yhd+`             o//    `-+ .`  ```        `                 .-`               
           .-//-    .:oys+-.         -//`  ` `-:-..      `````                    ``.`             
            `odo:      `:+yhyo:.`             oNNdy/:.``.:/oy+`                     ` ``           
             `+ss/`       `.:sdmds/-.`        .sNmo///yhymdNmo```                      ..          
              .::o+/..`       `/smmdhys+:.--/ooyddyy+omdsyo/-`   `.`                    `          
               `-:-:++/:.``.-:/++oyhhyo+ydydymymmsohh++/-:`        ``.`                            
                 ``-.:-/o+/--+:ohhso+ymdymyhyhyoy/---.: --..``        ```                          
                   .--...-:+//:/y/``./yydmyyymh.     `-`-. -/:`                                    
                     `-:.`   `.++++s-.+://-.+h+          -./+..:::                                 
                       `.-.     .-+o-..  `-`  ``.`         `:--.-:`:/`                             
                          `.-`     ```..`.-.:`  `..``         `::-`  ...`                          
                             `..`       ``-.`.``..``` .         ``` ..-.--:.                       
                                .`         `..    `-`  `..        `.::: `..-..`                    
                                              `- `-``..`  .`.        ://`` `. .-`                  
                                                .``:.  .``  `.-       ``.::     `.                 
                                                  ``.`-.-...`  `.        `-+..  .--```             
                                                   ` ...`.. `    .`        `..- -  : .``           
                                                       ...``.-.              `..-:.`  .:/          
                                                        ```` .-.   ``            `-/ `./..`        
                                                        `..    ``   `.`           -` `. ./-        
                                                        ``.`    ./    `            .-:-..`.:       
                                                               --:-   -..           -.:-.-:/`      
                                                          ```- .---    ```            :/.-`:..     
                                                            `-` .-..`   .`            `/`.--.:.``  
                                                            -`   .`.`    :`-           `/.-` --`-  
                                                            .`.`  .--    ``.   `.-      :..-`-o/:` 
                                                            .-`   -oo/` ````    `-..    -.-:````/` 
                                                           ..```   ./:  ` . ``  `.       .::-`.`..`
                                                           +::--`  --:`.    `.  .        `..--:.-.`
                                                           .-/+.:`-+y:`    `:.-   `        `.-.` -`
                                                           `./::-`+..+/:.`  ..`  `         ``-. ::.
                                                            `/-`.`..:.+-.`                `-``.../.
                                                             ...-   ` ./      `.`       `````.```.`
                                                             `.--`.  `./.    ``.`        ``   ..`.`
                                                               `.`. `--/+/.        `          -.```
                                                               `.`` `  //-.                 .``` ``
                                                             ``-:.    `-/-.        ``      ``--`.``
                                                              ./`   ```./-.``          ```   /.`..`
                                                              /.-   `.`/`-/`    `          `.:..-  
                                                             `/:.-.  -.-.:..         .     :`:s/:-`
                                                             : `:`  `:- ``++.             `-++/-+:`
                                                             /-:--  :.-`-.-:               ../-./`.
                                                             -`-:/   ` ``:+/.       `.`  ````- `.`.
                                                               `.`-..` -+o:`       `  ``     .-`::`
                                                                `/+.``    `:          ``   ./.:-/:.
                                                                ./o.    `--/::.``  ``  `  -.o/o/+:`
                                                               +- `.-   .:..   `    ` `   `.``.:/- 
                                                               ...-`   .`-.+/----.``  .::`   `..`: 
                                                                 `--`      `.-    `:++:.-`   :-:+o-
                                                                `-/..    `...- ``.//.```     `` //`
                                                                .`:.    `..:+:..+++/   `.::/-:/-+:`
                                                                `.`..   `--../:-/o+++.  --.  ..`.+-
                                                               ..-:-.     ``. .``.-+oo-`..` -::- :.
                                                                 `ms.`   -`.--..`  `..:o-.` :--:.. 
                                                                 -:+`   .o/o/::.  ``.  ``::   .-.:-
                                                                 `.//-   -../::.        `/+``.-o+:.
                                                                  -:`--  `....``.`     `.`` ```.-.`
                                                                  :+````.. ` `:.::.`               
                                                                 -`-`. ``.+-  .`::.      ``.`..````
                                                                `-` .   :ydys+/::.   `-/..``.  `:-.
                                                                 -..`   `-+so-```  `-/:-   `-`  -:.
                                                                  `.``   -++o+.`` `-:--`     ````.`
                                                                /:.`-:   :/++:-`.   .---    `.-ss/`
                                                               `+ss:--`/-::-`       `.:`   .` .o//.
                                                                `:+-`` ..-`       ``` `    `.  -.  
                                                              `.`.:    ` `       ` `        `. ``` 
                                                             `:/..`   `- `         `.`     ``--..-`
                                                            .//o:-  .. `---`             .``--.`   
                                                         `-.`:/os/  `   .`.+    ``       `:``  `   
                                                     `.``:+/`-`.-.`.` ` `/:.   `.`    `.``-  ```   
                                                     :`   /-`  `/`     ```  ` .-.:  `./:``-  ``.`` 
                                                     -/+-oo:`` --...`     `````--` ``        :...  
                                                       `  `-..  -`   ` . ``-:.: ---``       `.-    
                                                    `... ` `..` .-``-` ``.:::-      ` ````` ..-  ` 
                                     .-:.`--.``   `:`  .. ..   - `..        `   .-..`  .``:-:. :..`    
    """)

def page116():
    print("""
    It is uselessto try to escape the soldiers. You are
surrounded. They take you to the king, and he
sadly tells you that you are just like all the rest. He
can't trust anyone. He will have to decide what to
do with you and in the meantime he throws you
into the dungeon.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
    print("""
         /dNNy++-                                                                                   
         sMMMohdhhs+-`                                                 ` ` `   `.                   
         sMMMsdyNdyoNmos.`            -                                .         -                  
         sNMMsy+s/o/mh/oysy+-`  `--:.``          ` ` `:```      .    ``-`--.``..-/`. ``..-`         
         yMMMys/++s/dd/:-sosssh++/:.-.`   . .`   -    `   :`.```:        `//......:/      :         
        :mMMMds+/os/hh+/:ss+o+my/+/:.`      --```/`       o     +`        .:      .:.`..`.-         
       `:hMMMdy++:s/dd:+:smm++o+/+/o+h+ssssshhsood/++oo+/+m//++od/////+++:..:` `` .``.`.`           
       `-`+hdhosh.s/yd:o/yyys:     `/ydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:+o     --    `-.         
        ./  `-hmo/yohmoy/dyd:-    ./.:NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo:..-..   .+      .         
       `./ .dydoo/o+ddosohyo`.`  `.:/omMMMMMMMMNNNNmMMMMMMMMMMMMMMMMMN/-  .-  `---:-`` -:-:.-..-    
      `+o:.+dhy:sohymmdhsdNmds.-..::hhhNMMMMNhmMMMMmyMMMMMMMMMMMMMMMMd::-.-:-://-  .-  .o-` ...:..` 
      `/-   ossohhsymMMdyhosoo-.-o+o+msNMMMmymMMMMMMoMMMMMMMMMMMMMMMMMd+oo.sNMNd-``//:-+/        -. 
    ``+-.:`:mhhNmmsyhyss//oo+o``/yo/hhyMMMMNdoMMMMMMmdMMMMMMMMMMMMMMMNhd/:/y+/:y+:`````:o.```````.. 
  `-::+syh/dmy/-````  `.-````....-+/hhoMMMMMM/oddMMMMdMMMMMMMMMMMMMMN/:/ ./`:  :+.     `o.`   ````` 
 -osmhyds:-so`     `.-`         ``/mmhsMMMMMM+ .+MmmNMMMMMMMMMMMMMMMMd/:`//`-+sdd:...`` -           
 hyhddyy/od/`     ./.              /mdsMMMMMMN/./+:..-:--+ymMMMMMMMMMM:-./++:yyddysy+: ``   ``..    
/ssmhoshsy:-:/`  `:.         ` `   .shdMMMMMMm+`      --  .-/hMMMMMMMM/::.-+.-/-sdhmmo::      `-    
shsysoooo.   :/ ./.      .-://+::/o.`.dMMMMMm-         .   ..`yMMMMMMMNNs.` `os-```+hmhh       ``   
sosysyhh/    o- /-      :-`  //:/:-   oMMMMMs  -            - `oNMMMMMMm+`  `/` --..+hNMo``` ``:`   
/yhhyyhh-.` -: -+      /-    y:.//` ``sMMMMM/ ``            -.  -hMMMMN: ://`  `yyyo/smMN+    ``    
  ``...+:oo/o` /`     :-    .s/-/.:/o+mMMMMM: .`:.      `   `h-```dMMM+  :o. `-/s/+o+:-NMd          
     `//++:y`  /     :/      s+/` `///NMMMMM/  `o:`         `d+..`yMMN```--``.:/:/++:.:mMM-         
     .s+ssos-.`.`   .+.`.-`  y-:.- `.sdMMMMMo   od+ ``.`.... ::  +NMMh```..``..`````..hNMM:         
      .dmMMMd-./yss/+/-`..---+-` :.`-ydMMMMM+ .-+Mso:-:.``.```y:hMMMd.`.::/`:.`:   .::mNNN-         
      /dhNNNy//+ydmhhhy/-..:s:`  `-:hhhMMMMm`.-+hMMs::-.::---`/NMMMM+  -.`/`-. s-.--.+ydNm`         
    .+dh+oyyodhsshs/dddhs.`-so`  :o+dhhMMMMd``-yMMMy.//++:-oo//NMMMN- .`-`:`-.`:/-./+dNmmN-         
  `/+No/:-. :o-::+:+mdmho+dddy-``.../yhMMMMy..-NMMMNoodd-`.-o:/NMMMN. ``.`.```+:hy/+omMdyNs         
 .somd..-   `..:/--mhymmdyNmNN+.  ..+hhMMMM/.`hMMMMmhymh:/+/++yMMMMMs` `    .shdMm.-sNNhhMm/        
.o+oNm/-     `:/:.smyhNyyNMMNN+  `-:+mhMMMm::/NMMMNymNMmmdmdhmNMMMMMh``:/::-:dhsy:.:dNMhNNMNy.      
o-+ymmy`  `.-/+/-oyNddhosmNMmmh-...-:dhMMMs-sNMMMMyhdNMNMMNMNMMMMMMMm-`-+yoo-:/y/..omNNmmdNdNh-     
dmNNNdN++hdmNNNMNhydyhhsodMMmmM+.`-: sdMMN-`hMMMMmdhdddNNNhdNMMMMMMMMss+:`:s/++y.``:ydmmmdMmmNd:    
hmNMMMMMMMMMMMMMMNmNdmNdhmNNNNN+` /: /mMMNo/hMMMMdhhhydNds//mMMMMMMMMNy+-`.y.++-  `:+dmNddMNddmd:   
 .-/+yMMMMMMMMMMMMMMMMMMMMMMNNM+  -:`-MMMMdhdMMMMNdmhdMNy-.:MMMMMMMMMMm. `o:-+/   .:omNmNmMMmdmMs   
      sMMMMMMMMMMMMMMMMMMMMdNsmNo-::-hMMMMMMMMMMmmmmmMMNy+/dMMMMMMMMMM/  -/.s+o.`-/+sNMmNNMNNmmN+   
       sMMMMMMMMMMMMMMMMMMmsdMNNy`:/-yMMMMMMMMMNhdsssNMNy+sMMMMMMMMMMd   :-.y+:``../hydsNNmss++/`   
       oNMMMMMMMMMMMMMMMMMM:-dmys++/+hmmmNMMMMMNds`  sMmsohMMMMMMMMMM:   ```oy-```-symMMm+`         
       ymdMMMMMMMMNmMMMMMNMy`/Nys+/sooyso+sdmNMMmh:  .NmysoNMMMMMMMMMhsso/:oos/ohhd:oNMy`           
       dMdNMMMMMMMdydmMMMMMMh/dm+y://:MNdhhyo+NMMdm:``mso+:dMMMMMMds+/+/+ydNMNmNMy-+mhm+            
       dMMMmNMMMNdyododNMMMMMdhhos+/o+MMMMmdddMMMmNy.`yyso:dMMMMMN-:+sdhhmMMmdmMy:yy-.o/            
       dMMMmmMMMNhysss/+mMMMMysyo+:+oyMMMMMMMMMMMMdh` :h+/+NMMMMMMMMMMMyhdmNohNm+dN:`.s-            
       dMMMMNMMMMhoy:/:+ysMMMNh:do/++hMMMMMMMMMMMMmho--ysosMMMMMMMMMMMMmyohmMhsmMsyNh/.             
       mMMMhNNMMMNshyo//s+MMMMm/mooo/yMMMMMMMMMMMMMmmoyomohMMMMMMMMMMMMMMdoymso/dNs:yo//            
      `NMMNmMMMMMNhdms+-/hMMMh+hm+/o/hNNNNNNNNMMMMMssmmddodNNNNNNNmmNNNNNm/-sho--y:..: +/           
      `NMMhosshNymhyMdo/+mNNN:s++-.``````...-:+s///-////::-...````` .o-````oshhdo`-./:  o-          
      -MMN..   /yydyNd+yh-.---s`           `..`                    `-`     `:++dh` /:`  `o          
      -MNh``   oyhd+/--.o `  :/          ```                      ...` ` .`.`.--+:  :-   :`         
      `sd+:   -/-`     :y -  -o-` ` ` ` .```   `...-...`.........`            / `::  .-  .:         
        :s/ `.          : -  //.             ``   ```             ........`.``+` `y-  .: .+         
        +/`..           :./ ..              -:-...---``.````````/.   `.-..-.-.``:+y++  -:-ys        
       `s+..       .`   :-o :            ```                   --  /o:://./oysysydmyo.`o+/smo`      
      .yh:/`.``.`-..:-  /yy           `-`                     /.   `...----:`    ..:s+. `:o/so      
     `myy:.  .`  `//.   +s+/    `--..::`.``. `.`       ```` .`             ` `.:+-..`-/oodhoy+      
     od/o.-o+o+++/`    /Nmho:.-`.-` -s-                                    -++/++:--:--``           
    .ddy:.+++:/+//-://:hmdh+` `.---:-                                                               
                     `.dNdh-/`.-`                                                                   
                       ohs/.`                                                                           
    """)

def page117():
    print("""
    How can you escape? The soldiers are coming
after you. You yell as loud as you can and everyone
in the theatersurrounds you, forming a barrier
to the soldiers. The soldiers stare at the people all
around them, hesitate, and then quickly leave.
They know that the odds are too great to win such
a fight.
    The people cry for the revolt to go on. The
crowd leaves the theater and heads to the king's
quarters. All along the route people join you and
even the king's soldiers begin to join the crowd.
You and the people are free; the king is put in
prison. The revolt is a success.


           _______ _    _ ______   ______ _   _ _____  
          |__   __| |  | |  ____| |  ____| \ | |  __ \ 
             | |  | |__| | |__    | |__  |  \| | |  | |
             | |  |  __  |  __|   |  __| | . ` | |  | |
             | |  | |  | | |____  | |____| |\  | |__| |
             |_|  |_|  |_|______| |______|_| \_|_____/ 
                                                       
    """)
page1()
input("...")


