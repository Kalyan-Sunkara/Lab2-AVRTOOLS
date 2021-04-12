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
    {'description': '100, 20, 0  => PORTD: 0x1E',
    'steps': [ {'inputs': [('PINA',0x64),('PINB',0x14),('PINC',0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x1E)],
    },
    {'description': '50,50,50 kilograms => PORTD: 0x25',
    'steps': [ {'inputs': [('PINA',0x32),('PINB',0x32),('PINC',0x32)], 'iterations': 5 } ],
    'expected': [('PORTD',0x25)],
    },
    {'description': '10,20,30 kilograms => PORTD: 0x0C',
    'steps': [ {'inputs': [('PINA',0x0A),('PINB',0x14),('PINC',0x1E)], 'iterations': 5 } ],
    'expected': [('PORTD',0x0C)],
    },
    {'description': 'D1 and D0 off  => PORTD: 0x22',
    'steps': [ {'inputs': [('PINA',0x00),('PINB',0x38),('PINC',0x55)], 'iterations': 5 } ],
    'expected': [('PORTD',0x22)],
    },
   ]
#watch = ['PORTB']
