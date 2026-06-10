import random
import time
plyrStats = {"Skill": 5,
             "Magic": [0, 0],
             "Strength": [0, 0],
             "Speach": [0, 0],
             "Tech": [0, 0],
             "Drama": [0, 0],
             "Resist": [0, 0]}
enmyStats = {"Skill": 0,
             "Magic": [0, 0],
             "Strength": [0, 0],
             "Speach": [0, 0],
             "Tech": [0, 0],
             "Drama": [0, 0],
             "Resist": [0, 0]}
difficulty = 0
enmyInfo = dict()


class dice:
    def rngSix(holder):
        choi = ["Magic", "Strength",
            "Drama","Speach",
            "Tech", "Resist"]
        for i in range(holder["Skill"]):
            diRoll = random.choice(choi)
            holder[diRoll][1] += 1
        for i in choi:
            for j in range(holder[i][0]):
                holder[i][1] += random.randint(1,
                                          3)
        print(holder)




class cpuAttack:
    def rngBase(intel):
        choi = []
        target = random.choice("Magic",
        "Strength",
        "Drama","Speach",
        "Tech", "Resist")
        for i in enmyStats:
            if enmyStats[i][1] > 0:
                choi.append(i)
        choi2 = random.choice(choi)
        dmg = random.randint(intel,
        round(enmyStats[choi2][1] / 2))
        plyrStats[target][1] -= dmg


    def dumBase(intel, intel2,
                 intel3, intel4):
        choi = []
        if intel4 < 1:
            intel3 = random.choice("Magic",
            "Strength",
            "Drama","Speach",
            "Tech", "Resist")
            intel4 = intel2
        else:
            intel4 -= 1
        for i in enmyStats:
            if enmyStats[i][1] > 0:
                choi.append(i)
        hld = enmyStats
        for i in choi:
            ans = True
            for j in choi:
                if not hld[i][1] >= hld[j][1]:
                    ans = False
            if ans == True:
                choi2 = i
        dmg = random.randint(intel,
        round(enmyStats[choi2][1] / 2))
        plyrStats[intel3][1] -= dmg


    def smartBase(intel, intel2, intel3, intel4):
        if intel4 < 1:
            bstScre = -999999
            trgt = None
            for stat in plyrStats:
                if stat == "Skill":
                    continue
                value = plyrStats[stat][1]
                score = value
                if value <= 5:
                    score += 10
                if score > bstScre:
                    bstScre = score
                    if random.randint(1,5) % 4 != 1:
                        trgt = stat
            intel3 = trgt
            intel4 = intel2
        else:
            intel4 -= 1
        strngst = None
        strngstVal = -1
        for stat in enmyStats:
            if stat == "Skill":
                continue
            if enmyStats[stat][1] > strngstVal:
                strngstVal = enmyStats[stat][1]
                strngst = stat
        maxDmg = max(intel, round(enmyStats[strngst][1] / 2))
        dmg = random.randint(intel, maxDmg)
        plyrStats[intel3][1] -= dmg
        print(f"Enemy attacked {intel3}, dealing {dmg} damage!")




def enemy_List(ans):
    Enemies = {"Cawalk": {"Patrn": "dumbase",
               "Agress": 2, "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 2, "strength": 2,
              "drama": 1},
    "Tricloppy": {"Patrn": "dumbase",
               "Agress": 5, "Stubrn": 4,
               "Focus": str, "Change": 0,
              "skill": 1, "strength": 3,
              "drama": 1},
    "Triclopog": {"Patrn": "dumbase",
               "Agress": 8, "Stubrn": 4,
               "Focus": str, "Change": 0,
              "skill": 1, "Strength": 5,
              "Drama": 2, "Resist": 2},
    "Xphizard": {"Patrn": "smrtbase",
               "Agress": 4, "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 5, "Magic": 4,
              "Speach": 2},
    "Goodue": {"Patrn": "rngbase",
               "Agress": 1, "Stubrn": 0,
               "Focus": str, "Change": 0,
              "skill": 5, "Resist": 2},
    "Drahqeon": {"Patrn": "smrtbase",
               "Agress": 19, "Stubrn": 3,
               "Focus": str, "Change": 0,
              "skill": 6, "Strength": 11,
              "Drama": 5, "Resist": 6,
                "Speach": 4},
    "Sanke": {"Patrn": "rngbase",
               "Agress": 3, "Stubrn": 3,
               "Focus": str, "Change": 0,
              "skill": 3, "Strength": 1,
              "Speach": 4},
    "Tobor": {"Patrn": "rngbase",
               "Agress": 5, "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 5, "Strength": 1,
              "Tech": 5}
               }
    
    enmyInfo.update(Enemies[ans])
    print(enmyInfo)
    return enmyInfo




def battle():
    nmychoi = None
    if difficulty == 0:
        nmychoi = "Goodue"
    else:
        nmychoi = random.choice("Cawalk", "Tricloppy",
                "Triclopog", "Xphizard",
                "Goodue", "Drahqeon",
                "Sanke", "Tobor")
    print("Something approaches!..")
    time.sleep(3)
    print(f"{nmychoi} appears!")
    time.sleep(1.5)
    print(plyrStats)
    enemy_List(nmychoi)
    enmyStats["Skill"] = enmyInfo["skill"]
    for i in enmyStats:
        for j in enmyInfo:
            print(i, j)
            if j == i:
                enmyStats[i][0] = enmyInfo[j]
    dice.rngSix(enmyStats)
    




def nature_story():
    setRng = {
        "setting1": ("mist-laden marshes", 1),
        "setting2": ("moonlit pine forests", 2),
        "setting3": ("sunlit meadows", 3),
        "setting4": ("storm-washed cliffs", 4),
        "setting5": ("ancient valleys", 5),
        "setting6": ("frost-covered tundras", 6),
        "setting7": ("rain-soaked jungles", 7)
    }
    themRng = {
        1: ("nasal swimming fog and mossy hint",
            "ever lasting echoes and unusual silence",
            "hard earthy smell and starving goopy mud"),
        2: ("whispering needles and wandering shadows",
            "icy shining moon and murky rocks",
            "silvered bark and strong stillness"),
        3: ("golden grasses and drifting pollen",
            "warm breezes and swaying stems",
            "eye-level plants and endless color"),
        4: ("roaring winds and crashing waves",
            "salt spray and thunderous surf",
            "towering bluffs and distant lightning"),
        5: ("echoing stone and slow-moving fog",
            "weathered slopes and winding streams",
            "hidden hollows and layered earth"),
        6: ("crystalline silence and pale horizons",
            "sparkling ice and endless snowfields",
            "cold skies and lifeless sight"),
        7: ("lush growth and exotic song",
            "warm rain and tangled growth",
            "flowing water and emerald foliage")
    }
    Set1 = random.choice(list(setRng.values()))
    Dtl = random.choice(themRng[Set1[1]])
    dice.rngSix(plyrStats)


    print(f"The planet brings you in.\n"
        f"Through {Set1[0]}, all the {Dtl} fill you in.\n"
        f"To change you once again, newly seen.")




def intro():
    Tutoro = "TutorIntro.txt"
    linecount = 1
    skip = False
    with open(Tutoro, "r", encoding="utf-8") as f:
        for line in f:
            if 1 < linecount and linecount < 9:
                print(line.strip())
                time.sleep(0)
            linecount += 1
            if linecount > 8:
                linecount = 0
                break
        time.sleep(1.5)
        input("(Type anything to continue)")
    with open(Tutoro, "r", encoding="utf-8") as f:
        for line in f:
            if 9 < linecount and linecount < 14:
                print(line.strip())
                time.sleep(1.5)
            linecount += 1
            if linecount > 13:
                break
        inp1 = input("Y/or type anything for no")
        if inp1.lower() == "y":
            for line in f:
                if 15 < linecount and linecount < 18:
                    print(line.strip())
                    time.sleep(1.5)
                linecount += 1
                if linecount > 20:
                    linecount = 0
                    break
            inp2 = input("Y/or type anything for no")
            if inp2.lower() == "y":
                for line in f:
                    if 18 < linecount and linecount < 21:
                        print(line.strip())
                        time.sleep(2)
                    linecount += 1
                    if linecount > 20:
                        linecount = 0
                        break
            else:
                for line in f:
                    if 22 < linecount and linecount < 25:
                        print(line.strip())
                        time.sleep(2)
                    linecount += 1
                    if linecount > 24:
                        linecount = 0
                        skip = True
                        break
        else:
            for line in f:
                if linecount == 24:
                    print(line.strip())
                    time.sleep(2)
                linecount += 1
                if linecount > 23:
                    break
        if skip == False:
            for line in f:
                if 24 < linecount and linecount < 33:
                    print(line.strip())
                    time.sleep(2)
                linecount += 1
                if linecount > 32:
                    break
        for line in f:
                if 32 < linecount and linecount < 35:
                    print(line.strip())
                    time.sleep(2)
                linecount += 1
                if linecount > 34:
                    break








dice.rngSix(enmyStats)
nature_story()
battle()
#intro()
