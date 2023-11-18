from function import harmony as hy
from function import note

# Transpose One Note
def transpose(note, interval):
    notes = ['do', 'do#', 'ré', 'ré#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']
    if note == "mib":
        note = "fa"
    if note == "sib":
        note = "la#"
    index = notes.index(note)
    new_index = (index + interval) % len(notes)
    return notes[new_index]

# Transpose List of Note
def transpose_list(list_note, interval):
    new_notes = []
    for note in list_note:
        new_note = transpose(note, interval)
        new_notes.append(new_note)
    return new_notes


def change_harmony_from_piano_to_sax(harmony):
    return print("Piano [", harmony, "]  : ", transpose_list(hy.harmony_from_note(harmony), 3), "     Sax ", note.convert_note_letter(transpose_list(
        note.convert_note_letter(harmony), 3), vers_note=True))