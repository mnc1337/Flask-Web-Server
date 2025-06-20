# Flask-Web-Server

---

## Simple web server for sharing files.

Actions with files that are supported here:
- Uploading;
- Downloading;
- Deleting.

---

## There are four keys(declared as constants) in helpful_files/config.py:

- SECRET_KEY (for session signing and CSRF-protection in forms);
- ADMIN_KEY (for admin who is a head of the server);
- ENTER_KEY (for entering to pages of server - basic URL-protection);
- DELETE_KEY (for deleting operations).

---

## Main file (engine of server) has the next location: files/app.py.
You can start the server by starting this file.
Also you can configure `host` and `port` parameters as you want:
- host:
    - `127.0.0.1` or `localhost` - server will be available only on your local machine(your computer);
    - `0.0.0.0` - makes your server externally available in your (local) or even global network(if port forwarding is configured);
- port:
    a number in range 0-65535 (including both points) - if it`s not taken by another process.

---

## Some words about structure:
- archive (7z) - folder with an archive and .txt file with hash sums of archive;
- helpful_files - folder with additional files that provide functions like generating new values, hashing existing and configuring the server protection;
- static - folder for static files(css/js/images etc.):
    - css: contains .css files(styles for HTML-pages);
    - js: contains .js files(scripts for HTML-pages);
- templates - folder which contains HTML-pages;
- uploads - folder for files, uploaded from server;
- app.py - main file that unites all project and helps to start all server(from one file).

---

## Some words about archive:
`IMPORTANT`: Archive contains all directories and files, except for one directory: `archive (7z)` (because archive is here), so if you download a ZIP-archive from GitHub interface (Code -> Download ZIP), it will have different hash sums. If you download an archive from `archive (7z)` directory - hash sums will be the same as in `hash_sums.txt` file.

---

### To launch server, choose root of the directory by default and use the next command: `python app.py` - it will start server on configured `host` and `port` (aforementioned).