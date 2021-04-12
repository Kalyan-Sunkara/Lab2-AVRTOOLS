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
	DDRD = 0xFF;
	PORTD = 0x00;
	DDRA = 0x00;
	PORTA = 0xFF;
	DDRB = 0x00;
        PORTB = 0xFF;
	DDRC = 0x00;
        PORTC = 0xFF;
    /* Insert your solution below */
	unsigned char tmpA = 0x00;
	unsigned char tmpB = 0x00;
	unsigned char tmpC = 0x00;
	unsigned char tmpD = 0x00;
	//unsigned char tmpD1 = 0x00;
	unsigned char total = 0x00;
    while (1) {
	tmpA = PINA;
	tmpB = PINB;
	tmpC = PINC;
	tmpD = 0;
	total = tmpA + tmpB + tmpC;
	if(total > 140){
		tmpD = tmpD | 0x01;  
	}
	if((tmpC - tmpA) > 80){
		tmpD = tmpD | 0x02;
	}
	else if((tmpA - tmpC) > 80){
		tmpD = tmpD | 0x02;
	}
	else{
		tmpD = tmpD & 0xFD;
	}
	total = total & 0xFC;
	PORTD = tmpD | total;
	}
    return 1;
}
