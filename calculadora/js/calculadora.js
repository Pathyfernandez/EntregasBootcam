    let display = document.getElementById('display');
    let operand1 = '';
    let operand2 = '';
    let operator = '';

    function press(num) {
    if (operator === '') {
        operand1 += num;
        display.innerHTML = operand1;
    } else {
        operand2 += num;
        display.innerHTML = operand2;
    }
    }

    function setOP(op) {
    operator = op;
    display.innerHTML = '';
    }

    function calculate() {
    let result;
    switch (operator) {
        case '+':
        result = parseFloat(operand1) + parseFloat(operand2);
        break;
        case '-':
        result = parseFloat(operand1) - parseFloat(operand2);
        break;
        case '*':
        result = parseFloat(operand1) * parseFloat(operand2);
        break;
        case '/':
        result = parseFloat(operand1) / parseFloat(operand2);
        break;
        default:
        return;
    }
    display.innerHTML = result;
    operand1 = result.toString();
    operand2 = '';
    operator = '';
    }

    function clr() {
    display.innerHTML = '0';
    operand1 = '';
    operand2 = '';
    operator = '';
    }
