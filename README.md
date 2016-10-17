# shop-api
Simple internet shop with REST API implementation using Django Rest Framework

To create migrations, superuser and rundevserver:

```bash
$ ./init_db_and_run.sh
```

Now you can log in as admin with password 'adminpass' at http://127.0.0.1:8000/admin

to run tests:
``` bash
$ python manage.py test shop_rest_api
```

methods available:

**Create Review**
----
  Creates Review objects and returns it's data.

* **URL**

  /reviews/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 

* **Data Params**

   **Required:**
 
   `item=[integer]`
   `author_name=[string]`
   `author_email=[string]`
   `content=[string]`
   `rating=[integer]`

* **Success Response:**

  * HTTP 201 Created
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept

    ```json
    {
        "id": 1,
        "items": 1,
        "author_name": "Denis",
        "author_email": "a@a.ru",
        "content": "asdsdf",
        "rating": 1,
        "approved": false,
        "item": 1
    }
    ```
 
* **Error Response:**

  * HTTP 400 Bad Request
    Allow: POST, OPTIONS<br>
    Content-Type: application/json<br>
    Vary: Accept

    ```json
    {
        "author_email": [
            "This field may not be blank."
        ]
    }
    ```

**Show Item**
----
  Returns JSON data about item.

* **URL**

  /items/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`


* **Data Params**

    None

* **Success Response:**

    * HTTP 200 OK<br>
      Allow: GET, HEAD, OPTIONS<br>
      Content-Type: application/json<br>
      Vary: Accept

     ```json
      {
          "id": 1,
          "reviews": [
              {
                  "id": 1,
                  "items": 1,
                  "author_name": "Denis",
                  "author_email": "a@a.ru",
                  "content": "asdsdf",
                  "rating": 1,
                  "approved": false,
                  "item": 1
              },
              {
                  "id": 2,
                  "items": 1,
                  "author_name": "Denis",
                  "author_email": "14a@a.ru",
                  "content": "asdsdf",
                  "rating": 1,
                  "approved": false,
                  "item": 1
              }
          ],
          "total_approved_reviews": 0,
          "avg_rating": null,
          "name": "testitem",
          "description": "heki",
          "attributes": "{\"attrr\":\"blue\"}",
          "images": "http://cdn.images.express.co.uk/img/dynamic/1/590x/tv-629703.jpg"
      }
      ```
 
* **Error Response:**

    * HTTP 404 Not Found<br>
      Allow: GET, HEAD, OPTIONS<br>
      Content-Type: application/json<br>
      Vary: Accept
 
 ```json
      {
          "detail": "Not found."
      }
  ```