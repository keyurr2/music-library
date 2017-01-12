var express = require('express');
var http = require('http');
var path = require('path');
var ms = require('mediaserver');
var fs = require('fs');
var app = express();
var server = http.createServer(app);

app.get('/:dir/:subdir/:song', function(req, res) {
	// console.log(req.params);
    var dataLength = 0;
    var song = path.join(__dirname, req.params.dir, toTitleCase(req.params.subdir), req.params.song);
    // var rstream = fs.createReadStream(song);
    // // using a readStream that we created already
    // rstream
    //     .on('data', function(chunk) {
    //     	console.log(chunk.length);
    //         dataLength += chunk.length;
    //     })
    //     .on('end', function() { // done
    //         console.log('The length was:', dataLength);
    //     });
    // rstream.pipe(res);
    try {
        console.log("Serving file >> ", req.params.dir, " > ", toTitleCase(req.params.subdir), " > ", req.params.song);
        ms.pipe(req, res, song);        
    } catch(e) {
        res.status(404).send({"Error" : e});
    }
});

function toTitleCase(str) {
    return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });
}

server.listen(parseInt(process.argv[2]) || 3020);
console.log('Express server started on port %s', server.address().port);
