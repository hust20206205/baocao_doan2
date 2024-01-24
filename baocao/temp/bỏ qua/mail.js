const nodemailer = require('nodemailer');

// Tạo một transporter với cấu hình MailHog
const transporter = nodemailer.createTransport({
  host: 'localhost',
  port: 1025,
  secure: false,
});

// Cấu hình email
const mailOptions = {
  from: 'your-email@example.com',
  // from: 'your-email@example.com',
  to: 'recipient@example.com',
  subject: 'Test Email',
  // subject: 'Test Email',
  text: 'Hello, this is a test email from MailHog!',
  // text: 'Hello, this is a test email from MailHog!',
};

// Gửi email
transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.error('Error sending email:', error);
  }
  console.log('Email sent:', info.response);
});
