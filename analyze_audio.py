import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)
    
    with audio_file as source:
        audio = recognizer.record(source)
    
    transcription = recognizer.recognize_google(audio, language="ru-RU")
    return transcription
