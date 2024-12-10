import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
import playsound
import os

root = tk.Tk()
root.title("Text to Speech - Omar Abouelkheir")
root.geometry("500x350")
root.config(bg="#f5f5f5")

current_theme = "light"
current_language = "en"

def detect_language(text):
    if any('\u0600' <= char <= '\u06FF' for char in text):
        return "ar" 
    return "en"  

def play_text():
    text = text_entry.get()

    if text.strip():
        try:
            detected_lang = detect_language(text)
            tts = gTTS(text=text, lang=detected_lang)
            tts.save("temp_audio.mp3")
            playsound.playsound("temp_audio.mp3")
            os.remove("temp_audio.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while playing the audio:\n{e}")
    else:
        messagebox.showerror("Error", "Please enter text to play.")

def clear_text():
    text_entry.delete(0, tk.END)

def exit_app():
    root.destroy()

def save_audio():
    text = text_entry.get()
    if text.strip():
        try:
            detected_lang = detect_language(text)
            tts = gTTS(text=text, lang=detected_lang)
            file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            if file_path:
                tts.save(file_path)
                messagebox.showinfo("Success", "تم حفظ الملف بنجاح!" if current_language == "ar" else "Audio file saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"حدث خطأ أثناء الحفظ:\n{e}" if current_language == "ar" else f"An error occurred while saving the audio:\n{e}")
    else:
        messagebox.showerror("Error", "يرجى إدخال نص للحفظ!" if current_language == "ar" else "Please enter text to save.")

def toggle_theme():
    global current_theme
    if current_theme == "light":
        root.config(bg="#2e2e2e")
        label.config(bg="#2e2e2e", fg="white")
        entry_frame.config(bg="#2e2e2e")
        button_frame.config(bg="#2e2e2e")
        theme_button.config(bg="#555", fg="white", text="الوضع الفاتح" if current_language == "ar" else "Switch to Light Mode")
        current_theme = "dark"
    else:
        root.config(bg="#f5f5f5")
        label.config(bg="#f5f5f5", fg="black")
        entry_frame.config(bg="#f5f5f5")
        button_frame.config(bg="#f5f5f5")
        theme_button.config(bg="#333", fg="white", text="الوضع الليلي" if current_language == "ar" else "Switch to Dark Mode")
        current_theme = "light"

def toggle_language():
    global current_language
    if current_language == "en":
        current_language = "ar"
        label.config(text="أدخل النص:", font=("Arial", 14))
        play_button.config(text="تشغيل")
        set_button.config(text="مسح")
        exit_button.config(text="خروج")
        save_button.config(text="حفظ")
        theme_button.config(text="الوضع الليلي")
    else:
        current_language = "en"
        label.config(text="Enter text:", font=("Arial", 14))
        play_button.config(text="Play")
        set_button.config(text="Set")
        exit_button.config(text="Exit")
        save_button.config(text="Save")
        theme_button.config(text="Switch to Dark Mode")

language_button = tk.Button(root, text="عربي / English", font=("Arial", 12), command=toggle_language, bg="#FFA500", fg="white", relief="raised")
language_button.pack(pady=10)

label = tk.Label(root, text="Enter text:", font=("Arial", 14), bg="#f5f5f5", anchor="w", padx=10)
label.pack(fill='x', pady=10)

entry_frame = tk.Frame(root, bg="#f5f5f5")
entry_frame.pack(pady=5)

text_entry = tk.Entry(entry_frame, width=40, font=("Arial", 12), borderwidth=2, relief="solid")
text_entry.pack(padx=10, pady=5)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), command=play_text, bg="#4CAF50", fg="white", relief="raised", width=12, height=2)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12), command=clear_text, bg="#2196F3", fg="white", relief="raised", width=12, height=2)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), command=exit_app, bg="#F44336", fg="white", relief="raised", width=12, height=2)
exit_button.grid(row=0, column=2, padx=10)

save_button = tk.Button(button_frame, text="Save", font=("Arial", 12), command=save_audio, bg="#FFC107", fg="black", relief="raised", width=12, height=2)
save_button.grid(row=1, column=0, columnspan=3, pady=10)

theme_button = tk.Button(root, text="Switch to Dark Mode", font=("Arial", 12), command=toggle_theme, bg="#333", fg="white", relief="raised")
theme_button.pack(pady=10)


root.mainloop()