# Installation
### Initial setup
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Python Django setup and credentials

* Initialize Django DB and run dev server
```
python manage.py migrate
python manage.py runserver
```
* Credentials
```
superuser: jovial/kajimida (read, write, delete)
office-stock-manager: test_staff/kajimida (read, write)
view-only-access: staffuser/kajimida (read)
```

