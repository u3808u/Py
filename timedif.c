#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
static int first_flag = 1;

int main(){
    FILE *fp;
    int tmp = 0;
    char buffer[128];
    double timedif = 0;
    time_t prev, now;

    while(1){
        if(first_flag == 1){
            puts("---------------------------------");
            time(&now);
            if((fp = fopen("./datetime", "w")) != NULL){
                sprintf(buffer, "%d\0", (int)now);
                fputs(buffer, fp);
            }
            first_flag = 0;
            fclose(fp);
            continue;
        }
        time(&now);
        //printf("now : %d\n", (int)now);
        if((fp = fopen("./datetime","r"))==NULL){
            puts("failed to open datetime mode read");
        }

        if(fgets(buffer, sizeof(buffer), fp)!=NULL){
            //buffer[strlen(buffer)-1] = '\0';
            printf("buffer : %s \n", buffer);
            sscanf(buffer,"%d", &tmp);
            prev = (time_t)tmp;
        }
        else{
            puts("못읽음");
        //  sprintf(buffer, "%d", (int)now);
        //  fputs(buffer, fp);
        }
        fclose(fp);

        if((fp = fopen("./datetime", "w")) == NULL)
            puts("faile write datetime");
        //timedif = (double)(now - prev);
        timedif = -45;
        printf("timedif : %.0lf\n", timedif);
        if(timedif < -90){
            puts("RRD create.");
            return 0;
        }
        else if(timedif >= -90 || timedif < 0){
            puts("time shift.\n");
            now = time(&now) + (time_t)(timedif*2);
            stime(&now);
            printf("now : %d\n", (int)now);
            puts("========================================");
            sprintf(buffer, "%d", (int)now);
        //  buffer[strlen(buffer)-1] = '\0';
            fputs(buffer, fp);
        }
        else if(timedif >= 0 || timedif < 86400 ){
            puts("in a day.");
        }
        else{
            puts("RRD create.");
            return 0;
        }

        fclose(fp);
        sleep(2);
    }
        return 0;
}
