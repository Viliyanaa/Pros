from fastapi import FastAPI
from typing import Optional

app = FastAPI()
# Не създаваме нищо, затова спрямо REST няма нужда заявката да е POST,
@app.get("/flights")
def get_flights(origin, destination, maxFlights: Optional[int] = None) :
    routes = find_all_routes(flights, origin, destination)
    if maxFlights is not None:
        routes = [r for r in routes if len(r['route']) - 1 <= maxFlights]
    return routes

def find_all_routes(flights, origin, destination):

    all_routes = []

    def search_routes (current, path, price, visited):
        path.append(current)
        visited.add(current)

        if current == destination:
            all_routes.append({'route': path.copy(), 'price': price})
        else:
            for flight in flights:
                if flight['from'] == current and flight['to'] not in visited:
                    search_routes(flight['to'], path, price + flight['price'], visited.copy())

        path.pop()
        visited.remove(current)

    search_routes(origin, [], 0, set())
    return sorted(all_routes, key=lambda n: n['price'])


flights = [
    {'from': 'SOF', 'to': 'IST', 'price': 10},
    {'from': 'IST', 'to': 'LON', 'price': 40},
    {'from': 'SOF', 'to': 'FRA', 'price': 20},
    {'from': 'FRA', 'to': 'LON', 'price': 30},
    {'from': 'FRA', 'to': 'PAR', 'price': 60},
    {'from': 'PAR', 'to': 'LON', 'price': 110},
    {'from': 'PAR', 'to': 'MLE', 'price': 100},
    {'from': 'MLE', 'to': 'CMB', 'price': 150},
    {'from': 'LON', 'to': 'CMB', 'price': 70}
]



# print("Destinations: Sofia(SOF), Istanbul(IST), Frankfurt(FRA), Paris(PAR), Maldives(MLE), Katunayake- Sri Lanka(CMB)")
#
# while True:
#     print("1. Find flight")
#     print("2. Exit")
#
#     choice = input("Chose an option: ")
#
#     if choice == '1':
#         origin = input("Origin (Please, use abbreviations): ").upper()
#         destination = input("Destination (Please, use abbreviations): ").upper()
#
#         all_cities = set(f['from'] for f in flights).union(set(f['to'] for f in flights))
#         if origin not in all_cities or destination not in all_cities:
#             print("Invalid cities. Please, try again")
#             choice = input("Select an option from the ones listed above: ")
#
#         routes = find_all_routes(flights, origin, destination)
#
#         if not routes:
#             print(f"No routes available from {origin} to {destination}")
#         else:
#             print(f"\nAll routes from {origin} to {destination}:")
#             for i, route in enumerate(routes, 1):
#                 print(f"{i}. {'->'.join(route['path'])} (Price: {route['total_price']})")
#
#     elif choice == '2':
#         break
#
#     else:
#         print("Please select one of the two options listed.")
#
