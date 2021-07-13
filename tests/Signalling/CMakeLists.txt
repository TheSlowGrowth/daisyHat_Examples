daisyhat_add_firmware(
    NAME Signalling_firmware
    SOURCES 
        main.cpp
)
daisyhat_add_custom_test(
    NAME Signalling
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/testRunner.py --elf $<TARGET_FILE:Signalling_firmware>
)