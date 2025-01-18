cmake_minimum_required(VERSION 3.8)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_target(
	genBuildNumber ALL
	COMMAND ${Python3_EXECUTABLE} ${gDir}/genBuildNumber.py -w ${sDir}
	BYPRODUCTS ${srcDir}/_gen_buildNumber.h
	COMMENT "generating build number"
)

list(APPEND INC
	${srcDir}
)

list(APPEND SRC
	${srcDir}/main.c
)

target_sources(app PRIVATE ${SRC})

target_include_directories(app PRIVATE ${INC})
