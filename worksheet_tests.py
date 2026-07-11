from typing import Any, Callable
from dataclasses import dataclass

#region classes
@dataclass
class TestCase:
    args: tuple
    expected: Any
    hint: str = ""


@dataclass
class Task:
    name: str
    tests: list[TestCase]
    times_check_failed = 0

    @classmethod
    def submit(self, function: Callable):
        print("──────────────────────────────")
        print(f"Submitting '{self.name}'... (failed {self.times_check_failed} times)\n")

        passed = 0

        for i, test in enumerate(self.tests, start=1):

            try:
                result = function(*test.args)

            except Exception as e:
                print(f"＼(º □ º )/ Exception: {e}")
                return

            if result != test.expected:
                self.times_check_failed += 1
                
                print(f"╥﹏╥: Failed Test {i}")

                print(f"Input:    {test.args}")
                print(f"Expected: {test.expected}")
                print(f"Got:      {result}")

                if test.hint:
                    print(f"\nHint: {test.hint}")

                return

            print(f"Passed Test {i}")

            passed += 1

        print(f"\nPassed {passed}/{len(self.tests)}")
        print("──────────────────────────────")

#endregion

#region Task 1
class PriceChangeTask(Task):
    name = "Price Change Task"
    tests = [
        TestCase((10, 15), 5, "Did you do the wrong order?")
    ]

class ToCentsTask(Task):
    name = "Dollars to Cents Task"
    tests = [
        TestCase((5,), 500, "Did you do the arithmetic wrong?"),
    ]

class PercentGainTask(Task):
    name = "PercentGainTask"
    tests = [
        TestCase((100, 200), 100.0),
        TestCase((320, 160), -50.0, "Losses should return a negative value"),
    ]

class MadeProftTask(Task):
    name = "Made Profit Task"
    tests = [
        TestCase((100, 200), True),
        TestCase((320, 160), False),
    ]

class CapitalGainTask(Task):
    name = "Capital Gain Task"
    tests = [
        TestCase((100, 120, 5), 100, "Remember to multiply by the quantity."),
        TestCase((20, 15, 4), -20, "Check which price is subtracted from the other."),
        TestCase((50, 50, 10), 0, "Buying and selling at the same price should give zero."),
        TestCase((12.5, 15.0, 2), 5.0, "Your function should also work with decimal prices."),
        TestCase((0, 100, 3), 300, "Use the given formula directly."),
    ]

#endregion

#region Task 2
class MaxStockPriceTask(Task):
    name="Max Stock Price Task"
    tests=[
        TestCase(([1.2,5.6,3.4],),5.6),
        TestCase(([-1,-5,-2],),-1)
    ]

class AverageOpenPriceTask(Task):
    name="Average Open Price Task"
    tests=[
        TestCase(([1,2,3],),2.0),
        TestCase(([10.5,11.5],),11.0)
    ]

class HighestDailyIncreaseTask(Task):
    name="Highest Daily Increase Task"
    tests=[
        TestCase(([10,12,11,18],),7,"Compare consecutive days."),
        TestCase(([5,4,3],),0,"If prices never increase, return 0.")
    ]

class CountUpDaysTask(Task):
    name="Count Up Days Task"
    tests=[
        TestCase(([1,2,2,5],),2,"Count only days where todays price is greater than yesterdays."),
        TestCase(([5,4,3],),0)
    ]

#endregion