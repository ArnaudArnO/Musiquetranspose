# from termcolor import colored

# Fonction pour transposer une note
def transposer(note, intervalle):
    notes = ['do', 'do#', 'ré', 'ré#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']
    if note == "mib":
        note = "fa"
    if note == "sib":
        note = "la#"
    index = notes.index(note)
    nouvel_index = (index + intervalle) % len(notes)
    return notes[nouvel_index]


def transposer_list(list_note, intervalle):
    new_note = []
    for note in list_note:
        nouvelle_note = transposer(note, intervalle)
        new_note.append(nouvelle_note)
    return new_note


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


def obtenir_notes_accord(accord):
    correspondances = {
        'C': ['C', 'E', 'G'],
        'C#': ['C#', 'E#', 'G#'],
        'Db': ['Db', 'F', 'Ab'],
        'D': ['D', 'F#', 'A'],
        'D#': ['D#', 'Fx', 'A#'],
        'Eb': ['Eb', 'G', 'Bb'],
        'E': ['E', 'G#', 'B'],
        'F': ['F', 'A', 'C'],
        'F#': ['F#', 'A#', 'C#'],
        'Gb': ['Gb', 'Bb', 'Db'],
        'G': ['G', 'B', 'D'],
        'G#': ['G#', 'B#', 'D#'],
        'Ab': ['Ab', 'C', 'Eb'],
        'A': ['A', 'C#', 'E'],
        'A#': ['A#', 'Cx', 'E#'],
        'Bb': ['Bb', 'D', 'F'],
        'B': ['B', 'D#', 'F#'],
        'Cm': ['C', 'Eb', 'G'],
        'C#m': ['C#', 'E', 'G#'],
        'Dbm': ['Db', 'E', 'Ab'],
        'Dm': ['D', 'F', 'A'],
        'D#m': ['D#', 'F#', 'A#'],
        'Ebm': ['Eb', 'Gb', 'Bb'],
        'Em': ['E', 'G', 'B'],
        'Em7': ['E', 'G', 'B', 'D'],
        'Fm': ['F', 'Ab', 'C'],
        'F#m': ['F#', 'A', 'C#'],
        'Gbm': ['Gb', 'A', 'Db'],
        'Gm': ['G', 'Bb', 'D'],
        'G#m': ['G#', 'B', 'D#'],
        'Abm': ['Ab', 'B', 'Eb'],
        'Am': ['A', 'C', 'E'],
        'A#m': ['A#', 'C#', 'E#'],
        'Bbm': ['Bb', 'Db', 'F'],
        'Bm': ['B', 'D', 'F#'],
        'Bm7': ['B', 'D', 'F#', 'A'],
        'C7': ['C', 'E', 'G', 'Bb'],
        'C#7': ['C#', 'E#', 'G#', 'B'],
        'Db7': ['Db', 'F', 'Ab', 'Cb'],
        'D7': ['D', 'F#', 'A', 'C'],
        'D#7': ['D#', 'Fx', 'A#', 'C#'],
        'Eb7': ['Eb', 'G', 'Bb', 'Db'],
        'E7': ['E', 'G#', 'B', 'D'],
        'F7': ['F', 'A', 'C', 'Eb'],
        'F#7': ['F#', 'A#', 'C#', 'E'],
        'Gb7': ['Gb', 'Bb', 'Db', 'Fb'],
        'G7': ['G', 'B', 'D', 'F'],
        'G#7': ['G#', 'B#', 'D#', 'F#'],
        'Ab7': ['Ab', 'C', 'Eb', 'Gb'],
        'A7': ['A', 'C#', 'E', 'G'],
        'A#7': ['A#', 'Cx', 'E#', 'G#'],
        'Bb7': ['Bb', 'D', 'F', 'Ab'],
        'B7': ['B', 'D#', 'F#', 'A']
    }

    notes_accord = correspondances.get(accord)

    if notes_accord:
        return notes_accord
    else:
        return []


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


def accord_note(accord):
    list_note = obtenir_notes_accord(accord)
    # convertir_note_a_lettre(list_note)
    return convertir_note_a_lettre(list_note)


def change_accord_from_piano_to_sax(accord):
    return print(accord, "  : ", transposer_list(accord_note(accord), 3))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    # Gamme de départ (exemple avec la gamme de do majeur)
    gamme_do_majeur = ['do', 'ré', 'mi', 'fa', 'sol', 'la', 'si']
    #intervalle = int(input("Entrez l'intervalle de transposition en demi-tons (positif pour transposer vers le haut, négatif pour transposer vers le bas) : "))
    # Transposer la gamme
    print(transposer_gamme(gamme_do_majeur, 3))
    # Afficher la gamme transposée
    print("Gamme d'origine :", gamme_do_majeur)
    print("Gamme transposée :", gamme_transposee)

    accords_piano = ['C', 'F', 'G']
    print("accord piano : ",  accords_piano)
    gamme_saxophone = accords_piano_vers_gamme_saxophone(accords_piano)
    print("Gamme pour saxophone alto (Eb) :", gamme_saxophone)
    lettres = convertir_note_a_lettre(accords_piano, vers_note=False)
    print("Lettres correspondantes :", lettres)
    test= convertir_note_a_lettre(trouver_elements_doublons(convertir_accords_en_gamme_blue(accords_piano)))
    print ("note qui asse partout : ", test)
    print("Gamme que on peux jouer sur tout les accord : ", convertir_note_a_lettre(trouver_elements_doublons(convertir_accords_en_gamme_blue(accords_piano))),vers_note=False)
    for accord in accords_piano:
        print("accord piano : ", accord )
        print("gamme saxo (lettre) par rapport a accord piano : ", gamme_saxophone_alto_rapport_accord(accord))
        new_note=convertir_note_a_lettre(gamme_saxophone_alto_rapport_accord(accord))
        gamme_blues_note = convertir_note_a_lettre(convertir_accords_en_gamme_blue(accord))
        print("gamme saxo (note) par rapport a accord piano : ", new_note)
        print("gamme saxo blues (note) par rapport a accord piano : ", gamme_blues_note)

"""
    print("")
    ##All star Martin Solveig
    print("all Start martin solveig")
    print("")
    note_all_start = ['la', 'fa#', 'ré']
    note_all_start_2 = ['fa#', 'sol', 'la', 'ré']

    print(transposer_list(note_all_start, 3))
    print(transposer_list(note_all_start_2, 3))

    print("")
    # Love generation : Em C F
    print("Love generation Martin solveig")
    change_accord_from_piano_to_sax("Em")
    change_accord_from_piano_to_sax("C")
    change_accord_from_piano_to_sax("F")
    # Ha bellaire : Sim Sim7 Mim7 Sim7
    Simineur = ['si', 'ré', 'fa#']
    Simineur7 = ['si', 'ré', 'fa#', 'la']
    Mimineur7 = ['mi', 'sol', 'si', 'ré']
    print("ha bellaire")
    print("")
    change_accord_from_piano_to_sax("Bm")
    change_accord_from_piano_to_sax("Bm7")
    change_accord_from_piano_to_sax("Em7")
    change_accord_from_piano_to_sax("Bm7")
    print("")
    print("Simineur7", transposer_list(Simineur7, 3))
    print("Mimineur7", transposer_list(Mimineur7, 3))
    ## grey :
    # lamineur domineur lamineur
    print("")
    lamineur = ['la', 'do', 'mi']
    domineur = ['do', 'ré#', 'sol']
    print("Grey Kolch")
    print("")
    change_accord_from_piano_to_sax("Am")
    change_accord_from_piano_to_sax("Cm")
    print("")
    print("Mome Playground")
    print("")
    # accord si si maj7, si, simaj7, réb, mibm,
    # print(convertir_note_a_lettre(["si", "ré", "mi"], vers_note=True))
    change_accord_from_piano_to_sax("B")
    change_accord_from_piano_to_sax("Bm7")
    change_accord_from_piano_to_sax("D")
    change_accord_from_piano_to_sax("E")
    print("")
    print("Clef des champs")
    print("")
    ##sibm, fa, sib, fa, mib7
    sibmineur = ['la', 'do', 'mi']
    change_accord_from_piano_to_sax("Bbm")
    change_accord_from_piano_to_sax("F")
    change_accord_from_piano_to_sax("Eb7")
    print("")
    print("weekend miliardaire")
    print("")
    # Gm Cm F Eb
    change_accord_from_piano_to_sax("Gm")
    change_accord_from_piano_to_sax("Cm")
    change_accord_from_piano_to_sax("F")
    change_accord_from_piano_to_sax("Eb")