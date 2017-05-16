# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from nltk.corpus import stopwords
import collections
import math
import os
import random
import zipfile
import io

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

import os


def ayristir(path):
    dirList = os.listdir(path)
    dirList.sort()
    fnames = []
    fpath = []
    dnames = []
    dpath = []
    for fname in dirList:
        if os.path.isdir(path + fname):
            dnames.append(path + fname + '/')
        if os.path.isfile(path + fname):
            fnames.append(path + fname)
    return dnames, fnames


def read_text(filename):
    # Extract the first file enclosed in a zip file as a list of words
    with open(filename, 'r', encoding='utf-8') as f:
        data = tf.compat.as_str(f.read(), 'utf-8').split()
    return data


def read_text2(filename):
    # Extract the first file enclosed in a zip file as a list of words
    with open(filename, 'r', encoding='utf-8') as f:
        data = tf.compat.as_str(f.read(), 'utf-8')
    return data


def write_text(filename, text):
    data = stopwords_remove(text)
    # Extract the first file enclosed in a zip file as a list of words
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


def listele(dir):
    (klasorler, dosyalar) = ayristir(dir)
    for dir in klasorler:
        print(" 109 Directory   => " + dir)
        (klasorler, dosyalar) = ayristir(dir)
        for item in dosyalar:
            print(" 113 File => " + item)
            # text = read_text2(dir + item)
            text = read_text2(item)
            write_text(item, text)


def stopwords_remove(sentence):
    stop = set(stopwords.words('turkish'))
    data = ''
    # sentence = "o ve ali bir asker"
    for i in sentence.lower().split():
        if i not in stop:
            # print(i)
            data += ' ' + i
    return data


# dir = "news/"
# listele(dir)

BHARFX = "Iİ"
KHARFX = "ıi"
# AYRACLAR = ",\.;«»!?-:/\*+_=\"<>()'[]|º#&%“’”‘…–´—•`˜·"
NOKTALAMA = list("\"\'\.,/\\&%\+!\*/=(){}[]-_–:;?«»<>|^—¦")
RAKAMLAR = list("0123456789.,")


def noktalama_yok(kelime):
    s = [h if h not in NOKTALAMA else ' ' for h in kelime]
    s = ''.join(s)
    # Eğer kelimede boşluk varsa, sonrasını at
    s = s.strip()
    p = s.find(' ')
    if p > 0:
        s = s[:p]
    return s


def rakam_yok(kelime):
    s = [h for h in kelime if h not in RAKAMLAR]
    return "".join(s)


def kucukHarfYap(sozcuk):
    ss = ''
    for i in range(len(sozcuk)):
        ok = False
        for j in range(len(BHARFX)):
            if sozcuk[i] == BHARFX[j]:
                ss += KHARFX[j]
                ok = True
                break
        if ok == False:
            ss += sozcuk[i]
    ss = ss.lower()
    return ss


def inceltme_harf(harf):
    """ inceltme yok fonksiyonu sadeleştirmesi"""
    harfler = {'â': 'a', 'Â': 'a', 'ê': 'e', 'Ê': 'e',
               'û': 'u', 'Û': 'u', 'î': 'i', 'Î': 'i'}
    return harfler[harf] if harf in harfler else harf


def inceltme_yok(sozcuk):
    s = [inceltme_harf(harf) for harf in sozcuk]
    return "".join(s)


def kelimelerine_ayir(metin):
    hamliste = metin.split()
    hamliste = list(map(noktalama_yok, hamliste))
    hamliste = list(map(rakam_yok, hamliste))
    hamliste = list(map(inceltme_yok, hamliste))
    hamliste = list(map(kucukHarfYap, hamliste))
    return hamliste


if __name__ == "__main__":
    metin = '''
    MERHABAlar. merhaba dunya
    '''
    dir = '/home/diablo/Documents/ClassificationSummarization/test/'
    print(listele(dir))
    # liste = set(kelimelerine_ayir(metin))
    # liste = kelimelerine_ayir(met/home/diablo/Documents/ClassificationSummarization/in)/home/diablo/Documents/ClassificationSummarization/

    # print(liste)
