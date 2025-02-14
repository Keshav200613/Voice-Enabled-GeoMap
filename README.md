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

- [Demo Video 1](#) *(https://github.com/Keshav200613/Voice-Enabled-GeoMap/blob/main/Demo%20Videos/2025-02-14%2021-18-38.mov)*
- [Demo Video 2](#) *(https://github.com/Keshav200613/Voice-Enabled-GeoMap/blob/main/Demo%20Videos/2025-02-14%2021-20-18.mov)*
- [Demo Video 3](#) *(https://github.com/Keshav200613/Voice-Enabled-GeoMap/blob/main/Demo%20Videos/2025-02-14%2021-23-09.mov)*
- [Demo Video 4](#) *(https://github.com/Keshav200613/Voice-Enabled-GeoMap/blob/main/Demo%20Videos/2025-02-14%2021-50-44.mov)*

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

