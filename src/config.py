class DevelopmentConfig():
  DEBUG = True
  MYSQL_HOST = '127.0.0.1'
  MYSQL_PORT = 3308
  MYSQL_USER = 'test'
  MYSQL_PASSWORD = 't3st'
  MYSQL_DB = 'app_payments'


config = {
  'development': DevelopmentConfig
}
