const NQueensNS = {};

algorithm_enum = {}
algorithm_enum.simpleBackTracking = 0;
algorithm_enum.hillClimbing = 1;
algorithm_enum.randomRestart = 2;
algorithm_enum.randomRestartPlus = 3;
algorithm_enum.SimulatedAnnealing = 4;
algorithm_enum.BranchAndBound = 5;
algorithm_enum.OR = 6;
algorithm_enum.Genetic = 7;


NQueensNS.initialize = function () {
    $('input[type=radio][name=algorithm]').on('change', NQueensNS.algorithm_change_notifier)

}

$("#queensNum").on('change', function () {
    NQueensNS.initializeBoard($("#queensNum").val())
})

NQueensNS.algorithm_change_notifier = function () {
    let selected_algorithm = parseInt($('input[type=radio][name=algorithm]:checked').val())
    $(".subAlgorithmContainer").slideUp();
    if (selected_algorithm == algorithm_enum.randomRestart)
        $("#randomRestart-container").slideDown();
    if (selected_algorithm == algorithm_enum.randomRestartPlus)
        $("#randomRestartPlus-container").slideDown();
    if (selected_algorithm == algorithm_enum.SimulatedAnnealing)
        $("#simulated-annealing-container").slideDown();
    if (selected_algorithm == algorithm_enum.Genetic)
        $("#genetic-container").slideDown();
}

NQueensNS.validateParameters = function () {
    let n = $("#queensNum").val();
    if (n == undefined || n == "") {
        global_NS.show("error", "Missing Board Size (N)");
        return false;
    }
    debugger;
    let selected_algorithm = parseInt($('input[type=radio][name=algorithm]:checked').val())
    if (isNaN(selected_algorithm)) {
        global_NS.show("error", "Must Choose an algorithm !")
        return false;
    }

    if (selected_algorithm == algorithm_enum.randomRestart && ( $("#random_restart_limit").val() == undefined || $("#random_restart_limit").val() == "" )) {
        global_NS.show("error", "Missing Iteration value");
        return false;
    }

    if (selected_algorithm == algorithm_enum.randomRestartPlus && ($("#random_restart_plus_limit").val() == undefined || $("#random_restart_plus_limit").val() == "")) {
        global_NS.show("error", "Missing Iteration value");
        return false;
    }

    if (selected_algorithm == algorithm_enum.randomRestartPlus && ($("#random_restart_plus_initial_no").val() == undefined || $("#random_restart_plus_initial_no").val() == "")) {
        global_NS.show("error", "Missing initial states value");
        return false;
    }


    if (selected_algorithm == algorithm_enum.SimulatedAnnealing && ($("#simulated_annealing_limit").val() == undefined || $("#simulated_annealing_limit").val() == "")) {
        global_NS.show("error", "Missing limit value");
        return false;
    }

    if (selected_algorithm == algorithm_enum.Genetic && ( $("#genetic-population").val() == undefined || $("#genetic-population").val() == "")) {
        global_NS.show("error", "Missing population number");
        return false;
    }

    if (selected_algorithm == algorithm_enum.Genetic && ( $("#genetic-mutation-prop").val() == undefined || $("#genetic-mutation-prop").val() == "")) {
        global_NS.show("error", "Missing mutation probability");
        return false;
    }

    return true;
}

NQueensNS.run = function () {
    board_animation = true;
    $("#boardContainer").slideDown();
    if (!NQueensNS.validateParameters())
        return;
    let n = $("#queensNum").val();
    let selected_algorithm = parseInt($('input[type=radio][name=algorithm]:checked').val())


    if (selected_algorithm == algorithm_enum.hillClimbing)
        requestHandler.send({}, `/hillclimbing?n=${n}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.randomRestart)
        requestHandler.send({}, `/randomrestart?n=${n}&limit=${$("#random_restart_limit").val()}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.randomRestartPlus)
        requestHandler.send({}, `/randomrestartplus?n=${n}&limit=${$("#random_restart_plus_limit").val()}&initial=${$("#random_restart_plus_initial_no").val()}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.SimulatedAnnealing)
        requestHandler.send({}, `/simulatedannealing?n=${n}&limit=${$("#simulated_annealing_limit").val()}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.simpleBackTracking)
        requestHandler.send({}, `/simplebacktracking?n=${n}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.BranchAndBound)
        requestHandler.send({}, `/branchandbound?n=${n}`, NQueensNS.success, () => { alert('an error occurred') })
    if (selected_algorithm == algorithm_enum.Genetic)
        requestHandler.send({}, `/genetic?n=${n}&populationSize=${$("#genetic-population").val()}&mutationProb=${$("#genetic-mutation-prop").val()}`, NQueensNS.success, () => { alert('an error occurred') })


    //send post with success
    reset_timer()
    start_timer()
    NQueensNS.start_board_animmation();
}

NQueensNS.success = function (response) {
    response = response.data;
    console.log(response)
    pause_timer();
    if (response == null || response.length == 0 ) {
        board_animation = false;
        $("#boardContainer").slideUp();
        alert('No solution was found');
        return;
    }
    board_animation = false;
    NQueensNS.fillBoard(response);

}


cellWidth = 0;
cellHeight = 0;
NQueensNS.initializeBoard = function(n = 5){
    let container = $("#boardContainer");
    cellWidth = container.width() / n  ;
    cellHeight = cellWidth;
    let html = ``;
    for (let i = 0; i < n; i++) {
        html += `<div class="row boardRow m-0" data-rowIndex='${i}' style="height:${cellHeight}px">`;
        for (let j = 0; j < n; j++) {
            let color = "#b58863";
            if ((i + j) % 2 == 0)
                color = "#f0d9b5"
            html += `<div class="boardCol m-0 p-0 d-flex" data-colIndex='${n-j-1}' style="background-color:${color};border:1px solid black;width:${cellWidth}px;height:${cellHeight}px">
                    </div>`
        }
        html += `</div>`
    }
    container.html(html);
}

NQueensNS.fillBoard = function (arr) {
    $(".queen-img").remove()
    let n = $("#queensNum").val();
    if (arr.length != n) {
        alrt('Invalid Input');
        return;
    }
    for (let row = 0; row < arr.length; row++) {
        $(`.boardRow[data-rowIndex=${row}]`).find(`.boardCol[data-colIndex=${arr[row]}]`).html(`<img src="images/queen_logo2.png" class="queen-img align-self-center mx-auto" style="width:${cellWidth - cellWidth * (32 / 100)}px;height:${cellHeight - cellHeight * (32 / 100)}px"/>`)
    }
}

board_animation = true;
NQueensNS.start_board_animmation = async function () {
    let n = $("#queensNum").val();
    while (board_animation) {
        let a = Array.from({ length: n }, () => Math.floor(Math.random() * n));
        NQueensNS.fillBoard(a);
        await sleep(100);
    }
}



















//timer 
function timeToString(time) {
    let diffInHrs = time / 3600000;
    let hh = Math.floor(diffInHrs);

    let diffInMin = (diffInHrs - hh) * 60;
    let mm = Math.floor(diffInMin);

    let diffInSec = (diffInMin - mm) * 60;
    let ss = Math.floor(diffInSec);

    let diffInMs = (diffInSec - ss) * 100;
    let ms = Math.floor(diffInMs);

    let formattedMM = mm.toString().padStart(2, "0");
    let formattedSS = ss.toString().padStart(2, "0");
    let formattedMS = ms.toString().padStart(2, "0");

    return `${formattedMM}:${formattedSS}:${formattedMS}`;
}


let startTime;
let elapsedTime = 0;
let timerInterval;

function print(txt) {
    document.getElementById("timer").innerHTML = txt;
}


function start_timer() {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
        elapsedTime = Date.now() - startTime;
        print(timeToString(elapsedTime));
    }, 10);
}

function pause_timer() {
    $(".circle").addClass('zoomAnimation')
    clearInterval(timerInterval);
}

function reset_timer() {
    $(".circle").removeClass('zoomAnimation')
    clearInterval(timerInterval);
    print("00:00:00");
    elapsedTime = 0;
}

