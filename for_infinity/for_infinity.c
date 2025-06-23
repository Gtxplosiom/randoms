#include <stdio.h>
#include <windows.h>

void select_loop();
void sleeping_index(void);
void limbo(void);
void hesitation(void);
void sisyphus(void);
void depression(void);

int main(void)
{ 
  printf("\nChoose a cursed for-loop technique:\n");
  printf("1. Sleeping Index\n");
  printf("2. Limbo\n");
  printf("3. Hesitation\n");
  printf("4. Sisyphus\n");
  printf("5. Depression\n");
  printf("0. Exit\n");

  select_loop();
}

void select_loop()
{
  int choice;

  do
  {
    printf("Input the number of your choice: ");
    scanf("%i", &choice);
    
    if (choice == 1)
    {
      printf("\"The sleeping index\"\n");
      sleeping_index();
    }
    else if (choice == 2)
    {
      printf("\"The limbo\"\n");
      limbo();
    }
    else if (choice == 3)
    {
      printf("\"The hesitation\"\n");
      hesitation();
    }
    else if (choice == 4)
    {
      printf("\"The Sisyphus\"\n");
      sisyphus();
    }
    else if (choice == 5)
    {
      printf("\"The depression\"\n");
      depression();
    }
  } while (choice != 0);
}

void sleeping_index(void)
{
  for (int i = 0; i < 1; i)
  {
    printf("z");
    Sleep(500);
  }
}

void limbo(void)
{
  for (int i = 0; i < 1; i++)
  {
    printf("-");
    Sleep(500);
    i--;
  }
}

void hesitation(void)
{
  for (int i = 0; i < 10; i++)
  {
    printf("%i", i);
    Sleep(500);

    if (i == 9)
    {
      i = 7;
    }
  }
}

void sisyphus(void)
{
  for (int i = 0; i < 10; i++)
  {
    printf("%i", i);
    Sleep(500);

    if (i == 9)
    {
      i = i - i;
    }
  }
}

void depression(void)
{
  int goal = 10;
  int crisis = 0;
  for (int i = 0; i < goal; i++)
  {
    printf("%i", i);
    Sleep(500);
    if (i == 9)
    {
      for (int j = 9; j >= 0; j--)
      {
        printf("%i", j);
        Sleep(500);
      }
      goal = 1;
      i = 0;
      crisis = 1;
    }
    if (crisis == 1)
    {
      i--;
    }
  }
}
