cmake_minimum_required(VERSION 3.26)
project(Uni_Tasks)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Uni_Tasks
        Car.cpp
        Car.h
        main.c++)
