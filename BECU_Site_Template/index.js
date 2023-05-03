window.addEventListener("load", function () { 
  var select = document.getElementById('os'); 
  select.addEventListener("change", (event) => {
    const result = document.getElementById('hidden_div');
    select = document.getElementById('os');
    console.log(select.value)
    result.style.display = 'block';
  });

  var select = document.getElementById('iso'); 
  select.addEventListener("change", (event) => {
    const result = document.getElementById('hidden_div2');
    const button = document.getElementById('submit');
    result.style.display = 'block';
    button.classList.remove('disabled');
  });

  const name = document.getElementById('submit');
  name.addEventListener("click", (event) => {
    const results = document.getElementById('hidden_div3');
    console.log("worked");
    results.style.display = 'block';
  });

 /* async function test() {
    const options = {
      method: 'GET',
      headers: {
      'Authorization': 'Bearer 8rLGxB7J4EZkK2qLdQb0aw',
      }
      };
    const response = await fetch('http://20.245.192.233/tasks/list', options);
    console.log(data);
  }
  test();*/
});

fetch(' http://cuckoosandbox.westus.cloudapp.azure.com/tasks/list', {
  headers: {
    'Authorization': 'Bearer 8rLGxB7J4EZkK2qLdQb0aw',
  },
  mode: 'no-cors'
})
  .then(res => console.log(res));