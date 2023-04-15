let userScore = 0;
let IAScore = 0;
const userScore_span = document.getElementById("user-score");
const IAScore_span = document.getElementById("ia-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_p = document.querySelector(".result > p");
const rock_div = document.getElementById("rock");
const paper_div = document.getElementById("paper");
const scissors_div = document.getElementById("scissors");

function getIAChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomNumber = Math.floor(Math.random() * 3);
    return choices[randomNumber];
}

function convertToWord(letter) {
    if (letter === "rock") return "Rock";
    if (letter === "paper") return "Paper";
    return "Scissors";
}

function win(userChoice, IAChoice) {
    const smallUserWord = "user".fontsize(3).sub();
    const smallIAWord = "ia".fontsize(3).sub();
    const userChoice_div = document.getElementById(userChoice);
    userScore++;
    userScore_span.innerHTML = userScore;
    IAScore_span.innerHTML = IAScore;
    result_p.innerHTML = `${convertToWord(userChoice)} ${smallUserWord} beats ${convertToWord(IAChoice)} ${smallIAWord} . You win!`;
    userChoice_div.classList.add('green-glow');
    setTimeout(() => {userChoice_div.classList.remove('green-glow')}, 500);
}

function lose(userChoice, IAChoice) {
    const smallUserWord = "user".fontsize(3).sub();
    const smallIAWord = "ia".fontsize(3).sub();
    const userChoice_div = document.getElementById(userChoice);
    IAScore++;
    userScore_span.innerHTML = userScore;
    IAScore_span.innerHTML = IAScore;
    result_p.innerHTML = `${convertToWord(userChoice)} ${smallUserWord} loses to ${convertToWord(IAChoice)} ${smallIAWord} . You lost...`;
    userChoice_div.classList.add('red-glow');
    setTimeout(() => {userChoice_div.classList.remove('red-glow')}, 500);
}

function draw(userChoice, IAChoice) {
    const smallUserWord = "user".fontsize(3).sub();
    const smallIAWord = "ia".fontsize(3).sub();
    const userChoice_div = document.getElementById(userChoice);
    result_p.innerHTML = `${convertToWord(userChoice)} ${smallUserWord} equals ${convertToWord(IAChoice)} ${smallIAWord} . It's a draw.`;
    userChoice_div.classList.add('gray-glow');
    setTimeout(() => {userChoice_div.classList.remove('gray-glow')}, 500);
}

function game(userChoice) {
    const IAChoice = getIAChoice();
    switch (userChoice + IAChoice) {
        case "rockscissors":
        case "paperrock":
        case "scissorspaper":
            win(userChoice, IAChoice);
            break;
        case "rockpaper":
        case "paperscissors":
        case "scissorsrock":
            lose(userChoice, IAChoice);
            break;
        case "rockrock":
        case "paperpaper":
        case "scissorsscissors":
            draw(userChoice, IAChoice);
            break;
        otherwise:
            console.log("error");
    }
}

function main() {
    rock_div.addEventListener('click', () => game("rock"));
    paper_div.addEventListener('click', () => game("paper"));
    scissors_div.addEventListener('click', () => game("scissors"));
}

main();