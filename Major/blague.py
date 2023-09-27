import random


def random_string():
    
            random_list=[
            "J'ai une blague sur les magasins, mais elle a pas, supermarché",
            "Pourquoi c'est difficile de conduire dans le Nord ? Parce que les voiture, arrêtent pas de caler.",
            "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont, Qu'un père.",
            "Pourquoi est-ce qu'on met tous les crocoo, en prison ? Parce que les crocos deale.",
            "Que faisaient les dinosaures quand ils n'arrivaient pas, à se décider? Des tirages aux zort ",
            "Qu'est-ce qu'un tennisman adore faire ? Rendre, des services ",
            "Que se passe-t-il quand 2 poissons, s'énervent ? Le thon monte ",
            "Quel fruit est assez fort pour couper, des arbres? Le ci-tron ",
            "Quel est le jambon, que tout le monde déteste ? Le sale, ami ",
            "Que fai un cendrier, devant un ascenseur ? Il veut, des cendres ",
            "Deux souris, voient passer une chauve-souris « Regarde, un ange ! »",
            "Les girafes, n'existent pas...C’est un cou monté",
            "Comment est-ce que les abeilles communiquent, entre elles ? Par i-miel ",
            "Quelle mamie fait peur au voleur ? Ma mitraillette."
            ]
        
        
            list_count = len(random_list)
            random_item = random.randrange(list_count)

            return random_list[random_item]

        

