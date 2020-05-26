mkdir config_template
cat>config_template/config.yaml<<EOF
postgre:
  host: 'your host'
  port: port| number
  username: 'username'
  password: 'password'
  database: 'database'
EOF