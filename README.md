# table-to-entity

数据库Table转实体

```bash
./tte --template tscypress --table_name job --entity_name Job
```

Log:
```
{'num': 1, 'field': 'id', 'type': 'int4', 'notnull': True, 'comment': None}
{'num': 2, 'field': 'created_user', 'type': 'varchar', 'notnull': False, 'comment': None}
{'num': 3, 'field': 'created_at', 'type': 'timestamp', 'notnull': False, 'comment': None}
{'num': 4, 'field': 'updated_user', 'type': 'varchar', 'notnull': False, 'comment': None}
{'num': 5, 'field': 'updated_at', 'type': 'timestamp', 'notnull': False, 'comment': None}
{'num': 6, 'field': 'name', 'type': 'varchar', 'notnull': False, 'comment': None}

  namespace Cypress {
    type Job = {
      id : number;
      created_user : string;
      created_at : string;
      updated_user : string;
      updated_at : string;
      name : string;
    }
  }

```