// function myFunction() {
//   var element = document.body;
//   element.classList.toggle("dark-mode");
// }

window.onload = function() {
  var isDarkModeEnabled = JSON.parse(localStorage.getItem('darkModeEnabled'));
  var element = document.body;
  
  if (isDarkModeEnabled) {
      element.classList.add("dark-mode");
      document.getElementById("modeToggle").checked = true;
  }
};

function myFunction() {
  var element = document.body;
  var isDarkModeEnabled = !element.classList.contains("dark-mode");
  
  element.classList.toggle("dark-mode", isDarkModeEnabled);
  document.getElementById("modeToggle").checked = isDarkModeEnabled;

  localStorage.setItem('darkModeEnabled', isDarkModeEnabled);
}

