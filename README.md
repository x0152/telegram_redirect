# telegram_redirect
Web page for redirect telegram links
## Build
```bash
docker build --tag telegram_redirect .

docker run --publish 80:80 --detach --name tr telegram_redirect

``` 
