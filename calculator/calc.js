const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const result = document.getElementById("result");

function calculate(op) {
  const a = num1.value;
  const b = num2.value;

  if (a === "" || b === "") {
    result.textContent = "Please enter both numbers";
    result.className = "err";
    return;
  }

  const x = Number(a);
  const y = Number(b);
  let answer;

  switch (op) {
    case "add":
      answer = x + y;
      break;

    case "sub":
      answer = x - y;
      break;

    case "mul":
      answer = x * y;
      break;

    case "div":
      if (y === 0) {
        result.textContent = "Error: Cannot divide by zero";
        result.className = "err";
        return;
      }
      answer = x / y;
      break;

    default:
      return;
  }

  answer = Number(answer.toPrecision(12));
  result.textContent = "Result: " + answer;
  result.className = "ok";
}

document.getElementById("add").addEventListener("click", () => calculate("add"));
document.getElementById("sub").addEventListener("click", () => calculate("sub"));
document.getElementById("mul").addEventListener("click", () => calculate("mul"));
document.getElementById("div").addEventListener("click", () => calculate("div"));

document.getElementById("clear").addEventListener("click", () => {
  num1.value = "";
  num2.value = "";
  result.textContent = "";
  result.className = "";
});