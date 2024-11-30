---

# Flask and MongoDB with Docker

This project demonstrates connecting Flask and MongoDB running in separate Docker containers using Docker networking.

https://hub.docker.com/repository/docker/crazyguy888/flask_docker_app/general

---

## **Prerequisites**
Ensure you have the following installed on your machine:
- Ubuntu (or compatible Linux distribution)

---

## **Setup Instructions**

### **Step 1: Install Docker**
Run the following commands to install the latest version of Docker:
```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt-get -y install docker-ce
sudo usermod -aG docker $USER, then restart, or:
```
> **Note:** Log out and back in or run `newgrp docker` to apply the group changes for the current session.

---

### **Step 2: Set Up the Flask Application**
1. Clone the repository containing the Flask app:
   ```bash
   git clone https://github.com/OmriFialkov/flask-and-mongo.githttps://github.com/OmriFialkov/flask-and-mongo.git
   cd app
   ```

2. Build the Flask Docker image:
   ```bash
   docker build -t flask .
   ```

3. Run the Flask container:
   ```bash
   docker run --name flask -d -p 5000:5000 flask
   ```
   > The Flask app is now running and exposed on port `5000`.

---

### **Step 3: Set Up MongoDB**
1. Pull and run the MongoDB container:
   ```bash
   docker pull mongo
   docker run --name mongo -p 27017:27017 -d mongo
   ```
   > The MongoDB instance is now running and exposed on port `27017`.

---

### **Step 4: Connect Flask and MongoDB Containers**
1. Create a Docker network:
   ```bash
   docker network create flask_mongo
   ```

2. Connect the containers to the network:
   ```bash
   docker network connect flask_mongo flask
   docker network connect flask_mongo mongo
   ```

3. Verify the connection:
   ```bash
   docker exec -it flask ping mongo
   ```
   > If you see responses, the containers are successfully connected!

---

### **Step 5: Verify MongoDB Data**
To interact with MongoDB from the host machine, install the MongoDB client:
```bash
sudo apt install mongodb-clients
```

Use the MongoDB client to connect to the MongoDB container:
```bash
mongo --host <mongo-container-ip> --port 27017
```

Once connected, verify the database and collection:
```javascript
show dbs                  // Lists all databases
use my_database           // Switch to your database
show collections          // Lists all collections
db.my_collection.find()   // Displays all documents in the collection
```

---

## **Project Overview**
- A Flask application inserts data into MongoDB.
- Flask and MongoDB run as separate containers connected via a Docker network.
- Data insertion and verification demonstrate the integration.

---

## **Key Commands Summary**
| Command                                   | Description                                           |
|-------------------------------------------|-------------------------------------------------------|
| `docker build -t flask .`                 | Build the Flask Docker image.                        |
| `docker run --name flask -d -p 5000:5000 flask` | Run the Flask container on port 5000.                |
| `docker pull mongo`                       | Pull the MongoDB image from Docker Hub.              |
| `docker run --name mongo -p 27017:27017 -d mongo` | Run the MongoDB container on port 27017.             |
| `docker network create flask_mongo`       | Create a Docker network for communication.           |
| `docker exec -it flask ping mongo`        | Test connectivity between Flask and MongoDB.         |
| `mongo --host <mongo-container-ip> --port 27017` | Connect to MongoDB using the client on the host.     |

---
