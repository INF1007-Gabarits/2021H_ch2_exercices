#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouveau_mot = ""
    for lettre in mot:
        if 97 <= ord(lettre) <= 122 or 224 <= ord(lettre) <= 246:
            nouveau_mot += chr(ord(lettre) - 32)
        else:
            nouveau_mot += lettre

    return nouveau_mot




if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre',
        'yolo'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
