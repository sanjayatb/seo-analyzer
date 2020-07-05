#!/usr/bin/env python3

import argparse


def main(args=None):
    if not args:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('site', help='URL of the site you are wanting to analyze.')
        arg_parser.add_argument('file', help='HTML file you are wanting to analyze.')
        args = arg_parser.parse_args()

        print(args)

    else:
        exit(1)


if __name__ == "__main__":
    main()
