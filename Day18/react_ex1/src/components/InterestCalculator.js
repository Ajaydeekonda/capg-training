import React, { useState } from 'react';

function InterestCalculator() {
    const [principal, setPrincipal] = useState('');
    const [rate, setRate] = useState('');
    const [time, setTime] = useState('');
    const [interest, setInterest] = useState('simple'); // Dropdown selection for interest type
    const [result, setResult] = useState(null);

    const calculateInterest = () => {
        let P = parseFloat(principal);
        let R = parseFloat(rate);
        let T = parseFloat(time);

        if (isNaN(P) || isNaN(R) || isNaN(T) || P <= 0 || R <= 0 || T <= 0) {
            setResult('Please enter valid positive numbers.');
            return;
        }

        let calculatedInterest = 0;

        if (interest === 'simple') {
            calculatedInterest = (P * R * T) / 100;
        } else if (interest === 'compound') {
            calculatedInterest = P * Math.pow(1 + R / 100, T) - P;
        }

        setResult(`Calculated ${interest === 'simple' ? 'Simple' : 'Compound'} Interest: ${calculatedInterest.toFixed(2)}`);
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
            <h2>Interest Calculator</h2>

            <label>Principal:</label>
            <input
                type="number"
                value={principal}
                onChange={(e) => setPrincipal(e.target.value)}
                placeholder="Enter Principal Amount"
                style={{ display: 'block', marginBottom: '10px', padding: '5px' }}
            />

            <label>Rate of Interest (%):</label>
            <input
                type="number"
                value={rate}
                onChange={(e) => setRate(e.target.value)}
                placeholder="Enter Rate of Interest"
                style={{ display: 'block', marginBottom: '10px', padding: '5px' }}
            />

            <label>Time (Years):</label>
            <input
                type="number"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                placeholder="Enter Time"
                style={{ display: 'block', marginBottom: '10px', padding: '5px' }}
            />

            <label>Interest Type:</label>
            <select
                value={interest}
                onChange={(e) => setInterest(e.target.value)}
                style={{ display: 'block', marginBottom: '10px', padding: '5px' }}
            >
                <option value="simple">Simple Interest</option>
                <option value="compound">Compound Interest</option>
            </select>

            <button onClick={calculateInterest} style={{ padding: '10px', cursor: 'pointer' }}>
                Calculate Interest
            </button>

            {result && <p style={{ marginTop: '20px', fontWeight: 'bold' }}>{result}</p>}
        </div>
    );
}

export default InterestCalculator;
