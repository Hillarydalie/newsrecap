from app import new_app
from flask_script import Manager,Server

app = new_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
  """
  To ran all tests in our app
  """
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=5).run(tests)


if __name__ == '__main__':
  manager.run()