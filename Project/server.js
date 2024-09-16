const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const session = require('express-session');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const bcrypt = require('bcryptjs');
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// User data storage (for demonstration purposes, use a database in production)
const users = [];

// Middleware setup
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public')); // Serve static files from the "public" directory
app.use(session({
  secret: 'secret_key', // Use a strong secret key in production
  resave: false,
  saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());

// Passport.js setup
passport.use(new LocalStrategy((username, password, done) => {
  const user = users.find(u => u.username === username);
  if (!user) return done(null, false, { message: 'Incorrect username.' });
  bcrypt.compare(password, user.password, (err, res) => {
    if (err) return done(err);
    if (!res) return done(null, false, { message: 'Incorrect password.' });
    return done(null, user);
  });
}));

passport.serializeUser((user, done) => done(null, user.username));
passport.deserializeUser((username, done) => {
  const user = users.find(u => u.username === username);
  done(null, user);
});

// Authentication routes
app.post('/login', passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/login',
  failureFlash: true
}));

app.post('/register', (req, res) => {
  const { username, password } = req.body;
  bcrypt.hash(password, 10, (err, hashedPassword) => {
    if (err) return res.status(500).send('Error hashing password');
    users.push({ username, password: hashedPassword });
    res.redirect('/login');
  });
});

// Chat server
io.on('connection', (socket) => {
  console.log('A user connected');

  socket.on('chatMessage', (data) => {
    io.emit('chatMessage', { message: data.message, type: 'normal' });
  });

  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
