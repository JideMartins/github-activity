from argparse import ArgumentParser

# parser object
parser = ArgumentParser(description="Simple CLI tool to display recent github activities")

# positional argument
parser.add_argument("username", type=str, help="Valid GitHub Username")

# parse argument
args = parser.parse_args()


# Use argument
