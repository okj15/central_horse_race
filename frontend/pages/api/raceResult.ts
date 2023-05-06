export async function fetchRaceResult(raceId: number = 202101010101) {
    const url = `http://localhost:8080/api/racing_horse/results/?race=${raceId}`;
    const response = await fetch(url);
    const data: RaceResultResponse[] = await response.json();

    const raceResults: RaceResultType[] = [];
    for (const obj of data) {
        raceResults.push({
            id: obj.id,
            bracket: obj.bracket,
            horseNumber: obj.horse_number,
            horseId: obj.horse.id,
            horseName: obj.horse.name,
            gender: obj.get_gender_display,
            age: obj.age,
            jockeyWeight: obj.jockey_weight,
            raceTime: obj.race_time,
            popularity: obj.popularity,
            odds: obj.odds,
            rank: obj.rank,
            trainingCenter: obj.get_training_center_display,
            jokeyName: obj.jockey.name,
            trainerName: obj.trainer?.name || '',
            ownerName: obj.horse.owner?.name || '',
        });
    }

    return raceResults;
}


type OwnerResponse = {
    id: number;
    name: string;
}

type HorseResponse = {
    id: number;
    name: string;
    owner: OwnerResponse
}

type JockeyResponse = {
    id: number;
    name: string;
}

type TrainerResponse = {
    id: number;
    name: string;
}

type RaceResultResponse = {
    id: number;
    bracket: number;
    horse_number: number;
    horse: HorseResponse;
    get_gender_display: string;
    age: number;
    jockey_weight: number;
    race_time: string;
    popularity: number;
    odds: number;
    rank: number;
    get_training_center_display: string;
    jockey: JockeyResponse;
    trainer: TrainerResponse;
}

export type RaceResultType = {
    id: number;
    bracket: number;
    horseNumber: number;
    horseId: number;
    horseName: string;
    gender: string;
    age: number;
    jockeyWeight: number;
    raceTime: string;
    popularity: number;
    odds: number;
    rank: number;
    trainingCenter: string;
    jokeyName: string;
    trainerName: string;
    ownerName: string;
}