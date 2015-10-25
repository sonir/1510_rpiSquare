
var dgram = require("dgram");

var host = "127.0.0.1";
var port = 7501; //7401;
var tmpl = [ 0x2f,0x73,0x71,0x75,0x61,0x72,0x65,0x00,0x2c,0x69,0x69,0x69,0x69,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00 ];

var resouces = new Uint8Array(9);
var antIndex = -1;

function update() {
    var time = Date.now() + 1000;
    var values = updateModel();
    var buffer = createOSCMessage(time, values);

    sendPacket(buffer, port, host, function() {
	    console.log("ant: " + antIndex + ", resouces: " + [].slice.call(resouces).map(function(x) {
			return (x / 256).toFixed(1);
		    }).join(", "));
	});
}

function updateModel() {
    var values = new Float32Array(9);

    antIndex = (antIndex + 1) % values.length;

    for (var i = 0; i < resouces.length; i++) {
	resouces[i] -= i;
    }

    for (var i = 0; i < values.length; i++) {
	if (i === antIndex) {
	    values[i] += 101;
	}
	values[i] += resouces[i] / 256;
    }

    return values;
}

function createOSCMessage(time, values) {
    var playbackTime = Math.floor(time / 1000);
    var deltaTime = time % 1000;
    var buffer = new Buffer(tmpl);

    buffer.writeUInt32BE(playbackTime, 6 * 4);
    buffer.writeUInt32BE(deltaTime, 8 * 4);

    for (var i = 0; i < values.length; i ++) {
	buffer.writeFloatBE(values[i], (10 + i) * 4);
    }

    return buffer;
}

function sendPacket(buffer, port, host, callback) {
    var socket = dgram.createSocket("udp4");

    socket.send(buffer, 0, buffer.length, port, host, function() {
	    socket.close();
	    if (typeof callback === "function") {
		callback();
	    }
	});
}

setInterval(update, 1000);


