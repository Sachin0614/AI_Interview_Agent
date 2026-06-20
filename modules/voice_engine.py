import pyttsx3
import io
import tempfile
from faster_whisper import WhisperModel


class VoiceEngine:
    def __init__(self):
        self.stt_model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )

    def text_to_speech(self, text_input):
        try:
            if not text_input:
                return

            speaker = pyttsx3.init()
            speaker.setProperty("rate", 165)

            voices = speaker.getProperty("voices")
            if voices and len(voices) > 1:
                speaker.setProperty("voice", voices[1].id)

            speaker.say(text_input)
            speaker.runAndWait()
            speaker.stop()

        except Exception as e:
            print("TTS Error:", e)

    def speech_to_text(self, audio_bytes):
        try:
            if not audio_bytes:
                return ""

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_bytes)
                temp_audio_path = temp_audio.name

            segments, info = self.stt_model.transcribe(
                temp_audio_path,
                beam_size=5
            )

            text = " ".join([segment.text for segment in segments])
            return text.strip()

        except Exception as e:
            return f"[Speech processing error: {str(e)}]"