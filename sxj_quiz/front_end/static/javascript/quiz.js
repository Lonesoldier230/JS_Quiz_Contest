// quiz.js

document.addEventListener('DOMContentLoaded', function() {
    // Quiz elements
    var revealButton = document.getElementById('reveal_answer');
    var answer = document.getElementById('answer');
    var countdownElement = document.getElementById('countdown');
    var addTimeButton = document.getElementById('add_time');
    var buzzerSound = document.getElementById('buzzer');

    // Get round number from URL query parameter
    var urlParams = new URLSearchParams(window.location.search);
    var roundNumber = parseInt(urlParams.get('round'));

    // Initialize timeLeft based on roundNumber
    var timeLeft = 15; // Default timer value

    switch (roundNumber) {
        case 1:
            timeLeft = 15; // 15 seconds for Round 1
            break;
        case 2:
            timeLeft = 10; // 10 seconds for Round 2
            break;
        case 3:
            timeLeft = 35; // 35 seconds for Round 3 (5 questions)
            break;
        case 5:
            timeLeft = 15; // 15 seconds per question for Round 5
            break;
        case 6:
            timeLeft = 15; // 15 seconds per question for Round 6
            break;
        case 7:
            timeLeft = 70; // 10 seconds per word for 7 words in Round 7
            break;
        case 8:
            timeLeft = 15; // 15 seconds for Round 8
            break;
        default:
            timeLeft = 15; // Default to 15 seconds
            break;
    }

    var timer = setInterval(updateCountdown, 1000);
    var canAddTime = true;

    // Function to update countdown
    function updateCountdown() {
        timeLeft--;
        countdownElement.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(timer);
            revealButton.disabled = false;
            addTimeButton.style.display = 'block';
            playBuzzer();
        }

        if (timeLeft < 0) {
            timeLeft = 0;
        }
    }

    // Function to play buzzer sound
    function playBuzzer() {
        buzzerSound.play();
    }

    // Event listener for revealing answer
    revealButton.addEventListener('click', function() {
        answer.classList.remove('hidden');
        revealButton.disabled = true;
        addTimeButton.style.display = 'none';
    });

    // Event listener for adding time
    addTimeButton.addEventListener('click', function() {
        if (canAddTime) {
            timeLeft += 5;
            countdownElement.textContent = timeLeft;
            timer = setInterval(updateCountdown, 1000);
            canAddTime = false;
            addTimeButton.disabled = true;
        }
    });
});
