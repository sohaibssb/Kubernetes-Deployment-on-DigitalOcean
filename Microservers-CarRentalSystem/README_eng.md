## Project name
* Microservers-CarRentalSystem

## Project description
* Microservers-CarRentalSystem is a project that aims to develop a comprehensive and efficient car rental system using microservices architecture. The system is designed to provide a seamless and user-friendly experience for both car rental agencies and customers.

## Project Structure
```
Microservers-CarRentalSystem/
└── src/
    ├── auth_service/
    ├── authentication/
    ├── cars_service/
    ├── gateway_service/
    ├── payment_service/
    ├── rental_service/
    └── statistique/

```

### Microservers-CarRentalSystem/src:


### src/auth_service:
* This module handles user authentication and authorization. It provides functionalities such as user registration, login, and access control.

### src/authentication:
* This app contains frontend code.

### src/cars_service:
* This service is responsible for managing the car inventory. It handles operations like adding new cars, updating car details, and retrieving car information.

### src/gate_way_service:
* This service serves as the entry point for external requests and acts as a gateway for accessing other microservices. It provides API endpoints for client applications to interact with the system.

### src/payment_service:
* This module handles payment processing for car rentals. It integrates with payment gateways or third-party services to handle payment transactions securely.

### src/rental_service:
* This module manages the rental process. It handles operations like creating rental bookings, calculating rental prices, and managing rental status.

### src/statistique/:
* This service is responsible for gathering and analyzing data related to car rentals.In this we use kafka. It provides statistical information and generates reports on rental patterns, revenue, and other relevant metrics.


---
Run the project

1. Clone the repository:
	```
	project git link = https://github.com/priyankush-siloria/ssb.git
	```

2. Navigate to the project directory:
	```
	- cd ssb/Microservers-CarRentalSystem
	```

3. Build the Docker image:
	```
	docker-compose build
	```
4. Run the Docker container:
	```
	docker-compoer up
	```
Click on [link](http://localhost:3000/) to test.


After login  your account will create automatically and send JWT tokens
