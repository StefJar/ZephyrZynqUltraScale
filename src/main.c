/*
 * Copyright (c) 2025, Stefan Jaritz
 *
 */

#include <stddef.h>
#include <string.h>
#include <errno.h>

#include <stdio.h>
#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>

#include <zephyr/logging/log.h>
#include <zephyr/logging/log_ctrl.h>
#include <zephyr/sys/reboot.h>

#include "_gen_buildNumber.h"
#include "dbglog.h"
#include "threadCfg.h"
#include "version.h"

LOG_MODULE_REGISTER(main, LOG_LEVEL_APP_MAIN);

typedef struct main_s {
	struct k_sem exitSem;
	bool rebootFlag;
} main_t;


main_t mainVar;

void main_gotoStandby(void) {
	LOG_DBG("activate standby");
	mainVar.rebootFlag = false;
	k_sem_give(&mainVar.exitSem);
}

void main_reboot(void) {
	LOG_DBG("trigger reboot");
	mainVar.rebootFlag = true;
	k_sem_give(&mainVar.exitSem);
}

int main(void) {
	k_sem_init(&mainVar.exitSem, 0, 0xFF);
	mainVar.rebootFlag = true;

	LOG_INF("starting %s on Zephyr v%u.%u.%u",
		//log_strdup(FW_VERSION),
		FW_VERSION,
		(unsigned int)SYS_KERNEL_VER_MAJOR(sys_kernel_version_get()),
		(unsigned int)SYS_KERNEL_VER_MINOR(sys_kernel_version_get()),
		(unsigned int)SYS_KERNEL_VER_PATCHLEVEL(sys_kernel_version_get())
	);

standby:
	k_thread_priority_set(k_current_get(), THREAD_PRIO_IDLE);
	LOG_DBG("startup done");
	k_sem_take(&mainVar.exitSem, K_FOREVER);

	if (false == mainVar.rebootFlag) {
		// enter standby
	} else {
		sys_reboot(SYS_REBOOT_COLD);
		sys_reboot(SYS_REBOOT_WARM);
	}
	return 0;
}

void k_sys_fatal_error_handler(unsigned int reason, const struct arch_esf * esf) {
	LOG_PANIC();
/*	for (;;) {

	}
*/
	sys_reboot(SYS_REBOOT_COLD);
	sys_reboot(SYS_REBOOT_WARM);
}
