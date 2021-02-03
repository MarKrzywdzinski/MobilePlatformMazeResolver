################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Src/adc.c \
../Src/gpio.c \
../Src/main.c \
../Src/stm32f1xx_hal_msp.c \
../Src/stm32f1xx_it.c \
../Src/syscalls.c \
../Src/sysmem.c \
../Src/system_stm32f1xx.c \
../Src/tim.c \
../Src/usart.c 

OBJS += \
./Src/adc.o \
./Src/gpio.o \
./Src/main.o \
./Src/stm32f1xx_hal_msp.o \
./Src/stm32f1xx_it.o \
./Src/syscalls.o \
./Src/sysmem.o \
./Src/system_stm32f1xx.o \
./Src/tim.o \
./Src/usart.o 

C_DEPS += \
./Src/adc.d \
./Src/gpio.d \
./Src/main.d \
./Src/stm32f1xx_hal_msp.d \
./Src/stm32f1xx_it.d \
./Src/syscalls.d \
./Src/sysmem.d \
./Src/system_stm32f1xx.d \
./Src/tim.d \
./Src/usart.d 


# Each subdirectory must supply rules for building sources it contributes
Src/adc.o: ../Src/adc.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/adc.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/gpio.o: ../Src/gpio.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/gpio.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/main.o: ../Src/main.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/main.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/stm32f1xx_hal_msp.o: ../Src/stm32f1xx_hal_msp.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/stm32f1xx_hal_msp.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/stm32f1xx_it.o: ../Src/stm32f1xx_it.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/stm32f1xx_it.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/syscalls.o: ../Src/syscalls.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/syscalls.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/sysmem.o: ../Src/sysmem.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/sysmem.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/system_stm32f1xx.o: ../Src/system_stm32f1xx.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/system_stm32f1xx.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/tim.o: ../Src/tim.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/tim.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Src/usart.o: ../Src/usart.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F103xB -DDEBUG -c -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc -I../Inc -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Device/ST/STM32F1xx/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/CMSIS/Include -IC:/Users/marcin/STM32Cube/Repository/STM32Cube_FW_F1_V1.8.0/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/usart.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

