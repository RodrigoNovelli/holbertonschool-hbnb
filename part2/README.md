# Project Name

## Overview

This project is a platform where users can add places and find one to rent, leave reviews, and more. It follows a modular structure using classes to represent different entities and their relationships in the system. Below are the descriptions of the key classes within the project, their attributes, and responsibilities.

---

## Class Descriptions

### User Class

The `User` class represents a user of the platform. they can be `owners` of a `Place`

#### Attributes:
- **id** (String): A unique identifier for each user.
- **first_name** (String): The first name of the user (Required, max 50 characters).
- **last_name** (String): The last name of the user (Required, max 50 characters).
- **email** (String): The email address of the user (Required, must be unique and follow standard email format).
- **is_admin** (Boolean): Indicates whether the user has administrative privileges (Default is `False`).
- **created_at** (DateTime): Timestamp when the user was created.
- **updated_at** (DateTime): Timestamp when the user was last updated.

---

### Place Class

The `Place` class represents a location or property listed on the platform. It stores the details about the place including its pricing, location, and ownership.

#### Attributes:
- **id** (String): A unique identifier for the place.
- **title** (String): The title of the place (Required, max 100 characters).
- **description** (String): A detailed description of the place (Optional).
- **price** (Float): The price per night for the place (Must be a positive value).
- **latitude** (Float): The latitude coordinate for the place's location (Range between -90.0 to 90.0).
- **longitude** (Float): The longitude coordinate for the place's location (Range between -180.0 to 180.0).
- **owner** (User): A reference to the `User` instance who owns the place (Must be validated to ensure the owner exists).
- **created_at** (DateTime): Timestamp when the place was created.
- **updated_at** (DateTime): Timestamp when the place was last updated.

---

### Review Class

The `Review` class allows users to submit reviews for places they have stayed at. It includes the review text, rating, and references to the `Place` and `User` involved.

#### Attributes:
- **id** (String): A unique identifier for each review.
- **text** (String): The content of the review (Required).
- **rating** (Integer): A rating between 1 and 5 (Must be between 1 and 5).
- **place** (Place): A reference to the `Place` instance being reviewed (Must be validated to ensure the place exists).
- **user** (User): A reference to the `User` instance who wrote the review (Must be validated to ensure the user exists).
- **created_at** (DateTime): Timestamp when the review was created.
- **updated_at** (DateTime): Timestamp when the review was last updated.


---

### Amenity Class

The `Amenity` class represents the various amenities available at a place (e.g., Wi-Fi, parking). It allows the platform to manage and list these amenities for each place.

#### Attributes:
- **id** (String): A unique identifier for each amenity.
- **name** (String): The name of the amenity (e.g., "Wi-Fi", "Parking") (Required, max 50 characters).
- **created_at** (DateTime): Timestamp when the amenity was created.
- **updated_at** (DateTime): Timestamp when the amenity was last updated.

---
