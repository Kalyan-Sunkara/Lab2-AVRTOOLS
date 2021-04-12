# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used)
tests = [ {'description': '0 kilograms => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00),('PINC',0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x00)],
    },
    {'description': 'Max kilograms => PORTD: 0xFD',
    'steps': [ {'inputs': [('PINA',0xFF),('PINB',0xFF),('PINC',0xFF)], 'iterations': 5 } ],
    'expected': [('PORTD',0xFD)],
    },
    {'description': '50,50,50 kilograms => PORTD: 0x95',
    'steps': [ {'inputs': [('PINA',0x32),('PINB',0x32),('PINC',0x32)], 'iterations': 5 } ],
    'expected': [('PORTD',0x95)],
    },
    {'description': '20,20,100 kilograms => PORTD: 0x8C',
    'steps': [ {'inputs': [('PINA',0x14),('PINB',0x14),('PINC',0x64)], 'iterations': 5 } ],
    'expected': [('PORTD',0x8C)],
    },
    {'description': '10,10,10 kilograms => PORTD: 0x1C',
    'steps': [ {'inputs': [('PINA',0x0A),('PINB',0x0A),('PINC',0x0A)], 'iterations': 5 } ],
    'expected': [('PORTD',0x1C)],
    },
    {'description': 'D1 on D0 off  => PORTD: 0x5E',
    'steps': [ {'inputs': [('PINA',0x05),('PINB',0x0A),('PINC',0x5A)], 'iterations': 5 } ],
    'expected': [('PORTD',0x6A)],
    },
   ]
#watch = ['PORTB']
