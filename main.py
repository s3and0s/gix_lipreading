import os
os.getcwd()

for vid in os.listdir(open("/")):
  print(vid)

command = "ffmpeg -i \"{0}\" -vn -ab 128k -ar 44100 -y \"{0}.mp3\"".format('front.webm')
os.system(command)
print(command)

ffmpeg -i "front.webm" -vn -y "front.webm.ogg"
# https://stackoverflow.com/questions/36458214/split-speech-audio-file-on-words-in-python
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_silence, detect_nonsilent
from pydub.playback import play

# https://github.com/jiaaro/pydub/blob/master/API.markdown
sound_file = AudioSegment.from_ogg("./front.webm.ogg")
# len(detect_silence(sound_file, min_silence_len=12))
detect_nonsilent(sound_file, min_silence_len=100)
audio_chunks = split_on_silence(wav_audio, min_silence_len=10)
print(len(audio_chunks))

for i, chunk in enumerate(audio_chunks):
    print(chunk)
    out_file = "chunk{0}.wav".format(i)
    print(out_file)
    # print ("exporting", out_file)
    chunk.export(out_file, format="wav")
