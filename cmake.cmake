cmake_minimum_required(VERSION 3.10)
project(pybind)
add_subdirectory(pybind11)
pybind11_add_module(websocket simplechat.cpp)