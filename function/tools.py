def find_duplicate_element(lst):
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