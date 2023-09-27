import blague
import random_responses
import datetime
import time
import locale
import random
import json

# pour racine des mots
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup as bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import pyaudio

# retirer les log de chargement dans terminal
from vosk import SetLogLevel, KaldiRecognizer, Model

SetLogLevel(-1)


def get_response():
    # des blagues
    if "une blague" in speak["text"] or "une autre" in speak["text"]:
        return blague.random_string()

    elif "c'était pas marrant" in speak["text"]:
        return "Je ne l'ai pas inventé"

    # recherche net
    elif (
        speak["text"] == "recherche dans google"
        or speak["text"] == "google"
        or speak["text"] == "recherche google"
        or speak["text"] == "va sur google"
    ):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.find_element(By.ID, "L2AGLb").click()
        while driver:
            print("Que recherches tu ?")
            os.system(
                'espeak -v mb-fr1 -s 120 -p 40 -g 0.2 -k 0.5 "Que recherches tu ?"'
            )
            use = input("=>")
            if "ferme la page" in use or "ferme page" in use:
                driver.quit()
                break
            # recuperer la barre de recherche
            search = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
            search.clear()
            # très important laisse le tps de recherche entre mot et enter
            search.send_keys(use)
            time.sleep(2)
            search.send_keys(Keys.RETURN)

    # stopper le pgm
    elif (
        "au revoir" in speak["text"]
        or "a bientot" in speak["text"]
        or speak["text"] == "stop"
    ):
        mic.terminate()
        return "A bientôt."

    elif speak["text"] == "":
        mic.terminate()
        return "A toute."

    # si ce n'est pas la bonne reponse
    elif get_response != 0:
        return random_responses.random_string()


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

while True:
    data = stream.read(CHUNK)
    if rec.AcceptWaveform(data):
        speak = json.loads(rec.Result())
        print("==> :", speak["text"])

        # reponse de Major
        print("Major : ", get_response())
        if (
            os.system(
                'espeak -v mb-fr1 -s 120 -p 40 -g 0.2 -k 0.5 "{}"'.format(
                    get_response()
                )
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
