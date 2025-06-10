## Flask-Web-Server

# Simple web server for sharing files.

Actions with files that are supported here:
- Uploading;
- Downloading;
- Deleting.

---

# There are four keys(declared as constants) in helpful_files/config.py:

- SECRET_KEY(for session signing and CSRF-protection in forms);
- ADMIN_KEY(for admin who is a head of the server);
- ENTER_KEY(for entering to pages of server - basic URL-protection);
- DELETE_KEY(for deleting operations).

---

Main file(engine of server) has the next location: files/app.py.
You can start the server by starting this file.
Also you can configure `host` and `port` parameters as you want:
- host:
    - (`127.0.0.1` or `localhost`) - server will be available only on your local machine(your computer);
    - `0.0.0.0` - makes your server externally available in your network(if port forwarding is configured).