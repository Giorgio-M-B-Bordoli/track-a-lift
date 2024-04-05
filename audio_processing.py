import sys
from openai import OpenAI

client = OpenAI()

if len(sys.argv) < 2:
    print("Audio file name not provided.")
    sys.exit(1)

file_name = sys.argv[1]

try:
    # Assuming the file exists and is readable
    with open(file_name, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    # Print the transcription or a placeholder text if the 'text' key is missing
    print(transcription)
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)

