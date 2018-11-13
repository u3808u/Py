#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <syslog.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#include <sys/wait.h>

void sig_handler(int signum){
    if(signum==SIGINT){
        printf("\n catched SIGINT > \n");
        exit(0);
    }

}
static void test_daemon(){

    int count=0;
    pid_t pid;

    pid = fork();

    if(pid<0)
        exit(EXIT_FAILURE);
    if(pid>0)
        exit(EXIT_SUCCESS);
    if(setsid()<0)
        exit(EXIT_FAILURE);

    signal(SIGCHLD, SIG_IGN);
    signal(SIGHUP, SIG_IGN);

    umask(027);

    chdir("/tmp");

    //while(count<5){
        pid = fork();
        if(pid<0)
            exit(EXIT_FAILURE);
        if(pid>0)
            exit(EXIT_SUCCESS);
        if(pid==0){
            if(signal(SIGINT, sig_handler) == SIG_ERR)
                printf("\n< Can't catch SIGINT >\n");
            while(count<5){
                printf("\ndaemon pid[%d] is working...\n", getpid());
                sleep(2);
                count++;
            }
        }

    //}

}

int main(){
    //if(signal(SIGINT, sig_handler) == SIG_ERR)
    //  printf("\ncan't catch SIGINT\n");

    test_daemon();

    return EXIT_SUCCESS;

}
