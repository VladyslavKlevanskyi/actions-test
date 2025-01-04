import pytest
from main import add_or_mult

data = [
    {"num1": 2, "num2": 3, "mult_result": 6, "sum_result": 5},
    {"num1": 3, "num2": 4, "mult_result": 12, "sum_result": 7},
    {"num1": 4, "num2": 2, "mult_result": 8, "sum_result": 6},
]


class TestCalcScenarios:
    IDS = [
        f"Test that multiplying the numbers {data[0]['num1']} and {data[0]['num2']} will be {data[0]['mult_result']}",
        f"Test that multiplying the numbers {data[1]['num1']} and {data[1]['num2']} will be {data[1]['mult_result']}",
        f"Test that multiplying the numbers {data[2]['num1']} and {data[2]['num2']} will be {data[2]['mult_result']}",
        f"Test that sum of numbers {data[0]['num1']} and {data[0]['num2']} will be {data[0]['sum_result']}",
        f"Test that sum of numbers {data[1]['num1']} and {data[1]['num2']} will be {data[1]['sum_result']}",
        f"Test that sum of numbers {data[2]['num1']} and {data[2]['num2']} will be {data[2]['sum_result']}",
    ]
    VALIDATION_SCENARIOS = [
        (data[0]["num1"], data[0]["num2"], "mult", data[0]["mult_result"]),
        (data[1]["num1"], data[1]["num2"], "mult", data[1]["mult_result"]),
        (data[1]["num1"], data[2]["num2"], "mult", data[2]["mult_result"]),
        (data[0]["num1"], data[0]["num2"], "sum", data[0]["sum_result"]),
        (data[1]["num1"], data[1]["num2"], "sum", data[1]["sum_result"]),
        (data[1]["num1"], data[2]["num2"], "sum", data[2]["sum_result"]),
    ]

    @pytest.mark.parametrize(
        "num1, num2, operator, result",
        VALIDATION_SCENARIOS,
        ids=IDS
    )
    def test_the_function(self, num1, num2, operator, result):
        if operator == "mult":
            sign = "*"
        else:
            sign = "+"
        assert add_or_mult(num1, num2, sign) == result
