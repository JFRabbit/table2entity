from table_to_entity.db_manager import PostgreSQLManager

SQL_TABLE_INFO = """SELECT 
    a.attnum AS num,
    a.attname AS field,
    t.typname AS type,
    -- a.attlen AS length,
    -- a.atttypmod AS lengthvar,
    a.attnotnull AS notnull,
    b.description AS comment
FROM pg_class c,
    pg_attribute a
LEFT OUTER JOIN pg_description b ON a.attrelid=b.objoid AND a.attnum = b.objsubid, pg_type t
WHERE c.relname = '%s'
    and a.attnum > 0
    and a.attrelid = c.oid
    and a.atttypid = t.oid
ORDER BY a.attnum"""


def get_table_info(manager: PostgreSQLManager, table_name: str):
    return PostgreSQLManager.sql_result_2_dict(
        ('num', 'field', 'type', 'notnull', 'comment'),
        manager.find(sql=SQL_TABLE_INFO % table_name)
    )
