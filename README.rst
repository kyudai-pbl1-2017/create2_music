.. -*- coding: utf-8; -*-

===============================
 iRobot Create2 曲再生サンプル
===============================

`libcreate2py <https://github.com/s-hosoai/libcreate2py/>`_ を用いてiRobot Create2で曲を定義・再生するサンプルプログラムです。

Required Libraries
==================

* `libcreate2py <https://github.com/s-hosoai/libcreate2py/>`_

  * pipで導入できます。

Usage
=====

* 曲定義ファイルを用意します。

.. code-block:: python

   note = [
       ["C4", 32],
       ["D4", 32],
       ["E4", 32],
       ["F4", 32],
       ["G4", 32],
       ["F4", 32],
       ["E4", 32],
       ["D4", 32],
       ["C4", 32],
       ]

* ``python main_music.py note_doremi.py`` のように曲定義ファイルを指定して実行します。

Limitations
===========

NOT TESTED YET!

Copyright, License
==================

Copyright (c) 2015-2017, Kyushu University

This software is released under the BSD 3-clause license. See ``LICENSE``.
