#include <stdio.h>
#include <string.h>

int main() {
    char text[500];
    int shift,i;
    fgets(text, 500, stdin);
    for (i = 0; text[i]; i++) 
    { 
        if (text[i] == '\n') 
        { 
            text[i] = 0;
             break; 
        } 
    }
   // printf("Enter the shift amount:");
    scanf("%d", &shift);
    for (i = 0; text[i]; i++) {
    if(text[i]>=97 && text[i]<=122){
   // (text[i] - 97) gives 0-25. Add shift, wrap with % 26, then add 'a' back.
    text[i]= (text[i] - 97 + shift + 26) % 26 + 97;
    }
    printf("%c", text[i]);
  }
    // Encrypt and print
    return 0;
}
