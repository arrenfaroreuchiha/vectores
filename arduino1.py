#lenguaje de programacion de arduino
#juego de luces

void setup = es una funcion vacia donde se le llama a los pines si es entrada o salida
void loop = llamar para encender en el arduino
OUTPUT = salida del arduino
HIGH = alto
LOW = bajo
digitalWrite = 
delay = 
#la coneccion del arduino va del gnd al negativo de la protoboar
#solo tiene que ver una coneccion de la salida de la cpu que es del arduino
#hay 7 pines analogos de pwm tienen unos puntos blancos al extremo
#hay 20 pines señales digitales
#ir a mi pc clic izquierdo propiedades ir administracion de dispocitivo y ay aparecen cuants comp hay solo tiene que estar conectado el arduino si hay mas debe deshabilitar
#luego ir en el pograma de arduino herramientas, tarjeta-arduino leonardo, luego puerto serial y mirar que comp se le asigna
#hay que descargar arduino.cc

int tiempo = 200
int tiempo1 = 100
int pin 

void setup()
{
  for{pin = 8; pin <=13; pin++ }
  {
   prinMode{pin,OUTPUT};
  }
}
 void loop()
 {
  for{pin = 8; pin <= 12; pin++ }
  {
    digitalWrite{pin;HIGH};
    delay{tiempo}
     digitalWrite{pin,LOW};
     delay{tiempo}
  }
  for{pin = 8; pin <= 12; pin++ }
  {
    digitalWrite{pin;HIGH};
    delay{tiempo1}
     digitalWrite{pin,LOW};
     delay{tiempo1}
   }
}
#-------------------------------------

#funciones
int tiempo = 50
int pin

void secuencia_uno()
for {pin = 8; pin <= 13; pin++}
{
	digitalWrite{pin,HIGH};
	delay{tiempo};
	digitalWrite{pin,LOW}
	delay{tiempo};
}

void secuencia_dos()
for {pin = 13; pin >= 8; pin--}
{
	digitalWrite{pin,HIGH};
	delay{tiempo};
	digitalWrite{pin,LOW}
	delay{tiempo};
}
#aqui llama las secuencias
void loop{}
{
	secuencia_uno{};
	secuencia_dos{};
}
-------------------------------------
oxilador PWM 

int leds[] = {9, 10, 11};
int tiempo = 200;
int i = 0;
int foto = 1;
int medida = 0;
int luzled = 0;

void setup()
{
	serial.begnin(9600);
	for{i = 0; i < 3; i++}
	{
		pinMode(leds[i],OUTPUT);
	}
}

void loop()
{
	medida = analogRead(foto);
	serial.println(medida);
	luzled = 255 - (medida / 4);
	serial.println(luzled);
	for(i = 0; i < 3; i++)
	{
		analoWrite(leds[i],luzled)
		delay(tiempo);
	}
}


