import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.set('available_seats', 50);

let reservationEnabled = true;

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats);
};

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    
    if (availableSeats === 0) {
      reservationEnabled = false;
      done(null, 'Not enough seats available');
    } else {
      await reserveSeat(availableSeats - 1);
      if (availableSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
