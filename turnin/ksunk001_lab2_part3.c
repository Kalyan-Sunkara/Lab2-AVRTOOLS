/*	Author: ksunk001
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #2  Exercise #2
 *	Exercise Description: 
 *	Parking sensor part 1
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
	DDRC = 0xFF;
	PORTC = 0x00;
	DDRA = 0x00;
	PORTA = 0xFF;
    /* Insert your solution below */
	unsigned char tmpA0 = 0x00;
	unsigned char tmpA1 = 0x00;
	unsigned char tmpA2 = 0x00;
	unsigned char tmpA3 = 0x00;
	unsigned char cntavail = 0x00;
    while (1) {
	tmpA0 = PINA & 0x01;
	tmpA1 = (PINA & 0x02) >> 1;
	tmpA2 = (PINA & 0x04) >> 2;
	tmpA3 = (PINA & 0x08) >> 3;
	cntavail = 0x04 - (tmpA0 + tmpA1 + tmpA2 + tmpA3);
	if(cntavail == 0x00){
		cntavail = cntavail | 0x80;
	}
	PORTC = cntavail;
	}
    return 1;
}
