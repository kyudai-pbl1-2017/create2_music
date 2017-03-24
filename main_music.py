# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2017, Kyushu University
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the Institute nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE INSTITUTE AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE INSTITUTE OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import sys
import os
import importlib

import music_controller

#======================================================================
if __name__ == '__main__':
    # 引数の数をチェック
    if len(sys.argv) < 2:
        print "Usage: python %s <notefile>" % sys.argv[0]
        quit()

    # 曲定義ファイルのパス
    note_base = sys.argv[1]
    # 曲定義ファイル名を分解
    note_path = os.path.dirname(note_base)
    note_file, note_ext = os.path.splitext(os.path.basename(note_base))

    # 曲定義ファイルのディレクトリをimport pathに追加
    sys.path.append(note_path)
    # 曲定義ファイルを読み込み
    try:
        note = importlib.import_module(note_file)
    except ImportError:
        sys.stderr.write("Cannot load note file.\n")
        quit()

    # create制御クラスをインスタンス化
    create = music_controller.MusicController()

    # 曲を定義
    create.DefineSong(note.note)
    # 曲を再生
    create.PlaySong()

    # インスタンスを破棄
    del create
