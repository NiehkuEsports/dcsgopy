class BaseScript(object):

	@property
	def command(self):
		raise NotImplementedError('Please set name of command Example: command = \'some-command\'')

	@classmethod
	def add_to_subparser(cls, subparser):
		raise NotImplementedError('Please implement add_subparser function')

	@classmethod
	def run(cls, args):
		raise NotImplementedError('Please implement run function')
