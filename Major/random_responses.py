import random


# création d'une def pour toute questons non comprises
def random_string():
    random_list = [
        "Qui me parle",
        "c'est toi qui parle ?",
        "J'ai pas compris",
        "Peux-tu, répéter ?",
        "Toi pas parler très bien",
        "Tu me parle ?",
        "Quoi...!?",
        "Parle plus fort je suis vieux",
        "Parle, Humain.",
        "j'ai L'impréssion de parler seul",
        "tu m'a parlé ?",
        "Sujet, verbe, complément, connaard !.",
        "Je ne comprend pas",
        "Tu as dit quoi ?!",
        "Comment !",
        "Plait-il ?",
        "Tu peux répéter ?!",
        "Répète s'il te plait.",
        "qu'est ce que tu as dit",
        "Moi pas comprendre",
        "A qui tu parle ?",
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
