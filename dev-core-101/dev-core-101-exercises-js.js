let readline = require('readline');

let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Игра "Угадай число"
function number() {
    rl.question('Введите число от 1 до 10: ', (input) => {
        let num = parseInt(input);

        if (num < 8) {
            console.log("Число больше");
        } else if (num > 8) {
            console.log("Число меньше");
        } else {
            console.log("Вы угадали число");
        }

        primeCheck();
    });
}

// Простое, составное
function primeCheck() {
    rl.question('Введите число: ', (input) => {
        let num = parseInt(input);

        if (num <= 1) {
            console.log("Не простое и не составное число");
        } else {
            let isPrime = true;
            for (let x = 2; x <= Math.sqrt(num); x++) {
                if (num % x === 0) {
                    console.log("Число составное");
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                console.log("Число простое");
            }
        }

        convertTemperature();
    });
}

// Цельсии, Фаренгейт
function convertTemperature() {
    rl.question('Введите температуру в ℃: ', (input) => {
        let temp = parseInt(input);
        console.log(`${temp} ℃ = ${F(temp)} ℉`);

       
        checkSchool();
    });
}

function F(temp) {
    return temp * 9 / 5 + 32;
}

// Школа
function checkSchool() {
    rl.question('Введите ваш возраст: ', (input) => {
        let age = parseInt(input);

        if (age < 6) {
            console.log("Ты ещё не учишься в школе.");
        } else if (age >= 6 && age < 18) {
            console.log("Ты уже можешь учиться в школе.");
        } else {
            console.log("Ты уже закончил школу.");
        }

       
        rl.close();
    });
}

number();

