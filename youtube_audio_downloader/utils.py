import os
import sys
import yaml

from static_ffmpeg import run

import youtube_audio_downloader.constants as constants


def remove_dir_files_except_part(dir):
    for item in os.listdir(dir):
        if not item.endswith('.part'):
            os.remove(os.path.join(dir, item))

def get_ydl_opts(option, format, temp_dir, output_dir):
    ffmpeg_location = run.get_or_fetch_platform_executables_else_raise()[0]

    ydl_opts = {
        'format': format,
        'ffmpeg_location': ffmpeg_location,
    }

    if option == 1:
        ydl_opts.update({
            'outtmpl': output_dir + '%(title)s.%(ext)s',
        })
    elif option == 2:
        ydl_opts.update({
            'outtmpl': {
                'default': temp_dir + '%(id)s.%(ext)s',
                'chapter': output_dir + '%(title)s\%(section_title)s.%(ext)s',
            },
            'postprocessors': [{
                'force_keyframes': False,
                'key': 'FFmpegSplitChapters',
            }],
        })
    elif option == 3:
        ydl_opts.update({
            'outtmpl': {
                'default': temp_dir + '%(id)s.%(ext)s',
                'chapter': output_dir + '%(title)s\%(section_number)02d. %(section_title)s.%(ext)s',
            },
            'postprocessors': [{
                'force_keyframes': False,
                'key': 'FFmpegSplitChapters',
            }],
        })

    return ydl_opts

def get_cli_args():
    video_id = sys.argv[1] if len(sys.argv) > 1 else input(constants.VIDEO_URL_INPUT_TEXT)
    option = int(sys.argv[2] if len(sys.argv) > 2 else input(constants.OPTION_INPUT_TEXT))

    return {
        'video_id': video_id,
        'option': option,
    }

def get_config():
    try:
        stream = open(constants.CONFIG_PATH, 'r')
        config = yaml.full_load(stream)
        stream.close()
    except FileNotFoundError:
        config = {}

    was_modified = False

    for field in constants.CONFIG_DEFAULT_VALUE_BY_FIELD.keys():
        if field in config:
            continue

        default = constants.CONFIG_DEFAULT_VALUE_BY_FIELD[field]
        text = constants.CONFIG_VALUE_INPUT_TEXT_BY_FIELD[field]
        config[field] = input(text.format(default=default)) or default
        was_modified = True

    if was_modified:
        stream = open(constants.CONFIG_PATH, 'w')
        yaml.dump(config, stream)
        stream.close()

    return config

