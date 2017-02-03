import sqllite3
import os


class Database(object):

	db_dir = '/opt/dcsgopy/'

	def create_db(self, start=27015, end=27019, start_tv=27020, end_tv=27023):

		if not os.path.exists(self.db_dir):
			os.makedirs(self.db_dir)

		c = self.conn.cursor()

		c.execute('''CREATE TABLE port_range
						(integer start, integer end, integer start_tv, integer end_tv)''')
		c.execute('''INSERT INTO port_range VALUES ({}, {}, {}, {})'''.format(start, end, start_tv, end_tv))
	
	def destroy(self):
		os.remove(os.path.join(self.db_dir, 'dcsgodb.db'))

	@property
	def conn(self):
		if hasattr(self, '_conn'):
			self._conn = sqllite3.connect(os.path.join(self.db_dir, 'dcsgodb.db'))
		return self._conn
