# from termcolor import colored
from function import transpose as tp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("")
    ##All star Martin Solveig
    print("All Start Martin Solveig")
    note_all_start = ['la', 'fa#', 'ré']
    note_all_start_2 = ['fa#', 'sol', 'la', 'ré']

    print(tp.transpose_list(note_all_start, 3))
    print(tp.transpose_list(note_all_start_2, 3))

    print("")
    # Love generation : Em C F
    print("Love generation Martin solveig")
    tp.change_harmony_from_piano_to_sax("Em")
    tp.change_harmony_from_piano_to_sax("C")
    tp.change_harmony_from_piano_to_sax("F")
    # Ha bellaire : Sim Sim7 Mim7 Sim7
    print("")
    print("Ha Bellaire")
    tp.change_harmony_from_piano_to_sax("Bm")
    tp.change_harmony_from_piano_to_sax("Bm7")
    tp.change_harmony_from_piano_to_sax("Em7")
    tp.change_harmony_from_piano_to_sax("Bm7")
    print("")


    ## grey :
    # lamineur domineur lamineur
    print("")
    print("Grey Kolch")
    tp.change_harmony_from_piano_to_sax("Am")
    tp.change_harmony_from_piano_to_sax("Cm")
    print("")

    print("Mome Playground")
    # accord si si maj7, si, simaj7, réb, mibm,
    tp.change_harmony_from_piano_to_sax("B")
    tp.change_harmony_from_piano_to_sax("Bm7")
    tp.change_harmony_from_piano_to_sax("D")
    tp.change_harmony_from_piano_to_sax("E")

    print("")
    print("Clef Des Champs")
    ##sibm, fa, sib, fa, mib7
    tp.change_harmony_from_piano_to_sax("Bbm")
    tp.change_harmony_from_piano_to_sax("F")
    tp.change_harmony_from_piano_to_sax("Eb7")

    print("")
    print("Weekend Miliardaire")
    # Gm Cm F Eb
    tp.change_harmony_from_piano_to_sax("Gm")
    tp.change_harmony_from_piano_to_sax("Cm")
    tp.change_harmony_from_piano_to_sax("F")
    tp.change_harmony_from_piano_to_sax("Eb")