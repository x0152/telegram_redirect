# Telegram redirect
Web page for redirect telegram links
![image](https://user-images.githubusercontent.com/45021974/170572301-e3874571-b874-4683-8721-84134ad6995d.png)

## Build
```bash
docker build --tag telegram_redirect .

docker run --publish 80:5000 --detach --name tr telegram_redirect

``` 
