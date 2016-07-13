var mysql = require("mysql");
var express = require('express');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password987",
  database: "bookstore"
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

// con.query("SELECT book_name FROM book_mast;",function(err,rows){
//   if(err) {
//     console.log(err.toString());
//     return;
//   }
//
//   console.log("Data received from Db:\n");
//   console.log(JSON.stringify(rows));
// });

// con.query('SELECT book_name, aut_name, cate_descrip, pub_name, Book_price ' +
// 'FROM book_mast ' +
// 'left JOIN author ' +
// 'ON book_mast.aut_id = author.aut_id ' +
// 'left JOIN category ' +
// 'ON book_mast.cate_id = category.cate_id ' +
// 'left JOIN publisher ' +
// 'ON book_mast.pub_id = publisher.pub_id;',function(err,rows){
//   if(err) {
//     console.log(err.toString());
//     return;
//   }
//
//   console.log("Data received from Db:\n");
//   console.log(JSON.stringify(rows));
// });

// con.end();
var app = express();

// app.get('/', function(req, res) {
//   con.query('SELECT book_name FROM book_mast;',function(err,rows){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//     res.send(JSON.stringify(rows));
//   });
// });

app.get('/', function(req, res) {
  con.query('SELECT book_name, aut_name, cate_descrip, pub_name, Book_price ' +
  'FROM book_mast ' +
  'left JOIN author ' +
  'ON book_mast.aut_id = author.aut_id ' +
  'left JOIN category ' +
  'ON book_mast.cate_id = category.cate_id ' +
  'left JOIN publisher ' +
  'ON book_mast.pub_id = publisher.pub_id;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.stringify(rows));
  });
});

var port = 3000;
app.listen(port, function(){
  console.log('I am listening on port ' + port);
});
