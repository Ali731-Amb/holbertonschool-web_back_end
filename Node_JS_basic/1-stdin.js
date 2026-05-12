process.stdin.on('data', (input) => {
  console.log("Your name is: " + input.toString().trim());
});
