import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;
public class PersonTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Scanner reader=new Scanner(System.in);
//		String str=reader.nextLine();
		if(args[0].equals("cid")) {
			//?���ַ�
			//String s=reader.nextLine();
			if(args.length!=2)
				System.out.println("error");
			else {
				System.out.println(IDNum.checkIDNum(args[1]));
			}
		}
		else if(args[0].equals("np")) {
			//���� ���֤��
//			String sname=reader.nextLine();
//			String sid=reader.nextLine();
			//���� ���֤�� ��?��?����newPerson()?����
			//����?������� ��"ID illegal"��
			//���ںϷ������?�ö����toString()
			Person cxy=new Person();
			//IDNum cxyid=new IDNum();
			//String ss=IDNum.toString(sid);
			cxy=Person.newPerson(args[1], args[2]);
			if(cxy==null)
				System.out.println("ID illegal");
			else {
				String ss=IDNum.toString(args[2]);
				cxy=Person.newPerson(args[1], ss);
				
				String sss=cxy.toString();
				System.out.println(sss);
			}
		}
	}

}