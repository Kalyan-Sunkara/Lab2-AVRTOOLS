/*	Author: ksunk001
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #2  Exercise #1
 *	Exercise Description: 
 *	Garage Open at night
 *	[optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	DDRB = 0xFF;
	PORTB = 0x00;
	DDRA = 0x00;
	PORTA = 0xFF;
    /* Insert your solution below */
	unsigned char tmpA0 = 0x00;
	unsigned char tmpA1 = 0x00;
	unsigned char tmpB = 0x00;
    while (1) {
	tmpA0 = PINA & 0x01;
	tmpA1 = PINA & 0x02;
	if(tmpA0 && !tmpA1){
		tmpB = 0x01;
	}
	else{
		tmpB = 0x00;
	}
	PORTB = tmpB;
    }
    return 1;
}
