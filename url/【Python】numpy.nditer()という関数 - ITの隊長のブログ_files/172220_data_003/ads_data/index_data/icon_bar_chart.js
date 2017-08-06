/**********************************
* Icon Animation .JS Fragment File
***********************************/
var iconAnimationName = "bar_chart";
var iconAnimationVersion = 2.1;
var spriteSheetName = "spritesheet_bar_chart.png";
var spriteSheet = new Image();

// For rescaling on other unit sizes
var iconUnitScale = 1; // Scale = 1 for 300x250
var iconRegistrationX = 0; // Null registration point of animation. Adjust as needed on other unit sizes (728x90, 160x600)
var iconRegistrationY = 0; // 0, 0 is based on the 300x250

// From Dynamic API
var iconAnimationStartTime = parseFloat(dynamicContent.APAC_GDN_Q4_Tangram_Datasheet_JP_160x600_JP[0].Start_Time_Icon_Animation); //Start_Time_Icon_Animation
var copyBatch2StartTime = parseFloat(dynamicContent.APAC_GDN_Q4_Tangram_Datasheet_JP_160x600_JP[0].Start_Time_Text_2); //Start_Time_Icon_Animation

var objPart = [];
var objPartCount = 4;
var objPartStartX = [6, 26, 56, 2];
var objPartStartY = [355, 349, 377, 402];
var objPartDockX = [26, 26, 36, 26];
var objPartDockY = [370, 370, 370, 380];

var square = [];
var squareCount = 5;
var squaretartX = [57, 77, 57, 87, 50];
var squaretartY = [350, 350, 390, 380, 370];
var squareDockX = [67, 67, 67, 77, 67];
var squareDockY = [340, 340, 340, 370, 380];

var arrow = [];
var arrowCount = 8;
var arrowtartX = [90, 100, 110, 100, 90, 100, 120, 80];
var arrowtartY = [320, 320, 355, 390, 378, 350, 392, 411];
var arrowDockX = [101, 120, 110, 120, 110, 110, 110, 110];
var arrowDockY = [345, 345, 363, 363, 363, 392, 402, 411];


function createIconParts()
{
	var i = 0;
	var tempElement;
	var iconHolder = $("#iconHolder");
	// Create Phone Icon Parts & attach to DOM

	divHolder1 = document.createElement("div");
	divHolder1.setAttribute("id", "arrowCont");
	$("#iconHolder").appendChild(divHolder1);

	// Create & Attach Phone Receiver Handle to DOM
	tempElement =  document.createElement("div");
	tempElement.setAttribute("id", "whiteSquare");
	iconHolder.appendChild(tempElement);


	for (i = 0; i < objPartCount; i++)
	{
		tempElement =  document.createElement("div");
		tempElement.setAttribute("id", "obj" + i);
		tempElement.setAttribute("class", "sprite obj" + i);
		iconHolder.appendChild(tempElement);
		objPart[i] = $("#obj" + i);
		TweenLite.to(objPart[i], 0, {opacity:0, x:(objPartStartX[i] * iconUnitScale + iconRegistrationX), y:(objPartStartY[i] * iconUnitScale + iconRegistrationY)});
	}


	for (i = 0; i < squareCount; i++)
	{
		tempElement =  document.createElement("div");
		tempElement.setAttribute("id", "square" + i);
		tempElement.setAttribute("class", "sprite square" + i);
		iconHolder.appendChild(tempElement);
		square[i] = $("#square" + i);
		TweenLite.to(square[i], 0, {opacity:0, x:(squaretartX[i] * iconUnitScale + iconRegistrationX), y:(squaretartY[i] * iconUnitScale + iconRegistrationY)});
	}

	for (i = 0; i < arrowCount; i++)
	{
		tempElement =  document.createElement("div");
		tempElement.setAttribute("id", "arrow" + i);
		tempElement.setAttribute("class", "sprite arrow" + i);
		divHolder1.appendChild(tempElement);
		arrow[i] = $("#arrow" + i);
		TweenLite.to(arrow[i], 0, {opacity:0, x:(arrowtartX[i] * iconUnitScale + iconRegistrationX), y:(arrowtartY[i] * iconUnitScale + iconRegistrationY)});
	}

}

function initIconAnimations()
{

	// Timeline Markers Definitions
	tlIcon.addLabel("dockPhone", iconAnimationStartTime);
	tlIcon.addLabel("screenTime", iconAnimationStartTime);
	tlIcon.addLabel("arrowShow", iconAnimationStartTime);
	tlIcon.addLabel("moveUp", copyBatch2StartTime + 1);

	// Animation Definitions
	dockPhone();
	screenTime();
	arrowShow();

	tlIcon.to([$("#arrowCont")], 1, {y:-19, ease:Power3.easeInOut}, "moveUp");

	// End Animation
}

function dockPhone()
{
	var i = 0;
	for (i = 0; i < objPartCount; i ++)
	{
		tlIcon.to(objPart[i], 0.3, {opacity:1}, "dockPhone");
		tlIcon.to(objPart[i], 1, {x:(objPartDockX[i] * iconUnitScale + iconRegistrationX), y:(objPartDockY[i] * iconUnitScale + iconRegistrationY), ease:Power4.easeInOut}, "dockPhone");
	}
}

function screenTime() 
{
	var i = 0;
	for (i = 0; i < squareCount; i ++)
	{
		tlIcon.to(square[i], 0.3, {opacity:1}, "screenTime");
		tlIcon.to(square[i], 1, {x:(squareDockX[i] * iconUnitScale + iconRegistrationX), y:(squareDockY[i] * iconUnitScale + iconRegistrationY), ease:Power4.easeInOut}, "screenTime");
	}
}

function arrowShow() 
{
	var i = 0;
	for (i = 0; i < arrowCount; i ++)
	{
		tlIcon.to(arrow[i], 0.3, {opacity:1}, "arrowShow");
		tlIcon.to(arrow[i], 1, {x:(arrowDockX[i] * iconUnitScale + iconRegistrationX), y:(arrowDockY[i] * iconUnitScale + iconRegistrationY), ease:Power4.easeInOut}, "arrowShow");
	}
}

// Create and initialize icon parts + animation
createIconParts();
initIconAnimations();

console.log("Animation: " + iconAnimationName + " ver " + iconAnimationVersion);
console.log("-----");

function onSpriteSheetLoad(e)
{
	// startAnimations is called from main.js
	// it will play the main timeline (tl)
	// + your icon timeline (tlIcon) at the same time
	startAnimations(); // STARTS THE ENTIRE UNIT ANIMATION when SpriteSheet is loaded
}

// play animation once spritesheet is confirmed to have loaded
spriteSheet.addEventListener("load", onSpriteSheetLoad, false);
spriteSheet.src = spriteSheetName;
