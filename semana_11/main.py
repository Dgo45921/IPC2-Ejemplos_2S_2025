from flask import Flask, jsonify, redirect, request, make_response

app = Flask(__name__)

# ---------------------------
# 1xx - Informational
# ---------------------------
@app.route("/continue")
def continue_request():
    response = make_response(jsonify(message="Request received, continue sending body"), 100)
    return response

@app.route("/switching_protocols")
def switching_protocols():
    response = make_response(jsonify(message="Switching protocols"), 101)
    return response


# ---------------------------
# 2xx - Success
# ---------------------------
@app.route("/ok")
def ok():
    return jsonify(message="Everything is fine"), 200

@app.route("/created", methods=["POST"])
def created():
    data = request.get_json() or {}
    return jsonify(message="Resource created", data=data), 201

@app.route("/accepted")
def accepted():
    return jsonify(message="Request accepted, processing asynchronously"), 202

@app.route("/no_content")
def no_content():
    return "", 204


# ---------------------------
# 3xx - Redirection
# ---------------------------
@app.route("/moved_permanently")
def moved_permanently():
    return redirect("/ok", code=301)

@app.route("/found")
def found():
    return redirect("/ok", code=302)

@app.route("/see_other")
def see_other():
    return redirect("/ok", code=303)

@app.route("/not_modified")
def not_modified():
    response = make_response("", 304)
    return response

@app.route("/temporary_redirect")
def temporary_redirect():
    return redirect("/ok", code=307)

@app.route("/permanent_redirect")
def permanent_redirect():
    return redirect("/ok", code=308)


# ---------------------------
# 4xx - Client Errors
# ---------------------------
@app.route("/bad_request")
def bad_request():
    return jsonify(error="Bad Request"), 400

@app.route("/unauthorized")
def unauthorized():
    return jsonify(error="Unauthorized"), 401

@app.route("/forbidden")
def forbidden():
    return jsonify(error="Forbidden"), 403

@app.route("/not_found")
def not_found():
    return jsonify(error="Resource not found"), 404

@app.route("/method_not_allowed", methods=["POST"])
def method_not_allowed():
    return jsonify(error="Method Not Allowed"), 405

@app.route("/conflict")
def conflict():
    return jsonify(error="Conflict"), 409

@app.route("/gone")
def gone():
    return jsonify(error="Resource is gone"), 410

@app.route("/unprocessable_entity")
def unprocessable_entity():
    return jsonify(error="Unprocessable Entity"), 422

@app.route("/too_many_requests")
def too_many_requests():
    return jsonify(error="Too Many Requests"), 429


# ---------------------------
# 5xx - Server Errors
# ---------------------------
@app.route("/internal_error")
def internal_error():
    return jsonify(error="Internal Server Error"), 500

@app.route("/not_implemented")
def not_implemented():
    return jsonify(error="Not Implemented"), 501

@app.route("/bad_gateway")
def bad_gateway():
    return jsonify(error="Bad Gateway"), 502

@app.route("/service_unavailable")
def service_unavailable():
    return jsonify(error="Service Unavailable"), 503

@app.route("/gateway_timeout")
def gateway_timeout():
    return jsonify(error="Gateway Timeout"), 504


# ---------------------------
# Global Error Handlers
# ---------------------------
@app.errorhandler(404)
def handle_404(e):
    return jsonify(error="Custom handler: Resource not found"), 404

@app.errorhandler(500)
def handle_500(e):
    return jsonify(error="Custom handler: Internal server error"), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error="Unexpected error", details=str(e)), 500


# ---------------------------
# Main entry point
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
