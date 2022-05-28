# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import winsound
from datetime import datetime
from multiprocessing import Process
import os

# VoiceVoxで喋る及びファイルに出力
def talk(filename):
    winsound.PlaySound(filename,  winsound.SND_FILENAME)

def audio_query(text, filename, speaker, removes):
    query_payload = {"text": text, "speaker": speaker}
    try:
            r = requests.post("http://localhost:50021/audio_query", 
                    params=query_payload, timeout=(3.0, 7.5))
            if r.status_code == 200:
                query_data = r.json()
            synth_payload = {"speaker": speaker}    
            r = requests.post("http://localhost:50021/synthesis", params=synth_payload, 
                              data=json.dumps(query_data), timeout=(3.0, 7.5))
            if r.status_code == 200:
                with open(filename, "wb") as fp:
                     fp.write(r.content)
                talk(filename)
                if(removes==1):
                    os.remove(filename)
    except:
        print ("なんかエラーだって")
        sys.exit(-1)

def main():
    speaker = 1
    removes = 1
    if len(sys.argv) > 1:
        text = sys.argv[1]
        if(len(sys.argv)>2):
            speaker = sys.argv[2]
            if(len(sys.argv)>3):
                removes = sys.argv[3]
        filename = str(datetime.now().strftime('temp%Y%m%dT%H%M%S_%f')+".wav")
        audio_query(text,filename,speaker,removes)

if __name__ == '__main__':
    main()
    sys.exit()

