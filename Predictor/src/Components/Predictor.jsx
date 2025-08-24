import { useState } from 'react'

function Predictor() {

    const [team1, setTeam1] = useState('')
    const [team2, setTeam2] = useState('')
    const [teamScore, setTeamScore] = useState('')


    //Calling backend here
    const handlePredict = async () => {

        try {
            const responce = await fetch('http://127.0.0.1:8000/predict', {
                method: "Post",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    team1_strength: Number(team1),
                    team2_strength: Number(team2),
                }),
            })

            const data = await responce.json();
            setTeamScore(data)
        } catch (error) {

            console.error("Error Fetching data  ", error)

        }

    }





    return (
        <div>
            <h1>Predict Wining chances of your Team</h1>
            <div>
                <div>
                    <input type='number' placeholder='Score of Team 1' value={team1} onChange={(e) => setTeam1(e.target.value)} />
                    <input type='number' placeholder='Score of Team 2' value={team2} onChange={(e) => setTeam2(e.target.value)} />
                </div>
                <div>
                    <button onClick={handlePredict}
                    >
                        Predict
                    </button>
                </div>
                <div>
                    {teamScore && (
                        <div>
                            <p><b>Predicted Winner</b> Team {teamScore.predicted_winner + 1}</p>
                            <p><b>Probablites: </b></p>
                            <ul>
                                <li>Team 1: {(teamScore.probabilities.team1 * 100).toFixed(2)}%</li>
                                <li>Team 2: {(teamScore.probabilities.team2 * 100).toFixed(2)}%</li>


                            </ul>
                        </div>
                    )
                    }
                </div>
            </div>
        </div>
    )
}

export default Predictor