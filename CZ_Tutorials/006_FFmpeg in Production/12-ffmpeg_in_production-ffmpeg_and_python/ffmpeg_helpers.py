import subprocess

FFMPEG_PATH = "D:/ffmpeg/ffmpeg-4.2.1/bin/ffmpeg.exe"


def encode_image_sequence(image_seq_path, output_path, framerate=24, crf=21, preset="ultrafast", audio_path=None):

    ffmpeg_cmd = FFMPEG_PATH
    ffmpeg_cmd += ' -y '
    ffmpeg_cmd += ' -framerate {0}'.format(framerate)
    ffmpeg_cmd += ' -i {0}'.format(image_seq_path)
    if audio_path:
        ffmpeg_cmd += ' -i {0}'.format(audio_path)

    ffmpeg_cmd += ' -c:v libx264 -crf {0} -preset {1}'.format(crf, preset)
    if audio_path:
        ffmpeg_cmd += ' -c:a aac -filter_complex "[1:0] apad" -shortest'

    ffmpeg_cmd += ' {0}'.format(output_path)

    print(ffmpeg_cmd)
    subprocess.call(ffmpeg_cmd)


if __name__ == "__main__":

    img_seq_path = "D:/ffmpeg/ffmpeg-4.2.1/bin/tears_of_steel/overrun.%04d.png"
    audio_path = "D:/ffmpeg/ffmpeg-4.2.1/bin/overrun.wav"
    output_path = "D:/ffmpeg/ffmpeg-4.2.1/bin/overrun.mp4"

    encode_image_sequence(img_seq_path, output_path, audio_path=audio_path)
