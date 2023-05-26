import java.util.*;
public class A_StarSearch {
	Scanner sc= new Scanner(System.in);
	@SuppressWarnings("rawtypes")
	public static void solu() {
		
		 HashMap A =new HashMap<>();
	       A.put(4,'B');
	       A.put(2,'C');
	    
	       
	       HashMap<Integer,Character> B=new HashMap<>();
	       B.put(2,'D');
	       
	       
	       HashMap<Integer,Character> C= new HashMap<>();
	       C.put(3,'D');
	       
	       HashMap<Integer,Character> D= new HashMap<>();
	       
	       
	      
	       
	       
	       HashMap<Object,Integer> h1=new HashMap<>();
	       h1.put(A,0);
	       h1.put(B,6);
	       h1.put(C,4);
	       h1.put(D,6);
	       

	       HashMap c1=A;
	        HashMap c2=D;
	        int w=0;
	        HashMap cn=c1;
	        String s="A";
	      while(cn!=c2)
	        {
	        	w=w+h1.get(cn)+(int) Collections.min(cn.keySet());
	        	
	        	Character sw1=(Character) cn.get(Collections.min(cn.keySet()));
	        	char c=sw1.charValue();
	        	
	        	s=s+"-"+c;
	        	if(c=='A') {
	        		cn=A;
	        	}else if(c=='B') {
	        		cn=B;
	        	}else if(c=='C') {
	        		cn=C;
	        	}else if(c=='D'){
	        		cn=D;
	        	}else {
	        		
	        		break;
	        	}
	        	
	        }
	        
	      System.out.println("Total cost is : "+w);
	      System.out.println("Path is : "+s);
	    
	    
	        
	}

	public static void main(String[] args) {
		System.out.println("A* algorithm Solution is follows");
		solu();
      
        
        
	}

}
