from argparse import ArgumentParser
from github_events import get_events

# parser object
parser = ArgumentParser(description="Simple CLI tool to display recent github activities")

# positional argument
parser.add_argument("username", type=str, help="Valid GitHub Username")

# parse argument
args = parser.parse_args()


# Use argument
get_events(args.username)