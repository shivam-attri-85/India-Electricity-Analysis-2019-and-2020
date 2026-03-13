import os
from functools import wraps

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret-key")

# Tableau public view URLs built from the embed codes in `embade code tablue.txt`.
STORY_VIEW = {
    "title": "Story: Electricity Consumption in India",
    "url": "https://public.tableau.com/views/ElectricityConsumption_17734110756840/StoryonElectricityConsumptioninIndia?:showVizHome=no&:embed=yes",
}

DASHBOARD_VIEWS = [
    {
        "title": "Dashboard 1",
        "url": "https://public.tableau.com/views/ElectricityConsumption_17734110756840/Dashboard1?:showVizHome=no&:embed=yes",
    },
    {
        "title": "Dashboard 2",
        "url": "https://public.tableau.com/views/ElectricityConsumption_17734110756840/Dashboard2?:showVizHome=no&:embed=yes",
    },
    {
        "title": "Dashboard 3",
        "url": "https://public.tableau.com/views/ElectricityConsumption_17734110756840/Dashboard3?:showVizHome=no&:embed=yes",
    },
]


def is_auth_enabled() -> bool:
    return bool(os.getenv("APP_PASSWORD"))


def is_logged_in() -> bool:
    return session.get("authenticated", False)


def login_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not is_auth_enabled():
            return view_func(*args, **kwargs)
        if is_logged_in():
            return view_func(*args, **kwargs)
        return redirect(url_for("login", next=request.path))

    return wrapped


@app.context_processor
def inject_globals():
    return {
        "story_view": STORY_VIEW,
        "dashboard_views": DASHBOARD_VIEWS,
        "auth_enabled": is_auth_enabled(),
        "logged_in": is_logged_in(),
    }


@app.route("/")
@login_required
def home():
    return render_template("index.html")


@app.route("/dashboards")
@login_required
def dashboards():
    return render_template("dashboards.html", dashboards=DASHBOARD_VIEWS)


@app.route("/story")
@login_required
def story():
    return render_template("story.html", story=STORY_VIEW)


@app.route("/conclusion")
@login_required
def conclusion():
    return render_template("conclusion.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if not is_auth_enabled():
        return redirect(url_for("home"))

    error = None
    next_url = request.args.get("next") or request.form.get("next") or url_for("home")
    if request.method == "POST":
        entered_password = request.form.get("password", "")
        if entered_password == os.getenv("APP_PASSWORD"):
            session["authenticated"] = True
            return redirect(next_url)
        error = "Invalid password. Please try again."

    return render_template("login.html", error=error, next_url=next_url)


@app.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("login" if is_auth_enabled() else "home"))


if __name__ == "__main__":
    app.run(debug=True)
