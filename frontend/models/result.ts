export async function fetchApiData() {
    const response = await fetch('http://localhost:8080/api/result/races/');
    const data: RaceResultResponse[] = await response.json();

    const raceResults: RaceResult[] = [];
    for (const obj of data) {
        raceResults.push({
            id: obj.id,
            horseNumber: obj.horse_number,
            horse: obj.horse,
            getGenderDisplay: obj.get_gender_display,
            age: obj.age,
        });
    }

    return raceResults;
}

type RaceResultResponse = {
    id: number;
    horse_number: number;
    horse: string;
    get_gender_display: string;
    age: number;
}

export type RaceResult = {
    id: number;
    horseNumber: number;
    horse: string;
    getGenderDisplay: string;
    age: number;
}