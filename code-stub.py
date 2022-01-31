import argparse
import logging

parser = argparse.ArgumentParser(description='Will find the sum of all even Fibonnaci numbers up to number provided.')
parser.add_argument("-log", "--log", default="warning", help=("Provide logging level. "
        "Example --log debug', default='warning'"))
args = parser.parse_args()

# set your logging level, take argument from user to define what level, otherwise it will default to warn
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(args.log.lower())
logging.basicConfig(level=level)

