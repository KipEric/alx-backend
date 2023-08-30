function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(`Error setting ${schoolName}: ${err}`);
    } else {
      console.log(`Set ${schoolName}: ${reply}`);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error retrieving ${schoolName}: ${err}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  });
}
