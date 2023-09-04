# Telegram groups spammer

## Description

This project is a simple script for **spamming into telegram groups**. It uses Pyrogram library for interacting with
telegram API.

## Installation

To install and set up the project, follow these steps:

1. Make sure that python is installed on your computer

2. Clone the repository:

```bash
git clone https://github.com/Amir23714/TG_tools.git
```

3. Navigate to the project directory:

```bash
cd TG_tools
```

And create 'sessions' directory:
```bash
mkdir sessions
```

4. Run setup file (**do not forget to put the text to be spammed to text.txt**):

```bash
python setup.py
```

### Alembic configuration

5. Initialize alembic migrations

```bash
alembic init migrations
```

6. In file alembic.ini update value of variable **sqlalchemy.url** to your url to database(or copy it from *
   *databases/db_config.py**)
7. In file migrations/env.py update row **target_metadata = None** with:

```bash
from models.models import Base
target_metadata = Base.metadata
```
8. Run
```bash
alembic revision --autogenerate
alembic upgrade head
```

## Choose correct file for your aim

9. Run the spam.py to spam the participants of a certain chat directly into private messages:

```bash
python spam.py
```

10. Run the spam_to_chats.py to spam to all chats in which you are a member of.

```bash
python spam_to_chats.py
```

11. Run the users_grabber.py to collect active users of a certain chat into the database

```bash
python users_grabber.py
```

## Error while setup

If you get an error while running setup file, you can rerun by running setup.py file again:

```bash
python setup.py
```


