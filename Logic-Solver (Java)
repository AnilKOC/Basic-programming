import java.util.Scanner;

public class main {
	public static void main(String args[]){String text;
	Scanner veriAL=new Scanner(System.in);
	System.out.println("- Enter your logic problem.");
	text=veriAL.nextLine();
	char [] array=text.toCharArray();
	int null_ct=1;
	for(int i=0;i<array.length;i++){
		if(array[i]==' ')null_ct++;
	}
	String [] array_2=new String[null_ct];
	null_ct=0;
	for(int j=0;j<array.length;j++){
		if(array[j]==' ')null_ct++;
		if(array[j]=='('){
			array_2[null_ct]="(";
		}
		if(array[j]==')'){
			array_2[null_ct]=")";
		}
		if(array[j]=='\''){
			array_2[null_ct]="\'";
		}
		if(array[j]=='A'){
			if(array[j+1]=='n'){
				if(array[j+2]=='d'){
					array_2[null_ct]="And";
				}
			}
		}
		if(array[j]=='N'){
			if(array[j+1]=='o'){
				if(array[j+2]=='r'){
					array_2[null_ct]="Nor";
				}
			}
		}
		if(array[j]=='X'){
			if(array[j+1]=='o'){
				if(array[j+2]=='r'){
					array_2[null_ct]="Xor";
				}
			}
		}
		if(array[j]=='N'){
			if(array[j+1]=='a'){
				if(array[j+2]=='n'){
					if(array[j+3]=='d'){
						array_2[null_ct]="Nand";
					}
				}
			}
		}
		if(array[j]=='O'){
			if(array[j+1]=='r'){
				array_2[null_ct]="Or";
			}
		}
		if(array[j]=='X'){
			if(array[j+1]=='n'){
				if(array[j+2]=='o'){
					if(array[j+3]=='r'){
						array_2[null_ct]="Xnor";
					}
				}
			}
		}
		if(array[j]=='t'){
			if(array[j+1]=='r'){
				if(array[j+2]=='u'){
					if(array[j+3]=='e'){
						array_2[null_ct]="true";
					}
				}
			}
		}
		if(array[j]=='f'){
			if(array[j+1]=='a'){
				if(array[j+2]=='l'){
					if(array[j+3]=='s'){
						if(array[j+4]=='e'){								
							array_2[null_ct]="false";
						}
					}
				}
			}
		}
	}
		boolean q,p;
		int temp_1=0;
		for(int k=0;k<array_2.length;k++){
			if(array_2[k]=="(" && array_2[k+2]==")"){
				String array_1[]=new String[array_2.length-2];
				array_1[k]=array_2[k+1];
				for(int a=k+1;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-1;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
			}
			else {				
				if(array_2[k]=="("){
					temp_1=k;
				}
				if(array_2[k]==")"){
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="\'"){
							q=Boolean.parseBoolean(array_2[b-1]);
							String array_1[]=new String[array_2.length-1];
							array_1[b-1]=Boolean.toString(Not(q));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+1];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k--;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="Nand"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(NAnd(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="Nor"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(NOr(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="Xor"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(XOr(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="Xnor"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(XNOr(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="And"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(And(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
					for(int b=temp_1;b<k;b++){
						if(array_2[b]=="Or"){
							q=Boolean.parseBoolean(array_2[b-1]);
							p=Boolean.parseBoolean(array_2[b+1]);
							String array_1[]=new String[array_2.length-2];
							array_1[b-1]=Boolean.toString(Or(q,p));
							for(int a=b;a<array_1.length;a++){
								array_1[a]=array_2[a+2];
							}
							for(int a=b-2;a>=0;a--){
								array_1[a]=array_2[a];
							}
							array_2=new String[array_1.length];
							for(int j=0;j<array_2.length;j++){
								array_2[j]=array_1[j];
							}
							k-=2;
							if(array_2[b-2]=="(" && array_2[b]==")"){
								String array_3[]=new String[array_2.length-2];
								array_3[b-2]=array_2[b-1];
								for(int a=b-1;a<array_3.length;a++){
									array_3[a]=array_2[a+2];
								}
								for(int a=b-3;a>=0;a--){
									array_3[a]=array_2[a];
								}
								array_2=new String[array_3.length];
								for(int j=0;j<array_2.length;j++){
									array_2[j]=array_3[j];
								}
								k=-1;
							}
							b=temp_1;
						}
					}
				}
			}
			for (int h=0;h<array_2.length;h++){
				if(array_2[h]=="(" && array_2[h+2]==")"){
					String array_1[]=new String[array_2.length-2];
					array_1[h]=array_2[h+1];
					for(int a=h+1;a<array_1.length;a++){
						array_1[a]=array_2[a+2];
					}
					for(int a=h-1;a>=0;a--){
						array_1[a]=array_2[a];
					}
					array_2=new String[array_1.length];
					for(int j=0;j<array_2.length;j++){
						array_2[j]=array_1[j];
					}
					h=0;
					k=0;
				}
			}
		}
		for(int w=0;w<array_2.length;w++){
			System.out.println(array_2[w]);
		}
		System.out.println();
		for(int k=0;k<array_2.length;k++){
			if(array_2[k]=="\'"){
				q=Boolean.parseBoolean(array_2[k-1]);
				String array_1[]=new String[array_2.length-1];
				array_1[k-1]=Boolean.toString(Not(q));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+1];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
		}
		for(int k=0;k<array_2.length;k++){
			if(array_2[k]=="Nand"){				
				q=Boolean.parseBoolean(array_2[k-1]);
				p=Boolean.parseBoolean(array_2[k+1]);
				String array_1[]=new String[array_2.length-2];
				array_1[k-1]=Boolean.toString(NAnd(q,p));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
			if(array_2[k]=="Nor"){
				q=Boolean.parseBoolean(array_2[k-1]);
				p=Boolean.parseBoolean(array_2[k+1]);
				String array_1[]=new String[array_2.length-2];
				array_1[k-1]=Boolean.toString(NOr(q,p));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
			if(array_2[k]=="Xor"){
				q=Boolean.parseBoolean(array_2[k-1]);
				p=Boolean.parseBoolean(array_2[k+1]);
				String array_1[]=new String[array_2.length-2];
				array_1[k-1]=Boolean.toString(XOr(q,p));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
			if(array_2[k]=="Xnor"){
				q=Boolean.parseBoolean(array_2[k-1]);
				p=Boolean.parseBoolean(array_2[k+1]);
				String array_1[]=new String[array_2.length-2];
				array_1[k-1]=Boolean.toString(XNOr(q,p));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
		}
		for(int k=0;k<array_2.length;k++){
			if(array_2[k]=="And"){				
				q=Boolean.parseBoolean(array_2[k-1]);
				p=Boolean.parseBoolean(array_2[k+1]);
				String array_1[]=new String[array_2.length-2];
				array_1[k-1]=Boolean.toString(And(q,p));
				for(int a=k;a<array_1.length;a++){
					array_1[a]=array_2[a+2];
				}
				for(int a=k-2;a>=0;a--){
					array_1[a]=array_2[a];
				}
				array_2=new String[array_1.length];
				for(int j=0;j<array_2.length;j++){
					array_2[j]=array_1[j];
				}
				k=0;
			}
		}
		for(int k=0;k<array_2.length;k++){
				if(array_2[k]=="Or"){
					q=Boolean.parseBoolean(array_2[k-1]);
					p=Boolean.parseBoolean(array_2[k+1]);
					String array_1[]=new String[array_2.length-2];
					array_1[k-1]=Boolean.toString(Or(q,p));
					for(int a=k;a<array_1.length;a++){
						array_1[a]=array_2[a+2];
					}
					for(int a=k-2;a>=0;a--){
						array_1[a]=array_2[a];
					}
					array_2=new String[array_1.length];
					for(int j=0;j<array_2.length;j++){
						array_2[j]=array_1[j];
					}
					k=0;
				}
		}
		
		for(int w=0;w<array_2.length;w++){
			System.out.println(array_2[w]);
		}
	}
	public static boolean And(boolean q,boolean p){
		if(q==true && p==true) return true;
		else return false;
	}
	public static boolean Or(boolean q,boolean p){
		if(q==true || p==true) return true;
		else return false;
	}
	public static boolean Not(boolean q){
		if(q==false) return true;
		else return false;
	}
	public static boolean NAnd(boolean q,boolean p){
		if(q==true && p==true) return false;
		else return true;
	}
	public static boolean NOr(boolean q,boolean p){
		if(q==false && p==false) return true;
		else return false;
	}
	public static boolean XOr(boolean q,boolean p){
		if(q!=p) return true;
		else return false;
	}
	public static boolean XNOr(boolean q,boolean p){
		if(q==p) return true;
		else return false;
	}
}
