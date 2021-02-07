

main
		MOV R10, #0 ; Записываем 0 для дальнейшего использования
		MOV R11, #1 ; Записываем 1 аналогично 0

		; Настраиваем систему тактирования.
		BL init

		MOV32 R12, 0x42000000 + 0x1080C * 32 + 24; Записываем в регистр адрес бита ODR регистра вывода 6
		MOV R1, 8000000 ; R0 - light time
		MOV R2, #0 ; R1 - ... time
loop
		STR R11, [R12]

		MOV R0, R1;
		BL delay

		STR R10, [R12]

		MOVS R0, R2;
		
		BL delay

		B loop

delay
		PUSH {R0}
delay_loop
		SUBS R0, #1
		BNE delay_loop
		POP {R0}
		BLX LR

init
		PUSH {R0}

		MOV32 R0, 0x42000000 + 0x21018 * 32 + 8
		STR R11, [R0]

		MOV32 R0, 0x42000000 + 0x10800 * 32 + 96
		STR R11, [R0], #8

		STR R10, [R0], #4
		STR R10, [R0]

		POP {R0}

		BLX LR
		
; while (1) {
;	  odr = 1;
;	  delay (light_time);
;     odr = 0;
;     delay (period - light_time);
;     light_time += time_step
