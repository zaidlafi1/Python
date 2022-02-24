import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("https://devapi.elevatustesting.xyz/api/helper/v1/career-level")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["country"] == "United States"
    assert response_body["places"][0]["place name"] == "Beverly Hills"

