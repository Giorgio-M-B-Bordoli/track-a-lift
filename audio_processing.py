import requests
from pathlib import Path

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
    api_key = "your_openai_api_key_here"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers=headers,
        files={"file": file_path.open("rb")},
        data={"model": "whisper-medium"}
    )
    if response.status_code == 200:
        return response.json()['text']
    else:
        print(f"Failed to transcribe audio. Status code: {response.status_code}")
        exit()

# Main script execution
if __name__ == "__main__":
    file_path = get_audio_file_path()
    transcription = transcribe_audio(file_path)
    print("Transcription:", transcription)


