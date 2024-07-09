# test-task-ya
------------
The service is created as the test task.

It is used for retrieving current USD -> RUB currency rate based on info provided by Central Bank of Russia.
It allows to update rate only 1 time in 10 seconds for all users. If previous request was made less than 10 seconds ago, last requested rate is returned.

# Installation and local deploy
Follow these simple steps to local deploy.
* Clone the repo:
```
git clone git@github.com:DmitriyMikhalev/test-task-ya.git
```

* Create env file next to sample.env 

* Run Docker engine and start docker-compose:
```
docker-compose up -d
```

* App is available. Follow the link to see docs
```
http://127.0.0.1:8000/swagger/
```

* Follow the link to see currency rate:
```
http://127.0.0.1:8000/api/get-current-usd/
```