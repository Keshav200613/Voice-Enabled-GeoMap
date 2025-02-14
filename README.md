# Voice-Enabled GeoMap





## Overview

Voice-Enabled GeoMap is a lightweight and scalable voice-enabled user interface for geospatial map-based web applications. It is designed to operate efficiently with local GPU/NPU processing, avoiding reliance on online libraries. This project integrates speech recognition and geospatial data visualization for an intuitive user experience.

## Features

- 🎙️ **Voice Commands:** Navigate and interact with maps using natural language.
- ⚡ **Local Processing:** Runs on local hardware, leveraging GPU/NPU for performance.
- 🛠 **Lightweight & Scalable:** Designed for efficiency without heavy dependencies.
- 📡 **Customizable:** Easily extendable for different geospatial datasets and voice commands.

## Technologies Used

- **Frontend:** JavaScript, HTML, CSS
- **Speech Recognition:** Vosk Speech Recognition Model
- **Natural Language Processing:** Ollama and Mistral
- **Map Rendering:** Leaflet.js / OpenLayers
- **Backend:** FastAPI (api.py)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Keshav200613/Voice-Enabled-GeoMap.git
   cd Voice-Enabled-GeoMap
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # Install FastAPI and dependencies
   ```
3. Download and set up the Vosk model:
   ```bash
      wget https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip
   unzip vosk-model-en-in-0.5.zip
   ```
4. Install and set up Ollama and Mistral:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh  # Install Ollama
   ollama pull mistral  # Download Mistral model
   ```
5. Run the backend:
   ```bash
   uvicorn api:app
   ```
6. Open the frontend:
   - Open `index.html` in your browser.

## Demo Videos

🎥 **Watch it in action:**

[![Video Title](https://img.youtube.com/vi/geEBGBHT-r0/0.jpg)](https://www.youtube.com/watch?v=geEBGBHT-r0)
[![Video Title](https://img.youtube.com/vi/FsEB-3UtN8U/0.jpg)](https://youtu.be/FsEB-3UtN8U)
[![Video Title](https://img.youtube.com/vi/3ZiWlUfCDNI/0.jpg)](https://youtu.be/3ZiWlUfCDNI)
[![Video Title](https://img.youtube.com/vi/Olz5T_2WWP0/0.jpg)](https://youtu.be/Olz5T_2WWP0)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to your fork (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:

- **GitHub Issues:** [Submit a new issue](https://github.com/Keshav200613/Voice-Enabled-GeoMap/issues)
- **Email:** [your-email@example.com](mailto\:your-email@example.com)

---

### 🚀 Star this repository if you find it useful!

