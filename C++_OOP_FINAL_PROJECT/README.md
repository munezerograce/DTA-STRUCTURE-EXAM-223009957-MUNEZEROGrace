# C++ OOP Final Project – Hotel Reservation System

## Assigned Task
- Use OOP to manage hotel rooms and reservations
- Implement inheritance, polymorphism, dynamic memory
- Create base and derived room types
- Allow adding, removing, and reserving rooms

## How It Was Completed
- RoomBase is an abstract class with virtual reserve() and isReserved() methods
- EconomyRoom and LuxuryRoom inherit from RoomBase and implement the methods
- Reservation dates are stored dynamically
- Hotel class manages room list using dynamic array and pointer arithmetic
- main() demonstrates creation, reservation, removal, and display

## Annotated Code

```cpp
struct Date { int day, month, year;
bool operator==(const Date& d) const {
 return day==d.day && month==d.month && year==d.year; } }
