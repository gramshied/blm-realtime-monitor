#include "../include/ring_buffer.hpp"
#include <random>
#include <chrono>
#include <thread>

extern RingBuffer ringBuffer;

void detector()
{
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0.0,1.0);

    while(true)
    {
        double signal = distribution(generator);

        ringBuffer.push(signal);

        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}
