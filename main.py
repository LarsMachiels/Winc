__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile


def clean_cache():
    if os.path.exists("cache"):
        for file in os.listdir("cache"):
            os.remove("cache/" + file)
    else:
        os.mkdir("cache")
    return


def cache_zip(zip_path, unzip_path):
    clean_cache()
    zipfile.ZipFile(zip_path, "r").extractall(unzip_path)
    return


def cached_files():
    files_incl_path = []
    for f in os.listdir("cache"):
        files_incl_path.append(os.getcwd() + "\\cache\\" + f)
    return files_incl_path


'''
Voor wat betreft de functie find_password is de opdracht een beetje onduidelijk. 
Er wordt een hint gegeven dat het woord "password" wel eens de indicator zou kunnen
zijn voor het paswoord. Dit is echter geen vaststaand feit. De functie zou dus eigenlijk
bij elk bestand een aantal keywords moeten doorlopen zoals bijvoorbeeld: password, keyword, pw,
secrect_word etc, etc.. Verder is natuurlijk niet duidelijk waar dan het eigenlijke paswoord
zelf staat. Staat deze misschien voor het woord "password" zoals bijvoorbeeld 
geheim_pw = paswoord of daarna. Ook is niet duidelijk of en hoeveel spaties tussen het woord
paswoord en het eigenlijke paswoord staan (vandaar het gebruik van .split()). 
Omdat je deze gegevens niet hebt is het moeilijk hier een goede functie voor te schrijven. 
Ik ben er echter maar vanuit gegaan dat het allemaal niet zo ingewikkeld
bedoeld is in deze beginnerscursus en ben dan ook maar uitgegaan van de aannames
dat het keywoord "password" is, het eigenlijke paswoord zich direct na "password" bevindt en dat
"password" en het paswoord zelf gescheiden worden door een spatie. Ook heb ik er bewust voor
gekozen niet het hele bestand tegelijk in het werkgeheugen te laden omdat je
van te voren niet weet hoe groot de bestanden zijn.

'''
def find_password(cached_files):
    for f in cached_files:
        file = open(f, "r")
        for line in file:
            if line.lower().find("password") > -1:
                words = line.split()
                for i in range(len(words)):
                    if words[i].find("password") > -1 and len(words) > i:
                        file.close()
                        return words[i + 1]
        file.close()
    return ''
