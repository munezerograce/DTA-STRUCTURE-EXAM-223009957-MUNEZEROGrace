#include <iostream>
#include <string>

struct Date {
    int day, month, year;
    bool operator==(const Date& d) const {
        return day == d.day && month == d.month && year == d.year;
    }
};

class RoomBase {
protected:
    Date* reservedDates = nullptr;
    int reservedCount = 0;
    int roomId;
    std::string roomType;
public:
    RoomBase(int id, const std::string& type) : roomId(id), roomType(type) {}
    virtual ~RoomBase() { delete[] reservedDates; }
    virtual bool isReserved(const Date* d) = 0;
    virtual void reserve(const Date* d) = 0;
    int getId() const { return roomId; }
    std::string getType() const { return roomType; }
    void printReservations() {
        std::cout << "Room #" << roomId << " (" << roomType << ") Reservations:\n";
        for (int i = 0; i < reservedCount; ++i)
            std::cout << "  " << (reservedDates + i)->day << "/" << (reservedDates + i)->month << "/" << (reservedDates + i)->year << "\n";
    }
};

class EconomyRoom : public RoomBase {
public:
    EconomyRoom(int id) : RoomBase(id, "Economy") {}
    bool isReserved(const Date* d) override {
        for (int i = 0; i < reservedCount; ++i)
            if (*(reservedDates + i) == *d) return true;
        return false;
    }
    void reserve(const Date* d) override {
        if (isReserved(d)) return;
        Date* newDates = new Date[reservedCount + 1];
        for (int i = 0; i < reservedCount; ++i)
            *(newDates + i) = *(reservedDates + i);
        *(newDates + reservedCount) = *d;
        delete[] reservedDates;
        reservedDates = newDates;
        ++reservedCount;
    }
};

class LuxuryRoom : public RoomBase {
public:
    LuxuryRoom(int id) : RoomBase(id, "Luxury") {}
    bool isReserved(const Date* d) override {
        for (int i = 0; i < reservedCount; ++i)
            if (*(reservedDates + i) == *d) return true;
        return false;
    }
    void reserve(const Date* d) override {
        if (isReserved(d)) return;
        Date* newDates = new Date[reservedCount + 1];
        for (int i = 0; i < reservedCount; ++i)
            *(newDates + i) = *(reservedDates + i);
        *(newDates + reservedCount) = *d;
        delete[] reservedDates;
        reservedDates = newDates;
        ++reservedCount;
    }
};

class Hotel {
    RoomBase** rooms = nullptr;
    int roomCount = 0;
public:
    ~Hotel() {
        for (int i = 0; i < roomCount; ++i) delete rooms[i];
        delete[] rooms;
    }
    void addRoom(RoomBase* r) {
        RoomBase** newRooms = new RoomBase*[roomCount + 1];
        for (int i = 0; i < roomCount; ++i)
            *(newRooms + i) = *(rooms + i);
        *(newRooms + roomCount) = r;
        delete[] rooms;
        rooms = newRooms;
        ++roomCount;
    }
    void removeRoom(int id) {
        int idx = -1;
        for (int i = 0; i < roomCount; ++i)
            if (rooms[i]->getId() == id) idx = i;
        if (idx == -1) return;
        delete rooms[idx];
        RoomBase** newRooms = new RoomBase*[roomCount - 1];
        for (int i = 0, j = 0; i < roomCount; ++i)
            if (i != idx) *(newRooms + j++) = *(rooms + i);
        delete[] rooms;
        rooms = newRooms;
        --roomCount;
    }
    void reserveRoom(int id, const Date& d) {
        for (int i = 0; i < roomCount; ++i)
            if (rooms[i]->getId() == id)
                rooms[i]->reserve(&d);
    }
    void printAllReservations() {
        for (int i = 0; i < roomCount; ++i)
            rooms[i]->printReservations();
    }
};

int main() {
    Hotel hotel;
    hotel.addRoom(new EconomyRoom(101));
    hotel.addRoom(new LuxuryRoom(202));

    Date d1 = {18, 6, 2025};
    Date d2 = {19, 6, 2025};

    hotel.reserveRoom(101, d1);
    hotel.reserveRoom(202, d2);
    hotel.reserveRoom(101, d2);

    hotel.printAllReservations();

    hotel.removeRoom(101);

    std::cout << "\nAfter removing room 101:\n";
    hotel.printAllReservations();

    return 0;
}
