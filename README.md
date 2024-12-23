# QR Code Generator

## Overview
The **Apple-Style QR Code Generator** is a Python-based application designed to create visually appealing QR codes with customizable options such as error correction levels, colors, embedded logos, and more. This application provides a modern and intuitive graphical user interface (GUI) styled after Apple's design principles.

---

## Features
- **Customizable Content**: Enter any text, URL, or data to encode into a QR code.
- **Error Correction Levels**: Choose from Low (L), Medium (M), Quality (Q), or High (H) levels.
- **Customizable Appearance**:
  - Foreground and background colors.
  - Embedded logos for branding.
- **Version Selection**: Automatically choose the best QR code version or specify a version (1 to 40).
- **Preview in Real-Time**: See the QR code before saving.
- **Save QR Codes**: Export the generated QR code as a PNG image.
- **Responsive UI**: Optimized for macOS and other operating systems.

---

## Prerequisites
### Python Requirements
Ensure you have the following installed:
- **Python 3.7+**
- Required libraries:
  - `tkinter` (comes pre-installed with Python)
  - `Pillow`
  - `segno`

To install the required libraries, run:
```bash
pip install Pillow segno
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Anastasios3/QR-CODE-GENERATOR-MK-II.git
   ```
2. Navigate to the project directory:
   ```bash
   cd QR-CODE-GENERATOR-MK-II
   ```
3. Ensure the file `qr_generator.py` is present.

---

## Usage
1. Run the application:
   ```bash
   python qr_generator.py
   ```
2. The GUI window will open.

### Steps to Generate a QR Code
1. **Enter Content**: Type the text or URL to encode in the `Content` field.
2. **Set Properties**:
   - Choose error correction level.
   - Optionally, specify a version or leave it as "Auto."
3. **Customize Colors**:
   - Set foreground and background colors using the color picker.
4. **Embed a Logo**:
   - Click "Upload Logo" and choose an image file (optional).
5. **Generate QR Code**:
   - Click "Generate QR Code."
   - The QR code will appear in the preview section.
6. **Save the QR Code**:
   - Click "Save QR Code" to export the QR code as a PNG file.

---

## File Structure
- `qr_generator.py`: Main application script.
- `README.md`: Documentation for the project.

---

## Troubleshooting
1. **Error: Missing Libraries**
   - Ensure you have installed `Pillow` and `segno` using pip.
2. **No QR Code Preview**
   - Make sure you have entered content and clicked "Generate QR Code."
3. **Failed to Embed Logo**
   - Ensure the logo file is a valid image format (e.g., PNG, JPG).

---

## Future Enhancements
- Add support for SVG file output.
- Provide more advanced styling options for QR codes.
- Allow batch generation of QR codes from a file.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Contact
For questions or feedback, contact:
- **Name**: Anastasios Tatarakis
- **Email**: [tatarakis.a@gmail.com]
- **GitHub**: [Anastasios3](https://github.com/Anastasios3)
- **Website**: [Anastasios-Tatarakis](https://antatarakis.com)

---

Enjoy creating your custom QR codes!

