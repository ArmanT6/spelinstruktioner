# **1. Introduktion**
from colorama import Fore, init
import time
import os
def intro():
    input("Tryck enter för att börja: ")
    print("")
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX+"""
$
$$ |                $$ |                          \__|            $$ |    
$$ |       $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$\  $$\ $$$$$$$\  $$$$$$\   
$$ |       \____$$\ $$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$  __$$\ \_$$  _|  
$$ |       $$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |  \__|$$ |$$ |  $$ |  $$ |    
$$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |  $$ |$$\ 
$$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$ |      $$ |$$ |  $$ |  \$$$$  |
\________| \_______|\_______/  \____$$ |\__|      \__|\__|  \__|   \____/ 
                              $$\   $$ |                                  
                              \$$$$$$  |                            
                               \______/  """)
    time.sleep(1)
    print("")
    init(autoreset=True)
    print("Spelet handlar om att hitta rätt väg ut ur labyrinten. Lycka till!\n")
    os.system("cls")

# **2. Huvudmeny**
def huvudmeny():
    while True:
        print("\nHuvudmeny:")
        print("1. Läs hur spelet funkar\n2. Börja spela")
        val = input("Välj ett alternativ (1/2): ").strip()
        if val == "1":
            hur_spelet_funkar()
            huvudmeny()  # Återvänd till huvudmenyn efter att ha läst reglerna
        elif val == "2":
            startpunkten()
        else:
            print("Ogiltigt val. Försök igen.")

# **3. Spelregler**
def hur_spelet_funkar():
    print("\nSpelregler:")
    print("1. Stöter du på en fiende besegrar du den och går vidare.")
    print("2. Tomma vägar tar dig ett steg bak.")
    print("3. Hitta kistor för att få ledtrådar.")
    input("Tryck enter för att fortsätta...")

# **4. Startpunkten**
def startpunkten():
    print("\nDu är i startpunkten.")
    print("1. Gå fram\n2. Gå höger\n3. Gå vänster")
    val = input("Välj din väg (1/2/3): ").strip()
    if val == "1":
        vag_1()
    elif val == "2":
        check_1()
    elif val == "3":
        print("\nTom väg. Du går tillbaka till start.")
        startpunkten()
    else:
        print("Ogiltigt val. Försök igen.")
        startpunkten()  # Återvänd till startpunkten vid ogiltigt val

# **5. Väg 1**
def vag_1():
    print("\nDu står vid en korsning i labyrinten.")
    print("1. Gå fram\n2. Gå höger\n3. Gå vänster")
    val = input("Välj din väg (1/2/3): ").strip()
    if val == "1":
        print("\nDu stöter på en skrämmande fiende! Den attackerar utan varning, men du blockerar dess slag och slår tillbaka med ditt svärd. Fienden faller och du kan fortsätta framåt.")
        vag_2()
    elif val == "2":
        print("\nTom väg. Du går ett steg tillbaka.")
        startpunkten()
    elif val == "3":
        print("\nDu går vidare till väg 2.")
        vag_2()
    else:
        print("Ogiltigt val. Försök igen.")
        vag_1()  # Återvänd till väg 1 vid ogiltigt val

# **6. Väg 2**
def vag_2():
    print("\nDu är i väg 2.")
    print("1. Gå fram\n2. Gå höger\n3. Gå vänster")
    val = input("Välj din väg (1/2/3): ").strip()
    if val == "1":
        input("du hittade en kista\ntryck enter: ")
        anim = R"""



                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`"""
        print(anim)
        time.sleep(1)
        os.system("cls")
        anim2 = R"""

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'"""
        print(anim2)
        time.sleep(1)
        os.system("cls")
                    
        anim3 = """   
    ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
    |                            |.
    |        Ditt nästa
            steg är frammåt 
    |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/dc__________________________/."""
    
        input("du har tre sekunder på dig att läsa brevet: ")
        print(anim3)
        time.sleep(3)
        os.system("cls")
        check_1()
    elif val == "2":
        print("\nTom väg. Du går ett steg tillbaka.")
        vag_1()
    elif val == "3":
        print("\nTom väg. Du går ett steg tillbaka.")
        vag_1()
    else:
        print("Ogiltigt val. Försök igen.")
        vag_2()  # Återvänd till väg 2 vid ogiltigt val

# **7. Kontrollpunkt 1**
def check_1():
    print("\nDu är i kontrollpunkt 1.")
    print("1. Gå fram\n2. Gå höger\n3. Gå vänster")
    val = input("Välj din väg (1/2/3): ").strip()
    if val == "1":
        print("\nDu stöter på en fiende! Du besegrar fienden och går vidare.")
        check_2()
    elif val == "2":
        print("\nDu går vidare till kontrollpunkt 2.")
        check_2()
    elif val == "3":
        print("\nTom väg. Du går ett steg tillbaka.")
        vag_2()
    else:
        print("Ogiltigt val. Försök igen.")
        check_1()  # Återvänd till kontrollpunkt 1 vid ogiltigt val

# **8. Kontrollpunkt 2**
def check_2():
    print("\nDu är i kontrollpunkt 2.")
    print("1. Gå fram\n2. Gå höger\n3. Gå vänster")
    val = input("Välj din väg (1/2/3): ").strip()
    if val == "1":
        print("\nTom väg. Du går ett steg tillbaka.")
        check_1()
    elif val == "2":
        print("\nTom väg. Du går ett steg tillbaka.")
        check_1()
    elif val == "3":
        print("\nDu går vidare till bossen.")
        fight_scene()
    else:
        print("Ogiltigt val. Försök igen.")
        check_2()  # Återvänd till kontrollpunkt 2 vid ogiltigt val

# **9. Slutscen - Boss Fight**
def fight_scene():
    print("\nDu möter bossen!")
    print("Bossen hotar dig, men med ditt legendariska svärd lyckas du slå tillbaka och vinna spelet!")
    input("Tryck enter för att ta det avgörande slaget mot bossen och besegra den")
    print("Grattis du har besegrat bossen och du är nu den nuvarande bossen!!")
    exit()

# Starta spelet
intro()
huvudmeny()