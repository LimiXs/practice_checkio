"""
https://py.checkio.org/en/mission/the-cheapest-flight/
"""


def cheapest_flight(costs: list, a: str, b: str) -> int:
    flights = {}
    for city1, city2, cost in costs:
        flights.setdefault(city1, {})[city2] = cost
        flights.setdefault(city2, {})[city1] = cost

    prices = {city: (0 if city == a else float('inf')) for city in flights}
    cities = sorted(flights)

    for _ in cities:
        for city1 in cities:
            for city2 in flights[city1]:
                price = prices[city1] + flights[city1][city2]
                if price < prices[city2]:
                    prices[city2] = price

    return prices[b] if prices[b] != float('inf') else 0


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
