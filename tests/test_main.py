import pytest
from main import add_or_mult, sub_or_div

data = [
    {
        "num1": 4,
        "num2": 2,
        "mult_result": 8,
        "sum_result": 6,
        "div_result": 2,
        "sub_result": 2
    },
    {
        "num1": 16,
        "num2": 4,
        "mult_result": 64,
        "sum_result": 20,
        "div_result": 4,
        "sub_result": 12
    },
    {
        "num1": 12,
        "num2": 3,
        "mult_result": 36,
        "sum_result": 15,
        "div_result": 4,
        "sub_result": 9
    },
]


negative_data = [
    {
        "num1": 4,
        "num2": 2,
        "mult_result": 123,
        "sum_result": 123,
        "div_result": 123,
        "sub_result": 123
    },
    {
        "num1": 16,
        "num2": 4,
        "mult_result": 123,
        "sum_result": 123,
        "div_result": 123,
        "sub_result": 123
    },
    {
        "num1": 12,
        "num2": 3,
        "mult_result": 123,
        "sum_result": 123,
        "div_result": 123,
        "sub_result": 123
    },
]


@pytest.mark.smoke
class TestSumMultPositiveScenarios:
    IDS = [
        f"Test that multiplying the numbers {data[0]['num1']}"
        f" and {data[0]['num2']} will be {data[0]['mult_result']}",
        f"Test that multiplying the numbers {data[1]['num1']}"
        f" and {data[1]['num2']} will be {data[1]['mult_result']}",
        f"Test that multiplying the numbers {data[2]['num1']}"
        f" and {data[2]['num2']} will be {data[2]['mult_result']}",
        f"Test that sum of numbers {data[0]['num1']}"
        f" and {data[0]['num2']} will be {data[0]['sum_result']}",
        f"Test that sum of numbers {data[1]['num1']}"
        f" and {data[1]['num2']} will be {data[1]['sum_result']}",
        f"Test that sum of numbers {data[2]['num1']}"
        f" and {data[2]['num2']} will be {data[2]['sum_result']}",
    ]
    VALIDATION_SCENARIOS = [
        (data[0]["num1"], data[0]["num2"], "mult", data[0]["mult_result"]),
        (data[1]["num1"], data[1]["num2"], "mult", data[1]["mult_result"]),
        (data[2]["num1"], data[2]["num2"], "mult", data[2]["mult_result"]),
        (data[0]["num1"], data[0]["num2"], "sum", data[0]["sum_result"]),
        (data[1]["num1"], data[1]["num2"], "sum", data[1]["sum_result"]),
        (data[2]["num1"], data[2]["num2"], "sum", data[2]["sum_result"]),
    ]

    @pytest.mark.parametrize(
        "num1, num2, operator, result",
        VALIDATION_SCENARIOS,
        ids=IDS
    )
    def test_the_add_or_mult_function(self, num1, num2, operator, result):
        if operator == "mult":
            sign = "*"
        else:
            sign = "+"
        assert add_or_mult(num1, num2, sign) == result


@pytest.mark.smoke
class TestSumMultNegativeScenarios:
    IDS = [
        f"Test that multiplying the numbers {negative_data[0]['num1']}"
        f" and {negative_data[0]['num2']}"
        f" will not be {negative_data[0]['mult_result']}",
        f"Test that multiplying the numbers {negative_data[1]['num1']}"
        f" and {negative_data[1]['num2']}"
        f" will not be {negative_data[1]['mult_result']}",
        f"Test that multiplying the numbers {negative_data[2]['num1']}"
        f" and {negative_data[2]['num2']}"
        f" will not be {negative_data[2]['mult_result']}",
        f"Test that sum of numbers {negative_data[0]['num1']}"
        f" and {negative_data[0]['num2']}"
        f" will not be {negative_data[0]['sum_result']}",
        f"Test that sum of numbers {negative_data[1]['num1']}"
        f" and {negative_data[1]['num2']}"
        f" will not be {negative_data[1]['sum_result']}",
        f"Test that sum of numbers {negative_data[2]['num1']}"
        f" and {negative_data[2]['num2']}"
        f" will not be {negative_data[2]['sum_result']}",
    ]
    VALIDATION_SCENARIOS = [
        (
            negative_data[0]["num1"],
            negative_data[0]["num2"],
            "mult", negative_data[0]["mult_result"]
        ),
        (
            negative_data[1]["num1"],
            negative_data[1]["num2"],
            "mult", negative_data[1]["mult_result"]
        ),
        (
            negative_data[2]["num1"],
            negative_data[2]["num2"],
            "mult", negative_data[2]["mult_result"]
        ),
        (
            negative_data[0]["num1"],
            negative_data[0]["num2"],
            "sum", negative_data[0]["sum_result"]
        ),
        (
            negative_data[1]["num1"],
            negative_data[1]["num2"],
            "sum", negative_data[1]["sum_result"]
        ),
        (
            negative_data[2]["num1"],
            negative_data[2]["num2"],
            "sum", negative_data[2]["sum_result"]
        ),
    ]

    @pytest.mark.parametrize(
        "num1, num2, operator, result",
        VALIDATION_SCENARIOS,
        ids=IDS
    )
    def test_the_add_or_mult_function(self, num1, num2, operator, result):
        if operator == "mult":
            sign = "*"
        else:
            sign = "+"
        assert add_or_mult(num1, num2, sign) != result


class TestSubDivScenarios:
    IDS = [
        f"Test that dividing the numbers {data[0]['num1']}"
        f" and {data[0]['num2']} will be {data[0]['div_result']}",
        f"Test that dividing the numbers {data[1]['num1']}"
        f" and {data[1]['num2']} will be {data[1]['div_result']}",
        f"Test that dividing the numbers {data[2]['num1']}"
        f" and {data[2]['num2']} will be {data[2]['div_result']}",
        f"Test that subtraction of numbers {data[0]['num1']}"
        f" and {data[0]['num2']} will be {data[0]['sub_result']}",
        f"Test that subtraction of numbers {data[1]['num1']}"
        f" and {data[1]['num2']} will be {data[1]['sub_result']}",
        f"Test that subtraction of numbers {data[2]['num1']}"
        f" and {data[2]['num2']} will be {data[2]['sub_result']}",
    ]
    VALIDATION_SCENARIOS = [
        (data[0]["num1"], data[0]["num2"], "div", data[0]["div_result"]),
        (data[1]["num1"], data[1]["num2"], "div", data[1]["div_result"]),
        (data[2]["num1"], data[2]["num2"], "div", data[2]["div_result"]),
        (data[0]["num1"], data[0]["num2"], "sub", data[0]["sub_result"]),
        (data[1]["num1"], data[1]["num2"], "sub", data[1]["sub_result"]),
        (data[2]["num1"], data[2]["num2"], "sub", data[2]["sub_result"]),
    ]

    @pytest.mark.parametrize(
        "num1, num2, operator, result",
        VALIDATION_SCENARIOS,
        ids=IDS
    )
    def test_the_sub_or_div_function(self, num1, num2, operator, result):
        if operator == "div":
            sign = "//"
        else:
            sign = "-"
        assert sub_or_div(num1, num2, sign) == result
