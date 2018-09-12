#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define BUF_SIZE 64

struct iface{
    int rx_byte;
    int tx_byte;
    int rx_packet;
    int tx_packet;
};

static char interface[128][BUF_SIZE];
static char read_buf[4096];
int main(){
    FILE *fp;
    char *running;
    char *token;
    char delimiter[] = " ,";
    int x = 0;
    int y = 0;
    struct iface ifaces[42];
    char eth[3];
    int ethnum[42] = { 0, };
    int iface_flags[42] = {
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0 };

    fp = fopen("./test1.txt", "r");

    while(fgets(read_buf, 4095, fp)){
        sscanf(read_buf,"eth%d,%d,%d,%d,%d", &ethnum[x],&ifaces[x].rx_byte,
                &ifaces[x].tx_byte, &ifaces[x].rx_packet, &ifaces[x].tx_packet);
        printf("ethnum : %d\trbyte : %d\ttbyte : %d\trpacket : %d\ttpacket : %d\n", ethnu
m[x], ifaces[x].rx_byte, ifaces[x].tx_byte, ifaces[x].rx_packet, ifaces[x].tx_packet);
        x++;
    }

    printf("로우 개수 : %d\n", x);

    for(y=0; y < x ; y++)
        iface_flags[ethnum[y]] = 1;
    for(y=0; y < 42; y++)
         printf("iface flag%d : %d \tethnum : %d\n", y, iface_flags[y], ethnum[x]);
     puts("Interface Informations");
     for(y=0,x=0; y < 42; y++){
         if(iface_flags[y] != 0){
             printf("eth%d\n rbyte : %d\ttbyte : %d\trpacket : %d\ttpacket : %d\n"
                , y, ifaces[x].rx_byte, ifaces[x].tx_byte,
                     ifaces[x].rx_packet, ifaces[x].tx_packet);
             x++;
         }
     }

     return 0;
 }

