# -*- coding: utf-8 -*-
import sys
import requests
import json
import winsound

# VoiceVoxで喋る
def talk(filename):
    winsound.PlaySound(filename,  winsound.SND_MEMORY)

def audio_query(text,  speaker):
    query_payload = {"text": text, "speaker": speaker}
    try:
            r = requests.post("http://localhost:50021/audio_query", 
                    params=query_payload, timeout=(1.0, 7.5))
            if r.status_code == 200:
                query_data = r.json()
            synth_payload = {"speaker": speaker}    
            r = requests.post("http://localhost:50021/synthesis", params=synth_payload, 
                              data=json.dumps(query_data), timeout=(1.0, 7.5))
            if r.status_code == 200:
                talk( r.content)
    except:
        print ("なんかエラーだって")
        sys.exit(-1)

def main():
    speaker = 0
    removes = 1
    if len(sys.argv) > 1:
        text = sys.argv[1]
        if(len(sys.argv)>2):
            speaker = sys.argv[2]
        audio_query(text,speaker)

if __name__ == '__main__':
    main()
    sys.exit()
