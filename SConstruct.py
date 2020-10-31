import os
env = Environment(ENV = os.environ)
 
env['AR'] = 'arm-none-eabi-ar'
env['AS'] = 'arm-none-eabi-as.exe'
env['CC'] = 'arm-none-eabi-gcc'
env['CXX'] = 'arm-none-eabi-g++'
env['LINK'] = 'arm-none-eabi-g++'                # predefined is 'arm-none-eabi-gcc'
env['RANLIB'] = 'arm-none-eabi-ranlib'
env['OBJCOPY'] = 'arm-none-eabi-objcopy'
env['PROGSUFFIX'] = '.elf'
 
# include locations
env['CPPPATH'] = [
    '#Drivers/CMSIS/Include',
    '#Drivers/CMSIS/Device/ST/STM32F1xx/Include',
    '#Drivers/STM32F1xx_HAL_Driver/Inc',
    '#Drivers/STM32F1xx_HAL_Driver/Inc/Legacy',
    '#Inc',
    ]
 
# compiler flags
env.Append(CCFLAGS = [
    '-mcpu=cortex-m3',
    '-mthumb',
    #'-mfpu=fpv4-sp-d16',
    '-mfloat-abi=soft',
    '-O0',
    '-g3',
    '-fsigned-char',
    '-ffunction-sections',
    '-fdata-sections',
    '-std=gnu11',
    '-fmessage-length=0',
    '-mthumb-interwork',
    ])

env.Append(CXXFLAGS = [
    '-mcpu=cortex-m3',
    '-mthumb',
    '-mfloat-abi=soft',
    '-O0',
    '-g3',
    '-fsigned-char',
    '-ffunction-sections',
    '-fdata-sections',
    #'-std=gnu11',
    '-fmessage-length=0',
    '-mthumb-interwork',
    ])
 
# linker flags
env.Append(LINKFLAGS = [
    '-ffunction-sections',
    '-fdata-sections',
    '-TSTM32F103C8Tx_FLASH.ld',
    '-Xlinker',
    '--gc-sections',
    #'--specs=nano.specs',
    '--specs=nosys.specs',
    '-mcpu=cortex-m3',
    '-mthumb',
    '-mfloat-abi=soft',
    ]) 
 
# defines
env.Append(CPPDEFINES = [
    'STM32F103xx',
	'STM32F103xB'
    'USE_HAL_DRIVER',
    'USE_FULL_LL_DRIVER',
])

srcFiles = [
        'Src/main.c',
        'Src/stm32F1xx_hal_msp.c', # msp library not used
        'Src/stm32F1xx_it.c',
		'Src/system_stm32F1xx.c',
        'startup_stm32F103xb.s',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_adc.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_adc_ex.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_cortex.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_dma.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_exti.c',
		'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_flash.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_flash_ex.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_gpio.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_pwr.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_rcc.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_rcc_ex.c',
		'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_spi.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_tim.c',
		'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_tim_ex.c',
        'Drivers/STM32F1xx_HAL_Driver/Src/stm32F1xx_hal_uart.c'
    ]

buildDir    = 'build'
objDir      = buildDir + '/' + 'all_object_files'
binaryName  = 'main'

#var_src = [ buildDir + '/' + f for f in srcFiles]
#files = Glob('build\*.c')

for n, source in enumerate(srcFiles):
    obj_file = objDir + '/' + source.replace('.cpp', '.o').replace('.c', '.o').replace('.s', '.o')
    srcFiles[n] = env.Object(source=source, target=obj_file)

# build everything
prg = env.Program(
    target = buildDir + '/' + binaryName,
    source = srcFiles,
)

# binary file builder
def arm_generator(source, target, env, for_signature):
    return '$OBJCOPY -O binary %s %s'%(source[0], target[0])
env.Append(BUILDERS = {
    'Objcopy': Builder(
        generator=arm_generator,
        suffix='.bin',
        src_suffix='.elf'
    )
})
 
env.Objcopy(prg)
