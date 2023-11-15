#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char const *argv[])
{
	int pid = fork();
	if (pid == 0)
	{
		printf("soy el hijo\n");
		exit(0);
	}
	else if (pid > 0)
	{
		printf("soy el padre\n");
		system("ps -l");
		sleep(20);
	}
	system("ps -l");
	return 0;
}