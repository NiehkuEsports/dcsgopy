from csgo.scripts.basescript import BaseScript


class Create(BaseScript):

	command = 'create'

	@classmethod
	def add_to_subparser(cls, subparser):
		parser = subparser.add_parser(cls.command, help='Create csgo docker container')
		parser.add_argument('-n', '--name', dest='name', help='Name of the docker container')

	@classmethod
	def run(cls, args):
		print("Not implemented create csgo container with name = {}".format(args.name))
