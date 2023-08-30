import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

console.log('Job processor is running...');
