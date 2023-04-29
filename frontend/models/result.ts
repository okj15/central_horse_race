export async function fetchApiData() {
    const response = await fetch('http://localhost:8080/api/result/races/');
    const data: RaceResultResponse[] = await response.json();

    const raceResults: RaceResult[] = [];
    for (const obj of data) {
        raceResults.push({
            id: obj.id,
            bracket: obj.bracket,
            horseNumber: obj.horse_number,
            horse: obj.horse,
            getGenderDisplay: obj.get_gender_display,
            age: obj.age,
            jockeyWeight: obj.jockey_weight,
            raceTime: obj.race_time,
            popularity: obj.popularity,
            odds: obj.odds,
        });
    }

    return raceResults;
}

type RaceResultResponse = {
    id: number;
    bracket: number;
    horse_number: number;
    horse: string;
    get_gender_display: string;
    age: number;
    jockey_weight: number;
    race_time: string;
    popularity: number;
    odds: number;
}

export type RaceResult = {
    id: number;
    bracket: number;
    horseNumber: number;
    horse: string;
    getGenderDisplay: string;
    age: number;
    jockeyWeight: number;
    raceTime: string;
    popularity: number;
    odds: number;
}