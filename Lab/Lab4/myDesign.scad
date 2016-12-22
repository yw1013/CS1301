//Yea Won Yoon, Nija Kurien
//B3
//903076043
//yyoon75/yw1013@gatech.edu
//I worked on the homework assignment alone, using only this semester's course materials.


//Because I wasn't able to come up with any cool idea, I asked my boyfriend what would he want if I can make anything. He said he wants a bed because his bed is too squeaky. So I made a bed!

//frame
translate([-14,5,25]) // I was just moving around the frame.
difference(){
	translate([-40,-60,0]) color("Crimson",1) cube([165,110,7]);
	translate([-37.5,-57,1]) color("Crimson",1) cube([160,105,10]);
} //Difference subtracts further shapes from the first shape .

//I made a hallow box so I can fit the mattress in. 


//shorter bed legs 
rotate(45) //Because of frame, I had to rotate legs.
	for ( i = [0:1]) {
		rotate(i*90/1)
			translate([0,78,0])
				union(){
					translate([0,0,81]) color("Red",1) sphere(r = 5);
					color("DarkRed",1) cylinder(h = 80, r1 = 3, r2 = 2);
				} //Union combines shapes that are in {}.
	}
	
//longer bed legs
rotate(45)
translate([121,-121,0])
	for ( i = [0:1]) {
		rotate(i*90/1)
			translate([0,82,0])
				union(){
					translate([0,0,101.5]) color("Red",1) sphere(r = 6);
					color("DarkRed",1) cylinder(h = 100, r1 = 4, r2 = 2.5);
				}
	}

//I used for loop so I can make two bed legs in one function. I didn't combine shorter bed legs and longer bed legs because there sizes are different. To decorate more, I added spheres on top of the bed leg.


//mattress
translate([-46.5,-47,27])
	color("DeepPink",1) minkowski() {
   		cube([150,95,1]);
    		cylinder(r=5,h=30);
	} // Minkowski is used to make rounded corners for mattress.

//I made a mattress for my bed!


//side frame
legDistance = 110; //This is my assigned variable for if statement. 

if (legDistance == 110) {
	union(){
		translate([113,-55,10]) color("Crimson",1) cube([2,110,37]);
		difference(){
			translate([113,-56,40]) color("Crimson",1) cube([2,112,60]);
			translate([113,0,96]) scale([2,23,3]) sphere(r=4);
			translate([112,-52.5,79]) cube([4,106,2.5]);
			translate([112,-50,74]) cube([4,100,2.0]);
		}
	}
	difference(){
		translate([-56,-55,10]) color("Crimson",1) cube([2,110,60]);
		translate([-58,-52.5,65]) cube([5,105,2.5]);
		translate([-58,-50,60]) cube([5,100,2.0]);
	}
} else {
	cube([0,0,0]);
}

//If leg distance is not 110, it won't make side bed frames because it won't fit. If leg distance is 110, it will make perfect side frame with simple design.

