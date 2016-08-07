class Const(object):
    def get_system_db(self):
        return 'LightDB'

    SYSTEM_DB = property(get_system_db)

    def get_system_db_prefix(self):
        return 'light'

    SYSTEM_DB_PREFIX = property(get_system_db_prefix)

    def get_system_db_config(self):
        return 'configuration'

    SYSTEM_DB_CONFIG = property(get_system_db_config)

    def get_system_db_validator(self):
        return 'validator'

    SYSTEM_DB_VALIDATOR = property(get_system_db_validator)

    def get_system_db_i18n(self):
        return 'i18n'

    SYSTEM_DB_I18N = property(get_system_db_i18n)

    def get_system_db_structure(self):
        return 'structure'

    SYSTEM_DB_STRUCTURE = property(get_system_db_structure)

    def get_system_db_board(self):
        return 'board'

    SYSTEM_DB_BOARD = property(get_system_db_board)

    def get_system_db_route(self):
        return 'route'

    SYSTEM_DB_ROUTE = property(get_system_db_route)

    def get_system_db_tenant(self):
        return 'tenant'

    SYSTEM_DB_TENANT = property(get_system_db_tenant)

    def get_env_light_db_port(self):
        return 'LIGHTDB_PORT'

    ENV_LIGHT_DB_PORT = property(get_env_light_db_port)

    def get_env_light_db_host(self):
        return 'LIGHTDB_HOST'

    ENV_LIGHT_DB_HOST = property(get_env_light_db_host)

    def get_env_light_db_user(self):
        return 'LIGHTDB_USER'

    ENV_LIGHT_DB_USER = property(get_env_light_db_user)

    def get_env_light_db_pass(self):
        return 'LIGHTDB_PASS'

    ENV_LIGHT_DB_PASS = property(get_env_light_db_pass)
