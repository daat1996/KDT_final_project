document.addEventListener('DOMContentLoaded', function() {
    var drawButton = document.getElementById('draw-button');
    var cardValue = document.getElementById('card-value');
    var resultValue = document.getElementById('result-value');
    var resultDiv = document.getElementById('result');

    drawButton.addEventListener('click', function() {
        // 카드 뽑기 요청을 서버에 보냄
        fetch('/draw-card')
        .then(response => response.json())
        .then(data => {
            cardValue.textContent = data.card;
            resultValue.textContent = data.result;
            resultDiv.style.display = 'block';
        });
    });
});
