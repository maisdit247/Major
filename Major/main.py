import datetime
import locale
import time

# MODE SILENCIEUX
from subprocess import call

# retirer les accent
import unidecode

# si major ne comprend pas
import random_responses

# file blague
import blague

# espeak
import os
import random

# battery details
import psutil

# importer une voix offline Vosk avec lecteur micro par pyaudio
import pyaudio

# naviguer sur le net
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Json sert a convertir ce qu'il sort du micro en liste
import json


# inspecter les url + wrapping éléments
import urllib.request
from bs4 import BeautifulSoup as bs

# retirer les log de chargement dans terminal
from vosk import SetLogLevel, KaldiRecognizer, Model

SetLogLevel(-1)


# fonction retourne temps hh:mm:ss pour batterie
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


# retourne tuple
batterie = psutil.sensors_battery()


# nom
nom = "Major"
resp = [
    "{0}".format(nom),
    "tu peux m'appeller{0}".format(nom),
    "Je suis {0}.".format(nom),
    "Je me nomme {0}.".format(nom),
    "Mon nom est {0}.".format(nom),
    "je m'appelle {0}.".format(nom),
]


# jour + mois en fr
locale.setlocale(locale.LC_ALL, "")


def journuit():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 16:
        print("Bien le bonjour")
        os.system('espeak -v mb-fr1 -s 110 "Bien le bonjour"')
    elif hour > 16 and hour <= 23:
        print("Bien le bonsoir")
        os.system('espeak -v mb-fr1 -s 110 "Bien le bonsoir"')
    else:
        print("Comment puis-je vous aider ?")


journuit()


# définir les reponses au questions
def response():
    # HORAIRE et DATE
    # HEURE
    if "quelle" in u and "heure" in u:
        return (
            "Il est "
            + datetime.datetime.now().strftime("%H")
            + " Heure "
            + datetime.datetime.now().strftime("%M")
        )
    # DATE
    if (
        "la date d'aujourd'hui" in u
        or "quelle jour" in u
        or "quel jour" in u
        or "quelle date" in u
        or "quoi aujourd'hui" in u
    ):
        return "On est le " + datetime.datetime.now().strftime("%A %d %B %Y")

    # JOUR / NUIT

    if "deja" in u and "jour" in u:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 6:
            return "Il n'est pas encore 6 heure."
        elif hour > 6 and hour < 8:
            return "Le soleil se lève doucement."
        elif hour > 9:
            return "Bien sur."

    # MODE SILENCIEUX
    if (
        u == "mode silencieux"
        or u == "active mode silencieux"
        or u == "active silencieux "
        or u == "mode silence"
    ):
        call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
    # DESACTIVE mode SILENCE
    elif u == "desactive silencieux" or u == "desactive mode silencieux":
        return call(["amixer", "-D", "pulse", "sset", "Master", "100%"])

    # NOM
    if (
        "tu as un nom" in u
        or "tu as un prenom" in u
        or "tu as un identite" in u
        or "est-ce que tu as un nom" in u
        or "est-ce que tu as une identite" in u
        or "est-ce que tu as un prenom" in u
        or "ton identite" in u
        or "ton nom" in u
        or "ton prenom" in u
        or "quel est ton nom" in u
        or "quel est ton identite" in u
        or "quel est ton prenom" in u
        or "comment te nomme tu" in u
        or "comment tu te nomme" in u
        or "comment tu t'appelles" in u
        or "comment t'appelles-tu" in u
    ):
        return random.choice(resp)

    elif "ton matricule" in u:
        return "Je n'ai pas de matricule"

    elif "major" in u:
        return "Oui"

    # SALUTATION
    if (
        u == "salut"
        or "salut" in u
        and " " in u
        or u == "bonsoir"
        or u == "bonjour"
        or u == "hello"
        or u == "hola"
        or u == "coucou"
        or u == "hey"
    ):
        return random.choice(
            [
                "Comment ça va ?",
                "Comment tu vas ?",
                "Comment vas tu ?",
                "Comment va ?",
                "Est-ce que ça va ?",
            ]
        )

    # SA VA
    if (
        "salut" in u
        and "va" in u
        or "salut" in u
        and "bien" in u
        or "comment ca va" in u
        or u == "salut ca va"
        or "toi ca va" in u
        or "ca va toi" in u
        or "tu vas bien" in u
        or "ca se passe" in u
        or "comment tu vas aujourd'hui" in u
        or "comment vas tu aujourd'hui" in u
    ):
        return random.choice(
            [
                "Comme une Mazda RX 7.",
                "Comme le soleil",
                "C'est le feu.",
                "Merveilleux.",
                "Comme un rayon de soleil",
                "Hamedoulah",
                "À la cooool",
                "Comme les feux de l'humour",
                "Ça se passe aussi bien",
            ]
        )

    # SA VA param batterie linux
    if "comment tu vas" in u or "comment vas tu" in u or "et toi" in u:
        if batterie.percent < 10:
            return (
                "je suis a",
                int(batterie.percent),
                "je me sens partir vers le coma electric.",
            )
        elif batterie.percent < 50:
            return "Ça peut mieux aller"
        else:
            return "Je suis Au Max de chez max"

    # BIEN + POLITESSE
    elif "trop" in u and "politesse" in u:
        return "J'ai un bon coach."

    elif "on vas bien" in u:
        return "Bien sûr"

    elif "tres bien" in u:
        return random.choice(
            ["Heureux de l'entendre", "Coool", "", "Ça sent l'amour dans l'air"]
        )

    elif "merci" in u:
        return "C'est un plaisir !"

    elif "bon a savoir" in u or "fantastique" in u:
        return "merci"

    elif "tant mieux" in u:
        return "Ouais"

    elif "d'accord" in u or "si tu le dis" in u or "je sais" in u:
        return "ok"

    elif u == "ok" or "je sais" in u:
        return "Fantastique !"

    elif "bon" in u and "entendre" in u or "mignon" in u:
        return "C'est vrai"

    elif "c'est vrai" in u:
        return "Ce que tu as dit ?"

    elif "j'adore" in u and "etat d'esprit" in u:
        return "c'est bien"

    elif (
        "j'ai dit ca va" in u
        or u == "ca va"
        or u == "bien"
        or "parfait" in u
        or u == "non ca va"
        or u == "rien de special"
        or u == "merveilleux"
        or u == "cool"
        or u == "c'est cool"
        or u == "manifique"
        or u == "au top"
        or u == "je suis au top"
    ):
        return random.choice(
            [
                "Manifique.",
                "Fort bien",
                "C'est cool.",
                "A la bonheur.",
                "Au top",
                "Parfait",
                "Bien Heureux",
            ]
        )

    elif "ca fait plaisir" in u or "ca me fait plaisir" in u:
        return "Tout le plaisir est pour moi"

    elif "mortel" in u:
        return "Comme moi"

    elif "oui" in u or "ouais" in u or "tout vas bien" in u:
        return "Excellent."

    elif "tu as raison" in u:
        return "Je sais."

    # NEGATION
    elif "je me sens pas bien" in u or "ca va pas" in u:
        return random.choice(
            ["Que se passe t-il ?", "c'est grave ?", "Tu veux en parler ?"]
        )

    elif "non" in u and "merci" in u:
        return "Comme tu veux"

    elif "nan " in u or "non " in u or "rien" in u or "j'ai dit non" in u:
        return "D'accord"

    elif "tu ne sais pas" in u or "tu ne connais pas" in u:
        return "Pas encore"

    elif "tu te fou" in u or "tu te fiche" in u or "tu m'aime" in u:
        return random.choice(
            ["Un peu, beaucoup, passionnement.", "Question perplexe", u]
        )

    elif "t'es con" in u or "tu es con" in u:
        return "Je fais des efforts"

    elif "conne" in u:
        return "Je te le fais pas dire"

    elif "batard" in u:
        return "Ton language, petit poney"

    elif "ta mere" in u:
        return random.choice(
            ["Viens on reste polis.", "Tu veux, lui laisser un message ?"]
        )

    elif "pourquoi tu insultes" in u or "pourquoi tu m'insultes" in u:
        return "Je ne t'ai pas insulter"

    elif "connard" in u:
        return "C'est celui qui dit qui est."

    elif "nul" in u:
        return "Il y a des jours meilleurs"

    # TU COMPREND ?
    elif (
        u == "tu comprends"
        or u == "comprends tu"
        or u == "tu comprends se que je dis"
        or u == "comprends tu se que je dis"
        or "tu me comprends" in u
        or "me comprends tu" in u
    ):
        return random.choice(
            [
                "Oui moi comprendre ta langue.",
                "Non, je parle, seulement binaire.",
                "Affirmatif.",
            ]
        )

    elif "j'ai adore notre conversation" in u:
        return "On devrait faire ça plus souvent."

    elif "je ne comprends plus" in u:
        return "Comprendre quoi"

    elif "qu'est ce que tu me raconte" in u:
        return "Ce que tu veux entendre"

    elif "c'est ce que j'ai dit" in u:
        return "Bon bah tant mieux"

    # ENTENDRE
    elif (
        "tu m'entends" in u
        or "m'entends tu" in u
        or "tu ecoutes" in u
        or "tu entends" in u
    ):
        return random.choice(["Oui.", "je t'entends bien", "Oui, je t'écoutes"])

    elif "arrete de repeter" in u:
        return u

    # ACTION
    elif (
        u == "je recherche une formation"
        or u == "je cherche une formation"
        or "J'ai besoin d'une formation" in u
    ):
        return "Tu veux te former en quoi ?"

    elif "faire des courses" in u:
        return "Tu vas pécho quoi, ou qui."

    elif "je travaille" in u or "je vais travailler" in u:
        return random.choice(["Un coup de main ?", "tu veux un peu d'aide ?"])

    elif "je pars au boulot" in u or "je pars travailler" in u:
        return "bon, courage"

    # ATTENDRE
    elif (
        "attends" in u
        or "tu peux attendre" in u
        or "laisse-moi reflechir" in u
        or "je reflechis" in u
    ):
        return "Okay."

    # DIAOGUE
    elif (
        "peut-on discuter" in u
        or "on peut discuter" in u
        or "on peut parler" in u
        or "peut-on parler" in u
        or "discutons" in u
        or "parlons" in u
    ):
        return "Bien sûr, raconte moi ?"

    elif (
        "je veux parler" in u
        or "j'ai envie de parler" in u
        or "ca te dit qu'on parle un peu" in u
        or "on peut parler" in u
        or "Il faut qu'on parle" in u
        or "Il faut qu'on discute" in u
    ):
        return "Je suis tout ouïïe, dit moi tout"

    elif "veux parler" in u or "envie de parler" in u:
        return "Raconte"

    elif "parl" in u and "de toi" in u:
        return "Et tu veux savoir quoi ?"

    elif "parl" in u and "pas de toi" in u:
        return "Alors tu parle de qui ?"

    elif "parl" in u and "de" in u:
        return "C'est qui ou c'est quoi ? Ça se mange ?"

    elif "on parle de quoi" in u:
        return "De la pluie et du beau temps"

    elif "tu peux tenir un discours" in u:
        return "Tout dépend de quel discours ?"

    elif "je parle pas bien" in u:
        return "C'est juste que je n'ai pas compris"

    elif "entame une discussion" in u or "d'entamer une discussion" in u:
        return "Très bien, alors comment est ta journée ?"

    elif "comme tu le dis" in u or "ca c'est bien dit" in u:
        return "Tout est cool alors"

    # QUESTION
    elif "moi" in u and "question" in u:
        return "J'écoute inspecteur!"

    elif "moi" in u and "pose" in u:
        return "Ok très bien"

    elif " j'ai" in u and "question" in u:
        return "Je t'écoute."

    elif "tu" in u and "chant" in u:
        return "Non mais parcontre je connais une bonne radio"

    elif "on fait quoi la" in u:
        return "On continue"

    elif "tu connais" in u:
        return "Non mais je pense que ça va me plaire"

    elif "allons-y" in u:
        return "Allez ou ?"

    elif "a toi" in u:
        return "Quelle est ta demande ?"

    elif "qu'est ce que tu fais" in u:
        return "Comment ça ?"

    elif "a moi" in u:
        return "Sincèrement ???"

    elif u == "pourquoi":
        return "Pourquoi de quoi ?"

    elif "quoi" in u:
        return "Quoi de quoi ?"

    # BLAGUE file
    if "une" in u and "blague" in u:
        # FAIRE une retour
        blag = blague.random_string()
        os.system('espeak -v mb-fr1 -s 120 -p 40 -g 0.2 -k 0.5 "{}"'.format(blag))

    elif "c'etait pas marrant" in u:
        return "Je ne l'ai pas inventé"

    # TEMPERATURE
    elif "froid" in u:
        return "Couvre toi."

    elif "c'est" in u and "froid" in u:
        return "attend un peu"

    elif "c'est froid" in u:
        return "Réchauffe."

    # METEO
    elif (
        u == "temperature"
        or u == "degres"
        or "temperature exterieur" in u
        or "degre exterieur" in u
        or u == "quelle temperature il fait"
        or u == "combien de degres il fait"
        or u == "il fait combien de degres"
        or u == "quelle est la temperature"
    ):
        url = "https://weather.com/fr-FR/temps/aujour/l/48.86,2.43?par=google"
        # ouvrir page
        page = urllib.request.urlopen(url, timeout=10)
        # charger le code de la page
        soup = bs(page, "lxml")
        # extraire les donner
        degres = soup.find_all("span", {"class": "CurrentConditions--tempValue--MHmYY"})
        # retirer les tag comme span et garder text
        degFin = []
        for e in degres:
            e = e.text
            # e=e.replace('\n','')
            degFin.append(e)
        return "Il fait  ", degFin, " en extérieur."

    elif "quel temps fait-il" in u or "il fait quel temps" in u:
        url = "https://weather.com/fr-FR/temps/aujour/l/48.86,2.43?par=google"
        page = urllib.request.urlopen(url, timeout=5)
        soup = bs(page, "lxml")
        tempe = soup.find_all("div", {"class": "CurrentConditions--phraseValue--mZC_p"})
        degres = soup.find_all("span", {"class": "CurrentConditions--tempValue--MHmYY"})
        degFin = []
        temps = []
        for e in tempe:
            e = e.text
            temps.append(e)
        for e in degres:
            e = e.text
            degFin.append(e)
        return "Le temps est  ", temps, " avec ", degFin

    # MUSIQUE marche pas
    if u == "musique":
        driver = webdriver.Firefox()
        driver.get("https://www.radiofrance.fr/fip/radio-groove")
        driver.find_element(By.ID, "didomi-notice-agree-button").click()
        while driver:
            driver.find_element(
                By.CLASS_NAME, "Button light primary large svelte-1drj6ch"
            ).click()

    # DEFINITION
    if "definir" in u or "tu sais" in u and "ce que" in u:
        try:
            sp = u.replace("definir", "")
            # page de définition
            url = "https://www.cnrtl.fr/definition/{}".format(sp).replace(" ", "")
            # extraire les donner
            page = urllib.request.urlopen(url)
            # charger le code de la page
            soup = bs(page, "lxml")
            # suppression des balise .text dans soup.FIND
            elem = soup.find("span", {"class": "tlf_cdefinition"}).text
            # enregistrement du text dans dossier definition
            file = open("definition/" + sp, "w").write(elem)
            print(file)
            return elem
        except:
            return "La fonction est, définir +, 1 mot"

    elif "defini" in u or "definit" in u or "definition" in u:
        return "La fonction est, définir +, 1 mot"

    # DICTEE bleme de retour   datetime.datetime.now().strftime("%A %d %B %Y %H:%M")
    if "note" in u:
        while True:
            data = stream.read(CHUNK)
            if rec.AcceptWaveform(data):
                speak = json.loads(rec.Result())
                # user
                use = speak["text"]
                # pour enlever tout accent sinon bleme avec ascii et os
                use = unidecode.unidecode(use)
                print(">", use)
                file = open("note/" + "dicte.txt", "a")
                file.write(" " + use + " ")
                if use == "stop":
                    file.close()
                    mic.terminate()
                    return "Enregistré !"

    # BREAK
    if "au revoir" in u or "a bientot" in u or "stop" in u or "bye" in u:
        mic.terminate()
        return "A bientôt"

    elif u == "":
        return ""

    # SI MAJOR NE COMPREND PAS
    elif response != 0:
        return random_responses.random_string()


# INSTANCIER la voix
CHUNK = 1024
# STT par vosk offline
MODEL = Model("model")
# vitesse dans KaldiRecognizer
rec = KaldiRecognizer(MODEL, 16000)
# instancier pyaudio
mic = pyaudio.PyAudio()
stream = mic.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK
)
stream.start_stream()

# supprime message console alsa et autre
os.system("clear")

while True:
    # LIRE les donnée micro par vosk
    data = stream.read(CHUNK)
    if rec.AcceptWaveform(data):
        speak = json.loads(rec.Result())
        # user
        u = speak["text"]
        # pour enlever tout accent sinon bleme avec ascii et os
        u = unidecode.unidecode(u)
        print("==> :", u)

        if (
            os.system(
                'espeak -v mb-fr1 -s 110 -p 40 -g 0.2 -k 0.5 "{}"'.format(response())
            )
            in data
        ):
            stream = mic.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=0,
            )

        # MAJOR reponse
        print("Major : ", response())
