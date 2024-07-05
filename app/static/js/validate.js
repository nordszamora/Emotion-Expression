function validate() {
  const expression = document.querySelector('.form-control').value;
    
  if(expression.trim() === "") {
    alert("Provide your text.");
    return false;
  }
}
