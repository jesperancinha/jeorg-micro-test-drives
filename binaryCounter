
/* Led Binary counter */ 

int LED1 = 13;
int LED2 = 12;
int LED3 = 11;
int LED4 = 10;

int delayTime = 1000;
int count = 0;
int mask1 = 1;
int mask2 = 2;
int mask3 = 4;
int mask4 = 8;
void setup() {
   pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);
   pinMode(LED3, OUTPUT);
   pinMode(LED4, OUTPUT);
}


void loop() {
  if((count & mask1)>0){
      digitalWrite(LED1, HIGH); 
  } else {
      digitalWrite(LED1, LOW); 
  }
  if((count & mask2) > 0){
      digitalWrite(LED2, HIGH);
  } else {
      digitalWrite(LED2, LOW);
  }
  if((count & mask3) > 0){
    digitalWrite(LED3, HIGH);   
  } else {
    digitalWrite(LED3, LOW);   
  }
  if((count & mask4) > 0){
    digitalWrite(LED4, HIGH);    
  } else {
    digitalWrite(LED4, LOW);    
  }
  delay(delayTime);   
  count++;
  if(count == 16){
    count = 0;
  }
}
