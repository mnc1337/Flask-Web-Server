# Flask-Web-Server

---

## Simple web server for sharing files.

Actions with files that are supported here:
- Uploading;
- Downloading;
- Deleting.

---

## There are four keys (declared as constants) in helpful_files/config.py:

- SECRET_KEY (for session signing and CSRF-protection in forms);
- ADMIN_KEY (for admin who is a head of the server);
- ENTER_KEY (for entering to pages of server - basic URL-protection);
- DELETE_KEY (for deleting operations).

---

## Main file (engine of server) has the next location: files/app.py.
You can start the server by starting this file.
Also you can configure `host` and `port` parameters as you want:
- host:
    - `127.0.0.1` or `localhost` - server will be available only on your local machine (your computer);
    - `0.0.0.0` - makes your server externally available in your (local) or even global network (if port forwarding is configured);
- port:
    a number in range 0-65535 (including both points) - if it`s not taken by another process.

---

## Some words about structure:
- _security - folder with a security archive, which has nested archive with server files (`.7z`) and a digital sign (`.asc`);
- helpful_files - folder with additional files that provide functions like generating new values, hashing existing and configuring the server protection;
- static - folder for static files (css/js/images etc.):
    - css: contains .css files (styles for HTML-pages);
    - js: contains .js files (scripts for HTML-pages);
- templates - folder which contains HTML-pages;
- uploads - folder for files, uploaded from server;
- app.py - main file that unites all project files and helps to start all server (from one file).

---

## Security
There is a `_security` folder in projects structure. It contains an archive with a nested archive and an `.asc` file - digital signature. **To check archive originality**, you can download archive **from `_security` folder**, extract nested archive (`.7z`) and `.asc` file from it to directory **selected by you** and use there the next command in Bash/WSL console: `gpg --verify flask_webserver_archive.7z.asc flask_webserver_archive.7z` - first parameter is a digital signature (`.asc` file), second parameter is an archive.

---

### To launch server, choose root of the directory by default and use the next command: `python app.py` - it will start server on configured `host` and `port` (aforementioned).