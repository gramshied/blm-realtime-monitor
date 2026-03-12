#include "../include/ring_buffer.hpp"
#include <thread>

RingBuffer ringBuffer;

void detector();
void monitor();

int main()
{
    std::thread t1(detector);
    std::thread t2(monitor);

    t1.join();
    t2.join();
}
