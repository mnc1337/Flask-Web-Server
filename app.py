from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
from helpful_files.config import *
import os
from send2trash import send2trash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = SECRET_KEY,
    MAX_CONTENT_LENGTH = 5000 * 1024 * 1024,
)

def limit_func():
    return get_remote_address()

limiter = Limiter(
    key_func=limit_func,
    app=app,
    default_limits=["3 per 5 seconds"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return redirect(url_for("check_key"))

@app.route("/check_key")
def check_key():
    return render_template("check_key.html")

@app.route("/upload_redirect_download")
def upload_redirect_download():
    return render_template("upload_redirect_download.html")

@app.route("/upload_redirect_delete")
def upload_redirect_delete():
    return render_template("upload_redirect_delete.html")

@app.route("/upload_redirect_get_all")
def upload_redirect_get_all():
    return render_template("upload_redirect_get_all.html")

@app.route("/upload_redirect_check_shortcuts")
def upload_redirect_check_shortcuts():
    return render_template("upload_redirect_check_shortcuts.html")

@app.route("/<string:enter_key>/get_enter_key")
def get_enter_key(enter_key):
    if enter_key == ENTER_KEY:
        return jsonify(key=ENTER_KEY)
    else:
        return jsonify(error="Enter key is incorrect"), 400
    
@app.route("/<string:delete_key>/get_delete_key")
def get_delete_key(delete_key):
    if delete_key == DELETE_KEY:
        return jsonify(key=DELETE_KEY)
    else:
        return jsonify(error="Delete key is incorrect"), 400

@app.route("/<string:enter_key>/upload", methods=["GET", "POST"])
def upload(enter_key):
    if enter_key != ENTER_KEY:
        return redirect(url_for("home"))
    
    if request.method == "GET":
        return render_template("upload.html")
    
    if "mainInput" not in request.files:
        return jsonify(error="There is not any file in request"), 400
    
    file = request.files["mainInput"]
    filename = file.filename

    if file and filename:
        full_path = os.path.join(UPLOAD_FOLDER, filename)
        if not os.path.exists(full_path):
            try:
                file.save(full_path)
                return jsonify(message="File was successfully uploaded to a directory"), 200
            except Exception as e:
                return jsonify({
                    "error": "Exception",
                    "errorMessage": str(e),
                }), 500
        else:
            return jsonify(error="The requested file path already exists in directory"), 400
    else:
        return render_template("file_not_found_error.html"), 404
    
@app.route("/<string:enter_key>/upload_shortcuts")
def upload_shortcuts(enter_key):
    if enter_key == ENTER_KEY:
        return render_template("upload_shortcuts.html")
    else:
        return render_template("key_error.html"), 400

@app.route("/<string:enter_key>/download/<string:filename>", methods=["GET", "POST"])
def download_by_filename(enter_key, filename):
    if enter_key == ENTER_KEY:
        full_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(full_path):
            try:
                return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True), 200
            except Exception as e:
                return jsonify({
                    "error": "Exception",
                    "errorMessage": str(e),
                }), 500
        else:
            return render_template("path_error.html"), 404
    else:
        return render_template("key_error.html"), 400
    
@app.route("/<string:delete_key>/delete/<string:filename>", methods=["GET", "DELETE"])
def delete_by_filename(delete_key, filename):
    if delete_key == DELETE_KEY:
        full_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(full_path):
            try:
                send2trash(full_path)
                return jsonify(message="File was successfully sent to trash bin"), 200
            except Exception as e:
                return jsonify({
                    "error": "Exception",
                    "errorMessage": str(e),
                }), 500
        else:
            return render_template("path_error.html"), 404
    else:
        return render_template("key_error.html"), 400

@app.route("/<string:enter_key>/get_all")
def get_all(enter_key):
    if enter_key == ENTER_KEY:
        files = [{
            "filename": elem.name,
            "filepath": elem.path,
            "filesize": elem.stat().st_size
        } for elem in os.scandir(UPLOAD_FOLDER) if elem.is_file()]

        return render_template("all_files.html", files=files, upload_folder=UPLOAD_FOLDER)
        # if os.listdir(UPLOAD_FOLDER):
        #     return jsonify([{
        #         "ID": idx,
        #         "filename": elem.name,
        #         "filepath": elem.path,
        #         "filesize(in bytes)": elem.stat().st_size,
        #     } for idx, elem in enumerate(os.scandir(UPLOAD_FOLDER), start=1) if elem.is_file()]), 200
        # else:
        #     return jsonify(info="There is not any file in directory"), 200
    else:
        return render_template("key_error.html"), 400

@app.route("/<string:admin_key>/delete_all", methods=["GET", "DELETE"])
def delete_all(admin_key):
    if admin_key == ADMIN_KEY:
        try:
            if os.listdir(UPLOAD_FOLDER):
                for elem in os.listdir(UPLOAD_FOLDER):
                    full_path = os.path.join(UPLOAD_FOLDER, elem)
                    send2trash(full_path)
                return jsonify(message="All files were successfully sent to the trash bin"), 200
            else:
                return jsonify(info="There is not any file in directory"), 200
        except Exception as e:
            return jsonify({
                "error": "Exception",
                "errorMessage": str(e),
            }), 500
    else:
        return jsonify(error="Admin key is incorrect:("), 400

@app.route("/404")
def error_404():
    return render_template("404.html"), 404
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("405.html"), 405

@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template("413.html"), 413

@app.errorhandler(429)
def too_many_requests(error):
    return render_template("429.html"), 429

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")