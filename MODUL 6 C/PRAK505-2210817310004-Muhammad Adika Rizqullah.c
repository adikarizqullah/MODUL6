#include<stdio.h>

void Biodata(int tahunLahir, char Namaku[20], char Asal[15]){
    int tahun_sekarang = 2020;
    printf("\nPerkenalkan Nama Saya : %s\n", Namaku);
    printf("Umur Saya : %d\n", tahun_sekarang - tahunLahir);
    printf("Saya Adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari : %s\n\n", Asal);
}
int main(){
    int tahunLahir;
    char Namaku[20], Asal[15];
    scanf("%d\n", &tahunLahir);
    scanf("%[^\n]%*c\n", &Namaku);
    scanf("%[^\n]%*c", &Asal);
    Biodata(tahunLahir, Namaku, Asal);
    return 0;
}
