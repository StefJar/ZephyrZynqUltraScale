/*
 * Copyright (c) 2025, Stefan Jaritz
 */

#ifndef VERSION_H_
#define VERSION_H_

#include "_gen_buildNumber.h"

#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)

// firmware version
#define FW_VERSION "v0.1.0(b" STR(FW_BUILD_NUMBER) ")"

#endif /* VERSION_H_ */
