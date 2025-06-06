document.addEventListener('documentReady', () => {
    // DOM Elements
    const setupContainer = document.getElementById('setup-container');
    const mainGameContainer = document.getElementById('main-game');
    const resultsContainer = document.getElementById('results-container');

    const timerInput = document.getElementById('timer-input');
    const startSetupBtn = document.getElementById('start-setup-btn');
    const timerDisplay = document.getElementById('timer-display');
    const keywordsDisplay = document.getElementById('keywords-display');
    const resultsDisplay = document.getElementById('results-display');
    const pauseBtn = document.getElementById('pause-btn');
    const stopBtn = document.getElementById('stop-btn');
    const continueBtn = document.getElementById('continue-btn');
    const newGameBtn = document.getElementById('new-game-btn');

    // Game State
    let allWords = [];
    let gameWords = [];
    let timerId = null;
    let timeLeft = 0;
    let isPaused = false;
    let originalTime = 0;

    /**
     * Fetches and parses word data from the CSV file.
     */
    async function loadWords() {
        try {
            const response = await fetch('tamil_word_game.csv');
            if (!response.ok) {
                throw new Error('Network response was not ok. Ensure tamil_word_game.csv is in the same folder.');
            }
            const csvText = await response.text();
            allWords = csvText.trim().split('\n').slice(1).map(line => {
                const columns = line.split(',');
                return { 
                    category: columns[0], 
                    keyword: columns[1], 
                    clues: [columns[2], columns[3], columns[4]] 
                };
            });
             if (allWords.length === 0) throw new Error("CSV file is empty or could not be parsed.");
        } catch (error) {
            console.error('Error loading or parsing CSV file:', error);
            document.body.innerHTML = `<div style="text-align: center; padding: 2rem;"><h1>Error</h1><p>வார்த்தை கோப்பை ஏற்றுவதில் பிழை. 'tamil_word_game.csv' கோப்பு இதே போல்டரில் உள்ளதா என சரிபார்க்கவும்.</p></div>`;
        }
    }
    
    /**
     * Set up and start a new round
     */
    function startNewRound() {
        timeLeft = originalTime;
        isPaused = false;
        pauseBtn.textContent = 'இடைநிறுத்து';

        // Select 5 new random words
        const shuffled = [...allWords].sort(() => 0.5 - Math.random());
        gameWords = shuffled.slice(0, 5);
        
        // Display keywords
        keywordsDisplay.innerHTML = '';
        gameWords.forEach(({ keyword }) => {
            const card = document.createElement('div');
            card.className = 'keyword-card';
            card.textContent = keyword;
            keywordsDisplay.appendChild(card);
        });

        updateTimer();
        
        // Show the correct screen
        setupContainer.style.display = 'none';
        resultsContainer.style.display = 'none';
        mainGameContainer.style.display = 'block';

        startTimer();
    }

    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    function startTimer() {
        if (timerId) clearInterval(timerId); 
        
        timerId = setInterval(() => {
            if (!isPaused) {
                timeLeft--;
                updateTimer();

                if (timeLeft <= 0) {
                    endGame();
                }
            }
        }, 1000);
    }
    
    function showResults() {
        resultsDisplay.innerHTML = '';
        gameWords.forEach(({ keyword, clues }) => {
            const item = document.createElement('div');
            item.className = 'result-item';
            item.innerHTML = `
                <p class="keyword">வார்த்தை: ${keyword}</p>
                <p class="clues">குறிப்புகள்: ${clues.join(', ')}</p>
            `;
            resultsDisplay.appendChild(item);
        });

        mainGameContainer.style.display = 'none';
        resultsContainer.style.display = 'block';
    }
    
    function endGame() {
        clearInterval(timerId);
        timerId = null;
        showResults();
    }


    // Event Listeners
    startSetupBtn.addEventListener('click', () => {
        originalTime = parseInt(timerInput.value, 10);
        if (isNaN(originalTime) || originalTime <= 0) {
            alert('தயவுசெய்து சரியான நேரத்தை உள்ளிடவும்.');
            return;
        }
        startNewRound();
    });

    pauseBtn.addEventListener('click', () => {
        isPaused = !isPaused;
        pauseBtn.textContent = isPaused ? 'தொடரவும்' : 'இடைநிறுத்து';
    });

    stopBtn.addEventListener('click', () => {
        endGame();
    });
    
    // "Continue" button starts the next round
    continueBtn.addEventListener('click', () => {
        startNewRound();
    });
    
    // "New Game" button goes back to the setup screen
    newGameBtn.addEventListener('click', () => {
        resultsContainer.style.display = 'none';
        mainGameContainer.style.display = 'none';
        setupContainer.style.display = 'block';
    });

    // Initial load
    loadWords();
});

// A robust way to ensure the script runs after the DOM is loaded.
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        document.dispatchEvent(new Event('documentReady'));
    });
} else {
    document.dispatchEvent(new Event('documentReady'));
}