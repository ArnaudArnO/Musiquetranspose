from function  import note

def find_note_harmony(harmony):
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
    notes_accord = correspondances.get(harmony)

    if notes_accord:
        return notes_accord
    else:
        return []


# Find the Harmony from a note
def harmony_from_note(harmony):
    list_note = find_note_harmony(harmony)
    return note.convert_note_letter(list_note)



def harmony_to_gamme_blue(harmonys):
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

    for harmony in harmonys:
        notes_accord = correspondances.get(harmony)
        if notes_accord:
            gamme.extend(notes_accord)

    return gamme


