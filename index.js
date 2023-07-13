import { createTransport } from "nodemailer";


const transporter = createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: false, // set to true when using SSL/TLS
  auth: {
    user: 'daviddflix@gmail.com',
    pass: 'jchmimzuurlmpndh'
  },
});



function sendEmailWithExpirationLink() {
  
  let link = 'https://t.me/qcryto' // generic link
  
  let emailBody = ` <h1 style>Welcome to AI Alpha</h1>
                    <p>We are happy you have decided to try our product</p>
                    <p>To start interacting with AI Alpha Bot</p>
                    <p>To start interacting with AI Alpha Bot click on the next Button</p>
                    <button href=${link}>Access Link</button>`;

  const mailOptions = {
    from: 'daviddflix@gmail.com',
    to: 'david-972010@hotmail.com',
    subject: 'Content Access Link',
    html: emailBody
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('Error sending email:', error);
    } else {
      console.log('Email sent successfully:', info.response);
    }
  });
}

// sendEmailWithExpirationLink()  // uncomment when you want to send the email.