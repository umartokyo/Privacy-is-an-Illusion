const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

function startScramble(event) {
    let iteration = 0;

    // Play the sound
    let sound = document.getElementById("scramble-sound");
    sound.currentTime = 0;
    sound.play();

    clearInterval(interval);
  
    interval = setInterval(() => {
        event.target.innerText = event.target.innerText
            .split("")
            .map((letter, index) => {
                if(index < iteration) {
                    return event.target.dataset.value[index];
                }
      
                return letters[Math.floor(Math.random() * 26)];
            })
            .join("");
    
        if(iteration >= event.target.dataset.value.length){ 
            clearInterval(interval);
        }
    
        iteration += 1 / 3;
    }, 10);
}

document.querySelector("h1").onmouseover = function(event) {
    document.getElementById("data").style.display = "block";
    startScramble(event);
};

// Apply the effect to all <p> elements inside the #data div
let ps = document.querySelectorAll("#data p");
for (let p of ps) {
    p.dataset.value = p.innerText;
    p.onmouseover = function(event) {
        document.getElementById("data").style.display = "block";
        startScramble(event);
    };
}
