// Users I followed
var up_flat_up = [];
var flat_down = [];
var flat_down_up = [];

// Users followed me
var up_flat = [];
var up_flat_down = [];

// My usual followers
var flat = [];
var flat_up = [];



var flat_up_coord = [];
var flat_down_coord = [];
var flat_down_up_coord = [];
var up_flat_coord = [];
var up_flat_down_coord = [];

var white_x1 = 0;
var white_x2 = 0;
var white_y = 0;


function preload() {
  //my table is comma separated value "csv"
  //and has a header specifying the columns labels
  table = loadTable("data/working.csv", "csv", "header");
  console.log(table);
  
 
  

}



function setup() {
	
 /*
	var states = table.getColumn(0);
	console.log(states)
*/
	

	
	// 	var just = [];
	
	for (var i = 0; i < table.getRowCount(); i ++){
		// print the row
	// 		console.log(table.getRow(i));
		
		var row = table.getRow(i);
		var entry = new Object();
		for (var c = 1; c < table.getColumnCount(); c++){
	/*
			console.log(c)
			console.log(row.getString(c));
	*/			if (row.getString(c) != ""){
				entry[row.getString(c)] = c;
			}
			
		}
		if (("follower" in entry) && (entry["follower"] == 1) && (Object.keys(entry).length == 1)){
			flat.push(entry);
		}
		 else if (("following" in entry)  && (Object.keys(entry).length == 1)){
			up_flat_up.push(entry);
		} 
		else if (("follower" in entry) && (entry["follower"] == 1) && ("unfollowed" in entry)){
			flat_up.push(entry);
		} else if (("follower" in entry) && (entry["follower"] != 1) && ("following" in entry) && (!("unfollowed" in entry))){
			flat_down.push(entry);
		} else if (("follower" in entry) && (entry["follower"] != 1) && ("unfollowed" in entry) && ("following" in entry)){
			flat_down_up.push(entry);
		} else if (("follower" in entry) && (Object.keys(entry).length == 1)){
			up_flat.push(entry);
		} else if ((!("following" in entry)) && ("follower" in entry) && ("unfollowed" in entry)){
			up_flat_down.push(entry);
		}
		}
		
// 	console.log(up_flat_up.length);
	/*
	console.log(flat.length);
	console.log(up_flat_up.length);
	console.log(flat_up.length);
	console.log(flat_down.length);
	console.log(flat_down_up.length);
	console.log(up_flat.length);
	console.log(up_flat_down.length);
	*/
/*
	console.log(flat_down);
	console.log(flat.length  + flat_up.length + flat_down.length + flat_down_up.length + up_flat.length + up_flat_down.length)
*/;
	
// 	console.log(up_flat_up);
/*
	for (var i = 0; i <= up_flat_up.length; i ++){
	console.log(up_flat_up[i])
	}
*/
	
	flat_height_max = 2 * windowHeight/3 + flat.length/3;
	flat_height_min = 2 * windowHeight/3;
	
	
	for (var i = 0; i < flat_up.length; i++){
 		console.log(flat_up[i]["unfollowed"]);
		var x = (flat_up[i]["unfollowed"] - 1 + Math.random());
// 		var y = Math.random() * (2 * windowHeight/3);
		flat_up_coord.push(x);
	}

	for (var i = 0; i < flat_down.length; i++){
// 		console.log(flat_down[i]["unfollowed"]);
		var x1 = (flat_down[i]["following"] - 2 + Math.random());
		var x2 = (flat_down[i]["follower"] - 2 + Math.random());
		var y = Math.random() * (windowHeight/5) + 2 * windowHeight/8;
		flat_down_coord.push([x1, x2, y]);
	}
	
	for (var i = 0; i < flat_down_up.length; i++){
		console.log(flat_down_up[i]["unfollowed"]);
		var x1 = (flat_down_up[i]["following"] - 2 + Math.random());
		var x2 = (flat_down_up[i]["follower"] - 2 + Math.random());
		var x3 = (flat_down_up[i]["unfollowed"] - 2 + Math.random());
		var y = Math.random()  *(windowHeight/3) +   windowHeight/3;
		flat_down_up_coord.push([x1, x2, x3, y]);
}

	for (var i = 0; i < up_flat.length; i++){
//  		console.log(up_flat[i]["follower"]);
		var x = (up_flat[i]["follower"] - 1 + Math.random());
// 		var y = Math.random() * (2 * windowHeight/3);
		up_flat_coord.push(x);
	}
	
	for (var i = 0; i < up_flat_down.length; i++){
// 		console.log(up_flat_down[i]["unfollowed"]);
		var x1 = (up_flat_down[i]["follower"] - 2 + Math.random());
		var x2 = (up_flat_down[i]["unfollowed"] - 2 + Math.random());

// 		var y = Math.random()  *(windowHeight/3) +   windowHeight/3;
		up_flat_down_coord.push([x1, x2]);
}
	
// 	flat_down_coord
	console.log(up_flat_coord);
}


function draw() {
   
createCanvas(windowWidth, windowHeight);
background(40);


for (var lx = 1; lx < 7; lx++){
	stroke(250, 250, 250,30);
	line_x = map(lx, 0, 7, 0, windowWidth);
	line(line_x, 0 , line_x,  windowHeight);
	
	noStroke();
	fill(250, 250, 250);
	var some_day = "day " + lx;
	text(some_day, line_x-windowWidth/12, 30);
	
}

noStroke();
fill(160, 79, 63)
var orange_text = "Bots following me and dropping: " + up_flat_down_coord.length;
text(orange_text, 30, 80 - 25);

fill(117, 101, 14)
var swamp_text = "I followed, they followerd back and dropped: " + flat_down_up_coord.length;
text(swamp_text, 30, 80 + 25 - 25);

fill(2, 122, 106)
var teal_text = "I am following and they dropped: " + flat_up_coord.length;
text(teal_text, 30, 80 + 25 + 25 - 25);

fill(89, 221, 77)
var lgreen_text = "I followed and they followed back: " + flat_down_coord.length;
text(lgreen_text, 30, 80 + 25 + 25 + 25 - 25);


fill(2, 122, 64)
var dgreen_text = "My pre-bot followers : " + flat.length;
text(dgreen_text, 30, 80 + 25 + 25 + 25 + 25 - 25);

fill(219, 142, 41)
var orange_text = "Bots following me : " + up_flat_coord.length;
text(orange_text, 30, 80 + 25 + 25 + 25 + 25 + 25 - 25);	

fill(169, 169, 169)
var white_text = "I followed and they didn't respond : " + up_flat_up.length + " (obviously not plotted)";
text(white_text, 30, 80 + 25 + 25 + 25 + 25 + 25 + 25 - 25);	




	
	
// PLOT THE FLAT ONES

for(var i = 0; i < up_flat_down_coord.length; i ++){
	stroke(160, 79, 63);
// 	console.log(flat_up_coord[i]);
	var x1 = map(up_flat_down_coord[i][0], 0, 7, 0, windowWidth - 20);
	var x2 = map(up_flat_down_coord[i][1], 0, 7, 0, windowWidth - 20);
	noFill();
// 	line(0, 2 * windowHeight/3 - i , x, 2 * windowHeight/3 - i);
	bezier(x1 , windowHeight, 
		   x1 , windowHeight - 200, 
		   x2 - 50 , 2 * windowHeight/3 + flat.length + i, 
		   x2, 2 * windowHeight/3 + flat.length + i);
	
	
	bezier(x2 , 		2 * windowHeight/3 + flat.length + i, 
		   x2 + 50 , 2 * windowHeight/3 + flat.length + i - 50, 
		   windowWidth - 200 , windowHeight/3 - flat_up_coord.length - flat_down_up_coord.length - i - 50, 
		   windowWidth - 20, windowHeight/3 - flat_up_coord.length - flat_down_up_coord.length - i);
	

	
	}
	
	
	
for(var i = 0; i <= flat.length; i ++){
	stroke(2, 122, 64);
/*
	line(0, 2 * windowHeight/3 + i , 
		windowWidth - 20, 2 * windowHeight/3 + i);
*/
	
	bezier(0 , 		2 * windowHeight/3 + i, 
	   100 , 2 * windowHeight/3 + i, 
	   windowWidth - 100 , 2 * windowHeight/3 + i, 
	   windowWidth - 20, 2 * windowHeight/3 + i)}
	
// console.log(flat_down_coord);
// 	flat_up_coord
for(var xi = 0; xi < flat_down_coord.length; xi ++){
	
	stroke(89, 221, 77);
// 	console.log(flat_down_coord[xi]);
	var x1 = map(flat_down_coord[xi][0], 0, 7, 0, windowWidth - 20);
	var x2 = map(flat_down_coord[xi][1], 0, 7, 0, windowWidth - 20);
// 	noFill();
/*
	line(x1, flat_down_coord[xi][2] , x2, flat_down_coord[xi][2]);
	bezier(x2 , flat_down_coord[xi][2], x2 + 100, flat_down_coord[xi][2], 
		windowWidth - 20 - 150 , 2 * windowHeight/3 - flat_up_coord.length - xi, 
		windowWidth - 20 ,  2 * windowHeight/3 - flat_up_coord.length - xi);
*/
		
	if (xi != 30){
	
		noFill();
		stroke(89, 221, 77);
		line(x1, flat_down_coord[xi][2] , x2, flat_down_coord[xi][2]);
		bezier(x2 , flat_down_coord[xi][2], 
			   x2 + 250, flat_down_coord[xi][2], 
		windowWidth - 20 - 250 , 2 * windowHeight/3 - flat_up_coord.length - xi, 
		windowWidth - 20 ,  2 * windowHeight/3 - flat_up_coord.length - xi);
	} else {
// 		noStroke()

	
		white_x1 = x1;
		white_x2 = x2;
		white_y = flat_down_coord[xi][2];
				
		noFill();
		strokeWeight(4);
		stroke(221, 221, 221);
		line(x1, flat_down_coord[xi][2] , x2, flat_down_coord[xi][2]);
		bezier(x2 , flat_down_coord[xi][2], 
			   x2 + 250, flat_down_coord[xi][2], 
		windowWidth - 20 - 250 , 2 * windowHeight/3 - flat_up_coord.length - xi, 
		windowWidth - 20 ,  2 * windowHeight/3 - flat_up_coord.length - xi);
		strokeWeight(1);
	}
	noFill();
/*
	line(windowWidth - 20 - 80,  2 * windowHeight/3 - flat_up_coord.length - xi,
		 windowWidth - 20 , 	  2 * windowHeight/3 - flat_up_coord.length - xi);
*/
	}

for(var xi = 0; xi < flat_down_up_coord.length; xi ++){
	stroke(117, 101, 14);
// 	console.log(flat_down_up[xi]);
	var x1 = map(flat_down_up_coord[xi][0], 0, 7, 0, windowWidth - 20);
	var x2 = map(flat_down_up_coord[xi][1], 0, 7, 0, windowWidth - 20);
	var x3 = map(flat_down_up_coord[xi][2], 0, 7, 0, windowWidth - 20);
// 	noFill();
	line(x1, flat_down_up_coord[xi][3] , 
		 x2, flat_down_up_coord[xi][3]);
		 
	bezier(x2 ,     	flat_down_up_coord[xi][3], 
		   x2 + 100, 	flat_down_up_coord[xi][3] + 30, 
		   x3 - 50 , 	2 * windowHeight/3 - flat_up_coord.length - xi, 
		   x3 ,	2 * windowHeight/3 - flat_up_coord.length - xi);
		   
	bezier(x3 ,	2 * windowHeight/3 - flat_up_coord.length - xi, 
		   x3 + 250,	2 * windowHeight/3 - flat_up_coord.length - xi, 
		   windowWidth - 20 - 250 , windowHeight/3 - flat_up_coord.length - xi , 
		   windowWidth - 20 , windowHeight/3 - flat_up_coord.length - xi );
	}	
	

	
	
	
for(var i = 0; i <= flat_up_coord.length; i ++){
	stroke(2, 122, 106);
// 	console.log(flat_up_coord[i]);
	var x = map(flat_up_coord[i], 0, 7, 0, windowWidth - 20);
	noFill();
	line(0, 2 * windowHeight/3 - i , x, 2 * windowHeight/3 - i);
		bezier(x , 2 * windowHeight/3 - i, 
			   x + 150, 2 * windowHeight/3 - i - 30, 
			    windowWidth - 20 - 150 , windowHeight/3-i+15, 
			    windowWidth - 20, windowHeight/3-i);
	}


for(var i = 0; i <= up_flat_coord.length; i ++){
	stroke(219, 142, 41);
// 	console.log(flat_up_coord[i]);
	var x = map(up_flat_coord[i], 0, 7, 0, windowWidth - 20);
	noFill();
// 	line(0, 2 * windowHeight/3 - i , x, 2 * windowHeight/3 - i);
	bezier(x , 		windowHeight, 
		   x , windowHeight - 350, 
		   windowWidth - 400 , 2 * windowHeight/3 + flat.length + i, 
		   windowWidth - 20, 2 * windowHeight/3 + flat.length + i);
	}



noStroke();
stroke(0, 0, 0);
fill(221, 221, 221)
var white_text1 = "I clicked 'follow'";
text(white_text1, white_x1 + 30, white_y-15);

stroke(0, 0, 0);
ellipse(white_x1, white_y, 10, 10);
noStroke();
var white_text2 = "They followed me back";
text(white_text2, white_x2 + 50, white_y + 15);
stroke(0, 0, 0);
ellipse(white_x2 , white_y, 10, 10);

// console.log(table);


}
