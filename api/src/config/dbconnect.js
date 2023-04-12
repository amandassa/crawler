import mongoose from "mongoose";
import dotenv from 'dotenv'

dotenv.config()

mongoose.connect(`mongodb+srv://${process.env.MONGO_USERNAME}:${process.env.MONGO_PW}@${(process.env.ATLAS_DB_NAME).toLowerCase()}.ipe20.mongodb.net/${process.env.ATLAS_DB_NAME}`);
let db = mongoose.connection;
export default db;