import sys
from yt_dlp import YoutubeDL
from static_ffmpeg import run
import youtube_audio_downloader.utils as utils

def main():
    config = None

    try:
        config = utils.get_config()
        cli_args = utils.get_cli_args()
        run.get_or_fetch_platform_executables_else_raise()
        ydl_opts = utils.get_ydl_opts(
            cli_args['option'],
            config['format'],
            config['temp_dir'],
            config['output_dir']
        )
        YoutubeDL(ydl_opts).download(cli_args['video_id'])
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        if config is not None and 'temp_dir' in config:
            utils.remove_dir_files_except_part(config['temp_dir'])
        sys.exit(1)
