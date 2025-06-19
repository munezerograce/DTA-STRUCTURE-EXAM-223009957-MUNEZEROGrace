#include <iostream>

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
public:
    virtual bool isReserved(const Date* d) = 0;
    virtual void reserve(const Date* d) = 0;
    virtual ~RoomBase() { delete[] reservedDates; }
};

class EconomyRoom : public RoomBase {
public:
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

class LuxuryRoom : public EconomyRoom {
    // Same logic, could add extra rules
};

class Hotel {
    RoomBase** rooms = nullptr;
    int roomCount = 0;
public:
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
        if (id < 0 || id >= roomCount) return;
        delete rooms[id];
        RoomBase** newRooms = new RoomBase*[roomCount - 1];
        for (int i = 0, j = 0; i < roomCount; ++i)
            if (i != id) *(newRooms + j++) = *(rooms + i);
        delete[] rooms;
        rooms = newRooms;
        --roomCount;
    }

    ~Hotel() {
        for (int i = 0; i < roomCount; ++i) delete rooms[i];
        delete[] rooms;
    }

    RoomBase* getRoom(int i) { return i < roomCount ? rooms[i] : nullptr; }
};

// Example usage (optional):
// int main() {
//     Hotel h;
//     h.addRoom(new EconomyRoom());
//     Date d = {1, 1, 2025};
//     if (!h.getRoom(0)->isReserved(&d)) h.getRoom(0)->reserve(&d);
//     return 0;
// }
