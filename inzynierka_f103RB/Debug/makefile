################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Startup/subdir.mk
-include Src/subdir.mk
-include Drivers/STM32F1xx_HAL_Driver/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
inzynierka_f103RB.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
inzynierka_f103RB.list \

OBJCOPY_BIN += \
inzynierka_f103RB.bin \


# All Target
all: inzynierka_f103RB.elf secondary-outputs

# Tool invocations
inzynierka_f103RB.elf: $(OBJS) $(USER_OBJS) C:\Users\marcin\Documents\Stm32\1True\inzynierka_f103RB\STM32F103RBTX_FLASH.ld
	arm-none-eabi-gcc -o "inzynierka_f103RB.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"C:\Users\marcin\Documents\Stm32\1True\inzynierka_f103RB\STM32F103RBTX_FLASH.ld" --specs=nosys.specs -Wl,-Map="inzynierka_f103RB.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

inzynierka_f103RB.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "inzynierka_f103RB.list"
	@echo 'Finished building: $@'
	@echo ' '

inzynierka_f103RB.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "inzynierka_f103RB.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
