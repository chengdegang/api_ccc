javascript: (function() {
	var image = document.images[0];
	var width = 640;
	image.setAttribute('width', width);
	image.setAttribute('height', width / image.naturalWidth * image.naturalHeight);
	var canvas = document.createElement('CANVAS');
	canvas.height = image.height;
	canvas.width = image.width;
	var ctx = canvas.getContext('2d');
	ctx.drawImage(image, 0, 0, image.naturalWidth, image.naturalHeight, 0, 0, image.width, image.height);
	dataURL = canvas.toDataURL("image/jpeg");
	console.log("original size: " + image.naturalWidth + ", " + image.naturalHeight);
	console.log("target size: " + image.width + ", " + image.height);
	console.log(dataURL);
})()