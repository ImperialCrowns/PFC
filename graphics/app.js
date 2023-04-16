let userScore = 0;
let IAScore = 0;
let whoWinLast = "none";
let IAList = [];
let userList = [];
let rep = 0;
const userScore_span = document.getElementById("user-score");
const IAScore_span = document.getElementById("ia-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_p = document.querySelector(".result > p");
const rock_div = document.getElementById("rock");
const paper_div = document.getElementById("paper");
const scissors_div = document.getElementById("scissors");

function countChoice() {
    rock = 0;
    paper = 0;
    scissors = 0;
    for (let i = 0; i < userList.length; i++) {
        if (userList[i] === "rock") {
            rock++;
        } else if (userList[i] === "paper") {
            paper++;
        } else {
            scissors++;
        }
    }
    return [rock, paper, scissors];
}

function randomChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomNumber = Math.floor(Math.random() * 11);
    if (randomNumber >= 5) {
        return choices[2];
    } else if (randomNumber < 2) {
        return choices[0];
    } else {
        return choices[1];
    }
}

function chooseDefeat() {
    if (userList.length >= 3) {

        if (userList[userList.length - 1] === userList[userList.length - 2] && userList[userList.length - 2] === userList[userList.length - 3]) {
            if (rep === 1) {
                rep = 0;
                return userList[userList.length - 1];
            } else {
                if (userList[userList.length - 1] === "rock") {
                    rep = 1;
                    return "paper";
                } else if (userList[userList.length - 1] === "paper") {
                    rep = 1;
                    return "scissors";
                } else {
                    rep = 1;
                    return "rock";
                }
            }
        }
    }
    rep = 0;
    if (IAList[IAList.length - 1] === "rock") {
        return "scissors";
    } else if (IAList[IAList.length - 1] === "paper") {
        return "rock";
    } else {
        return "paper";
    }
}

function chooseWin() {
    if (userList.length >= 3) {

        if (userList[userList.length - 1] === userList[userList.length - 2] && userList[userList.length - 2] === userList[userList.length - 3]) {
            if (rep === 1) {
                rep = 0;
                return userList[userList.length - 1];
            } else {
                if (userList[userList.length - 1] === "rock") {
                    rep = 1;
                    return "paper";
                } else if (userList[userList.length - 1] === "paper") {
                    rep = 1;
                    return "scissors";
                } else {
                    rep = 1;
                    return "rock";
                }
            }
        }

        if (userList.length >= 5) {
            proba = countChoice();
            userConfidentChoice = Math.max(proba[0], proba[1], proba[2]);
            if (userConfidentChoice === proba[0]) {
                return "paper";
            } else if (userConfidentChoice === proba[1]) {
                return "scissors";
            } else {
                return "rock";
            }
        }

        uncommon = Math.floor(Math.random() * 3);
        if (uncommon === 0 || uncommon === 1) {
            if (userList[userList.length - 1] === "rock") {
                return "paper";
            } else if (userList[userList.length - 1] === "paper") {
                return "scissors";
            } else {
                return "rock";
            }
        } else {
            IAChoice = Math.floor(Math.random() * 3);
            if (IAChoice === 0) {
                return "rock";
            } else if (IAChoice === 1) {
                return "paper";
            } else {
                return "scissors";
            }
        }
    }
}

function getIAChoice() {
    if (IAList.length === 0) {
        return randomChoice();
    } else if (whoWinLast === "user") {
        return chooseWin();
    } else if (whoWinLast === "ia") {
        return chooseDefeat();
    } else {
        return randomChoice();
    }
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
    whoWinLast = "user";
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
    whoWinLast = "ia";
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
    whoWinLast = "user";
    result_p.innerHTML = `${convertToWord(userChoice)} ${smallUserWord} equals ${convertToWord(IAChoice)} ${smallIAWord} . It's a draw.`;
    userChoice_div.classList.add('gray-glow');
    setTimeout(() => {userChoice_div.classList.remove('gray-glow')}, 500);
}

function game(userChoice) {
    const IAChoice = getIAChoice();
    userList.push(userChoice);
    IAList.push(IAChoice);
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