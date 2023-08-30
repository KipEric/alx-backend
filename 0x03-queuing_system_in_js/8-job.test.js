import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
  let queue;

  before(function () {
    queue = kue.createQueue();
    kue.testMode.enter();
  });

  after(function () {
    kue.testMode.exit();
  });

  it('displays an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('creates two new jobs to the queue', function () {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});
