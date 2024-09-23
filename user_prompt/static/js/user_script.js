var message_ele = document.getElementById("message_class");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 2500);
// Timeout is 3 sec, you can change it

document.querySelectorAll('.hint').forEach(hint => {
   hint.addEventListener('click', function() {
       const hintBox = this.querySelector('.hint-box');
       if (hintBox.style.display === 'block') {
           hintBox.style.display = 'none';
       } else {
           hintBox.style.display = 'block';
       }
   });
});
