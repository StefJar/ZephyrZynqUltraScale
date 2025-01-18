cmake_minimum_required(VERSION 3.13.2)

set(BOARD_FLASH_RUNNER "openocd")

set(BOARD "mercury_xu_apu")
set(BOARD_ROOT "${CMAKE_SOURCE_DIR}")
set(SOC_ROOT "${CMAKE_SOURCE_DIR}")

# set(SHIELD "gorilla_empty")

add_compile_definitions(FW_DBG_LVL=4)

# set(CMAKE_EXPORT_COMPILE_COMMANDS Y)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(app)

set(srcDir "src")
set (gDir ${CMAKE_SOURCE_DIR}/gen)
set (sDir ${CMAKE_SOURCE_DIR}/src)

include("${CMAKE_SOURCE_DIR}/src/demo.cmake")
