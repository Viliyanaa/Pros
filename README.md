# Pros

## Quality Assurance

### Assignment: 
Alice wants to book a flight. She needs to enter a starting point and a destination. As a result of the program, she gets a list of all possible flights sorted by price in ascending order.


## Case 1: Flight without using maxFlights
In this case, Alice enters two cities. As a result, she receives all possible routes, whether direct or not, sorted by price.

## Case 2: Direct flight using maxFlights=0
In this case, Alice enters two cities between which there is a direct flight, but she also uses the option maxFlights=0, which means there are no layovers between the cities.

## Case 3: Flight using maxFlights=1 or 2 or …
In this case, Alice enters two cities and uses the option maxFlights=1 or maxFlights=2, and so on. As a result, she receives all flights between these cities that are not direct.

## Case 4: Invalid input data
Тhe expected error is 400 Bad Request. Automatically by FastAPI  422 Unprocessable Entity

## Cace 5: Nonexistent city
Тhe expected error is 400 Bad Request.

## Case 6: No available routes
Here we expect 200 OK with an empty list.

## Case 7: Identical origin and destination
Here we expect 200 OK with an empty list. 

## Case 8: Invalid JSON
Тhe expected error is 400 Bad Request.

## Case 9: Empty request 
Тhe expected error is 400 Bad Request.

## Case 10: Valid cities without routes in between 
Тhe expected error is 404 Not Found, but here we can also expect 200 OK with an empty list.


In Task 2 and Task 3 I used FastAPI because we are not creating anything so compared to REST there is no need for the request to be POST

