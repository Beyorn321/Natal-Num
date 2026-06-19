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
Immunities = {"Magic": "Tech",
              "Tech": "Drama",
              "Drama": "Resist",
              "Resist": "Speach",
              "Speach": "Strength",
              "Strength": "Magic"}




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




class cpuAttack:
    def rngBase(intel):
        choi = []


        target = random.choice([
            "Magic", "Strength", "Drama",
            "Speach", "Tech", "Resist"
        ])


        for stat, values in enmyStats.items():
            if stat != "Skill" and values[1] > 0:
                choi.append(stat)


        choi2 = random.choice(choi)
        if intel > enmyStats[choi2][1]:
            intel = enmyStats[choi2][1]
        dmg = random.uniform(
            intel, float(enmyStats[choi2][1]))
        for Prey1, Prey2 in Immunities.items():
            if Prey1 == choi2 and Prey2 == target:
                print(f"Enemy attacked {target}", 
                    f"using its {choi2}, and blundered")
                break
            elif Prey1 == "Strength":
                plyrStats[target][1] -= round(dmg / 2, 1)
                if plyrStats[target][1] < 0:
                    plyrStats[target][1] = 0
                print(f"Enemy attacked {target},",
                f"dealing {round(dmg / 2, 1)} damage,",
                f"using its {choi2}!")
                time.sleep(1.5)


    def dumBase(intel, intel2,
                 intel3, intel4):
        choi = []
        if intel4 < 1:
            intel3 = random.choice(["Magic",
            "Strength",
            "Drama","Speach",
            "Tech", "Resist"])
            intel4 = intel2
        else:
            intel4 -= 1
        for stat, values in enmyStats.items():
            if stat != "Skill" and values[1] > 0:
                choi.append(stat)
        hld = enmyStats
        for i in choi:
            ans = True
            for j in choi:
                if not hld[i][1] >= hld[j][1]:
                    ans = False
            if ans == True:
                choi2 = i
        if intel > enmyStats[choi2][1]:
            intel = enmyStats[choi2][1]
        dmg = random.uniform(
            intel, float(enmyStats[choi2][1]))
        for Prey1, Prey2 in Immunities.items():
            if Prey1 == choi2 and Prey2 == intel3:
                print(f"Enemy attacked {intel3}", 
                    f"using its {choi2}, and blundered")
                break
            elif Prey1 == "Strength":
                plyrStats[intel3][1] -= round(dmg / 2, 1)
                if plyrStats[intel3][1] < 0:
                    plyrStats[intel3][1] = 0
                print(f"Enemy attacked {intel3},",
                      f"dealing {round(dmg / 2, 1)} damage,",
                    f"using its {choi2}!")
        if plyrStats[intel3][1] < 0:
            plyrStats[intel3][1] = 0
        time.sleep(1.5)




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
        maxDmg = max(intel,
                     round(float(enmyStats[strngst][1]) / 2, 1))
        dmg = round(random.uniform(intel, maxDmg), 1)
        for Prey1, Prey2 in Immunities.items():
            if Prey1 == strngst and Prey2 == intel3:
                print(f"Enemy attacked {intel3}", 
                    f"using its {strngst}, and blundered")
                break
            elif Prey1 == "Strength":
                plyrStats[intel3][1] -= dmg
                if plyrStats[intel3][1] < 0:
                    plyrStats[intel3][1] = 0
                print(f"Enemy attacked {intel3}, dealing {dmg / 2} damage,",
                    f"using its {strngst}!")
        if plyrStats[intel3][1] < 0:
            plyrStats[intel3][1] = 0
        time.sleep(1.5)




def enemy_List(ans):
    RLvUp = 0
    DLvUp = 0
    SLvUp = 0
    if difficulty != 0 and difficulty % 4 == 0:
        RLvUp += 2
    if difficulty != 0 and difficulty % 6 == 0:
        DLvUp += 2
    if difficulty != 0 and difficulty % 10 == 0:
        SLvUp += 3
    Enemies = {"Cawalk": {"Patrn": "dumbase",
               "Agress": 2 + (DLvUp / 2), "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 2 + DLvUp,
            "strength": 2 + DLvUp,
              "drama": 1 + DLvUp},
    "Tricloppy": {"Patrn": "dumbase",
               "Agress": 5 + (DLvUp / 2), "Stubrn": 4,
               "Focus": str, "Change": 0,
              "skill": 1 + DLvUp,
              "strength": 3 + DLvUp,
              "drama": 1 + DLvUp},
    "Triclopog": {"Patrn": "dumbase",
               "Agress": 8 + (DLvUp / 2),
                 "Stubrn": 4,
               "Focus": str, "Change": 0,
              "skill": 1 + DLvUp,
              "Strength": 5 + DLvUp,
              "Drama": 2 + DLvUp,
              "Resist": 2 + DLvUp},
    "Xphizard": {"Patrn": "smrtbase",
               "Agress": 4 + (SLvUp / 2),
                 "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 5 + SLvUp,
              "Magic": 4 + SLvUp,
              "Speach": 2 + SLvUp},
    "Goodue": {"Patrn": "rngbase",
               "Agress": 1 + (RLvUp / 2),
                 "Stubrn": 0,
               "Focus": str, "Change": 0,
              "skill": 5 + RLvUp,
              "Resist": 0  + RLvUp},
    "Drahqeon": {"Patrn": "smrtbase",
               "Agress": 19 + (SLvUp / 2),
               "Stubrn": 3,
               "Focus": str, "Change": 0,
              "skill": 6 + SLvUp,
              "Strength": 11 + SLvUp,
              "Drama": 5 + SLvUp,
              "Resist": 6 + SLvUp,
                "Speach": 4 + SLvUp},
    "Sanke": {"Patrn": "rngbase",
               "Agress": 3 + (RLvUp / 2),
                 "Stubrn": 3,
               "Focus": str, "Change": 0,
              "skill": 3  + RLvUp,
              "Strength": 1  + RLvUp,
              "Speach": 4  + RLvUp},
    "Tobor": {"Patrn": "rngbase",
               "Agress": 5 + (RLvUp / 2),
                 "Stubrn": 2,
               "Focus": str, "Change": 0,
              "skill": 5  + RLvUp,
              "Strength": 1 + RLvUp,
              "Tech": 5 + RLvUp}
               }
   
    enmyInfo.update(Enemies[ans])
    return enmyInfo




def battle():
    global difficulty
    nmychoi = None
    if difficulty == 0:
        nmychoi = "Goodue"
    else:
        nmychoi = random.choice(["Cawalk", "Tricloppy",
                "Triclopog", "Xphizard",
                "Goodue", "Drahqeon",
                "Sanke", "Tobor"])
    print("Something approaches!..")
    time.sleep(3)
    print(f"{nmychoi} appears!")
    time.sleep(1.5)
    enemy_List(nmychoi)
    enmyStats["Skill"] = enmyInfo["skill"]
    for i in enmyStats:
        for j in enmyInfo:
            if j == i:
                enmyStats[i][0] = enmyInfo[j]
    dice.rngSix(enmyStats)
    nmyLoss = 6
    plyrLoss = 6
    plyrLife = True
    plyr = "Shtirk"
    plyrTurn = True
    while nmyLoss > 0 and plyrLoss > 0 or plyrLife == True and nmyLoss > 0:
        if plyrLoss == 0:
            print("Shtirk has fallen!")
            time.sleep(1.5)
            print("Exphee takes place!")
            time.sleep(1)
            plyrLoss = 6
            plyrLife = False
            plyr = "Xphee"
            dice.rngSix(plyrStats)
        if plyrTurn == True:
            nmyLoss = 6
            print(f"{plyr}:")
            for key, value in plyrStats.items():
                if isinstance(value, list):
                    print(f"{key}: {value[1]}")
            try:
                print("Be accurate in spelling!\n")
                plyrTrn1 = input("What enemy ability will you attack?")
                plyrTrn2 = input("What ability will you use?")
                damage = float(input("How much power will you use in your ability?"
                               "(Power / 2 = damage   Power = ability value)"))
                if (plyrTrn1.lower() in map(str.lower, plyrStats) and
    plyrTrn2.lower() in map(str.lower, enmyStats)):
                    if damage <= plyrStats[plyrTrn2][1]:
                        for Prey1, Prey2 in Immunities.items():
                            if Prey1 == plyrTrn2 and Prey2 == plyrTrn1:
                                print(f"Player attacked {plyrTrn1}", 
                                    f"using its {plyrTrn2}, and blundered")
                                time.sleep(1.5)
                                break
                            elif Prey1 == "Strength":
                                enmyStats[plyrTrn1][1] -= damage / 2
                                if enmyStats[plyrTrn1][1] < 0:
                                    enmyStats[plyrTrn1][1] = 0
                                print(f"You delt {damage / 2} damage to its {plyrTrn1}!")
                                time.sleep(1.5)
                            
                    else:
                        print("You exceeded your power, and",
                                "overestimated yourself")
                        damage -= damage
                        time.sleep(1.5)
                else:
                    print("The ability you typed was off or",
                      "you didn't properly used numbers.")
            except:
                print("The ability you typed was off or",
                      "you didn't properly used numbers.")
                time.sleep(1.5)
            finally:
                print("End of turn.")
                time.sleep(1)
            plyrTurn = False
            for stat, values in enmyStats.items():
                if stat != "Skill" and values[1] <= 0:
                    nmyLoss -= 1
                else:
                    nmyLoss = 6
        else:
            plyrLoss = 6
            V1 = enmyInfo["Agress"]
            V2 = enmyInfo["Stubrn"]
            V3 = enmyInfo["Focus"]
            V4 = enmyInfo["Change"]
            if enmyInfo["Patrn"] == "rngbase":
                cpuAttack.rngBase(V1)
            elif enmyInfo["Patrn"] == "dumbase":
                cpuAttack.dumBase(V1, V2, V3, V4)
            else:
                cpuAttack.smartBase(V1, V2, V3, V4)
            plyrTurn = True
            for stat, values in plyrStats.items():
                if stat != "Skill" and values[1] <= 0:
                    plyrLoss -= 1
                else:
                    plyrLoss = 6
    if nmyLoss <= 0:
        for stat, values in plyrStats.items():
            if stat != "Skill":
                print(stat, values)
                values[1] = 0
        print(f"You defeated the {nmychoi}!")
        time.sleep(1)
        plyrStats["Skill"] += 2
        difficulty += 1
        print("You gained 2 skill points!")
        time.sleep(1)
        if difficulty + 1 % 3 == 0:
            print("You got a wild roll gain!")
            time.sleep(1)
            inputz = None
            while inputz == None:
                inputz = input("What stat do you want to gain in?")
                if inputz.lower() == any(k.lower() for k in plyrStats):
                    plyrStats[inputz][0] += 1
                    print(f"Your {inputz} has gain in chance!")
                else:
                    inputz = None
                    print("You mistyped, try again!")
                    time.sleep(1)
        time.sleep(1)
        nature_story()
    elif plyrLoss <= 0:
        print(f"The {nmychoi} defeated you!")
        time.sleep(1.5)
        print("Game over!")
        time.sleep(1.5)
        print(f"You defeated {difficulty}",
              "enemies, and gained a total of",
              f"{plyrStats['Skill'] - 5} skill",
              "points!")
        time.sleep(3)
        quit()




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
    time.sleep(2.5)
    input("Continue?")
    battle()








def intro():
    Tutoro = "TutorIntro.txt"
    linecount = 1
    skip = False
    with open(Tutoro, "r", encoding="utf-8") as f:
        for line in f:
            if 1 < linecount and linecount < 9:
                print(line.strip())
                time.sleep(4.5)
            linecount += 1
            if linecount > 8:
                break
        time.sleep(1.5)
        input("(Type anything to continue)")
        for line in f:
            if 10 < linecount and linecount < 15:
                print(line.strip())
                time.sleep(1.5)
            linecount += 1
            if linecount > 14:
                break
        inp1 = input("Y/or type anything for no")
        if inp1.lower() == "y" or inp1.lower() == "yes":
            for line in f:
                if 15 < linecount and linecount < 18:
                    print(line.strip())
                    time.sleep(1.5)
                linecount += 1
                if linecount > 20:
                    break
            inp2 = input("Y/or type anything for no")
            if inp2.lower() == "y" or inp2.lower() == "yes":
                for line in f:
                    if 1 < linecount and linecount < 26:
                        print(line.strip())
                        time.sleep(2)
                    linecount += 1
                    if linecount > 25:
                        print("")
                        break
            else:
                for line in f:
                    if 22 < linecount and linecount < 25:
                        print(line.strip())
                        time.sleep(2)
                    linecount += 1
                    if linecount > 24:
                        skip = True
                        break
        else:
            for line in f:
                if linecount == 27:
                    print(line.strip())
                    time.sleep(2)
                linecount += 1
                if linecount > 27:
                    break
        if skip == False:
            for line in f:
                if 27 < linecount and linecount < 36:
                    print(line.strip())
                    time.sleep(4)
                linecount += 1
                if linecount > 35:
                    break
        for line in f:
                if 37 < linecount and linecount < 40:
                    print(line.strip())
                    time.sleep(2)
                linecount += 1
                if linecount > 39:
                    break
    dice.rngSix(plyrStats)
    battle()



intro()
