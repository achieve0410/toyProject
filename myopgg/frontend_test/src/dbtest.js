
const { Client } = require('pg');

const client = new Client({
    user : 'wonhyo',
    host : '127.0.0.1',
    database : 'myopgg',
    password : '6chldnjsgy!@',
    port : 5432,
});

client.connect();

client.query('SELECT * from ACCOUNT_TEST', (err, res) => {
    console.log(err, res)
    client.end()
});
