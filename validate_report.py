import json
import sys

try:
    with open('testing_report.json', 'r') as f:
        report = json.load(f)

    if not isinstance(report, list):
        print("Error: Report is not a list")
        sys.exit(1)

    required_fields = [
        "title", "description", "deepLink", "filePath", "lineNumber",
        "confidence", "rationale", "context", "language", "category",
        "estimatedImpact"
    ]

    allowed_categories = [
        "missing-test-file", "untested-function", "missing-error-test",
        "missing-edge-case", "flaky-test", "integration-gap", "other"
    ]

    for item in report:
        for field in required_fields:
            if field not in item:
                print(f"Error: Missing field '{field}' in item: {item.get('title', 'Unknown')}")
                sys.exit(1)

        if not isinstance(item['confidence'], int) or not (1 <= item['confidence'] <= 3):
             print(f"Error: Invalid confidence score in item: {item.get('title')}")
             sys.exit(1)

        if not isinstance(item['estimatedImpact'], int) or not (1 <= item['estimatedImpact'] <= 3):
             print(f"Error: Invalid estimatedImpact score in item: {item.get('title')}")
             sys.exit(1)

        if item['category'] not in allowed_categories:
             print(f"Error: Invalid category '{item['category']}' in item: {item.get('title')}")
             sys.exit(1)

    print("Validation successful!")

except Exception as e:
    print(f"Validation failed: {e}")
    sys.exit(1)
