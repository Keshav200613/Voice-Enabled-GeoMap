import requests
import vosk
import wave

# Define Ollama API Endpoint
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:8b"  # Use DeepSeek model

def deepseek(text):
    payload = {
        "model": MODEL,
        "prompt": text,
        "stream": False
    }
    
    response = requests.post(OLLAMA_API, json=payload)
    
    if response.status_code == 200:
        return response.json().get("response", "No response received.")
    else:
        return f"Error: {response.status_code}, {response.text}"

print(deepseek("answer in one number. What is the distance between delhi and mumbai "))
