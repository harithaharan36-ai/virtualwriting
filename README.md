# Virtual Air Writing AI

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)

Virtual Air Writing AI is a production-quality desktop application that allows users to write in the air using only their index finger and a webcam. It leverages computer vision and deep learning to track hand movements, recognize gestures, draw on a virtual canvas, and convert hand-drawn text into digital format using OCR.

## 🚀 Features

- **Real-time Hand Tracking**: Powered by MediaPipe for high-precision 21-point landmark detection.
- **Gesture-based Control**: 
  - ☝️ **Index Finger**: Draw on canvas.
  - ✌️ **Two Fingers**: Pause/Resume.
  - 🖐️ **Open Palm**: Clear canvas.
  - 👍 **Thumb Up**: Save progress.
- **Smart OCR**: Integrated EasyOCR for recognizing handwritten text.
- **Multi-format Export**: Save as TXT, DOCX, PDF, or Image.
- **Voice Synthesis**: Read recognized text aloud using Pyttsx3.
- **Modern GUI**: Built with Tkinter featuring Dark/Light modes and real-time statistics.

## 🛠️ Technology Stack

- **OpenCV**: Image processing and webcam handling.
- **MediaPipe**: Hand tracking and landmark detection.
- **EasyOCR**: Optical Character Recognition for handwriting.
- **Pyttsx3**: Text-to-speech engine.
- **Tkinter**: Graphical User Interface.
- **Pillow**: Image manipulation.
- **ReportLab/python-docx**: Document generation.

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Virtual-Air-Writing.git
   cd Virtual-Air-Writing
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## ⌨️ Keyboard Shortcuts

- `Ctrl+S`: Save
- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo
- `Ctrl+N`: New/Clear
- `Ctrl+Q`: Exit

## 📂 Project Structure

```text
Virtual-Air-Writing/
├── src/                # Source code
│   ├── camera.py       # Webcam management
│   ├── hand_tracker.py # MediaPipe integration
│   ├── gesture.py      # Gesture logic
│   ├── drawing.py      # Canvas & strokes
│   ├── ocr.py          # OCR management
│   ├── voice.py        # TTS engine
│   └── gui.py          # Main interface
├── docs/               # Documentation
├── tests/              # Unit tests
├── output/             # Saved notes and images
└── main.py             # Entry point
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
