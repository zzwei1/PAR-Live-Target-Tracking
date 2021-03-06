// gcc -o spi_initate spi_initiate.c -l bcm2835

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <bcm2835.h>

void error(const char *msg);
void writeBeamformerRegister(char *reg, char *data);
void BeamSteering();

#define MAXBUFFER       8
#define COMMANDLENGTH   4  // command field length in nybbles
#define DATALENGTH      2  // data field length in nybbles

int main(int argc, char *argv[]) {
  if(argc < 3) {
    fprintf(stderr,"sudo ./spitest cmd(4) dat(2)\n");
    exit(1);
  } // end if()

// begin setup RPi SPI interface
  if(!bcm2835_init())
    return 1;
  bcm2835_spi_begin();
  bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      // The default
  bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   // The default
  bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_65536); // The default

  Init_ADAR1000(); // initialize beamformer register

  bcm2835_spi_end();
  bcm2835_close();
  return 0;
} // end main()

void error(const char *msg) {
    perror(msg);
    exit(1);
} //end error()

void writeBeamformerRegister(char *reg, char *data, int cs) {
  char buffer[MAXBUFFER],
       command_string[COMMANDLENGTH + 1],
       data_string[DATALENGTH + 1],
       writebuffer[MAXBUFFER];
  int ii,
      n,
      ishex = 0;

  char spibuf[3];

  int command = 0,
      data = 0;
      //buffer = 0;

  //  bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_1024);
  if(cs) {
    // write to the second beamformer register
    bcm2835_spi_chipSelect(BCM2835_SPI_CS1);                      
    bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS1, LOW);      
  }
  else {
    // write to the first beamformer register
    bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);      
  }
// end setup RPi SPI interface

  sscanf(reg, "%x", &command);
  sscanf(reg, "%s", command_string);
  sscanf(data, "%x", &data);
  sscanf(data, "%s", data_string);

  for(ii = 0; ii < 4; ii++) {
    if(!((command_string[ii] >= '0' && command_string[ii] <= '9') ||
         (command_string[ii] >= 'a' && command_string[ii] <= 'f') ||
         (command_string[ii] >= 'A' && command_string[ii] <= 'F'))) {
      sprintf(writebuffer, "command: %c\n", command_string[ii]);
      ishex = -1;
      exit(-1);
    }
  }

  for(ii = 0; ii < 2; ii++) {
    if(!((data_string[ii] >= '0' && data_string[ii] <= '9') ||
         (data_string[ii] >= 'a' && data_string[ii] <= 'f') ||
         (data_string[ii] >= 'A' && data_string[ii] <= 'F'))) {
      sprintf(writebuffer, "value: %c\n", data_string[ii]);
      ishex = -1;
      exit(-1);
    }
  }

  if(ishex >= 0) {
    spibuf[0] = command >> 8;
    spibuf[1] = command;
    spibuf[2] = data;
    fprintf(stderr, "%.2x %.2x %.2x\n", spibuf[0], spibuf[1], spibuf[2]);
    bcm2835_spi_transfern(spibuf, sizeof(spibuf));
    if(n < 0) error("ERROR writing to spi");
    fprintf(stderr, "%.2x %.2x %.2x\n", spibuf[0], spibuf[1], spibuf[2]);
  }
}

void BeamSteering() {
  // NEED DEFINITION FOR ARRAY VALUES HERE to be able to steer to correct locations
  unsigned int delay = 100000; // Delay for 0.1 seconds or 100 milliseconds or 100,000 microseconds

}
