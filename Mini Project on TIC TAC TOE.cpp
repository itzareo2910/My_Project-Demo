/*A Mini Project to build a game TIC-TAC-TOE*/
#include<stdio.h>
void check_row(int(*)[3]);
void check_col(int(*)[3]);
void check_diagonals(int(*)[3]);
int flag=0;
int main()
{
    int a[3][3];
    int i,j;
    for(i=0;i<3;i++)
    {
        printf("Enter either 0 for 'O' or 1 for 'X':");
        for(j=0;j<3;j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
     for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    check_row(a);
    if(flag==0) {
    check_col(a);
    if(flag==0) {
    check_diagonals(a);
    if(flag==0)
    {
        printf("Game draw\n");
    }
    }
    }
    return 0;
}

void check_row(int (*a)[3])
{
    printf("Row_wise Checking\n");
    int i,j;
    int c=0;
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
           c=a[i][0];
           if(c==a[i][j])
           {
              if(j<2)
              continue;
         printf("Winner found at %dth row\n",i);
         flag=1;
            break;
           }
           else
           {
               printf("Winner not found.Check again\n");
               break;
           }
        }
        if(flag==1)
        {
            break;
        }
    }
}
void check_col(int (*a)[3])
{
    printf("Column_wise Checking\n");
    int i,j;
    int c=0;
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
           c=a[0][i];
           if(c==a[j][i])
           {
              if(j<2)
              continue;
         printf("Winner found at %dth col\n",i);
         flag=1;
            break;
           }
           else
           {
               printf("Winner not found.Check again\n");
               break;
           }
        }
        if(flag==1)
        {
            break;
        }
    }
}
void check_diagonals(int (*a)[3])
{
     printf("Diagonal_wise Checking\n");
     if(a[0][0]==a[1][1] && a[1][1]==a[2][2])
     {
         printf("Winner found at leading diagonal\n");
         flag=1;
     }
     else if(a[0][2]==a[1][1] && a[1][1]==a[2][0])
     {
         printf("Winner found at second diagonal\n");
         flag=1;
     }
     else
     {
          printf("Winner not found.Check again\n");
     }
}
