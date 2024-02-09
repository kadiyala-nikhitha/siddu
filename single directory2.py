#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct
{
char dname[10],fname[10][10];
int fcnt;
}dir;
void main()
{
int i,ch;
char f[30];
dir.fcnt=0;
print("\n enter name of directory-")
scanf("%s",dir.name);
while(1)
{
printf("\n\n1.Create File\t2.Delete File\t3.Search File\n4.Display Files\t5.Exit\nEnter your choice-");
scanf("%d",&ch);
switch(ch)
{
case 1:
printf("\nEnter the name of the file-");
scanf("%s",dir.fname[dir.fcnt]);
dir.fcnt++;
break;

