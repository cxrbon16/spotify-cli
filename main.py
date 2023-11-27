import auth
from processor import processor
import argparse

sp = auth.auth()
proc_object = processor(spotipy_auth=sp)


def main():
    parser = argparse.ArgumentParser(
                    prog='spotify-cli',
                    description='a command line application to use spotify playback features like next song, pause, volume up etc.',
                    )
    subparsers = parser.add_subparsers(dest='command')

    parser_vol = subparsers.add_parser('vol')
    parser_vol.add_argument('adj', type=int)
    parser_vol.set_defaults(func=proc_object.adjust_volume_directly)

    parser_next = subparsers.add_parser('next')
    parser_next.set_defaults(func=proc_object.next_track)

    parser_next = subparsers.add_parser('playlists')
    parser_next.set_defaults(func=proc_object.get_playlists)

    parser_current = subparsers.add_parser('current')
    parser_current.set_defaults(func=proc_object.get_current)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
