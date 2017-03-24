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

import create2.create2

#======================================================================
class MusicController():
    def __init__(self, create=None):
        self.create = create
        if self.create is None:
            self.create = create2.create2.Create2()
        return

    #--------------------------------------------------
    def DefineSong(self, notes, song_num=0):
        # notes: 音程と長さのリスト[["A4", 8], ["A4", 8]]

        # 曲番号，音符の個数
        bytes = [song_num, len(notes)]

        # 音程データを変換
        for note in notes:
            freq, length = note
            bytes.extend([create2.opcode.MIDI_TABLE[freq], length])

        # send to create2
        self.create.opcode.song(bytes)
        
        return

    #--------------------------------------------------
    def PlaySong(self, song_num=0):
        self.create.opcode.play(song_num)
        return
