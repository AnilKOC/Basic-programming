#include <stdio.h>
#include <stdlib.h>
struct n{
	int x;
	n*next;
};
typedef n node;
void show(node*r){
    printf("--------------------------------\n");
    int i=1;
    while(r!=NULL){
        printf("%d. value is = %d\n",i,r->x);
        r=r->next;
        i++;
    }
    printf("--------------------------------\n");
}
void add(node *r,int x,int s){
        for(int i=2;i<s;i++){
            r=r->next;
        }
        node*temp=(node*)malloc(sizeof(node));
        temp->x=x;
        temp->next=r->next;
        r->next=temp;
}
void killer(node *r,int s){
        for(int i=2;i<s;i++){
            r=r->next;
        }
        r->next=r->next->next;
}
int main(void) {
	node *root;
	root=(node *)malloc(sizeof(node));
	root ->x=1;
	root -> next=(node *)malloc(sizeof(node));
	root -> next ->x=2;
	root -> next -> next=(node *)malloc(sizeof(node));
	root -> next -> next -> x=3;
	root -> next -> next -> next=(node *)malloc(sizeof(node));
	root -> next -> next -> next->x=4;
	root -> next -> next -> next->next=NULL;
	node *iter;
	iter=root;
	show(root);
	int c,s;
    printf( "Enter your value :");
    scanf("%d",&c); 
    printf("\n");
    printf( "Which sequence do you want :");
    scanf("%d",&s); 
    printf("\n");
    add(root,c,s);
    show(root);
    printf( "Which sequence do you want to kill :");
    scanf("%d",&s); 
    printf("\n");
    killer(root,s);
    show(root);
    printf("Big-O = 39+(s-1)+(show_1*3)+(show_2*3)+{if s=1}(4)+{else}(killer_s-1+4)"); 
    return EXIT_SUCCESS;
}
