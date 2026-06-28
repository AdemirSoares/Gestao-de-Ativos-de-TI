from flask import render_template

def init_app(app):
    
    @app.route("/")
    def dashboard():
        return render_template("dashboard.html")