# Text-to-Speech Application

This project is a **Text-to-Speech (TTS) desktop application** built with Python and the Tkinter library. The application allows users to convert written text into speech in both English and Arabic. It features a user-friendly graphical interface with various functionalities.

---

## Features and Buttons Overview

### 1. **Text Input Field**
   - **Purpose:** Enter the text you want to convert to speech.
   - **Usage:** Type or paste the desired text into the input box.

---

### 2. **Buttons**

#### **Play Button**
   - **Purpose:** Converts the entered text into speech and plays the audio.
   - **How It Works:**
     - Detects the language (English or Arabic) automatically.
     - Uses Google Text-to-Speech (gTTS) to generate the audio.
     - Plays the audio using the `playsound` library.

#### **Set Button**
   - **Purpose:** Clears the input field.
   - **How It Works:**
     - Deletes all text from the input field.

#### **Save Button**
   - **Purpose:** Saves the converted audio file to your computer.
   - **How It Works:**
     - Detects the language automatically.
     - Prompts the user to choose a save location and file name.
     - Saves the file in `.mp3` format.

#### **Exit Button**
   - **Purpose:** Closes the application.

#### **Toggle Language Button**
   - **Purpose:** Switches the application’s language between English and Arabic.
   - **How It Works:**
     - Updates all button labels and prompts based on the selected language.

#### **Toggle Theme Button**
   - **Purpose:** Switches between light and dark modes.
   - **How It Works:**
     - Changes the background and text colors of the application interface.

---

## How to Use
1. Run the application.
2. Enter your desired text in the input field.
3. Use the **Play** button to hear the audio.
4. Save the audio file with the **Save** button if needed.
5. Clear the text using the **Set** button.
6. Customize the app by toggling between languages or themes.
7. Exit the application using the **Exit** button.

---

## Technologies Used
- **Python**: Programming language.
- **Tkinter**: GUI library for creating the desktop application.
- **gTTS**: Converts text to speech.
- **playsound**: Plays the generated audio.

---

## Dev
By Dev [Omar](https://t.me/Dev3mora)

---
