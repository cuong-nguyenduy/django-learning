var playerName = $('#idPlayerName');
var playerColor = $('#idPlayerColor');
var playField = $('.playField');
var playResult = $('#result');

var bluePlayerName = prompt("Please enter BLUE PLAYER:", "ANDY");
var redPlayerName = prompt("Please enter RED PLAYER:", "CUONG")
// var bluePlayerName = 'ANDY';
// var redPlayerName = 'CUONG';

// Set the color of players
function setPlayer(name, color) {
    playerName[0].textContent = name;
    playerName.css('color', color);
    playerColor.css('background', color);
}

function bluePlayer() {
    setPlayer(bluePlayerName, 'blue');
};

function redPlayer() {
    setPlayer(redPlayerName, 'red');
};


// Drawing the table 8x8
var numRows = 8;
var numCols = 12;
var animatingInterval = 10;
// Adding the grid to track if any player has won
var cellFilled = [];
// Current Player, blue starts first
var currentPlayer;
var gameOver;
var animating;
resetGame();

function getCoordination(cell_id) {
    var temp = cell_id.split('_');
    var row = parseInt(temp[1]);
    var col = parseInt(temp[2]);
    return [row, col];
}


function makeCellFalling(row, col, color) {
    var timerID = setInterval(animate, animatingInterval);
    var i = 0;
    var originalState = true;
    animating = true;

    function animate() {
        if (i === row) {
            clearInterval(timerID);
            animating = false;
            $('#cell_' + row + '_' + col).css('background', color);
        } else {
            var cell = $('#cell_' + i + '_' + col);
            if (originalState) {
                originalState = false;
                // var cell = $('#cell_' + i + '_' + col);
                cell.css('background', color);
            } else {
                originalState = true;
                cell.css('background', 'grey');
                i++;
            }
        }
    }
}

// Update the cell and the cellFilled
function setCell(cell_id) {
    var cell = $('#' + cell_id);
    var coordination = getCoordination(cell_id);
    var row = coordination[0];
    var col = coordination[1];
    makeCellFalling(row, col, currentPlayer);
    setTimeout(function() {
        cellFilled[row][col] = currentPlayer;
        if (currentPlayer === 'blue') {
            currentPlayer = 'red';
            redPlayer()
        } else {
            currentPlayer = 'blue';
            bluePlayer();
        }
        if (check_winning(cell_id)) {
            gameOver = true;
            console.log('Game Over!');
            newGame();
        }
    }, animatingInterval*(numRows + 5));
}


function check_horizonal(cell_row, cell_col) {
    var color = cellFilled[cell_row][cell_col];
    var count = 1;
    for (var col = cell_col + 1; col < numCols; col++) {
        if (cellFilled[cell_row][col] === color) {
            count++;
        } else {
            break
        }
    }
    for (var col = cell_col - 1; col >=0; col--) {
        if (cellFilled[cell_row][col] === color) {
            count++;
        } else {
            break;
        }
    }
    return count;
}


function check_vertical(cell_row, cell_col) {
    var color = cellFilled[cell_row][cell_col];
    var count = 1;
    for (var row = cell_row + 1; row < numRows; row++) {
        if (cellFilled[row][cell_col] === color) {
            count++;
        } else {
            break;
        }
    }
    for (var row = cell_row - 1; row >=0; row--) {
        if (cellFilled[row][cell_col] === color) {
            count++;
        } else {
            break
        }
    }
    return count;
}


function check_diagonal(cell_row, cell_col) {
    var color = cellFilled[cell_row][cell_col];
    var count;

    // Top-Left to Bottom-Right
    count = 1;
    for (var i = 1; cell_row - i >= 0 && cell_col - i >= 0; i++) {
        if (cellFilled[cell_row - i][cell_col - i] === color) {
            count++;
        } else {
            break;
        }
    }
    for (var i = 1; cell_row + i < numRows && cell_col + i < numCols; i++) {
        if (cellFilled[cell_row + i][cell_col + i] === color) {
            count++;
        } else {
            break;
        }
    }
    if (count >= 4) {
        return count;
    }

    // Bottom-Left to Top-Right
    count = 1;
    for (var i = 1; cell_row + i < numRows && cell_col - i >= 0; i++) {
        if (cellFilled[cell_row + i][cell_col - i] === color) {
            count++;
        } else {
            break;
        }
    }
    for (var i = 1; cell_row - i >= 0 && cell_col + i < numCols; i++) {
        if (cellFilled[cell_row - i][cell_col + i] === color) {
            count++;
        } else {
            break;
        }
    }
    return count;
}

function check_winning(cell_id) {
    var temp = getCoordination(cell_id);
    var cell_row = temp[0];
    var cell_col = temp[1];

    // Return
    if (check_horizonal(cell_row, cell_col) >= 4) {
        return true;
    }

    if (check_vertical(cell_row, cell_col) >= 4) {
        return true;
    }

    if (check_diagonal(cell_row, cell_col) >= 4) {
        return true;
    }

    return false;
}

function process_click(cell_id) {
    var temp = getCoordination(cell_id);
    var cell_row = temp[0];
    var cell_col = temp[1];

    for (temp = numRows - 1; temp >= 0; temp--) {
        if (cellFilled[temp][cell_col] === 'blank') {
            // Cell is not free, stop
            break;
        }
    }
    if (temp === -1) {
        // No more cell, do nothing
        // However, log to console
        console.log('Colum [' + cell_col + '] is full!');
    } else {
        cell_id = 'cell_' + temp + '_' + cell_col;
        console.log('Update cell ' + cell_id + ' with currentPlayer = ' + currentPlayer + ', Current cellFilled:' + cellFilled[temp][cell_col]);
        setCell(cell_id);
    }
}


// Reset the Game
function resetGame() {
    // Drawing the table 8x8
    var table = '';
    for (var row = 0; row < numRows; row++) {
        var tr = '';
        for (var col = 0; col < numCols; col++) {
            tr += '<td class="cell" id="cell_' + row + '_' + col + '"></td>';
        }
        table += '<tr>' + tr + '</tr>';
    }
    playField.html(table);

    // Adding the grid to track if any player has won
    cellFilled = [];
    for(var row = 0; row < numRows; row++) {
        cellFilled.push(Array(numCols).fill('blank'));
    }

    // Current Player, blue starts first
    bluePlayer();
    currentPlayer = 'blue';
    gameOver = false;
    animating = false;
    // Function to handle the click on cells
    for (var row = 0; row < numRows; row++) {
        for (var col = 0; col < numCols; col++) {
            var cell = $('#cell_' + row + '_' + col);
            cell.click(function(event) {
                cell_id = event.target.id;
                if (gameOver || animating) {
                    return;
                }
                process_click(cell_id);
            });
        }
    }
    playResult.html('');
}

// Start New Game
function newGame() {
    var winner = bluePlayerName;
    bluePlayer();
    if (currentPlayer === 'blue') {
        winner = redPlayerName;
        redPlayer();
    }
    html = '<tr><td><h1><strong>' + winner + '</strong> WON!</h1></td></tr>';
    html += '<tr><td><button type="submit" id="idNewGame" class="btn btn-default btn-lg">New Game</button></td></tr>';
    playResult.html(html);

    $('#idNewGame').click(function() {
        resetGame();
    });
}