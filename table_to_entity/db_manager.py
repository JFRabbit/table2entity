import psycopg2
from ariestools import Object

MYSQL = 'mysql'
HOST = 'host'
PORT = 'port'
USERNAME = 'username'
PASSWORD = 'password'
DATABASE = 'database'
CHARSET = 'charset'

MONGO = 'mongo'


class DBManager(Object):
    def __init__(self, func, kwargs: dict):
        try:
            self.__connect = func(kwargs)
        except Exception as e:
            self.__isClose = True
            raise e

        self.__cursor = self.__connect.cursor()
        self.__isClose = False

    def __del__(self):
        self.close()

    def close(self):
        """关闭数据库连接"""
        if self.__isClose is False:
            print('Close Connection')
            self.__connect.close()
            self.__isClose = True

    def find(self, sql, find_size=0, find_all=True):
        """查询：
            如果all = True 返回所有数据
            否则只返回第一条数据
        """
        self.__cursor.execute(sql)

        if find_size > 0:
            return self.__cursor.fetchmany(find_size)

        if find_all:
            return self.__cursor.fetchall()

        return self.__cursor.fetchone()

    def execute(self, sql):
        """更改：
            可适用于增、删、改
        """
        try:
            num = self.__cursor.execute(sql)
            self.__connect.commit()
            return num
        except Exception as e:
            self.__connect.rollback()
            return None

    @staticmethod
    def sql_result_2_dict(select_items: tuple, result_items: tuple):
        """将查询结果匹配查询的key"""
        if len(select_items) is 0 or len(result_items) is 0:
            raise Exception("Data length is 0")

        if len(select_items) is not len(result_items[0]):
            raise Exception("Data length different")

        if len(result_items) is 1:
            obj = {}
            for j in select_items:
                obj[j] = result_items[0][select_items.index(j)]

            return obj

        result = []
        for i in result_items:
            obj = {}
            for j in select_items:
                obj[j] = i[select_items.index(j)]

            result.append(obj)

        return result

    @staticmethod
    def dict_2_class(data: dict, target_class: object):
        for k, v in target_class.__dict__.items():  # type: str, object
            try:
                setattr(target_class, k, data[k])
            except KeyError:
                setattr(target_class, k, v)
        return target_class


class PostgreSQLManager(DBManager):
    def __init__(self, host='localhost', port=5432, username=None, password=None, database=None, kwargs=None):
        if kwargs is not None and isinstance(kwargs, dict):
            super().__init__(self.__connect_init, kwargs)
        else:
            self.host = host
            self.port = port
            self.username = username
            self.password = password
            self.database = database
            super().__init__(self.__connect_init, self.__dict__)

    def __connect_init(self, kwargs: dict):
        return psycopg2.connect(
            host=kwargs[HOST],
            port=kwargs[PORT],
            user=kwargs[USERNAME],
            password=kwargs[PASSWORD],
            database=kwargs[DATABASE],
        )
