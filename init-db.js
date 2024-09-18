// this is to test mongodb locally and create the DB, users and tasks.
// copy this code and use in the mongodb playground 
db = db.getSiblingDB('task-manager-local-db'); // Connect to the database

db.createUser({
    user: "root", // Replace with your desired username
    pwd: "example", // Replace with a strong password
    roles: [ { role: "readWrite", db: "task-manager-local-db" } ]
});

db.createCollection("users");
db.createCollection("tasks");