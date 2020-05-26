from table_to_entity import *


class Config(Object):
    def __init__(self, postgre: dict):
        self.postgre = postgre


def get_conf(config_path):
    _config = namedtupled.load_yaml(path=config_path, name='config')
    print(_config)

    return Config(
        postgre=namedtupled.reduce(_config.postgre)
    )


if __name__ == '__main__':
    _conf = get_conf(os.path.realpath(ROOT) + replace_sys_path(DEFAULT_CONFIG_PATH))
    print(_conf.postgre)
