const quizData = [
    {
        question: "Who invented Facebook ?",
        a: "Mark Zuckerberg",
        b: "Zack Dorsey",
        c: "Larry Page",
        d: "Faisal Khan",
        answer: 'a'
    },
    {
        question: "Indian Independence is celebrated on ?",
        a: "1st January",
        b: "15th August",
        c: "24th April",
        d: "14th August",
        answer: 'b'
    },
    {
        question: "Who is the best person in the world ?",
        a: "Leonardo DiCaprio",
        b: "Tony Stark",
        c: "One taking this quiz!",
        d: "Thanos",
        answer: 'c'
    }

]
let quest = document.getElementById('question');
let ans_a = document.getElementById("ans_a");
let ans_b = document.getElementById('ans_b');
let ans_c = document.getElementById('ans_c');
let ans_d = document.getElementById('ans_d');
// let submission = document.getElementById("sub");
let body = document.getElementById('body');
//let h1 = body.getElementsByClassName('big-text')[0];
let current = 0;
let ans_id = undefined;
let currentQ = quizData[current];
let quest_div = document.getElementById('quest');
let ans_div = document.getElementById('ans');
let correct = 0;

loadQuiz();
function loadQuiz() {
    deselectOption();
    const currentQ = quizData[current];
    quest.innerText = currentQ.question;
    ans_a.innerText = currentQ.a;
    ans_b.innerText = currentQ.b;
    ans_c.innerText = currentQ.c;
    ans_d.innerText = currentQ.d;
    document.getElementById("sub").onclick = function () {
        validate();
    }
}

function validate() {
    currentQ = quizData[current];
    ans_div.style.display = "block";
    ans = getSelectedAnswer();
    console.log(ans_id);
    console.log(current);
    if (current > quizData.length) {
        alert('Quiz Finished!!')
    } else {
        if (current < quizData.length) {
            console.log('validate length');
            console.log(currentQ.question)
            console.log(currentQ.answer)
            console.log(ans_id)
            if (currentQ.answer === ans_id) {
                correct += 1;
                console.log('checking answer...')
                document.getElementsByClassName('big-text')[0].innerHTML = "That's Correct!!!!"
                document.getElementById('question').innerHTML = "Keep Going!"
                document.getElementById("sub").innerHTML = "Next Question";
                showMessage();
            } else {

            }
        } else {
            alert('Quiz Finished!! Your Score is : ' + correct * 10);
            current = 0;
            loadQuiz();
        }
    }


}

function getSelectedAnswer() {
    console.log('get slected answer....')
    let selection = document.querySelectorAll('.answer');
    //console.log(selection.values);
    selection.forEach(ans => {
        if (ans.checked) {
            ans_id = ans.id;
        }
    });
    return ans_id;
}

function showMessage() {

    console.log(current + " show message called");

    ans_div.style.display = "none";

    document.getElementById("sub").onclick = function () {

        document.getElementsByClassName('big-text')[0].innerHTML = "Quiz App"
        document.getElementById("sub").innerHTML = "Submit";
        current += 1;
        console.log("onclick " + current + ' ' + quizData.length);
        ans_div.style.display = "block";
        if (current >= quizData.length) {
            current = 0;
            alert('Quiz Finished!! Your Score is : ' + correct * 10);
            loadQuiz();
        } else {
            loadQuiz();
        }

    }

}
function deselectOption() {
    let selection = document.querySelectorAll('.answer');
    //console.log(selection.values);
    selection.forEach(ans => {
        ans.checked = false;
    });
}

