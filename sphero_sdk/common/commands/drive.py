#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x16-driving.json
# Device ID:          0x16
# Device Name:        drive
# Timestamp:          10/12/2019 @ 01:43:14.085581 (UTC)

from sphero_sdk.common.enums.drive_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def raw_motors(left_mode, left_speed, right_mode, right_speed, target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.raw_motors,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='leftMode',
                data_type='uint8_t',
                index=0,
                value=left_mode,
                size=1
            ),
            Parameter( 
                name='leftSpeed',
                data_type='uint8_t',
                index=1,
                value=left_speed,
                size=1
            ),
            Parameter( 
                name='rightMode',
                data_type='uint8_t',
                index=2,
                value=right_mode,
                size=1
            ),
            Parameter( 
                name='rightSpeed',
                data_type='uint8_t',
                index=3,
                value=right_speed,
                size=1
            ),
        ],
    }


def reset_yaw(target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.reset_yaw,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def drive_with_heading(speed, heading, flags, target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.drive_with_heading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='speed',
                data_type='uint8_t',
                index=0,
                value=speed,
                size=1
            ),
            Parameter( 
                name='heading',
                data_type='uint16_t',
                index=1,
                value=heading,
                size=1
            ),
            Parameter( 
                name='flags',
                data_type='uint8_t',
                index=2,
                value=flags,
                size=1
            ),
        ],
    }


def enable_motor_stall_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.enable_motor_stall_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_motor_stall_notify(target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.motor_stall_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='motorIndex',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='isTriggered',
                data_type='bool',
                index=1,
                size=1,
            ),
        ]
    }


def enable_motor_fault_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.enable_motor_fault_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_motor_fault_notify(target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.motor_fault_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='isFault',
                data_type='bool',
                index=0,
                size=1,
            ),
        ]
    }


def get_motor_fault_state(target, timeout): 
    return { 
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.get_motor_fault_state,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='isFault',
                data_type='bool',
                index=0,
                size=1,
            ),
        ]
    }
