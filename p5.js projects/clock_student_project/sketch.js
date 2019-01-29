
var step = 1;
var x1 = 0;
var x2 = 15
var x3 = 52;
var x4 = 55;

var xspacing = 5;     // Distance between each horizontal location
var w;                // Width of entire wave
var theta = 0.0;
var theta2 = 0.0;
var theta3 = 0.0;       // Start angle at 0
var amplitude = 12.0;
var amplitude2 = 20.0;
var amplitude3 = 40.0;  // Height of wave
var period = 260.0;   // How many pixels before the wave repeats
var dx;               // Value for incrementing x
var yvalues;          // Using an array to store height values for the wave


function setup() {
  createCanvas(windowWidth, windowHeight);

  w = 1600;
  dx = (TWO_PI / period) * xspacing;



  // var step = 0.4;
}

function draw() {
  createCanvas(windowWidth, windowHeight);
  var something = millis();



  background('#8892B3');

  calcWave3();
  renderWave3();
  calcWave2();
  renderWave2();
  calcWave();
  renderWave();

  stroke("#1D1F26");
  line(windowWidth/4, 0, windowWidth/4, windowHeight);
  line(windowWidth/2, 0, windowWidth/2, windowHeight);
  line(windowWidth/4*3, 0, windowWidth/4*3, windowHeight);
}

function calcWave() {
  // Increment theta (try different values for
  // 'angular velocity' here)
  var pew = second();
  // var millisecond = millis();

  var date = new Date();
  var currentMillis = date.getMilliseconds();
  // millisecond %= 1000;
  currentMillis /= 1000;

  pew += currentMillis;
  // console.log(pew);

  ipos = map(pew, 0, 60, 0, width)
  yvalues = new Array(floor(ipos/xspacing));
  theta += 0.15;
  // For every x value, calculate a y value with sine function
  var x = theta;

  for (var i = 0; i < yvalues.length; i++) {
    yvalues[i] = sin(x)*amplitude;
    x+=dx;
  }
  pew = 0;
}


function calcWave2() {
  // Increment theta (try different values for
  // 'angular velocity' here)
  var sec2 = second();

  var pew2 = minute();
  var millisecond2 = millis();


  pew2 *= 60;
  pew2 += sec2;
  millisecond2 %= 1000;
  millisecond2 /= 1000;

  pew2 += millisecond2;

  // text("Milliseconds \nrunning: \n" + pew2, 5, 40);
  // console.log(pew);

  ipos2 = map(pew2, 0, 3600, 0, width);
  yvalues2 = new Array(floor(ipos2/xspacing));
  theta2 += 0.15;
  // For every x value, calculate a y value with sine function
  var x2 = theta2;

  for (var i = 0; i < yvalues2.length; i++) {
    yvalues2[i] = sin(x2)*amplitude2;
    x2+=dx;
  }
  pew2 = 0;
}

function calcWave3() {
  // Increment theta (try different values for
  // 'angular velocity' here)
  var sec3 = second();
  var pew3 = minute();
  var hrs3 = hour();
  var millisecond3 = millis();
  hrs3 *= 3600
  pew3 *= 60;
  pew3 += sec3;
  pew3 += hrs3;
  millisecond3 %= 1000;
  millisecond3 /= 1000;

  pew3 += millisecond3;

  // text("Milliseconds \nrunning: \n" + pew3, 5, 40);
  // console.log(pew);

  ipos3 = map(pew3, 0, 86400, 0, width);
  yvalues3 = new Array(floor(ipos3/xspacing));
  theta3 += 0.15;
  // For every x value, calculate a y value with sine function
  var x3 = theta3;

  for (var i = 0; i < yvalues3.length; i++) {
    yvalues3[i] = sin(x3)*amplitude3;
    x3+=dx;
  }
  pew3 = 0;
}


function renderWave() {

  noStroke();
  fill(255);
  var squeeze = 10;
  // A simple way to draw the wave with an ellipse at each location
  for (var x = yvalues.length; x > 0; x--) {


    yvalues[x] = yvalues[x] * squeeze ;
    // console.log(yvalues[x])
    if (yvalues[x] < -5){
      stroke('#000000');
      strokeWeight(1);
      line(x*xspacing, height/2+yvalues[x], x*xspacing, height/2);
    } else if (yvalues[x] > 5){
      stroke('#000000');
      strokeWeight(1);
      line(x*xspacing, height/2+yvalues[x], x*xspacing, height/2);
    }
    strokeWeight(1);
    stroke(233, 233, 233);
    ellipse(x*xspacing, height/2+yvalues[x], 1, 1);
    squeeze /= 1.04;
    // console.log(yvalues[x])
  }
}




function renderWave2() {

  noStroke();
  fill(255);
  var squeeze2 = 15;
  // A simple way to draw the wave with an ellipse at each location
  for (var xp = yvalues2.length; xp > 0; xp--) {


    yvalues2[xp] = yvalues2[xp] * squeeze2;
    // console.log(yvalues[x])
    if (yvalues2[xp] < -5){
      stroke('#635F5A');
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues2[xp], xp*xspacing, height/2);
    } else if (yvalues2[xp] > 5){
      stroke('#635F5A');
      strokeWeight(2);
      line(xp*xspacing, height/2+yvalues2[xp], xp*xspacing, height/2);
    }
    strokeWeight(1);
    stroke(233, 233, 233);
    ellipse(xp*xspacing, height/2+yvalues2[xp], 2, 2);
    squeeze2 /= 1.05;
    // console.log(yvalues[x])
  }
}


function renderWave3() {

  noStroke();
  fill(255);
  var squeeze3 = 15;
  // A simple way to draw the wave with an ellipse at each location
  for (var xp = yvalues3.length; xp > 0; xp--) {


    yvalues3[xp] = yvalues3[xp] * squeeze3;
    // console.log(yvalues[x])
    if (yvalues3[xp] < -5 && xp*xspacing < width/4){
      stroke('#9E422A'); // red
      strokeWeight(4);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] > 5 && xp*xspacing < width/4){
      stroke('#1D1F26'); // black
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] < -5 && xp*xspacing < width/8*3 && xp*xspacing > width/4){
      stroke('#0E7AAB'); // blue
      strokeWeight(4);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] > 5 && xp*xspacing < width/8*3 && xp*xspacing > width/4){
      stroke('#9E422A'); // red
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] < -5 && xp*xspacing > width/8*3 && xp*xspacing < width/8*5){
      stroke('#0E7AAB'); // blue
      strokeWeight(4);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] > 5 && xp*xspacing > width/8*3 && xp*xspacing < width/8*5){
      stroke('#0E7AAB'); // blue
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] < -5 && xp*xspacing > width/8*5 && xp*xspacing < width/4*3){
      stroke('#0E7AAB'); // blue
      strokeWeight(4);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] > 5 && xp*xspacing > width/8*5 && xp*xspacing < width/4*3){
      stroke('#9E422A'); // red
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] < -5 && xp*xspacing > width/4*3 && xp*xspacing < width){
      stroke('#9E422A'); // red
      strokeWeight(4);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    else if (yvalues3[xp] > 5 && xp*xspacing > width/4*3 && xp*xspacing < width){
      stroke('#1D1F26'); // black
      strokeWeight(3);
      line(xp*xspacing, height/2+yvalues3[xp], xp*xspacing, height/2);
    }
    strokeWeight(1);
    stroke(233, 233, 233);
    ellipse(xp*xspacing, height/2+yvalues3[xp], 2, 2);
    squeeze3 /= 1.05;
    // console.log(yvalues[x])
  }
}
