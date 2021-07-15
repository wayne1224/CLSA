from pydub import AudioSegment
song = AudioSegment.from_file('Recording/sample_talk.wav')
song.export('sample_talk.mp3', format='mp3')