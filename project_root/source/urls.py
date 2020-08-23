from .. import app
from . import views

route = app.add_url_rule

# --- Format ---

# route(
#     "",
#     endpoint="",
#     view_func=views.,
#     methods=["GET", "POST"]
# )

route(
    "/you_up_yet",
    endpoint="/check",
    view_func=views.check,
    methods=["GET", "POST"]
)
