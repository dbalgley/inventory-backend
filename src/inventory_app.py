import logging
import sys

from flask import Flask

from app import create_app

def main(args):
    try:
        app = create_app()
        app.run(debug=True)
    except Exception as e:
        logging.info('Graceful shutdown of inventory application, %s', e)


if __name__ == '__main__':
    main(sys.argv)