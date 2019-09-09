/* this program is the interpretation routine of standard output protocol of TFmini product on Arduino.
For details, refer to Product Specifications.
For Arduino boards with only one serial port like UNO board, the function of software visual serial port is
to be used.
*/
#include<SoftwareSerial.h>//header file of software serial port

SoftwareSerial Serial1(2, 3); //define software serial port name as Serial1 and define pin2 as RX and pin3 as TX
/* For Arduinoboards with multiple serial ports like DUEboard, interpret above two pieces of code and
directly use Serial1 serial port*/
int dist; //actual distance measurements of LiDAR
int strength; //signal strength of LiDAR
int check; //save check value
int i;
int uart[9]; //save data measured by LiDAR
struct Lidar {
  int distance;
  int strength;
};
struct Lidar lidar_vals;

int mapped_dist;
const int HEADER = 0x59; //frame header of data package

/* Set motor pin for vibration feedback */
const int motorPin = 5;

void setup() {
  Serial.begin(9600); //set bit rate of serial port connecting Arduino with computer
  Serial1.begin(115200); //set bit rate of serial port connecting LiDAR with Arduino
  pinMode(motorPin, OUTPUT);
}
void loop() {
  lidar();
  mapped_dist = map(lidar_vals.distance, 1, 400, 1, 255);
  Serial.println(lidar_vals.distance);
  analogWrite(motorPin, mapped_dist);
}

void lidar () {
  if (Serial1.available()) //check if serial port has data input
  {
    if (Serial1.read() == HEADER) //assess data package frame header 0x59
    {
      uart[0] = HEADER;
      if (Serial1.read() == HEADER) //assess data package frame header 0x59
      {
        uart[1] = HEADER;
        for (i = 2; i < 9; i++) //save data in array
        {
          uart[i] = Serial1.read();
        }
        check = uart[0] + uart[1] + uart[2] + uart[3] + uart[4] + uart[5] + uart[6] + uart[7];
        if (uart[8] == (check & 0xff)) //verify the received data as per protocol
        {
          dist = uart[2] + uart[3] * 256; //calculate distance value
          lidar_vals.distance = dist;
          strength = uart[4] + uart[5] * 256; //calculate signal strength value
          lidar_vals.strength = strength;
          Serial.print("LiDAR dist = ");
          Serial.print(dist); //output measure distance value of LiDAR
          Serial.print('\t');
          Serial.print("strength = ");
          Serial.print(strength); //output signal strength value
          Serial.print('\n');
          if (lidar_vals.distance > 400)
          {
            lidar_vals.distance = 400;
          }
          if (lidar_vals.distance <= 0)
          {
            lidar_vals.distance = 1;  
          }
        }
      }
    }
  }
  return 0;
}
