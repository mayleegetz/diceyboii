#include <LiquidCrystal.h>
#include <Wire.h>
#include <Keypad.h>

//16by2, address 0x27

const byte n_rows = 4;
const byte n_cols = 4;
 
char keys[n_rows][n_cols] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
 
byte colPins[n_rows] = {27, 14, 12, 13};
byte rowPins[n_cols] = {32, 33, 25, 26};
 
Keypad myKeypad = Keypad( makeKeymap(keys), rowPins, colPins, n_rows, n_cols); 





void setup(){
  Serial.begin(115200);
}

void loop() {
  char myKey = myKeypad.getKey();
//  if (myKey != NULL){
//    Serial.print("Key pressed: ");
//    Serial.println(myKey);
//  }

  //display message for like 3 seconds
  //print("dicey boi-desu")

  //disappear to roll

  int tbc=0;
  while( myKey!='*' || myKey!='#'){
    tbc+=myKey;
    Serial.println(tbc);
  }



  





  int times, num;
  
  if( times>0 && times <=50 && num>1 && num<=10000){
    int rolls[times];
    int i;
  
    for( i=0; i<times; i++){
      rolls[i] = random(num);
    }
  }
}
