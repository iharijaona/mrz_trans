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

   pip install mrz_trans 

Cloning this repo (It may not work fine):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   git clone https://github.com/iharijaona/mrz_trans.git
   cd mrz_trans
   sudo python3 setup.py install

Features:
---------

-  [x] Transliteration of special Latin characters (acutes, tildes,
   diaeresis, graves, circumflex, etc)
-  [x] Arabic chars transliteration
-  [x] Several variations of Cyrillic added: Serbian, Macedonian,
   Belarusian, Ukrainian and Bulgarian
-  [x] Transliteration of modern Greek (experimental)
-  [x] Transliteration of modern Hebrew (without vowels) (experimental)