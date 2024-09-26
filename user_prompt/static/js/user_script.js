var message_ele = document.getElementById("message_class");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 2500);
// Timeout is 3 sec, you can change it



document.querySelectorAll('.hint').forEach(hint => {
    const hintBox = hint.querySelector('.hint-box');
    const closeButton = hintBox.querySelector('.hint-close');

    // Toggle hint-box visibility
    hint.addEventListener('click', function () {
        if (hintBox.style.display === 'block') {
            hintBox.style.display = 'none';
        } else {
            hintBox.style.display = 'block';
        }
    });

    // Close the hint-box when the "X" is clicked
    closeButton.addEventListener('click', function (event) {
        event.stopPropagation(); // Prevents triggering the click event of hint itself
        hintBox.style.display = 'none';
    });

    // Drag functionality
    let isDragging = false;
    let initialX, initialY, currentX, currentY, xOffset = 0, yOffset = 0;

    hintBox.addEventListener('mousedown', function (event) {
        isDragging = true;
        initialX = event.clientX - xOffset;
        initialY = event.clientY - yOffset;
        hintBox.classList.add('dragging');
        document.addEventListener('mousemove', drag, false);
        document.addEventListener('mouseup', stopDrag, false);
    });

    function drag(event) {
        if (isDragging) {
            event.preventDefault();
            currentX = event.clientX - initialX;
            currentY = event.clientY - initialY;
            xOffset = currentX;
            yOffset = currentY;
            setTranslate(currentX, currentY, hintBox);
        }
    }

    function stopDrag() {
        isDragging = false;
        hintBox.classList.remove('dragging');
        document.removeEventListener('mousemove', drag, false);
        document.removeEventListener('mouseup', stopDrag, false);
    }

    function setTranslate(xPos, yPos, element) {
        element.style.transform = `translate(${xPos}px, ${yPos}px)`;
    }
});
