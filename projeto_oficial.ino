#include <LiquidCrystal_I2C.h>
#include <EmonLib.h>
#include <Wire.h>

#define VOLT_CAL 520// VALOR DE CALIBRAÇÃO (DEVE SER AJUSTADO EM PARALELO COM UM MULTÍMETRO)

float potencia = 0; 
float valor_real = 0;
float tarifa = 120;
float total_taxa;

EnergyMonitor SCT013; // Cria uma instancia pra corrente
EnergyMonitor emon1; //CRIA UMA INSTÂNCIA pra tensao

// Inicializa o display no endereco 0x27
LiquidCrystal_I2C lcd (0x27,16,2);

double tempo;

void setup()
{
 emon1.voltage(0, VOLT_CAL, 1.7); //PASSA PARA A FUNÇÃO OS PARÂMETROS (PINO ANALÓGIO / VALOR DE CALIBRAÇÃO / MUDANÇA DE FASE)
 SCT013.current(1, 6.0606);
 Serial.begin(9600);
 pinMode(A1,INPUT);
 lcd.init();
 lcd.setBacklight(HIGH);
}

void loop()
{

 
 double Irms = SCT013.calcIrms(1480); // Calcula o valor da Corrente

 float supplyVoltage = emon1.Vrms;

 emon1.calcVI(17,2000); 
 
 potencia = (Irms * supplyVoltage) ; // Calcula o valor da Potencia Instantanea

 total_taxa =(tarifa/3600)*2.02116;
 
 valor_real = valor_real + (((potencia)/1000)*total_taxa); // Calcula o valor do custo em relacao à potencia consumida

 delay(200);
 
 //lcd.clear();
 //lcd.setCursor(0,0);
 //lcd.print("VALOR REAL = ");
 //lcd.print(valor_real);
 
 
  lcd.setCursor(0,0);          
  lcd.print("POT:");
  lcd.print(potencia);
  lcd.setCursor(0,1); 
  lcd.print("V:");
  lcd.print(supplyVoltage, 1);
  delay(1000);  
  lcd.clear();
  lcd.setCursor(0,0);  
  lcd.print("I:");
  lcd.print(Irms);
  lcd.setCursor(0,1); 
  lcd.print("R$: ");
  lcd.print(valor_real);
  delay(1000);  

  tempo = millis();
  
  Serial.println(String(potencia) + "|" + String(supplyVoltage) + "|" + String(Irms) + "|" + String(valor_real) + "|" + String(tempo/1000));
  //Serial.println(valor_real,7);
  //delay(3000); //Aguarda 30 segundos

}
