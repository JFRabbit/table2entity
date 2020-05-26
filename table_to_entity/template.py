from table_to_entity import *


class Template(Object):
    def get_template(self, *args, **kwargs) -> str:
        pass


class TsCypressTemplate(Template):
    _TEMPLATE = ''' namespace Cypress {
    type %s = {
      %s
    }
  }'''

    def get_template(self, *args, **kwargs) -> str:
        """

        :param args:
        :param kwargs: class_name = str, params = []
        :return:
        """
        s1 = kwargs['entity_name']
        s2 = ';\n      '.join(['%s : %s' % (i[0], i[1]) for i in kwargs['fields']]) + ';'

        return self._TEMPLATE % (s1, s2)
