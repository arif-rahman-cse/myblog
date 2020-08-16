[![s.jpg](https://i.postimg.cc/GhpCm3Xc/s.jpg)](https://postimg.cc/6TFSHKsS)
# myblog
This is Blog App Developed by django and also developed REST API of this Blog so other technologies like Mobile app can interact with it.

## Blog Features:
  * User Login and Registration
  * Auto User Porile Creation
  * Generating Access token for moblie app
  * Restrict API so that unauthenticated user does not access API
  * CRUD functionality on a live website:
     1. Create blog posts
     2. Retrieve blog posts
     3. Update blog posts
     4. Delete blog posts
 * Pagination (very important for mobile apps)
 * Serialization of data
 * JSON Data
 
## API Uses:
### Login API
http://127.0.0.1:8000/api/account/login/
 
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username": "admin",
    "email": "admin@gmail.com",
    "token": "5b72b39ecf1c4727c288b8a61e697e1133cf799e"
}

```

### Registration API
http://127.0.0.1:8000/api/account/register/

```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 40,
    "username": "testing123",
    "email": "smrahmanarif906@gmail.com",
    "token": "e4110d6a9349bf63afd0e4464b7f332f27f84782"
}

```
### Single Blog Post
http://127.0.0.1:8000/api/post/id  
Example: http://127.0.0.1:8000/api/post/22

```
Example

```

 
