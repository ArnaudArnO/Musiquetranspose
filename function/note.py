def convert_note_letter(musique, vers_note=False):
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

    result = []

    for element in musique:
        if vers_note:
            note = correspondances.get(element.lower())
            if note:
                result.append(note)
        else:
            letter = next((k for k, v in correspondances.items() if v.lower() == element.lower()), None)
            if letter:
                result.append(letter)

    return result