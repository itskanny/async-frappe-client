## Frappe Client

Simple Async wrapper for FrappeClient


> :warning: **Warning:** This project is still not complete and some testing is required. If you can help that will be great. For now all methods work but test are not yet converted


### Install

```
git clone https://github.com/itskanny/async-frappe-client
pip install -e async-frappe-client
```

### API

FrappeClient has a frappe like API
- `framework`
it is used if you have customized the frappe framework

#### Login

Login to the Frappe HTTP Server by creating a new FrappeClient object

```py
import asyncio
from frappeclient import FrappeClient


async def main():
    conn = FrappeClient("example.com")
    await conn.login("user@example.com", "password")


asyncio.run(main())
```

#### Use token based authentication

```py
from frappeclient import FrappeClient

client = FrappeClient("https://example.com")
client.authenticate("my_api_key", "my_api_secret")
```

For demonstration purposes only! Never store any credentials in your source code. Instead, you could set them as environment variables and fetch them with `os.getenv()`.

#### get_list

Get a list of documents from the server

Arguments:
- `doctype`
- `fields`: List of fields to fetch
- `filters`: Dict of filters
- `limit_start`: Start at row ID (default 0)
- `limit_page_length`: Page length
- `order_by`: sort key and order (default is `modified desc`)

```py
users = await conn.get_list('User', fields = ['name', 'first_name', 'last_name'], , filters = {'user_type':'System User'})
```

Example of filters:
- `{ "user_type": ("!=", "System User") }`
- `{ "creation": (">", "2020-01-01") }`
- `{ "name": "test@example.com" }`

#### insert

Insert a new document to the server

Arguments:

- `doc`: Document object

```python
doc = await conn.insert({
	"doctype": "Customer",
	"customer_name": "Example Co",
	"customer_type": "Company",
	"website": "example.net"
})
```

#### get_doc

Fetch a document from the server

Arguments
- `doctype`
- `name`

```py
doc = await conn.get_doc('Customer', 'Example Co')
```

#### get_value

Fetch a single value from the server

Arguments:

- `doctype`
- `fieldname`
- `filters`

```py
customer_name = await conn.get_value("Customer", "name", {"website": "example.net"})
```

#### update

Update a document (if permitted)

Arguments:
- `doc`: JSON document object

```py
doc = await conn.get_doc('Customer', 'Example Co')
doc['phone'] = '000000000'
await conn.update(doc)
```

#### delete

Delete a document (if permitted)

Arguments:
- `doctype`
- `name`

```py
await conn.delete('Customer', 'Example Co')
```

### Example

```python
from frappeclient import FrappeClient

async def main():
    conn = FrappeClient("example.com", "user@example.com", "password")
    new_notes = [
        {"doctype": "Note", "title": "Sing", "public": True},
        {"doctype": "Note", "title": "a", "public": True},
        {"doctype": "Note", "title": "Song", "public": True},
        {"doctype": "Note", "title": "of", "public": True},
        {"doctype": "Note", "title": "sixpence", "public": True}
    ]
    
    for note in new_notes:
        print(conn.insert(note))
    
    # get note starting with s
    notes = conn.get_list('Note',
        filters={'title': ('like', 's')},
        fields=["title", "public"]
    )

asyncio.run(main())

```

### Example

See example.py for more info

### License

MIT
