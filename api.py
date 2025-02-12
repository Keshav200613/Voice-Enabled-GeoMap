from fastapi import FastAPI
import subprocess
import vosk
import json
import sounddevice as sd
import numpy as np
import wave
import os
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import requests


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = os.path.abspath("./vosk-model-en-in-0-2.5")
AUDIO_FILE = "./temp.wav"
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "mistral"  

def record_audio(duration=5, samplerate=16000):
    """Records audio and saves it as a .wav file."""
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    
    with wave.open(AUDIO_FILE, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    
    print("Recording saved.")
def deepseek(text):
    payload = {
        "model": MODEL,
        "prompt": text,
        "stream": False
    }
    
    response = requests.post(OLLAMA_API, json=payload)
    
    if response.status_code == 200:
        print(response.json().get("response", "No response received."));
        return response.json().get("response", "No response received.")
    else:
        
        return f"Error: {response.status_code}, {response.text}"


async def transcribe_audio():
    wf = wave.open(AUDIO_FILE, "rb")
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, 16000)
    rec.SetWords(True)
    text_lst =[]
    p_text_lst = []
    p_str = []
    len_p_str = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            text_lst.append(rec.Result())
        else:
            p_text_lst.append(rec.PartialResult())

    if len(text_lst) !=0:
        jd = json.loads(text_lst[0])
        txt_str = jd["text"]
        
    elif len(p_text_lst) !=0: 
        for i in range(0,len(p_text_lst)):
            temp_txt_dict = json.loads(p_text_lst[i])
            p_str.append(temp_txt_dict['partial'])
       
        len_p_str = [len(p_str[j]) for j in range(0,len(p_str))]
        max_val = max(len_p_str)
        indx = len_p_str.index(max_val)
        txt_str = p_str[indx]
            
    else:
        txt_str =''

    return deepseek("don't spend much time thinking. answer fast. answer format: distance(if applicable) ,coordinates(in degrees). question: "+txt_str)


@app.post("/transcribe")
async def transcribe():
    record_audio()
    result = await transcribe_audio()
    os.remove(AUDIO_FILE)
    return {"text": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




