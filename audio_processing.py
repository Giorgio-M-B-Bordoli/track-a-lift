import openai
from pathlib import Path

# Ensure you've set the OPENAI_API_KEY environment variable for your API key

# Function to prompt the user for a file name and return the file path
def get_audio_file_path():
    file_name = input("Please provide the file name of your audio: ")
    file_path = Path(file_name)
    if not file_path.exists() or not file_path.is_file():
        print("File does not exist. Please check the file name and try again.")
        exit()
    return file_path

# Function to transcribe audio using the OpenAI Whisper API
def transcribe_audio(file_path):
    with open(file_path, 'rb') as audio_file:
        transcription = openai.audio.transcription.create(
          model="whisper-1",
          file=audio_file
        )
    return transcription['text']

# Main script execution
if __name__ == "__main__":
    file_path = get_audio_file_path()
    transcription = transcribe_audio(file_path)
    print("Transcription:", transcription)
