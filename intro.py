import time
import os
import colorama
word =      R"""                                  $$\              
$$ |                $$ |                          \__|            $$ |    
$$ |       $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$\  $$\ $$$$$$$\  $$$$$$\   
$$ |       \____$$\ $$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$  __$$\ \_$$  _|  
$$ |       $$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |  \__|$$ |$$ |  $$ |  $$ |    
$$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |  $$ |$$\ 
$$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$ |      $$ |$$ |  $$ |  \$$$$  |
\________| \_______|\_______/  \____$$ |\__|      \__|\__|  \__|   \____/ 
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/  """

input("tryck för att se vår intro: ")
print(" ")
time.sleep(1)
print(colorama.Fore.BLUE+word)
colorama.init(True)
time.sleep(1)
print(" ")
lst = [
    "Välkommen till vår labyrint", 
    "Spelet handlar om att hitta den rätta vägen ut ur labyrinten"
]
for i in lst:
    print(i)
start = input("vill du starta spelet: ").lower()
if start== "ja":
    print("Du skickas vidare till spawn")
elif start == "nej":
    print("Programmet Avslutas")
    exit()