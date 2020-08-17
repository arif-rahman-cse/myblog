![s.jpg](https://i.postimg.cc/GhpCm3Xc/s.jpg)

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
### Login POST API
--url http://127.0.0.1:8000/api/account/login/
 
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

### Registration POST API
--url http://127.0.0.1:8000/api/account/register/

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

### Blog Post API
  --url 'http://127.0.0.1:8000/api/posts-list/'  
  --header 'Authorization: Token <<access_token>>' 
  
  ```
{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/posts-list/?page=2",
    "previous": null,
    "results": [
        {
            "id": 24,
            "title": "WP Dummy Content",
            "content": "The next of the list is WP Dummy Content. Whilst not as often updated as FakerPress, it is still a very good WordPress Plugin to generate dummy content on your blog. It automatically creates posts, pages etc with single or multiple paragraphs of text. You can also insert unordered lists, shortcodes, block-quotes, links etc with just a click.",
            "date_posted": "2020-08-16T09:15:51.142016Z",
            "username": "admin"
        },
        {
            "id": 25,
            "title": "Better Lorem Ipsum Generator",
            "content": "Better Lorem Ipsum Generator is yet another dummy content generator for WordPress. This plugin has some additional features when compared to the rest above, the most important ones are its ability to generate custom taxonomies and custom post types automatically. Install this plugin and generate posts, pages, comments, tags, categories etc with ease.",
            "date_posted": "2020-08-16T09:16:03.799323Z",
            "username": "admin"
        },
        {
            "id": 26,
            "title": "How to Application Authentication",
            "content": "Application level authentication on version 3 is controlled by one of either a single query parameter, api_key, or by using your v4 access token as a Bearer token. You can request an API key by logging in to your account on TMDb and clicking the \"API\" link in the left hand side bar of your account page.",
            "date_posted": "2020-08-17T05:16:04.399429Z",
            "username": "testing123"
        }
    ]
}

```

### Single Blog Post
 --url http://127.0.0.1:8000/api/post/22  


```
{
    "id": 22,
    "title": "Top 10 Best Dummy Content (Lorem Ipsum) Generators WordPress Plugins",
    "content": "As a WordPress developer, whenever you build a new theme, plugin or even if you are testing out new features of WordPress that you might not be familiar with. There’s one task that get’s extremely repetitive, cumbersome and mundane.\r\n\r\nYou will always need to create some custom dummy data to test whether your plugin is working as expected, and as developers ourselves we have had this problem quite a lot. Thankfully, there are easy ways to solve it.\r\n\r\nThe usual way people tend to do this is either hire someone on Fiverr, to create all this dummy text or as a WordPress developer you’ll need to perform the task of filling up an empty theme with dummy content yourself.\r\n\r\nOur goal with this post is to help you to alleviate this time-consuming aspect of the development process by covering a list of plugins that help you achieve this goal in just a matter of seconds.\r\n\r\nNot only does the test data have to be comprehensive enough to capture all the possible post scenarios, it has to be as close enough as possible to real world data. This way you can effectively test the features you are building and luckily, these plugins do just that.",
    "date_posted": "2020-08-16T09:15:24.899202Z",
    "username": "admin"
}

```




 
