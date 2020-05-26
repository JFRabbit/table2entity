from table_to_entity.template import Template, TsCypressTemplate
from table_to_entity import *
from table_to_entity.db_manager import PostgreSQLManager
from table_to_entity.pgutil import get_table_info
from table_to_entity.conf import get_conf


def transfer(entity_name, table_info: list, template: Template):
    entity_fields = []

    for field in table_info:  # type: dict
        print(field)
        entity_fields.append([
            field['field'], transfer_type(field['type'])
        ])

    return template.get_template(
        entity_name=entity_name,
        fields=entity_fields
    )


def transfer_type(type):
    if 'int' in type or 'float' in type:
        return 'number'
    elif 'varchar' in type or 'timestamp' in type or 'text' in type:
        return 'string'
    else:
        return type


if __name__ == '__main__':
    args = Args(
        name='table-to-entity',
        args=[
            Arg('-c', '--config', '配置文件路径', './config/config.yaml'),
            Arg('-t', '--template', '模板', required=True),
            Arg('-tn', '--table_name', '表名', required=True),
            Arg('-en', '--entity_name', '实体名', required=True),
        ],
        desc='数据库表转实体'
    ).parse()

    _conf = get_conf(args.config)

    if args.template == 'tscypress':
        manager = PostgreSQLManager(kwargs=_conf.postgre)
    else:
        raise Exception('Not support template: %s', args.template)

    table_info = get_table_info(manager, args.table_name)

    _t = transfer(args.entity_name, table_info, TsCypressTemplate())

    print('\n', _t)
