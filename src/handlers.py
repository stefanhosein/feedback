import json
from .check_text import check_all_errors
from .routes import feedback


@feedback.route('/', methods=["POST"])
def check_errors(payload):
    try:
        responses = json.loads(str(payload, 'utf-8'))
    except ValueError:
        return "cannot get feedback", 400
    student_responses = [rd['studentResponse'] for rd in responses]
    expected_responses = [rd['expectedResponse'] for rd in responses]
    try:
        feedback = check_all_errors(student_responses, expected_responses)
    except Exception as e:
        return str(e), 500
    return json.dumps(feedback), 200
