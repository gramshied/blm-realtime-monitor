cmake_minimum_required(VERSION 3.10)

project(BLM_Simulator)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(blm_simulator
    src/main.cpp
    src/detector.cpp
    src/monitor.cpp
)
