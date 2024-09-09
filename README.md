# Octapipe Python SDK
This SDK provides an interface for interacting with the **octapipe API**. It includes methods for authentication and CRUD (Create, Read, Update, Delete) operations on various entities, such as Database Records, Notes, Notifications, Pipeline Cards, Tasks and Users.

## Installation
Install the SDK using pip:
```bash
pip install git+https://github.com/octaworksllc/octapipe-python-sdk.git
```

---

## Authentication
Before using the SDK methods, you need to authenticate:

```python
from octapipe_python_sdk import auth

auth.login(domain='your_domain', email='your_email', password='your_password')
```

---

## Database Records

### Create Database Record
```python
from octapipe_python_sdk import DatabaseRecord

database_record = DatabaseRecord(
    database_uuid='8fd45fd2-1af8-485d-b1bc-74ccae9ac5ac',
    name='Falcon III',
    custom_fields_values={'cf_vehicle_type': 'Spaceship'}
)
database_record.post()
```

### Get Database Record
```python
from octapipe_python_sdk import DatabaseRecord

database_record = DatabaseRecord.get(uuid='5f32bd52-e3b2-45e1-a9c6-1e7cfcdf116f')
```

### Get all Database Records
```python
from octapipe_python_sdk import DatabaseRecord

database_records = DatabaseRecord.get_all(page=1)
```

### Update Database Record
```python
from octapipe_python_sdk import DatabaseRecord

database_record = DatabaseRecord.get(uuid='5f32bd52-e3b2-45e1-a9c6-1e7cfcdf116f')
database_record.name = 'Falcon IV'
database_record.update()
```

### Delete Database Record
```python
from octapipe_python_sdk import DatabaseRecord

database_record = DatabaseRecord(uuid='28b4ecf8-6d90-4809-a015-0342f9ac9e92')
database_record.delete()
```

---

## Notes

### Create Note
```python
from octapipe_python_sdk import Note

note = Note(
    entity='pipeline_card',
    record_uuid='a5e15286-3e98-4230-b3af-5fdb9396761d',
    note='The damage to the Falcon II was caused on a mission'
)
note.post()
```

### Get all Notes
```python
from octapipe_python_sdk import Note

notes = Note.get_all(
    entity='card', 
    record_uuid='a5e15286-3e98-4230-b3af-5fdb9396761d', 
    page=1
)
```

### Delete Note
```python
from octapipe_python_sdk import Note

note = Note(uuid='225ba90c-c527-42f0-b301-e1867f42de90')
note.delete()
```

---

## Notifications

### Create Notification
```python
from octapipe_python_sdk import Notification

notification = Notification(
    owner_user_uuid='35f0796c-a720-49f6-bdc8-5bd61b9dc8f3',
    entity='user',
    record_uuid='24c1a5b4-a184-45d5-8b16-89de4428a0d8',
    message='Falcon II is broken'
)
```

### Get all Notifications
```python
from octapipe_python_sdk import Notification

notifications = Notification.get_all(page=1)
```

---

## Pipeline Cards

### Create Pipeline Card
```python
from octapipe_python_sdk import PipelineCard

pipeline_card = PipelineCard(
    name='Falcon II',
    pipeline_stage_uuid='a44a6961-08f6-4adb-864a-34896cb9bc70',
    sla=24,
    custom_fields_values={'cf_vehicle_condition': 'broken'}
)
pipeline_card.post()
``` 

### Get Card
```python
from octapipe_python_sdk import PipelineCard

pipeline_card = PipelineCard.get(uuid='91a1ff5e-36e5-4070-987c-52453371c970')
```

### Get All PipelineCards
```python
from octapipe_python_sdk import PipelineCard

cards = PipelineCard.get_all(page=1)
```

### Update PipelineCard
```python
from octapipe_python_sdk import PipelineCard

pipeline_card = PipelineCard.get(uuid='a5dcc9dd-57ba-4016-9d0a-330d0c76cbc2')
pipeline_card.pipeline_stage_id = 15379
pipeline_card.update()
```

### Delete PipelineCard
```python
from octapipe_python_sdk import PipelineCard

pipeline_card = PipelineCard(uuid='a5dcc9dd-57ba-4016-9d0a-330d0c76cbc2')
pipeline_card.delete()
```

---

## Tasks

### Create Task
```python
from octapipe_python_sdk import Task

task = Task(
    title='Fix Falcon II',
    start_date='2024-09-05',
    end_date='2024-09-15',
    start_time='10:00',
    end_time='10:00',
    status='pending',
    priority='medium',
)
task.post()
```

### Get Task
```python
from octapipe_python_sdk import Task

task = Task.get(uuid='e77f58f8-2eb4-47b7-a840-07dc77c918c5')
```

### Get All Tasks
```python
from octapipe_python_sdk import Task

tasks = Task.get_all(page=1)
```

### Update Task
```python
from octapipe_python_sdk import Task

task = Task.get(uuid='e77f58f8-2eb4-47b7-a840-07dc77c918c5')
task.priority = 'high'
task.update()
```

### Delete Task
```python
from octapipe_python_sdk import Task

task = Task(uuid='e77f58f8-2eb4-47b7-a840-07dc77c918c5')
task.delete()
```

---

## Users

### Create User
```python
from octapipe_python_sdk import User

user = User(
    first_name='Elon',
    last_name='Musk',
    email='elon.musk@tesla.com',
    initial_password='@Elon1234Musk',
    role='admin',
    enabled_pipelines=['16aa1c40-fc0a-4bf2-afd6-d6c72edd852f', 'eed00ebf-9229-43c6-a705-50d6fe74befd']
)
user.post()
```

### Get User
```python
from octapipe_python_sdk import User

user = User.get(uuid='96ab2d88-47d9-4e3b-9bb3-9d7c82a14532')
```

### Get All Users
```python
from octapipe_python_sdk import User

users = User.get_all(page=1)
```

### Update User
```python
from octapipe_python_sdk import User

user = User.get(uuid='96ab2d88-47d9-4e3b-9bb3-9d7c82a14532')
user.email = 'elon.musk@spacex.com'
user.update()
```

### Delete User
```python
from octapipe_python_sdk import User

user = User(uuid='96ab2d88-47d9-4e3b-9bb3-9d7c82a14532')
user.delete()
```
