# Wepipe Python SDK
This SDK provides an interface for interacting with the **wepipe API**. It includes methods for authentication and CRUD (Create, Read, Update, Delete) operations on various entities, such as Products, Files, Contacts, Companies, Users, Tasks, and Cards.

## Installation
Install the SDK using pip:
```bash
pip install git+https://github.com/octaworksllc/wepipe_python_sdk.git
```

## Authentication
Before using the SDK methods, you need to authenticate:

```python
from octapipe_python_sdk import auth

auth.login(domain='your_domain', email='your_email', password='your_password')
```


## Products
### Create Product

```python
from octapipe_python_sdk import Product

product = Product(name='Product01', price=2.5, color='#0C80F2')
product.post()
```
### Get Product

```python
from octapipe_python_sdk import Product

product = Product.get(id=67618)
```
### Get All Products

```python
from octapipe_python_sdk import Product

products = Product.get_all(page=1)
```
### Update Product

```python
from octapipe_python_sdk import Product

product = Product.get(id=67619)
product.name = 'Test Product 2'
product.update()
```
### Delete Product

```python
from octapipe_python_sdk import Product

product = Product(id=67619)
product.delete()
```


## Files
### Create File

```python
from octapipe_python_sdk import File

file = File(
    record_id=592332,
    entity='deal',
    name='file.png',
    url='https://wepipe.s3.sa-east-1.amazonaws.com/your_file',
    mime='image/png',
    size=20270,
)
file.post()
```
### Get All Files

```python
from octapipe_python_sdk import File

files = File.get_all(card_id=592332)
```
### Delete File

```python
from octapipe_python_sdk import File

file = File(id=175349)
file.delete()
```


## Contacts
### Create Contact

```python
from octapipe_python_sdk import Contact

contact = Contact(first_name='Contact01')
contact.post()
```
### Get Contact

```python
from octapipe_python_sdk import Contact

contact = Contact.get(id=250512)
```
### Get All Contacts

```python
from octapipe_python_sdk import Contact

contacts = Contact.get_all(page=1)
```
### Update Contact

```python
from octapipe_python_sdk import Contact

contact = Contact.get(id=272332)
contact.first_name = 'Contact02'
contact.update()
```
### Delete Contact

```python
from octapipe_python_sdk import Contact

contact = Contact(id=272332)
contact.delete()
```


## Companies
### Create Company

```python
from octapipe_python_sdk import Company

company = Company(company='Company01')
company.post()
```
### Get Company

```python
from octapipe_python_sdk import Company

company = Company.get(id=76482)
```
### Get All Companies

```python
from octapipe_python_sdk import Company

companies = Company.get_all(page=1)
```
### Update Company

```python
from octapipe_python_sdk import Company

company = Company.get(id=76484)
company.company = 'Company02'
company.update()
```
### Delete Company

```python
from octapipe_python_sdk import Company

company = Company(id=76484)
company.delete()
```
## Users
### Create User

```python
from octapipe_python_sdk import User

user = User(
    first_name='Elon',
    last_name='Musk',
    password='@Elon1234Musk',
    role='admin',
    email='elon.musk@tesla.com'
)
user.post()
```
### Get User

```python
from octapipe_python_sdk import User

user = User.get(id=2330)
```
### Get All Users

```python
from octapipe_python_sdk import User

users = User.get_all(page=1)
```
### Update User

```python
from octapipe_python_sdk import User

user = User.get(id=2691)
user.email = 'elon.musk@spacex.com'
user.update()
```
### Delete User

```python
from octapipe_python_sdk import User

user = User(id=2691)
user.delete()
```


## Tasks
### Create Task

```python
from octapipe_python_sdk import Task

task = Task(task_type_id=910, start='2024-09-10 08:00:00', end='2024-09-10 20:00:00', responsible_user_id=2597)
task.post()
```
### Get Task

```python
from octapipe_python_sdk import Task

task = Task.get(id=96752)
```
### Get All Tasks

```python
from octapipe_python_sdk import Task

tasks = Task.get_all(page=1)
```
### Update Task

```python
from octapipe_python_sdk import Task

task = Task.get(id=102619)
task.end = '2024-09-15 20:00:00'
task.update()
```
### Delete Task

```python
from octapipe_python_sdk import Task

task = Task(id=102619)
task.delete()
```


## Cards
### Create Card

```python
from octapipe_python_sdk import Card

card = Card(name='Card01', pipeline_id=2272, pipeline_stage_id=15378)
card.post()
``` 
### Get Card

```python
from octapipe_python_sdk import Card

card = Card.get(id=592336)
```
### Get All Cards

```python
from octapipe_python_sdk import Card

cards = Card.get_all(page=1)
```
### Update Card

```python
from octapipe_python_sdk import Card

card = Card.get(id=592255)
card.pipeline_stage_id = 15379
card.update()
```
### Delete Card

```python
from octapipe_python_sdk import Card

card = Card(id=592332)
card.delete()
```
