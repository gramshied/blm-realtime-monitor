#pragma once

#include <atomic>

const int BUFFER_SIZE = 100;

class RingBuffer
{
private:
    double buffer[BUFFER_SIZE];

    std::atomic<int> head{0};
    std::atomic<int> tail{0};

public:

    bool push(double value)
    {
        int next_head = (head + 1) % BUFFER_SIZE;

        if(next_head == tail)
        {
            return false;
        }

        buffer[head] = value;
        head = next_head;

        return true;
    }

    bool pop(double &value)
    {
        if(tail == head)
        {
            return false;
        }

        value = buffer[tail];
        tail = (tail + 1) % BUFFER_SIZE;

        return true;
    }
};
