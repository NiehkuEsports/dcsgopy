import sqllite3
import os


class Database(object):
	db_dir = '/opt/dcsgopy/'
	db_name = 'dcsgodb.db'

	def create_db(self, start=27015, end=27019, start_tv=27020, end_tv=27023):

		if not os.path.exists(self.db_dir):
			os.makedirs(self.db_dir)

		c = self.conn.cursor()

		c.execute('''CREATE TABLE port_range
						(integer start, integer end, integer start_tv, integer end_tv)''')
		c.execute('''INSERT INTO port_range VALUES ({}, {}, {}, {})'''.format(start, end, start_tv, end_tv))

		c.execute('''CREATE TABLE csgo_container
						(integer port, integer tv_port, text name''')

		self.close()

	def destroy(self):
		os.remove(os.path.join(self.db_dir, self.db_name))

	@property
	def conn(self):
		if hasattr(self, '_conn'):
			self._conn = sqllite3.connect(os.path.join(self.db_dir, self.db_name))
		return self._conn

	def close(self):
		self.conn.close()
		delattr(self, '_conn')

	def insert_csgo_container(self, port, tv_port, name):
		c = self.conn.cursor()
		ports = self.get_port_range()
		if ports['start'] <= port <= ports['end']:
			self.close()
			raise IndexError('port {} out of range: {}-{}'.format(port, ports['start'], ports['end']))

		if ports['start_tv'] <= port <= ports['end_tv']:
			self.close()
			raise IndexError('tv port {} out of range: {}-{}'.format(tv_port, ports['start_tv'], ports['end_tv']))

		if c.execute("SELECT port from csgo_container WHERE port={}".format(port)):
			self.close()
			raise IndexError('port {} is already in use'.format(port))

		if c.execute("SELECT tv_port from csgo_container WHERE tv_port={}".format(tv_port)):
			self.close()
			raise IndexError('tv port {} is already in use'.format(port))

		if c.execute("SELECT name from csgo_container WHERE name={}".format(name)):
			self.close()
			raise IndexError('name {} is already in use'.format(port))

		c.execute('''INSERT INTO csgo_container VALUES ({}, {}, {})'''.format(port, tv_port, name))
		self.close()

	def get_port_range(self):
		c = self.conn.cursor()
		ports = c.execute("SELECT * FROM port_range")[0]
		self.close()
		return {
			'start': ports[0],
			'end': ports[1],
			'start_tv': ports[2]
			'end_tv': ports[3]
		}

	def get_max_servers(self):
		c = self.conn.cursor()
		ports = c.execute("SELECT * FROM port_range")[0]
		self.close()

		return ports[1] - ports[0]

	def get_available_ports(self):
		port_range = self.get_port_range()
		c = self.conn.cursor()
		ports = c.execute('''SELECT port FROM csgo_container''')
		tv_ports = c.execute('''SELECT tv_port FROM csgo_container''')
		available_tv_ports = []
		available_ports = []
		for port in range(port_range['start'], port_range['end']):
			if port not in ports:
				available_ports.append(port)

		for tv_port in range(port_range['tv_start'], port_range['tv_end']):
			if tv_port not in tv_ports:
				available_tv_ports.append(tv_port)

		return available_ports, available_tv_ports
		self.close()
