var img = document.getElementById('game_frame');
var reward = document.getElementById('reward');

function refresh() {
    fetch('/game_frame')
        .then(response => response.json())
        .then(data => {
            img.src = 'data:image/jpeg;base64,' + data.image;
            reward.textContent = 'Reward: ' + data.reward;
        });
}

function sendAction(action) {
    fetch('/action', {
        method: 'POST',
        body: action.toString()
    });
}

// Keyboard event handler
window.onkeydown = function(e) {
    switch(e.key) {
        case 'ArrowUp':
            sendAction(2);
            break;
        case 'ArrowDown':
            sendAction(0);
            break;
        case 'ArrowLeft':
            sendAction(3);
            break;
        case 'ArrowRight':
            sendAction(1);
            break;
    }
};

// Refresh the game frame every 200 ms
setInterval(refresh, 200);