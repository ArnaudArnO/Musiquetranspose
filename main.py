from termcolor import colored

# Fonction pour transposer une note
def transposer(note, intervalle):
    notes = ['do', 'do#', 'ré', 'ré#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']
    index = notes.index(note)
    nouvel_index = (index + intervalle) % len(notes)
    return notes[nouvel_index]

# Fonction pour transposer une gamme
def transposer_gamme(gamme, intervalle):
    nouvelle_gamme = []
    for note in gamme:
        nouvelle_note = transposer(note, intervalle)
        nouvelle_gamme.append(nouvelle_note)
    return nouvelle_gamme


def accords_piano_vers_gamme_saxophone(accords_piano):
    gamme_saxophone = []

    for accord in accords_piano:
        notes_accord = accord.split('/')
        notes_saxophone = []

        for note in notes_accord:
            if note == 'C':
                notes_saxophone.append('Eb')
            elif note == 'C#':
                notes_saxophone.append('E')
            elif note == 'Db':
                notes_saxophone.append('F')
            elif note == 'D':
                notes_saxophone.append('F#')
            elif note == 'D#':
                notes_saxophone.append('G')
            elif note == 'Eb':
                notes_saxophone.append('Ab')
            elif note == 'E':
                notes_saxophone.append('A')
            elif note == 'F':
                notes_saxophone.append('Bb')
            elif note == 'F#':
                notes_saxophone.append('B')
            elif note == 'Gb':
                notes_saxophone.append('C')
            elif note == 'G':
                notes_saxophone.append('C#')
            elif note == 'G#':
                notes_saxophone.append('D')
            elif note == 'Ab':
                notes_saxophone.append('Eb')
            elif note == 'A':
                notes_saxophone.append('E')
            elif note == 'A#':
                notes_saxophone.append('F')
            elif note == 'Bb':
                notes_saxophone.append('Gb')
            elif note == 'B':
                notes_saxophone.append('G')

        gamme_saxophone.append('/'.join(notes_saxophone))

    return gamme_saxophone


def lettres_vers_notes(lettres):
    correspondances = {
        'do': 'C',
        'do#': 'C#',
        'ré': 'D',
        'ré#': 'D#',
        'mi': 'E',
        'fa': 'F',
        'fa#': 'F#',
        'sol': 'G',
        'sol#': 'G#',
        'la': 'A',
        'la#': 'A#',
        'si': 'B'
    }

    notes = []

    for lettre in lettres:
        note = correspondances.get(lettre.lower())
        if note:
            notes.append(note)

    return notes


def convertir_note_a_lettre(musique, vers_note=False):
    correspondances = {
        'lab': 'Ab',
        'la': 'A',
        'la#': 'A#',
        'sib': 'Bb',
        'si': 'B',
        'do': 'C',
        'do#': 'C#',
        'ré': 'D',
        'ré#': 'D#',
        'mib': 'Eb',
        'mi': 'E',
        'fa': 'F',
        'fa#': 'F#',
        'sol': 'G',
        'sol#': 'G#'
    }

    resultat = []

    for element in musique:
        if vers_note:
            note = correspondances.get(element.lower())
            if note:
                resultat.append(note)
        else:
            lettre = next((k for k, v in correspondances.items() if v.lower() == element.lower()), None)
            if lettre:
                resultat.append(lettre)

    return resultat


def gamme_saxophone_alto_rapport_accord(note_accord):
    correspondances = {
        'C': ['Eb', 'F', 'G', 'Ab', 'Bb'],
        'C#': ['E', 'F#', 'G#', 'A', 'B'],
        'Db': ['E', 'F', 'G', 'Ab', 'Bb'],
        'D': ['F', 'G', 'A', 'Bb', 'C'],
        'D#': ['F#', 'G#', 'A#', 'B', 'C#'],
        'Eb': ['G', 'Ab', 'Bb', 'C', 'D'],
        'E': ['G#', 'A', 'B', 'C#', 'D#'],
        'F': ['A', 'Bb', 'C', 'D', 'E'],
        'F#': ['A#', 'B', 'C#', 'D#', 'F'],
        'Gb': ['A', 'Bb', 'C', 'Db', 'E'],
        'G': ['Bb', 'C', 'D', 'Eb', 'F'],
        'G#': ['B', 'C#', 'D#', 'E', 'F#'],
        'Ab': ['B', 'Db', 'Eb', 'F', 'G'],
        'A': ['C', 'D', 'E', 'F', 'G'],
        'A#': ['C#', 'D#', 'F', 'F#', 'G#'],
        'Bb': ['D', 'Eb', 'F', 'G', 'A'],
        'B': ['D#', 'E', 'F#', 'G#', 'A#']
    }

    gamme = correspondances.get(note_accord)
    return gamme


def convertir_accords_en_gamme_blue(accords):
    correspondances = {
        'C': ['C', 'Eb', 'F', 'F#', 'G', 'Bb', 'C'],
        'C#': ['C#', 'E', 'F#', 'G', 'G#', 'B', 'C#'],
        'Db': ['Db', 'E', 'F#', 'G', 'Ab', 'B', 'Db'],
        'D': ['D', 'F', 'G', 'G#', 'A', 'C', 'D'],
        'D#': ['D#', 'F#', 'G#', 'A', 'A#', 'C#', 'D#'],
        'Eb': ['Eb', 'Gb', 'Ab', 'A', 'Bb', 'Db', 'Eb'],
        'E': ['E', 'G', 'A', 'A#', 'B', 'D', 'E'],
        'F': ['F', 'Ab', 'Bb', 'B', 'C', 'Eb', 'F'],
        'F#': ['F#', 'A', 'B', 'C', 'C#', 'E', 'F#'],
        'Gb': ['Gb', 'A', 'B', 'C', 'Db', 'E', 'Gb'],
        'G': ['G', 'Bb', 'C', 'C#', 'D', 'F', 'G'],
        'G#': ['G#', 'B', 'C#', 'D', 'D#', 'F#', 'G#'],
        'Ab': ['Ab', 'B', 'C#', 'D', 'Eb', 'F#', 'Ab'],
        'A': ['A', 'C', 'D', 'D#', 'E', 'G', 'A'],
        'A#': ['A#', 'C#', 'D#', 'E', 'F', 'G#', 'A#'],
        'Bb': ['Bb', 'Db', 'Eb', 'E', 'F', 'Ab', 'Bb'],
        'B': ['B', 'D', 'E', 'F', 'F#', 'A', 'B']
    }

    gamme = []

    for accord in accords:
        notes_accord = correspondances.get(accord)
        if notes_accord:
            gamme.extend(notes_accord)

    return gamme


def convertir_accords_en_gamme_minreur__setieme(accords):
    correspondances = {
        'C': ['C', 'Eb', 'F', 'F#', 'G', 'Bb', 'C'],
        'C#': ['C#', 'E', 'F#', 'G', 'G#', 'B', 'C#'],
        'Db': ['Db', 'E', 'F#', 'G', 'Ab', 'B', 'Db'],
        'D': ['D', 'F', 'G', 'G#', 'A', 'C', 'D'],
        'D#': ['D#', 'F#', 'G#', 'A', 'A#', 'C#', 'D#'],
        'Eb': ['Eb', 'Gb', 'Ab', 'A', 'Bb', 'Db', 'Eb'],
        'E': ['E', 'G', 'A', 'A#', 'B', 'D', 'E'],
        'F': ['F', 'Ab', 'Bb', 'B', 'C', 'Eb', 'F'],
        'F#': ['F#', 'A', 'B', 'C', 'C#', 'E', 'F#'],
        'Gb': ['Gb', 'A', 'B', 'C', 'Db', 'E', 'Gb'],
        'G': ['G', 'Bb', 'C', 'C#', 'D', 'F', 'G'],
        'G#': ['G#', 'B', 'C#', 'D', 'D#', 'F#', 'G#'],
        'Ab': ['Ab', 'B', 'C#', 'D', 'Eb', 'F#', 'Ab'],
        'A': ['A', 'C', 'D', 'D#', 'E', 'G', 'A'],
        'A#': ['A#', 'C#', 'D#', 'E', 'F', 'G#', 'A#'],
        'Bb': ['Bb', 'Db', 'Eb', 'E', 'F', 'Ab', 'Bb'],
        'B': ['B', 'D', 'E', 'F', 'F#', 'A', 'B']
    }

    gamme = []

    for accord in accords:
        if accord.endswith('m'):
            accord_base = accord[:-1]
            notes_accord = correspondances.get(accord_base)
            if notes_accord:
                gamme.extend([notes_accord[0], notes_accord[2], notes_accord[3], notes_accord[4], notes_accord[6]])
        elif accord.endswith('7'):
            accord_base = accord[:-1]
            notes_accord = correspondances.get(accord_base)
            if notes_accord:
                gamme.extend([notes_accord[0], notes_accord[2], notes_accord[3], notes_accord[4], notes_accord[6]])
                gamme.append(notes_accord[1])
        else:
            notes_accord = correspondances.get(accord)
            if notes_accord:
                gamme.extend(notes_accord)

    return gamme


def trouver_elements_doublons(lst):
    elements_doublons = []
    occurrences = {}

    # Compter le nombre d'occurrences de chaque élément
    for element in lst:
        occurrences[element] = occurrences.get(element, 0) + 1

    # Garder seulement les éléments en double ou plus
    for element, count in occurrences.items():
        if count >= 2:
            elements_doublons.append(element)

    return elements_doublons


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Gamme de départ (exemple avec la gamme de do majeur)
    gamme_do_majeur = ['do', 'ré', 'mi', 'fa', 'sol', 'la', 'si']
    #intervalle = int(input("Entrez l'intervalle de transposition en demi-tons (positif pour transposer vers le haut, négatif pour transposer vers le bas) : "))
    # Transposer la gamme
    #gamme_transposee = transposer_gamme(gamme_do_majeur, intervalle)
    # Afficher la gamme transposée
    #print("Gamme d'origine :", gamme_do_majeur)
    #print("Gamme transposée :", gamme_transposee)

    accords_piano = ['C', 'F', 'G']
    print("accord piano : ",  accords_piano)
    #gamme_saxophone = accords_piano_vers_gamme_saxophone(accords_piano)
    #print("Gamme pour saxophone alto (Eb) :", gamme_saxophone)
    #lettres = convertir_note_a_lettre(accords_piano, vers_note=False)
    #print("Lettres correspondantes :", lettres)
    test= convertir_note_a_lettre(trouver_elements_doublons(convertir_accords_en_gamme_blue(accords_piano)))
    print ("note qui asse partout : ", test)
    #print("Gamme que on peux jouer sur tout les accord : ", convertir_note_a_lettre(trouver_elements_doublons(convertir_accords_en_gamme_blue(accords_piano))),vers_note=False)
    for accord in accords_piano:
        print("accord piano : ", accord )
        print("gamme saxo (lettre) par rapport a accord piano : ", gamme_saxophone_alto_rapport_accord(accord))
        new_note=convertir_note_a_lettre(gamme_saxophone_alto_rapport_accord(accord))
        gamme_blues_note = convertir_note_a_lettre(convertir_accords_en_gamme_blue(accord))
        print("gamme saxo (note) par rapport a accord piano : ", new_note)
        print("gamme saxo blues (note) par rapport a accord piano : ", gamme_blues_note)
