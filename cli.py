#!/user/bin/env python

import argparse
from csgo.scripts.config import INSTALLED_SCRIPTS


def main():
	parser = argparse.ArgumentParser(prog='dcsgo')
	subparser = parser.add_subparsers(help='commands')

	for script in INSTALLED_SCRIPTS:
		script.add_to_subparser(subparser)

	args = parser.parse_args()
	if hasattr(args, 'func'):
		args.func(args)
	else:
		parser.print_usage()

if __name__ == '__main__':
	main()
