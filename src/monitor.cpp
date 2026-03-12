#include "../include/ring_buffer.hpp"
#include <iostream>
#include <chrono>
#include <cmath>
#include <fstream>

extern RingBuffer ringBuffer;

void monitor()
{
    double threshold = 2.5;
    std::ofstream logfile("signal_stream.txt");

    while(true)
    {
        double value;

        if(ringBuffer.pop(value))
        {
            auto start = std::chrono::high_resolution_clock::now();

            std::cout << "Signal: " << value << std::endl;
            logfile << value << std::endl;

            if(std::abs(value) > threshold)
            {
                std::cout << "ALERT: Beam loss detected!" << std::endl;
            }

            auto end = std::chrono::high_resolution_clock::now();

            auto latency =
                std::chrono::duration_cast<std::chrono::microseconds>(end - start);

            std::cout << "Latency: " << latency.count() << " us" << std::endl;
        }
    }
}
