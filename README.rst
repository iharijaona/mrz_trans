MRZ Text transliteration
===========================

.. code:: python

   from mrz_trans import transliterate

   name_out = transliterate("ÔSPELT BÉCK MARÏSA", sep='<<')

   print(name_out)

.. _output-2:

Output
''''''

::

   OSPELT<<BECK<<MARISA                                                                                                                                                                    

Installation:
-------------
::

   pip install git+https://github.com/iharijaona/mrz_trans.git

Features:
---------

-  [x] Transliteration of special Latin characters (acutes, tildes,
   diaeresis, graves, circumflex, etc)
-  [x] Arabic chars transliteration
-  [x] Several variations of Cyrillic added: Serbian, Macedonian,
   Belarusian, Ukrainian and Bulgarian
-  [x] Transliteration of modern Greek (experimental)
-  [x] Transliteration of modern Hebrew (without vowels) (experimental)