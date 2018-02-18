package ThirtyDaysOfCode

object TenFirstDays extends App {

 def Main(): Unit ={
    day5()
  }

  Main()

  def day0(): Unit = {
   val s = scala.io.StdIn.readLine("Introduce text\n");
   println("Hello, World.")
    println(s)
  }

  def day1(): Unit = {

    val i = 4
    val d = 4.0
    val s = "Hackerrank"

    val int : Int = scala.io.StdIn.readInt()
    val double: Double = scala.io.StdIn.readDouble()
    val str : String = scala.io.StdIn.readLine()

    println(i + int)
    println(d + double)
    println(s + str)

  }

  def day2(): Unit = {
    println("Introduce cost of meal, tip %, tax %")

    val mealCost : Double = scala.io.StdIn.readDouble()
    val tipPercent : Double = scala.io.StdIn.readInt()
    val taxPercent : Double = scala.io.StdIn.readInt()

    var result : Double = mealCost + mealCost * tipPercent/100 + mealCost * taxPercent/100
    result = Math.round(result)

    println(s"The total meal cost is $result dollars.")
  }

  def day3(): Unit = {

    val n : Double = scala.io.StdIn.readDouble()

    if(n % 2 != 0) println("Weird")
    if(n % 2 == 0) {
      if(n > 1 && n < 6) println("Not Weird")
      else if (n > 5 && n < 21) println("Weird")
      else println("Not Weird")
    }
  }

  def day4(): Unit = {
    var T = scala.io.StdIn.readInt()
    var i = 0
    for(i<-1 to T) {
      var age = scala.io.StdIn.readInt()
      var p = new Person(age)
      p.amIOld()
      var j = 0
      for(j<-1 to 3){
        p.yearPasses()
      }
      p.amIOld()
      println()
    }
  }

  class Person {
    var age: Int = 0

    def this(InitialAge:Int) = {
      this()
      if(InitialAge > 0) this.age = InitialAge
      else {
        this.age = 0
        println("Age is not valid, setting age to 0.")
      }
    }

    def amIOld(): Unit ={
      if(this.age < 13) println("You are young.")
      else if(this.age > 12 && this.age < 18) println("You are a teenager.")
      else println("You are old.")
    }

    def yearPasses(): Unit = {
      this.age += 1
    }
  }

  def day5(): Unit = {
    val n = scala.io.StdIn.readInt()
    var i = 0
    for(i<-1 to 10) {
      println(n + " x " + i + " = " + n*i)
    }
  }


}
