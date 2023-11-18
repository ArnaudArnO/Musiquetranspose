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



def convertir_accords_en_gamme_minreur(accords):
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