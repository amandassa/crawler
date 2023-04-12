// connection file for database + routes
import express from "express";
import db from "./config/dbconnect.js";
import routes from "./routes/index.js";

db.on("err", console.log.bind(console, "Database connection error."));

db.once("open", () => {
    console.log("Database connection successfully established.");
});

const app = express();

app.use(express.json());

routes(app);

export default app;