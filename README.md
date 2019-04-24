# rememberActivity

班级墙活动模块

## 安装依赖包：

```sh
pip install --upgrade pip

pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2

pip install -r requirements.txt
```

## 本地测试部署

```sh
python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate
```

## docker部署

```bash
docker-compose up -d db # 要等两分钟再执行下面的命令
docker-compose up -d web
docker-compose up -d nginx
```

## 该项目现存的问题

## 参考内容

[OperationalError at /admin/ no such table: xadmin_usersettings
](https://stackoverflow.com/questions/44108753/operationalerror-at-admin-no-such-table-xadmin-usersettings)  
