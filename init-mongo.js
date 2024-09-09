db = db.getSiblingDB('task-manager-local-db'); // Connect to the database

db.createUser({
    user: "root", // Replace with your desired username
    pwd: "example", // Replace with a strong password
    roles: [ { role: "readWrite", db: "task-manager-local-db" } ]
});

db.createCollection("users");
db.createCollection("tasks");
