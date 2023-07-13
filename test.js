import dotenv from 'dotenv';
dotenv.config();

const emailPassword = process.env.EMAIL_PASSWORD;
console.log(emailPassword)