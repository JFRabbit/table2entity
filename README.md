# table-to-entity

数据库Table转实体

---

### 安装依赖
```shell script
./install.sh
```

### 创建配置文件
```shell script
./init_config.sh
```

修改配置文件中的数据库配置

### 打包
```shell script
./package_mac.sh
```

### 调试

需要在/table_to_entity路径创建文件config,存放配置文件config.yaml

### Demo

```shell script
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