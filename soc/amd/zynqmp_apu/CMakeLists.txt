# Copyright (c) 2025, Stefan Jaritz
#
# SPDX-License-Identifier: Apache-2.0

zephyr_sources(
  soc.c
  arm_mpu_regions.c
)

zephyr_include_directories(.)

set(SOC_LINKER_SCRIPT ${ZEPHYR_BASE}/include/zephyr/arch/arm64/scripts/linker.ld CACHE INTERNAL "")

