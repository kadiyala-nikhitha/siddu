single level directory
#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
int nf=0,i=0,j=0,ch;
char mdname[10],fname[10][10],name[10];
clrscr();
printf("enter the directory name:");
scanf("%d",&nf);
do
{
printf("enter file name to be created:");
scanf("%s",name);
for(i=0;i<nf;i++)
{
if(!strcmp(fname[i]))

break;
}
if(i==nf)
{
strcpy(fname[j++],name);
nf++;
}
else
printf("There is already %s\n",name);
printf("Do you want to enter another file(yes-1 or n0-0):");
for(i=0;i<j;i++)
printf("\n%s",fname[i]);
getch();
}

Output:
Enter the directory name:SSS
Enter the number of files:3
Enter file name to be created:aaa
Do you want to enter another file(yes-1 or no-0):1
Enter file name to be created:bbb
D0 you want to enter another file(yes-1 or no-0):0
Directory name is:SSS
aaa
bbb
ccc