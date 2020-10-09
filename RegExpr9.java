import java.util.regex.Matcher;
import java.util.regex.Pattern

public class RegExpr9 {

	public static voidd main(String[] args) {
		// TODO Auto-generated method stub
		Pattern pattern=Pattern.compile("[ .,!]");
	
		String str[]=pattern.split("hi,how are you.Hello!i am Orvil dsilva");
		for(int i=0;i<str.length;i++) {
			System.out.println("MAtch:"+str[i])
		}

	}

}
