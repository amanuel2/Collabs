using System;

namespace FirstConsoleProject
{
	public class baseCharcater{

		public String name;
		public int attackPower;
		public int defensePower;
		public int amountOfIntelligence;

		public void printBase(){
			Console.WriteLine ("Your Characters name is " + name);
			Console.WriteLine ("The amount of attack power your character has is " + attackPower);
			Console.WriteLine ("The amount of defense power your character has is " + defensePower);
			Console.WriteLine ("The amount of intelligence your character has is " + amountOfIntelligence);

		}

		
	}

	public class animal : baseCharcater{
		public String typeOfAnimal;
		
		public void type(){
			Console.WriteLine ("Your Animals type is " + typeOfAnimal);
		}

	}

	public class person : baseCharcater{


	}


	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.WriteLine ("Travis");
			person Travis = new person ();
			Travis.name = "Travis";
			Travis.amountOfIntelligence = 30;
			Travis.attackPower = 100;
			Travis.defensePower = 10;
			Travis.printBase ();

			Console.WriteLine ();


			Console.WriteLine ("Dog");
			animal dog = new animal ();
			dog.name = "spooky";
			dog.amountOfIntelligence = 80;
			dog.typeOfAnimal = "dog";
			dog.attackPower = 100;
			dog.defensePower = 100;
			dog.printBase ();
			dog.GetType ();

			Console.ReadLine ();
			
	}
}
}
