#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow the GNU GPL, see:
# http://www.gnu.org/licenses
#
#
# Transliteration Function
# (c) Harijaona Ravelondrina 2022

__author__ = "Harijaona Ravelondrina"
__license__ = "GPL3"
__version__ = "0.1"

from mrz_trans.dictionaries.latin_based import transliteration as latin_based

def transliterate(string: str, dictionary: dict = latin_based, sep="<") -> str:
    """
    >>> from mrz_trans.dictionaries.cyrillic_serbian import transliteration as serbian
    >>> from mrz_trans.dictionaries.latin_based import transliteration as latin_based
    >>> from mrz_trans.dictionaries.arabic import transliteration as arabic
    >>> from mrz_trans.dictionaries.greek import transliteration as greek
    >>> transliterate("ТЕСТ МИЛИЦА", serbian)
    'TEST<MILICA'
    >>> transliterate("Þĩŝ ïŜ Á ţęšť", latin_based, " ")
    'THIS IS A TEST'
    >>> transliterate("محمود عبدالرحيم", arabic, "-")
    'MXHMWD-EBDALRXHYM'
    >>> transliterate("παράδειγμα δοκιμής", greek)
    'PAPADEIGMA<DOKIMIS'
    """
    word = string.replace(u"\u002D", u"\u0020").split(u"\u0020")
    for i in range(len(word)):
        final_word = ""
        for char in word[i]:
            final_word += dictionary[char] if char in dictionary else char
        word[i] = final_word.upper()
    return sep.join(word)
